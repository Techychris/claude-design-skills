# OpenDesign (nexu-io/open-design) - knowledge base

> Online validation 2026-11-12: corrections from `kb/validation.md` are applied below.

Source: /home/claude/nexu-io/open-design (read-only, snapshot read 2026-11-12; main HEAD bc06128, package.json version 0.25.1; latest GitHub release open-design-v0.26.1, published 22 Oct, per online validation).
Tags: [verified] = read in the cited file; [inferred] = my conclusion from names or structure.

## 1. Purpose

- OpenDesign is a local-first design workspace. A coding agent CLI already on the user's PATH produces prototypes, decks, images, video and audio from a brief, styled by a brand contract called `DESIGN.md`. [verified] README.md "What is OpenDesign", "Why OpenDesign"
- Output is real HTML/CSS that can be handed to code agents for continued build-out. [verified] README.md "A full workflow"
- Three entry points: desktop app, the `od` CLI, and a stdio MCP server that other agents (Claude Code, Codex, Cursor, etc.) can call. [verified] README.md "Use OpenDesign from your coding agent"
- Two execution modes: Local CLI (daemon spawns the agent, writes project files) and API/BYOK mode (daemon proxies to a provider, returns one `<artifact>` block). [verified] QUICKSTART.md "Two execution modes"
- Domain terms: Project, Normal Artifact vs Live Artifact, Artifact Entry File, Artifact Manifest, Active Project. An MCP-created deck is a Normal Artifact unless the user asks for refreshable data. [verified] CONTEXT.md
- License and posture: Apache-2.0; local daemon binds 127.0.0.1 by default. [verified] README.md "Security model"

## 2. Architecture and structure

Workspace (pnpm): `apps/*`, `packages/*`, `shells/*`, `tools/*`, `e2e`. [verified] AGENTS.md "Workspace directories"

Apps:
- `apps/web`: Next.js 16 App Router + React 18 client. `apps/nextjs` was removed; do not restore it. [verified] AGENTS.md
- `apps/daemon`: Node/Express local daemon. Owns `/api/*`, agent spawning, skills, design systems, artifacts, static serving; the `od` bin is `apps/daemon/src/cli.ts`. [verified] AGENTS.md, QUICKSTART.md file map
- `apps/desktop`: Electron shell. `apps/packaged`: thin packaged runtime entry. `apps/closure`: distributable "Closure" content. [verified] AGENTS.md
- Runtime adapters: 28 entries in `apps/daemon/src/runtimes/defs/`, registered in `apps/daemon/src/runtimes/registry.ts`. [verified] README.md, file count

Packages (19 dirs): `contracts` (pure TS shared web/daemon DTOs, no Node/Next/browser APIs), `sidecar-proto` (business DTOs and action names), `sidecar` (business-agnostic sidecar client), `platform` (OS process primitives), `standalone` (exact metadata, verification and launcher contract). [verified] AGENTS.md. Remaining names (agui-adapter, components, dsh-runtime, plugin-runtime, registry-protocol, release, etc.) are [inferred] from names only.

Shells: `shells/terminal` is the official Node carrier. [verified] AGENTS.md

Tools: `tools/dev` (`pnpm tools-dev` lifecycle), `tools/pack` (packaging, updater harness), `tools/serve` (fixture services such as the updater), `tools/release`. [verified] AGENTS.md

Content (not code), with counts from `find`:
- `skills/`: 169 SKILL.md. Functional capabilities the agent invokes mid-task. [verified]
- `design-templates/`: 116 entries, 115 SKILL.md. Rendering shapes (prototype, deck, image, video, audio, utility). [verified]
- `design-systems/`: 152 packages, each with manifest.json, DESIGN.md, tokens.css. [verified]
- `craft/`: 12 rule files plus README. Brand-agnostic craft rules injected on opt-in. [verified]
- `plugins/`: `_official/` (video-templates 23, scenarios 14, atoms 13, plus an examples tree), `community/` (10 folders), `registry/` (marketplace JSON), `spec/` (plugin spec kit). A plugin is a skill folder plus optional `open-design.json`. [verified] plugins/README.md
- `prompt-templates/`: 93 ready prompts per README. [verified] README.md
- Repo-wide: 562 SKILL.md files.

Four-axis model: skills (what the agent does), design-templates (what gets rendered), design-systems (whose brand), craft (universal quality rules). [verified] craft/README.md, README.md

Prompt composition for each send: base prompt + active design system DESIGN.md body + active skill SKILL.md body. Two implementations sit behind a rollout switch. [verified] QUICKSTART.md "Prompt composition"; AGENTS.md "Prompt variants"

Daemon data lives under `<project-root>/.tmp/<source>/<namespace>/...`. [verified] AGENTS.md boundary constraints

## 3. Skill inventory

