#!/usr/bin/env python3
"""
scan_tells.py -- deterministic scanner for mechanically-checkable AI writing tells.

Usage:
    python scan_tells.py <file>
    cat draft.txt | python scan_tells.py -

Scans PROSE PARAGRAPHS ONLY. Markdown table rows, list items, headers, and
fenced code blocks are excluded from every check, so a document that catalogs
or discusses these terms (like this skill's own reference file) does not
trigger false positives on its own examples.

Exit code 0 = no hard-gate hits. Exit code 1 = at least one hard-gate hit.
Hard-gate categories: em dash, banned vocabulary, "it's not X it's Y".
Heuristic categories (reported but not gating): sentence-length uniformity,
parenthetical density.
"""

import re
import sys
import statistics
import json

BANNED_WORDS = [
    "delve", "delves", "delving",
    "tapestry", "realm", "leverage", "harness", "unlock",
    "landscape", "crucial", "pivotal", "paramount",
    "comprehensive", "robust", "seamless", "underscore",
    "testament to", "multifaceted", "holistic",
    "moreover", "furthermore", "navigate the complexities",
]

# Unambiguous Claude-associated strings only. "load-bearing" and "honest take"
# are deliberately excluded -- too context-dependent for a regex (e.g. a real
# load-bearing wall), left to manual judgment per SKILL.md.
CLAUDE_PHRASES = [
    "you're absolutely right", "you are absolutely right",
    "i'd be happy to", "i would be happy to",
]

ITS_NOT_X_ITS_Y = re.compile(
    r"\bit'?s not\b[^.!?]{0,80}?,\s*(it'?s|its)\b", re.IGNORECASE
)

EM_DASH = "\u2014"


def _paired_spans(line, marker):
    """Return list of (start, end) spans between consecutive pairs of `marker`
    in line. Assumes well-formed pairs; odd trailing marker is ignored."""
    idxs = [m.start() for m in re.finditer(re.escape(marker), line)]
    spans = []
    for a, b in zip(idxs[0::2], idxs[1::2]):
        spans.append((a, b + len(marker)))
    return spans


def is_labeled_example(line, start, end):
    """True if [start,end) sits inside a quoted or **bolded** span on this
    line -- i.e. the term is being named/cataloged as an example, not
    actually committed in running prose. Checked against straight double
    quotes and markdown bold markers, since that covers how this catalog
    itself labels the patterns it documents."""
    for marker in ('"', "**"):
        for a, b in _paired_spans(line, marker):
            if a <= start and end <= b:
                return True
    return False


def extract_prose(text):
    """Return only prose paragraph lines: strip YAML frontmatter, tables,
    list items, headers, and fenced code blocks. Returns list of
    (line_number, line_text). Frontmatter is excluded because a SKILL.md
    description legitimately needs to name example terms for triggering
    (per skill-creator's guidance to be concrete and "pushy") -- that's
    metadata naming its subject, not prose committing the pattern."""
    lines = text.splitlines()
    frontmatter_end = None
    if lines and lines[0].strip() == "---":
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                frontmatter_end = idx
                break

    prose_lines = []
    in_code_block = False
    for i, line in enumerate(lines, start=1):
        if frontmatter_end is not None and i <= frontmatter_end + 1:
            continue
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if not stripped:
            continue
        if stripped.startswith("|"):  # markdown table row
            continue
        if stripped.startswith(("-", "*", "+")) and len(stripped) > 1 and stripped[1] == " ":
            continue  # bullet list item
        if re.match(r"^\d+\.\s", stripped):
            continue  # numbered list item
        if stripped.startswith("#"):
            continue  # header
        if stripped.startswith("["):  # checklist-style lines e.g. "[ ] ..."
            continue
        prose_lines.append((i, line))
    return prose_lines


