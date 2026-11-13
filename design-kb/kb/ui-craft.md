# UI craft knowledge base

> Online validation 2026-11-12: corrections from `kb/validation.md` are applied below.

Built 2026-11-12 from local clones under /home/claude. Read-only on the repos. Paraphrased; no quote over 15 words.
Tags: rules and facts are [verified] against the cited file unless marked [inferred]. Paths are absolute.

## Scope notes and gaps

- interface-design: the brief listed docs/ and a top-level agents/. Neither exists. agents/openai.yaml sits inside the skill folder. [verified]
- interface-design website/ holds only .vercel metadata, no site source. [verified]
- wireframe: /home/claude/markdown-viewer/wireframe-skill/wireframe is not a git repo. No LICENSE, no version. [verified]
- bluzir/claude-code-design has no LICENSE file. [verified]
- Not read in depth: unslop references/effects.md, visuals.md, tokens.md and story.mjs internals; bluzir starters/*, scripts/*, most of .claude/skills/*; markdown-viewer/skills research/ and scripts/; interface-design design-review body. Tests were not run.
- Other clones under /home/claude (emilkowalski, shadcn-ui, etc.) are out of scope.

---

## 1. heydamir/unslop
Path: /home/claude/heydamir/unslop (HEAD 97daa3e)

**Purpose.** A Claude Code / Codex / Antigravity skill that turns AI-looking UI ("slop") into a designed interface. It audits first, sets a direction from the product, then fixes in nine ordered passes. [verified README.md]

**Structure.**
- skills/unslop/SKILL.md (235 lines): the workflow, direction and nine passes, story video.
- skills/unslop/references/: signs.md (audit list), tokens.md (exact values), visuals.md, effects.md, refs.md, refs/*.webp.
- skills/unslop/scripts/: snapshot.mjs (save a live page as HTML, Playwright), story.mjs (build a ~10s square story video, Playwright + ffmpeg).
- skills/unslop/agents/openai.yaml: Codex UI metadata.
- examples/: two vibecoded screens (dashboard.html, hero.html). test/: two node:test files. CITATION.cff. [verified]

**Rules and checks.**
1. Audit before editing: list every sign with its location, using signs.md. Keep it to one line each. [verified SKILL.md "Run it" step 2]
2. Pick a mode: heavy slop (full nine passes), light slop (polish only, keep the existing brand), or no slop (say so, offer at most three small refinements). [verified SKILL.md "Run it" step 3]
3. Write a five-line direction (product, character, world, moments, signature) before editing. Wait for the user unless they said to just do it. [verified SKILL.md "Direction" and step 4]
4. Ban generic character words such as clean, modern, sleek, minimal, premium. [verified SKILL.md "Direction"]
5. Spacing on a 4px grid; replace one-off values like mt-[13px] with scale steps. [verified SKILL.md section 1]
6. Neutral surfaces with one rare accent. Remove hue-to-hue gradients, gradient text and colored glows. Hairline borders at 6 to 10% opacity. [verified SKILL.md section 2]
7. One icon set, 16 or 18px, 1.5 stroke; drop decorative emoji. [verified SKILL.md section 3]
8. Sentence case, weights 400 and 500 (600 rare), no 700 to 900 headings, no uppercase tracked labels. [verified SKILL.md section 5]
9. Nested radius equals outer radius minus padding, minimum 4. [verified SKILL.md section 7]
10. Remove looping motion, transition-all, hover scale on cards. Animate only transform and opacity; name the properties. [verified SKILL.md section 9]
11. Do not invent proof claims ("10x faster"). Confirm with the user or remove them, and list them in the report. [verified SKILL.md section 4]
12. Render again after the passes and compare with the audit list; fix anything still on it. [verified SKILL.md "Run it" step 6]
13. Keep a visual-generation rule: ask before every paid image generation; dashboards rarely need images. [verified README.md "What it does"]

**Commands and install.** [verified README.md]
- Claude Code: `git clone https://github.com/heydamir/unslop` then `cp -r unslop/skills/unslop ~/.claude/skills/` (or into a project's .claude/skills/).
- Codex: `$skill-installer install https://github.com/heydamir/unslop/tree/main/skills/unslop`, or copy into ~/.agents/skills/.
- Snapshot and story need `npm install -D playwright` and `npx playwright install chromium`, run in the project folder.
- `node <skill>/scripts/snapshot.mjs <url> unslop/original.html [label] [--dark|--light] [--width N] [--height N]` [verified snapshot.mjs usage string]
- `node <skill>/scripts/story.mjs <story.html> <out.mp4> [--wide]`, or `--play` to watch live. [verified story.mjs usage string]
- Tests: `node --test test/` [inferred: no package.json; files use node:test]

**License.** CC BY 4.0 (LICENSE; SKILL.md frontmatter; CITATION.cff). Credit the author (Damir Sokolovsky, @heydamir) and link the repo in any copy. LICENSE is byte-identical to /home/claude/markdown-viewer/skills/LICENSE. [verified]

**Gotchas.**
- No package.json. Playwright must be installed in the user's project, not in the skill. [verified README.md]
- Story video also needs ffmpeg on PATH. [verified README.md]
- snapshot.mjs drops script-drawn animated backgrounds; the audit must describe them from the live page. [verified SKILL.md step 1]
- .gitignore keeps only the two example HTML files and the assets folder under examples/. [verified .gitignore]
- Redesign output is meant to be handed to the site owner, so say so in the report. [verified SKILL.md step 1]

---

## 2. dammyjay93/interface-design
Path: /home/claude/dammyjay93/interface-design (HEAD 2f9be32)

**Purpose.** Craft-first skill for product UI: dashboards, admin panels, SaaS apps, settings, data tools. It explicitly excludes marketing and landing pages. It also saves decisions to `.interface-design/system.md`. The repo was renamed from claude-design-skill (README line 336); the old URL still resolves to HEAD 2f9be32. [verified README.md; SKILL.md "Scope"; online]

**Structure.**
- .claude/skills/interface-design/SKILL.md (320 lines) and agents/openai.yaml.
- .claude/commands/: design-review.md (strict craft review, reports only), design-deslop.md (diff-scoped slop strip).
- .claude-plugin/: plugin.json and marketplace.json (version stamped by hook).
- .githooks/pre-commit: stamps a version on each commit.
- reference/: system-template.md plus two example systems (warmth, precision).
- website/.vercel/: metadata only. [verified]

**Rules and checks.**
1. Intent first: name the person, the task and the feel. Ask one question if the prompt cannot identify them. [verified SKILL.md "Intent First"]
2. Explore the domain before proposing: at least five domain concepts, five colors from that world, one signature element, and three default choices to reject. [verified SKILL.md "Product Domain Exploration"]
3. Before every component, state intent, hierarchy, palette, depth, surfaces, typography and spacing, each with a reason. [verified SKILL.md "Before Writing Each Component"]
4. Use what exists: native HTML first, then a headless primitive for stateful controls, hand-roll last and then owe the full keyboard and ARIA contract. [verified SKILL.md "Use What Exists"]
5. Pick one depth strategy and keep it: borders only, subtle shadows, layered shadows, or surface shifts. Do not mix. [verified SKILL.md "Design System Essentials"]
6. Dark themes: step surfaces by a few percent of lightness and use low-alpha white borders; shadows do not read on dark. [verified SKILL.md "Subtle Layering" and "Polish"]
7. Type: pick a ratio around 1.2 to 1.333, and make hierarchy with weight and color before size. [verified SKILL.md "Type scale"]
8. Motion: keep UI under 300ms, use an ease-out curve, animate only transform and opacity, never scale from 0, and skip animation on actions repeated many times a day. [verified SKILL.md "Motion"]
9. Run four checks before showing work: swap, squint, signature (point to five elements), token (read the variable names aloud). [verified SKILL.md "The checks"]
10. Verify visually at desktop and mobile widths before presenting. [verified SKILL.md "Execution discipline" 5]
11. After the task, offer to save decisions to `.interface-design/system.md`. Once saved, hold later work to those values. [verified SKILL.md "After Completing a Task"]
12. Show a live specimen only when an inline render tool exists; otherwise fall back to code and tokens. [verified SKILL.md "Render It When You Can"]

**Commands and install.** [verified README.md; command files]
- `npx skills add https://github.com/dammyjay93/interface-design --skill interface-design --agent claude-code -g`
- Manual: `cp -R .claude/skills/interface-design ~/.claude/skills/`, or to ~/.agents/skills/ for Codex.
- Plugin: `/plugin marketplace add Dammyjay93/interface-design`, then select interface-design and restart.
- Slash commands: `/interface-design`, `/interface-design:design-review`, `/interface-design:design-deslop`.

**License.** MIT, copyright 2026 Damola Akinleye. [verified LICENSE; plugin.json author]

**Gotchas.**
- pre-commit uses BSD `sed -i ''` syntax. On GNU/Linux sed this fails. [verified script text; failure on Linux is [inferred]]
- Nothing in the repo sets `core.hooksPath` to .githooks, so the hook may never run. [verified grep: no mention in docs; [inferred] it is not wired]
- Every commit rewrites the plugin version in two JSON files. [verified pre-commit]
- The skill sits in the same family as unslop and design-lean but targets product UI only. Use unslop for landing pages. [verified SKILL.md scope; [inferred] on the pairing]
- Skills run with the agent's permissions; the README says to review them first. [verified README.md]
- Default fonts (Inter, system) are flagged as defaults when a direction was set. [verified SKILL.md "Avoid"]

---

## 3. bluzir/claude-code-design
Path: /home/claude/bluzir/claude-code-design (HEAD ce68c84)

**Purpose.** A Claude Code workspace that reproduces Anthropic Labs' Claude Design outputs (HTML decks, prototypes, design systems, animated videos) through skills, starter components and Chrome DevTools MCP. Self-described as a research and personal tool, macOS-first. [verified README.md, CLAUDE.md]

**Structure.**
- CLAUDE.md (workspace rules, anti-patterns, verification gates), README.md, GETTING_STARTED.md.
- .claude/skills/: 19 skill folders (README says 20; directory count is 19) (make-deck, interactive-prototype, wireframe, animated-video, create-design-system, ingest-*, export-*, verify-artifact, etc.).
- .claude/commands/: done, preview, screenshot, serve.
- starters/: deck_stage.js, device_frame.jsx, design_canvas.jsx, animations.jsx.
- scripts/: export-pdf.mjs, export-pptx.mjs, make-assets-index.mjs.
- test/: three smoke HTML pages. package.json: pptxgenjs, puppeteer. [verified]

**Rules and checks.**
1. Route the request to a skill through the keyword table in CLAUDE.md. [verified CLAUDE.md "Core workflow"]
2. Phase 0 before asking: read project tokens, check the org registry, glob codebase tokens. Then ask one consolidated question. [verified CLAUDE.md "Agent-autonomy discipline"]
3. Ambiguity gate: if two of audience, style and length are given, ask at most one or two questions. [verified CLAUDE.md "Ambiguity gate"]
4. Copy starters into the artifact folder rather than referencing them with a relative path. [verified CLAUDE.md "Artifact flow" 2]
5. Artifacts that load external .jsx need /serve (python3 http.server on 127.0.0.1:4567). file:// fails on CORS. [verified CLAUDE.md; serve.md]
6. Never edit artifact HTML without an explicit request. The tweak panel only buffers changes to pending.yaml. [verified CLAUDE.md "Tweaks persistence"]
7. Pin React 18.3.1 and Babel 7.29.0 with integrity hashes. Never declare a top-level `const styles`; prefix names per component. [verified CLAUDE.md "React + Babel contract"]
8. Anti-patterns: no Inter, Roboto, Arial or Fraunces; no emoji unless asked; no aggressive gradients; no rounded card with a left accent border; no invented stats. [verified CLAUDE.md "Anti-patterns"]
9. Minimum sizes: slide text 24px or more; print 12pt or more; mobile hit targets 44px or more. [verified CLAUDE.md "Scales"]
10. Done gate: a clean console, a verify-artifact pass, and a screenshot path quoted in the summary. [verified CLAUDE.md "Verification"]
11. Deck gate: hard-reload with cache bypass. Any overflow above 0 fails; headroom under 40px warns. [verified CLAUDE.md "Deck-specific gate"]
12. Wireframes are greyscale, use placeholders, show at least three options on a design canvas, and mix conservative with novel options. [verified .claude/skills/wireframe/SKILL.md]

**Commands and install.** [verified README.md, GETTING_STARTED.md, package.json]
- `git clone https://github.com/bluzir/claude-code-design.git`, then open Claude Code in that folder and run `/doctor`.
- `claude mcp add chrome-devtools -s user -- npx chrome-devtools-mcp@latest` (needs a restart).
- `brew install monolith` (only for /export-standalone). `npm install -D pptxgenjs puppeteer` (PPTX and PDF export).
- Node 20 or newer for the scripts. Optional: `gh` for /ingest-github, FIGMA_TOKEN for /ingest-figma.

**License.** No LICENSE file in the repo. README.md says MIT; package.json says ISC. The two disagree. Treat it as unlicensed until the owner confirms. [verified file list and both declarations; the conservative reading is [inferred]]

**Gotchas.**
- CLAUDE.md says the toolset is stateless with no local servers, yet /serve and JSX artifacts need one. The two statements conflict. [verified CLAUDE.md "No server" and serve.md]
- Requirements are macOS-first; GETTING_STARTED says Linux is untested. [verified GETTING_STARTED.md]
- PPTX export is screenshots only, not editable shapes. [verified README.md "Export"]
- Chrome DevTools MCP round trip is about 6 to 10 seconds, so there is no sub-second preview loop. [verified README.md "Parity status"]
- The project reproduces a named vendor product's outputs and taste rules. Check attribution and IP before reuse. [inferred]
- artifacts/ is git-ignored; assets and tweak logs live there. [verified README.md architecture]

---

## 4. markdown-viewer/wireframe-skill/wireframe (recovered copy)
Path: /home/claude/markdown-viewer/wireframe-skill/wireframe. Not a git repo.

**Purpose.** A drawio-based wireframe generator for web pages, iOS, Android and admin dashboards. Output is a fenced drawio block that Markdown Viewer renders. [verified SKILL.md] **Status.** Removed from upstream markdown-viewer/skills in commit 2da9334 (2026-04-11), which deleted wireframe/SKILL.md and all four examples. No wireframe path exists at HEAD 2672b69. This copy is the pre-removal version (commit 02052ea, 2026-03-26). [verified online]

**Structure.** SKILL.md (31 lines) and examples/: web-landing-page.md, dashboard-admin.md, ios-app-login.md, android-app-list.md. Each example has one drawio block. [verified]

**Rules and checks.**
1. Use a ```drawio fence. Never a ```xml fence, which does not render. [verified SKILL.md]
2. Spacing: 10px tight, 20px normal, 40px between sections. [verified SKILL.md]
3. Canvas sizes: iPhone 375x812, Android 360x800, desktop web 1200 or 1440 wide. [verified SKILL.md]
4. Pick a type from the table: web (mxgraph.mockup.*), iOS (mxgraph.ios7.*), Android (mxgraph.android.*), dashboard (mxgraph.mockup.*). [verified SKILL.md table]
5. Follow the base drawio rules for structure and edge routing, and check the stencil list before naming a shape. [verified SKILL.md; base files missing, see gotchas]

**Commands and install.** None recovered. Viewing needs Markdown Viewer (Chrome, Edge, Firefox or VS Code extension). [verified SKILL.md metadata]

**License.** Not established. The folder has no LICENSE. The sibling markdown-viewer/skills is CC BY 4.0. Do not assume the same terms. [verified absence; [inferred] on the reading]

**Gotchas.**
- Broken links: ../drawio/SKILL.md and ../drawio/stencils/README.md are not in the recovered copy. [verified]
- Every example says it is based on a layout/*.drawio template (wireframe_1, wireframe_2, wireframe_iphone, wireframe_android_phone). None is included. [verified]
- Metadata holds promotional copy and a product link. [verified SKILL.md frontmatter]
- The sibling documd-visuals package says drawio is not recommended for its output. The two skills disagree on tooling. [verified documd-visuals frontmatter]

---

## 5. markdown-viewer/skills (current head, summary only)
Path: /home/claude/markdown-viewer/skills (HEAD 2672b69). This repo no longer contains the wireframe skill; it was removed on 2026-04-11 (commit 2da9334). A third-party listing (skills.sh) still advertises it and is stale. [verified online]

**Purpose.** A package of agent skills for the docu.md Markdown pipeline. The single skill, documd-visuals, routes requests to text-based charts, diagrams, cards and layouts that render live in Markdown. [verified README.md, documd-visuals/SKILL.md]

**Structure.** documd-visuals/ (SKILL.md router, converting.md, catalog/, goals/, engines/, examples/, styles/), research/ (echarts, plantuml, vega, html-css, infographic), scripts/ (check-all, verify-examples, check-palette-contrast and others). [verified]

**Rules and checks.** Route by the reader's goal. Figures are text inside the Markdown. Not for slide decks or math. Themes come from styles/. Scripts gate theme drift, contrast and block coverage. [verified README.md, SKILL.md frontmatter]

**Commands and install.** `npx skills add markdown-viewer/skills`, or `cp -r skills/documd-visuals ~/.claude/skills/`. Optional export: `npx @markdown-viewer/documd` (Node 18+, Chrome or Chromium). [verified README.md, SKILL.md compatibility]

**License.** CC BY 4.0. The top LICENSE is byte-identical to unslop's. documd-visuals/LICENSE.md is a different file. [verified md5]

**Gotchas.**
- The README counts were recounted on 2026-11-12 and match: 242 example files, 183 scenarios in catalog/scenarios.json, 31 goal files in goals/. [verified online validation]
- The recent head commits made the documd CLI optional and removed the dot engine, so older guidance may mention dot. [verified git log]