Counts (by name prefix; grouping is [inferred] from names):
- `fal-*` 12 (hosted image/video/3D generation and editing)
- `gsap-*` 8 (animation library guidance)
- `figma-*` 7 (Figma import, generation, code connect)
- `frame-*` 7 (animated frame/background/logo effects)
- `venice-*` 5 (image, video, audio providers)
- `imagegen*` 3, `imagen`, `nanobanana-ppt`, `replicate`, `sora`, `speech` (generation providers)
- `deck-*` 3, `pptx*` 3, `docx` 1, `pdf` 1, `html-ppt` 1 (documents and slides; 48 `html-ppt-*` templates sit in design-templates/)
- `stitch-*` 2, `taste-*` 2
- Remaining ~114 directories: mixed briefs, reviews, motion, platform and social-card skills

Notable names (exist): `design-brief`, `brand-extract`, `design-md`, `design-review`, `redesign-skill`, `frontend-design`, `ui-ux-pro-max`, `web-clone`, `theme-factory`, `threejs`, `shadcn-ui`, `remotion`, `video-hyperframes`, `hand-drawn-diagrams`, `research-decision-room`, `pr-feedback-quality-gate`, `writing-guidelines`. [verified]

Design templates notable: `web-prototype`, `saas-landing`, `dashboard`, `mobile-app`, `pm-spec`, `team-okrs`, `eng-runbook`, `guizang-ppt`, `hyperframes`, `critique`, `tweaks`, and four wireframe templates: `wireframe-sketch`, `wireframe-greybox`, `wireframe-annotated`, `wireframe-mobile-flow`. [verified] README.md table, `ls design-templates`

## 4. Craft rules (actionable, paraphrased)

1. Keep neutrals at roughly 70-90% of pixels, one accent at 5-10%, and semantic colors under 5%. [verified] craft/color.md "Palette structure"
2. Cap visible accent use at two per screen (for example one eyebrow plus one primary CTA). Links and focus rings count as accent. [verified] craft/color.md "Accent discipline"
3. Name color tokens by purpose (`--accent`, `--success`), never by hue. [verified] craft/color.md "Semantic color naming"
4. Meet contrast floors: 4.5:1 for body text, 3:1 for large text and UI components. [verified] craft/color.md "Contrast minimums"
5. Use a multiplicative type scale (1.2 or 1.25) and cap a single artifact at 6-8 sizes. [verified] craft/typography.md "Type scale"
6. For CJK text, raise line-height to about 1.3-1.4 on display headings and 1.7-1.8 on body, and set letter-spacing to 0. [verified] craft/typography.md "CJK overrides"
7. Every surface that loads data needs five states: loading, empty, error, populated, and edge (long strings, huge row counts, missing optional fields). [verified] craft/state-coverage.md
8. Validate form fields on blur, not on the first keystroke. [verified] craft/state-coverage.md "Form-specific states"
9. Keep state-confirmation motion near 150 ms, keep non-navigation micro-interactions under 500 ms, and drop axis motion (translate, scale, rotate) under reduced-motion. [verified] craft/animation-discipline.md "Duration thresholds", "Reduced motion"
10. Make touch targets at least 24x24 CSS px (AA), with 44x44 as the craft target. [verified] craft/accessibility-baseline.md "Touch targets"
11. Never remove focus outlines outright; style `:focus-visible` instead. [verified] craft/accessibility-baseline.md "Focus visibility"
12. Avoid AI-slop tells the linter blocks: default Tailwind indigo accents, two-stop gradient heroes, emoji as feature icons, invented metrics, lorem-ipsum filler. [verified] craft/anti-ai-slop.md "The seven cardinal sins"

To opt a skill into craft sections, list slugs in `od.craft.requires` in its frontmatter, then run `pnpm lint:craft`. [verified] craft/README.md

## 5. Design-system format

- Required files: `manifest.json`, `DESIGN.md` (canonical prose), `tokens.css` (compiled semantic tokens). [verified] design-systems/README.md
- Optional: `USAGE.md`, `components.html`, `design-tokens.json`, `tailwind-v4.css`, `assets/`, `fonts/`, `preview/`, `source/`. [verified] design-systems/README.md
- Manifest `id` must equal the folder slug; `files.design` = `DESIGN.md`; `files.tokens` = `tokens.css`; every declared path must be relative and present. [verified] design-systems/README.md, design-systems/_schema/AGENTS.md
- Legacy folders with only `DESIGN.md` are still discovered (compatibility only). Manifest metadata overrides the old `> Category:` Markdown convention. [verified] design-systems/README.md
- Catalog is rescanned on every `/api/design-systems` request; no daemon restart needed. [verified] design-systems/README.md
- Schema sources: `design-systems/_schema/manifest.schema.ts` and `tokens.schema.ts`; canonical runtime copy in `packages/contracts`. [verified] design-systems/_schema/AGENTS.md
- Bundled packages are re-imported from an upstream "getdesign" tarball by `scripts/sync-design-systems.ts`. [verified] QUICKSTART.md file map
- Example package: `design-systems/claude` (terracotta accent `#c96442`, parchment canvas). Its DESIGN.md describes a brand-inspired style, not an official Anthropic kit. [verified] design-systems/claude/DESIGN.md; "not official" is [inferred]

## 6. How to run and install