def scan(text):
    prose = extract_prose(text)
    prose_text = "\n".join(l for _, l in prose)

    findings = {
        "em_dash": [],
        "banned_vocab": [],
        "claude_phrases": [],
        "its_not_x_its_y": [],
        "excluded_as_example": [],
        "sentence_uniformity": None,
        "parenthetical_density": None,
    }

    for lineno, line in prose:
        for m in re.finditer(re.escape(EM_DASH), line):
            entry = {"line": lineno, "text": line.strip()}
            bucket = "excluded_as_example" if is_labeled_example(line, m.start(), m.end()) else "em_dash"
            findings[bucket].append(dict(entry, category="em_dash") if bucket == "excluded_as_example" else entry)
        for w in BANNED_WORDS:
            for m in re.finditer(r"\b" + re.escape(w) + r"\b", line, re.IGNORECASE):
                entry = {"line": lineno, "word": w, "text": line.strip()}
                bucket = "excluded_as_example" if is_labeled_example(line, m.start(), m.end()) else "banned_vocab"
                findings[bucket].append(dict(entry, category="banned_vocab") if bucket == "excluded_as_example" else entry)
        for p in CLAUDE_PHRASES:
            for m in re.finditer(re.escape(p), line, re.IGNORECASE):
                entry = {"line": lineno, "phrase": p, "text": line.strip()}
                bucket = "excluded_as_example" if is_labeled_example(line, m.start(), m.end()) else "claude_phrases"
                findings[bucket].append(dict(entry, category="claude_phrases") if bucket == "excluded_as_example" else entry)
        for m in ITS_NOT_X_ITS_Y.finditer(line):
            entry = {"line": lineno, "text": line.strip()}
            bucket = "excluded_as_example" if is_labeled_example(line, m.start(), m.end()) else "its_not_x_its_y"
            findings[bucket].append(dict(entry, category="its_not_x_its_y") if bucket == "excluded_as_example" else entry)

    # Sentence-length uniformity (heuristic, not a hard gate)
    sentences = re.split(r"(?<=[.!?])\s+", prose_text)
    sentences = [s for s in sentences if len(s.split()) >= 3]
    if len(sentences) >= 3:
        lengths = [len(s.split()) for s in sentences]
        stdev = statistics.pstdev(lengths)
        mean = statistics.mean(lengths)
        narrow_band = sum(1 for l in lengths if abs(l - mean) <= 3) / len(lengths)
        findings["sentence_uniformity"] = {
            "sentence_count": len(sentences),
            "mean_words": round(mean, 1),
            "stdev_words": round(stdev, 1),
            "fraction_within_3_words_of_mean": round(narrow_band, 2),
            "flag": bool(stdev < 4 and narrow_band > 0.7 and len(sentences) >= 3),
        }

    # Parenthetical density (heuristic, not a hard gate)
    word_count = len(prose_text.split())
    paren_count = prose_text.count("(")
    if word_count > 0:
        density = paren_count / word_count * 1000  # per 1000 words
        findings["parenthetical_density"] = {
            "count": paren_count,
            "per_1000_words": round(density, 1),
            "flag": bool(density > 8 and paren_count >= 3),
        }

    return findings


def hard_gate_failed(findings):
    return bool(
        findings["em_dash"]
        or findings["banned_vocab"]
        or findings["claude_phrases"]
        or findings["its_not_x_its_y"]
    )


def print_report(findings):
    print("=== scan_tells.py report ===")
    print(f"Em dash hits: {len(findings['em_dash'])}")
    for f in findings["em_dash"][:10]:
        print(f"  line {f['line']}: {f['text'][:100]}")
    print(f"Banned vocabulary hits: {len(findings['banned_vocab'])}")
    for f in findings["banned_vocab"][:10]:
        print(f"  line {f['line']} [{f['word']}]: {f['text'][:100]}")
    print(f"Claude-specific phrase hits: {len(findings['claude_phrases'])}")
    for f in findings["claude_phrases"][:10]:
        print(f"  line {f['line']} [{f['phrase']}]: {f['text'][:100]}")
    print(f"'It's not X, it's Y' hits: {len(findings['its_not_x_its_y'])}")
    for f in findings["its_not_x_its_y"][:10]:
        print(f"  line {f['line']}: {f['text'][:100]}")

    if findings["excluded_as_example"]:
        print(f"Excluded as labeled example (quoted/bolded, not counted against gate): {len(findings['excluded_as_example'])}")
        for f in findings["excluded_as_example"][:10]:
            print(f"  line {f['line']} [{f['category']}]: {f['text'][:100]}")

    su = findings["sentence_uniformity"]
    if su:
        flag = "FLAG" if su["flag"] else "ok"
        print(
            f"Sentence uniformity (heuristic): {su['sentence_count']} sentences, "
            f"mean {su['mean_words']}w, stdev {su['stdev_words']}, "
            f"{su['fraction_within_3_words_of_mean']*100:.0f}% within 3 words of mean [{flag}]"
        )
    else:
        print("Sentence uniformity (heuristic): not enough sentences to assess")

    pd = findings["parenthetical_density"]
    if pd:
        flag = "FLAG" if pd["flag"] else "ok"
        print(f"Parenthetical density (heuristic): {pd['count']} parens, {pd['per_1000_words']}/1000 words [{flag}]")
    else:
        print("Parenthetical density (heuristic): no prose to assess")

    gate = "FAIL" if hard_gate_failed(findings) else "PASS"
    print(f"\nHard gate: {gate}")


def main():
    args = [a for a in sys.argv[1:] if a != "--json"]
    if len(args) != 1:
        print("Usage: python scan_tells.py <file> [--json]   (use - for stdin)")
        sys.exit(2)

    src = args[0]
    if src == "-":
        text = sys.stdin.read()
    else:
        with open(src, "r", encoding="utf-8") as fh:
            text = fh.read()

    findings = scan(text)
    print_report(findings)

    if "--json" in sys.argv:
        print(json.dumps(findings, indent=2))

    sys.exit(1 if hard_gate_failed(findings) else 0)


if __name__ == "__main__":
    main()
