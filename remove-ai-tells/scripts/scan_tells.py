#!/usr/bin/env python3
"""
scan_tells.py -- deterministic scanner for mechanically-checkable AI writing tells.

Usage:
    python scan_tells.py <file>
    cat draft.txt | python scan_tells.py -

Scans prose paragraphs, list items, and headers. Markdown table rows, fenced
code blocks, and YAML frontmatter are excluded. A term written inside quotes
or **bold** counts as a labeled example (a document naming the pattern rather
than committing it) and is reported separately instead of failing the gate.
Curly quotes and apostrophes are normalized first, so text pasted from Word or
Google Docs is matched the same as plain text.

Exit code 0 = no hard-gate hits. Exit code 1 = at least one hard-gate hit.
Hard-gate categories: em dash, banned vocabulary, Claude phrases, and the
"it's not X, it's Y" contrast (same-sentence and split-sentence forms).
Heuristic categories (reported but not gating): sentence-length uniformity,
parenthetical density, dash substitutes (spaced en dash or double hyphen).
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

# Negated subject + contrast clause. Run on apostrophe-normalized text.
_NEG = r"(?:it'?s not|it is not|it isn'?t|this is not|this isn'?t|that'?s not|that is not|that isn'?t|isn'?t|is not|wasn'?t|was not|aren'?t|are not)"
_POS = r"(?:it'?s|it is|it was|this is|that'?s|that is|they'?re|they are)"
ITS_NOT_X_ITS_Y = [
    # "It's not X, it's Y" / "isn't X; it's Y" (one sentence)
    re.compile(r"\b" + _NEG + r"\b[^.!?]{0,80}?[,;:]\s*" + _POS + r"\b", re.IGNORECASE),
    # "This isn't about X. It's about Y." (split across two sentences)
    re.compile(r"\b" + _NEG + r"\b[^.!?]{0,80}?[.!?]\s+" + _POS + r"\b", re.IGNORECASE),
]

# Common ways an em dash gets swapped out without rewriting the sentence.
DASH_SUBSTITUTES = re.compile(r"\s(?:\u2013|--)\s")

QUOTE_NORMALIZE = str.maketrans({"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"'})

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
    """Return scannable lines as (line_number, line_text, kind), where kind is
    "prose", "list", or "header". YAML frontmatter, markdown table rows, and
    fenced code blocks are dropped. List and header markers are stripped so
    they don't affect matching. Frontmatter is excluded because a SKILL.md
    description legitimately needs to name example terms for triggering;
    that's metadata naming its subject, not prose committing the pattern."""
    lines = text.splitlines()
    frontmatter_end = None
    if lines and lines[0].strip() == "---":
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                frontmatter_end = idx
                break

    out = []
    in_code_block = False
    for i, line in enumerate(lines, start=1):
        if frontmatter_end is not None and i <= frontmatter_end + 1:
            continue
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block or not stripped:
            continue
        if stripped.startswith("|"):  # markdown table row
            continue
        m = re.match(r"^(?:[-*+]\s+(?:\[[ xX]\]\s+)?|\d+[.)]\s+|\[[ xX]\]\s+)", stripped)
        if m:
            out.append((i, stripped[m.end():], "list"))
            continue
        if stripped.startswith("#"):
            out.append((i, stripped.lstrip("#").strip(), "header"))
            continue
        out.append((i, line, "prose"))
    return out


def scan(text):
    text = text.translate(QUOTE_NORMALIZE)
    lines = extract_prose(text)
    # Uniformity and density heuristics use running prose only: list items and
    # headers are fragments by design and would skew sentence statistics.
    prose_text = "\n".join(l for _, l, kind in lines if kind == "prose")

    findings = {
        "em_dash": [],
        "banned_vocab": [],
        "claude_phrases": [],
        "its_not_x_its_y": [],
        "excluded_as_example": [],
        "dash_substitutes": [],
        "sentence_uniformity": None,
        "parenthetical_density": None,
    }

    for lineno, line, _kind in lines:
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
        seen_contrast = set()
        for rx in ITS_NOT_X_ITS_Y:
            for m in rx.finditer(line):
                if m.start() in seen_contrast:
                    continue
                seen_contrast.add(m.start())
                entry = {"line": lineno, "text": line.strip()}
                bucket = "excluded_as_example" if is_labeled_example(line, m.start(), m.end()) else "its_not_x_its_y"
                findings[bucket].append(dict(entry, category="its_not_x_its_y") if bucket == "excluded_as_example" else entry)
        for m in DASH_SUBSTITUTES.finditer(line):
            if not is_labeled_example(line, m.start(), m.end()):
                findings["dash_substitutes"].append({"line": lineno, "text": line.strip()})

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

    if findings["dash_substitutes"]:
        print(f"Dash substitutes (heuristic, spaced en dash or --): {len(findings['dash_substitutes'])}")
        for f in findings["dash_substitutes"][:10]:
            print(f"  line {f['line']}: {f['text'][:100]}")

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