- Desktop app (recommended): macOS (Apple Silicon and Intel) and Windows x64. No prebuilt Linux artifact in official releases. [verified] README.md "Download the desktop app"
- Docker: `cd deploy && cp .env.example .env`, add `OD_API_TOKEN` (from `openssl rand -hex 32`), `docker compose up -d`, open `http://127.0.0.1:7456`. Basic-auth user is not documented in the repo; check `deploy/` before relying on it. [verified] README.md, QUICKSTART.md
- From source: `git clone`, `corepack enable && pnpm install`, `pnpm tools-dev run web`. Node `~24`; pnpm pinned to `10.33.2` via `packageManager` (`engines` allows `>=10.33.2 <11`). [verified] README.md, QUICKSTART.md
- Agent integration with no UI: `od mcp install <agent>` (README table lists 20 platforms; 19 use this command, covering 18 distinct agent names because `copilot` appears twice; DeepSeek Harness uses `od agent setup`; the README prose says "16+ CLIs"; `--print` dry-runs, `--uninstall` removes). [verified] README.md
- Checks: `pnpm guard`, `pnpm typecheck`, `pnpm --filter @open-design/daemon test`. [verified] AGENTS.md "Common commands"
- Packaging: `pnpm tools-pack mac build --to all`, `pnpm tools-pack win build --to nsis`, `pnpm tools-pack linux build --to appimage`. [verified] AGENTS.md

## 7. License

- Apache License 2.0. Confirmed by the LICENSE file header, `package.json` `"license": "Apache-2.0"`, and the README license section. [verified]
- Bundled third-party content keeps its own license: `design-templates/guizang-ppt/` (MIT) and `design-templates/html-ppt/` (MIT) per README "License". [verified] README.md line 735
- HyperFrames framework is Apache-2.0, but its catalog thumbnails are copyright HeyGen. [verified] README.md "Video & HyperFrames"
- Curated skill stubs in `skills/` point at upstream repos and do not vendor their assets. [verified] skills/AGENTS.md
- Not checked: per-directory LICENSE files inside the ~169 skills and 152 design systems. [inferred gap]

## 8. Gotchas

- Node must be `~24` (enforced via `package.json#engines`). Use corepack so pnpm 10.33.2 is selected. [verified] QUICKSTART.md
- There is no root `pnpm dev` or `pnpm start`; use `pnpm tools-dev`. [verified] AGENTS.md FAQ
- On macOS, `/usr/bin/od` can shadow the `od` CLI. Desktop users should use the Settings > MCP snippet, which uses absolute paths. [verified] README.md
- A GUI launched with a minimal PATH may show a globally installed agent CLI as "not installed". [verified] QUICKSTART.md "Local agent CLI and PATH"
- `better-sqlite3` breaks with ABI mismatch after a Node version change; `pnpm install` reruns postinstall, or rebuild with the filter command in QUICKSTART. [verified] QUICKSTART.md Troubleshooting
- LAN exposure needs `OD_BIND_HOST` plus `OD_ALLOWED_ORIGINS`. Private-range provider base URLs are blocked by default with "Internal IPs blocked". Internal LiteLLM or Ollama gateways need an explicit exception. [verified] README.md "Security model", "Internally-hosted model endpoints"
- Every user-facing capability must exist in both the web UI and the `od` CLI, sharing the same `/api/*` endpoints. [verified] AGENTS.md "Capability exposure"
- `packages/contracts` must stay pure TypeScript; web and daemon must not import each other's `src/`. [verified] AGENTS.md "Boundary constraints"
- Tests belong in a package-level `tests/` directory, not under `src/`; new `.js` files need a generated or vendor reason and must pass `pnpm guard`. [verified] AGENTS.md
- Codex can load too much plugin context; `OD_CODEX_DISABLE_PLUGINS=1` disables it. [verified] QUICKSTART.md Troubleshooting
- Claude Code exit code 1 usually means auth; check `claude auth status`. [verified] QUICKSTART.md Troubleshooting
- Counts disagree across docs: README says "100+ functional skills" and "151 design systems"; disk has 169 SKILL.md files under skills/ and 152 design-system manifests. [verified]
- `wireframe-sketch` is not under `skills/`. It is a design template at `design-templates/wireframe-sketch/` (SKILL.md plus example.html), with a copy under `plugins/_official/examples/`. [verified]
- `ui-audit/` holds one review note (`ui-audit/goal66/owner-s9r-re-review.md`), a BLOCK verdict on an owner check in `apps/daemon/src/routes/collab-sync.ts`. It is not an audit framework. [verified]
- `docs/spec.md` and `docs/roadmap.md` are archived; do not treat their dated decisions as current. [verified] AGENTS.md

## 9. Not read / limits

- Not read: `apps/` and `packages/` source, `e2e/`, `CHANGELOG.md`, `docs/` beyond headings, most of the 169 skill bodies, most of the 116 design-template bodies, `.github/`, and `plugins/spec/` beyond the README.
- Package purposes beyond the first five were inferred from names only.
- Grouping of skills by prefix is my inference; no source file defines these groups.
- Line count is kept under 200 for this file.
