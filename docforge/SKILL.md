---
name: docforge
description: "Create polished, professionally designed Word documents from a JSON spec — reports, memos, letters, executive briefs, and meeting minutes with real cover pages, TOCs, styled tables, callouts, metric rows, and embedded diagrams. Use this skill INSTEAD of writing ad-hoc docx-js code whenever the user wants to CREATE a new .docx deliverable: any mention of 'report', 'memo', 'letter', 'proposal', 'brief', 'minutes', 'Word doc', or 'professional document', including ones that need a flowchart, architecture sketch, or process diagram inside them. Pick a template, fill the spec, build, verify. Do NOT use for editing existing .docx files, tracked changes, or comments — defer to the default docx skill for those."
---

# docforge — themed document template system

Turns a small JSON spec into a designed .docx. Four themes × five templates × twenty-one block types, one entry point. All paths below are relative to this skill's directory.

## Workflow

1. Pick the closest template in `templates/` (see table) and a theme.
2. Copy it, replace the content, keep the block structure. If a section needs a flowchart, architecture sketch, or process diagram, generate it first with `diagram-forge` (`/mnt/skills/user/diagram-forge/scripts/diagram_kit.py`), run that skill's own required checks (overlap, border clipping, a look at the image), then reference the resulting PNG path in an `image` block. Never hand-roll a diagram with ad-hoc matplotlib or PIL code here; diagram generation and document assembly stay in their own skills on purpose.
3. Scrub drafted text for AI writing tells before treating it as final: `node scripts/extract_text.js myspec.json | python3 /mnt/skills/user/remove-ai-tells/scripts/scan_tells.py -`. Fix any hard-gated hits directly in the spec's text fields and re-run; cap it at two passes, the same bounded loop that skill documents. This is cheap enough to run on every document, not just high-stakes ones.
4. Build: `node scripts/build.js myspec.json out.docx`
5. Verify before delivering (required): `bash scripts/gates.sh myspec.json out.docx` — builds, renders to PDF via LibreOffice, checks text and page render for *that specific document*. Then look at the rendered page images yourself. (Running `bash scripts/gates.sh` with no arguments instead regression-tests the five bundled templates — useful when changing `build.js`/`components.js`/`themes.js`, not for verifying a document you're about to deliver.)
6. For a stakeholder-facing or otherwise high-stakes document, consider one more pass beyond step 3's mechanical scrub: `brknpipe`'s content-quality review, checking mechanism depth on any causal claim, a requirement-grounded rubric, and a self-referential cross-check if the document itself describes a rule-set or process. Most documents don't need this; reserve it for the ones where being wrong actually costs something, per that skill's own mode-selection guidance.
7. Deliver the .docx (and mention: Word will prompt "update fields" on open — answer Yes to populate the TOC/page counts).

## Templates

| File | Use for | Shows off |
|---|---|---|
| `templates/report.json` | Multi-section reports, reviews, proposals | cover, TOC, metrics, tables, callouts, quote, image |
| `templates/memo.json` | Internal announcements, policy changes | memohead (TO/FROM/DATE/RE), numbered, callout |
| `templates/letter.json` | Formal external correspondence | letterhead, signoff, no page chrome |
| `templates/brief.json` | One-page executive status | metrics row, tight sections |
| `templates/minutes.json` | Meeting minutes | kv block, decisions callout, action-item table |

## Themes (`scripts/themes.js`)

`boardroom` navy/rust, Segoe UI + Georgia · `editorial` oxblood/brass, Garamond + Georgia · `slate` charcoal/teal, all Segoe UI · `meridian` steel-blue/coral, Cambria + Calibri. All fonts are Word-safe. Add a theme by adding one token object: every component and style derives from tokens, and nothing is hard-coded.

## Spec schema (exactly what `scripts/build.js` implements)

```json
{ "theme": "boardroom",
  "meta": { "title": "...", "subtitle": "...", "org": "...", "author": "...",
            "version": "...", "for": "...", "date": "auto if omitted",
            "to/from/re": "memo fields" },
  "chrome": { "header": true, "footer": true },
  "blocks": [ ... ] }
```

`chrome` toggles the running header (title left, org right) and footer ("Page X of Y" fields; footer defaults on, so pass `false` for letters). When a `cover` block is present, both are automatically suppressed on the cover page (Word title-page section).

Block types, where `text` fields support `**bold**` and `*italic*`:

| Type | Fields | Renders |
|---|---|---|
| `cover` | uses meta (+overrides) | org band, title, subtitle, accent rule, meta lines, page break |
| `toc` | — | "Contents" + real Word TOC field (updates on open) |
| `h1` `h2` `h3` | `text` | themed headings (feed the TOC) |
| `p` | `text` | body paragraph |
| `bullets` / `numbered` | `items[]` | proper Word list numbering |
| `table` | `headers[]`, `rows[][]`, `widths[]` (ratios) | header band, zebra stripes, hairline rules |
| `callout` | `title`, `text`, `variant: note|warn|success` | tinted box, colored left bar |
| `metrics` | `items[{value,label}]` | big-number stat row |
| `kv` | `pairs[[k,v]]` | label/value block (minutes, memo fields) |
| `quote` | `text`, `by` | accent-barred pull quote |
| `image` | `src`, `widthIn` (optional), `caption` (optional) | centered PNG/JPG, scaled to fit content width (or `widthIn`), capped at 8in tall |
| `rule` | `accent: bool` | horizontal rule (paragraph border, never a table) |
| `caption` `spacer` `pagebreak` | `text` / `pt` / — | as named |
| `memohead` | uses meta to/from/re | MEMORANDUM header |
| `letterhead` | `senderLines[]`, `recipientLines[]` | letter opening block |
| `signoff` | `closing`, `name`, `title` | letter closing block |

Unknown block types fail loudly with the valid list. Fix the spec, don't patch the engine.

## Working with other skills

**diagram-forge → `image` block.** `src` is a path to a PNG or JPG, resolved relative to the current working directory at build time (same convention as the spec and output paths). Dimensions are read from the file itself, so an image never needs its aspect ratio stated by hand; it scales to fit the content width unless `widthIn` sets something narrower, and a document's own `assets/` folder is a reasonable place to keep one built for that document specifically.

**remove-ai-tells → `scripts/extract_text.js`.** Pulls the actual prose out of a spec (titles, headings, body paragraphs, bullets, callouts, quotes) while skipping table cells and key-value pairs, since those are data, not writing, and would only add noise to a sentence-level scan. Pipe its output straight into the scanner rather than saving an intermediate file.

**brknpipe → content review.** Where `gates.sh` checks that a document is structurally sound (compiles, renders, isn't blank), brknpipe checks whether the writing itself holds up: does a claim's explanation reach the actual mechanism or stop at the symptom, does the rubric reflect what the stakeholder actually asked for. The two layers are complementary, not redundant. A document can pass every gate in `gates.sh` and still have a hollow executive summary.

## Rules

- Never hand-write docx-js for a new document if a template fits; extend the spec instead.
- Never hand-roll a diagram in matplotlib/PIL when diagram-forge already does this; generate the PNG there and reference it with an `image` block.
- Custom one-off needs → add a block type to `scripts/build.js` + component in `scripts/components.js`, keep theme tokens as the only source of fonts/colors/sizes. A new block type also needs at least one bundled template using it, or the coverage gate in `gates.sh` will fail.
- Run the AI-tell scan on drafted text before treating it as final, not just on documents that feel high-stakes; it costs one command.
- Always run `gates.sh` and view the rendered pages before delivering. A document you haven't looked at is not done.
- Editing an existing .docx, tracked changes, comments, or reading .docx content → use the default `docx` skill, not this one.
