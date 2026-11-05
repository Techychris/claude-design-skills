---
name: remove-ai-tells
description: Detects and strips recognizable AI-writing tells from drafted text before it goes out to a reader. Covers em dashes, banned filler vocabulary (delve, tapestry, leverage, moreover, and similar), the "it's not X, it's Y" construction, overused parenthetical asides, uniform same-length sentences, and phrases like "you're absolutely right" or "I'd be happy to." Use this any time someone asks to make writing sound less like AI, remove AI tells, humanize a draft, check for em dashes, or asks whether a piece sounds like ChatGPT or Claude wrote it. Also use proactively before handing back any long-form document, email, article, or report that Claude drafted, since Claude's own output is the primary source of these patterns. Runs a bounded detect-rewrite-verify pass and reports what changed with confidence labels, rather than doing a single blind find-and-replace.
---

# Remove AI Tells

## Mechanism

Models overuse specific words and punctuation because their training data for polished prose (books, journalism, academic writing) contains those patterns far more densely than casual human writing does. Token-by-token sampling keeps landing on them because they sit high in the probability distribution for that context. A model has no paragraph-level self-awareness that it already used three em dashes, so it can't catch the pattern the way a human editor reading their own work back would. This is why a naive find-and-replace on one word or one character doesn't fix anything: the sentence rhythm underneath is still what gives it away. See `references/tell-catalog.md` for the full list with per-item mechanism notes and confidence tags (verified, single-source, or heuristic).

## Architecture

This is a bounded evaluator-optimizer loop, not a single pass and not an open-ended agent. The steps are fully known in advance, so there's no need for a planner that improvises what to do next.

1. **Detect.** Run `scripts/scan_tells.py` against the text. If the text was pasted into the conversation rather than uploaded as a file, write it to a temp file first or pipe it through stdin (`python scan_tells.py -`). The script scans prose paragraphs only; it skips markdown tables, list items, and code blocks, so a document that catalogs or discusses these terms doesn't get flagged for its own examples. Read the printed report rather than assuming what it will say.
2. **Rewrite.** For every hit in a hard-gated category (em dash, banned vocabulary, "it's not X, it's Y," Claude-specific phrases), apply the fix from the catalog. Rewrite the clause; don't do a character swap. Replacing an em dash with a hyphen everywhere, with no other change, is itself a recognizable pattern and should never be the applied fix.
3. **Verify.** Re-run the script on the full rewritten text, not just the edited lines, since a fix in one place can introduce a new instance elsewhere or overcorrect into a different tell. Heavy parenthetical use after stripping every em dash is a common overcorrection to watch for. If a hard-gated category still shows hits, do one more rewrite pass targeting only what remains.
4. **Stop condition.** Cap at two rewrite passes total. If hits remain after that, report them plainly instead of forcing a fix that would mangle the text or silently claiming a clean result. This cap matches the general finding that a first revision pass captures most of the available improvement, while further passes tend to plateau or regress rather than keep improving.

If `scan_tells.py` can't run in the current environment (no code execution available), fall back to `references/tell-catalog.md` and check manually against Sections 1 through 4. Flag in the output that this was a manual pass, since a human read-through catches different things than a regex does, and say so rather than presenting it as equivalent.

## Reading the script's output

Treat a hit in em dash, banned vocabulary, the "it's not X, it's Y" pattern, or the Claude-specific phrase list as a real problem to fix, not a judgment call: these are the hard-gated, mechanically-checkable categories. Sentence-length uniformity and parenthetical density are printed as heuristic flags, not gates: they catch a real pattern often enough to be worth a look, but plenty of legitimate human writing has a run of similar-length sentences too, so weigh whether the flagged passage actually reads as robotic before rewriting it. Note that the uniformity check averages across the whole document, so a locally uniform paragraph can hide inside an otherwise varied piece and never trip the flag; skim multi-paragraph text by eye for this even when the overall score reads fine. "Load-bearing" and "honest take" aren't in the script at all, because both have completely literal, non-tell meanings that a keyword match would misfire on constantly; watch for them by reading, not by regex.

## Output format

Lead with the cleaned text. Follow it with a short change log: category, count found, count fixed, and a confidence label carried over from the catalog. Match the length of the report to the length of the input; a three-sentence email doesn't need the same write-up as a ten-page report. Don't produce a full rubric-style breakdown unless asked for one.

## Maintaining this skill

This skill's entire purpose is catching AI tells, so its own files are held to that standard rather than exempted from it. Before saving any change to this file or to `references/tell-catalog.md`, run `scripts/scan_tells.py` against both and confirm the hard gate passes. Legitimate exclusions, meaning a term named in quotes or bold as a cataloged example, should show up in the excluded-as-example list rather than silently vanishing.
