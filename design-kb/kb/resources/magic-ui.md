# Magic UI: verification and resources

Checked 2026-11-12 against official sources: magicui.design docs, the GitHub repo (README, CONTRIBUTING, LICENSE.md, skills/magic-ui/SKILL.md, package.json, border-beam source). Pages were read through WebFetch summaries, so statements are paraphrased. Tags: [verified] = read in this run; [inferred] = deduced.

Scope: KB `kb/ui-components.md`, section 5 (Magic UI and its agent skill).

## Verdict table

| # | KB rule (section) | Verdict | Deciding URL | Note |
|---|---|---|---|---|
| 1 | Components install through the shadcn registry as `@magicui/<slug>` (5, Install) | CONFIRMED | https://magicui.design/docs/installation | Docs show the pnpm dlx form plus npm, yarn and bun variants [verified] |
| 2 | Run `shadcn init` first, then import from `@/components/ui/<slug>` (5, Install; SKILL.md) | CONFIRMED | https://magicui.design/docs/installation ; https://magicui.design/docs/components/border-beam | Import path shown on component pages [verified] |
| 3 | Keep the component API intact; customise through props or className (SKILL.md) | CONFIRMED | https://magicui.design/docs/components/border-beam ; https://raw.githubusercontent.com/magicuidesign/magicui/main/skills/magic-ui/SKILL.md | Props tables list className and style overrides; docs call components fully customisable with Tailwind [verified] |
| 4 | Motion budget: one core effect plus one supporting effect; do not stack many high-motion effects in one viewport (SKILL.md) | CONFIRMED (as guidance) | https://raw.githubusercontent.com/magicuidesign/magicui/main/skills/magic-ui/SKILL.md | Advice only, no numeric limit exists. The "one plus one" pairing is a default, not a hard rule [verified via summary] |
| 5 | Some components need global CSS keyframes or extra packages listed in their docs (5, Gotchas; SKILL.md) | CONFIRMED (general); examples vary | https://magicui.design/docs/installation/manual ; https://raw.githubusercontent.com/magicuidesign/magicui/main/CONTRIBUTING.md ; https://raw.githubusercontent.com/magicuidesign/magicui/main/apps/www/registry/magicui/border-beam.tsx | Manual install needs accordion keyframes in the Tailwind config and globals.css, plus tailwindcss-animate. CONTRIBUTING says registry entries carry keyframes. border-beam needs only `motion` and defines no keyframes, so the rule is not universal [verified]. Per-component Manual tabs were not readable in the fetch |
| 6 | Prerequisites: React or Next.js with Tailwind, shadcn initialised (SKILL.md) | CONFIRMED | https://raw.githubusercontent.com/magicuidesign/magicui/main/skills/magic-ui/SKILL.md | [verified via summary] |
| 7 | Version pins for React, Next.js, Tailwind (implied by section 5) | UNVERIFIABLE | https://magicui.design/docs/installation/manual | Docs name no versions. Manual install says to follow Tailwind's own guide. border-beam uses Tailwind v4 class syntax, so v4 is likely [inferred] |
| 8 | Repo development needs Node >= 22.14 and pnpm >= 9 (5, Dependencies) | CONFIRMED | https://raw.githubusercontent.com/magicuidesign/magicui/main/package.json ; https://raw.githubusercontent.com/magicuidesign/magicui/main/CONTRIBUTING.md | package.json engines field gives both numbers. CONTRIBUTING says Node 22 [verified]. This applies to the repo, not to consumers |
| 9 | 79 registry:ui items; the site lists 78 (5, Component inventory) | UNVERIFIABLE | https://magicui.design/llms.txt | Count not re-run. The llms index describes about 120 component pages, which may include variants. Discrepancy noted [verified text] |
| 10 | Maintenance: active, last commit 2026-11-12 (5, Summary) | UNVERIFIABLE | https://github.com/magicuidesign/magicui | Commit history not checked in this run (GitHub API not used). KB value carried forward from its earlier run |
| 11 | License MIT (5, Summary) | CONFIRMED | https://raw.githubusercontent.com/magicuidesign/magicui/main/LICENSE.md | Standard MIT, copyright line "Magic UI". Copies must keep the notice. No template or redistribution limits [verified] |
| 12 | Troubleshooting: components.json or init errors, `@/` alias mismatch, missing global CSS, missing packages (SKILL.md) | CONFIRMED | https://raw.githubusercontent.com/magicuidesign/magicui/main/skills/magic-ui/SKILL.md | [verified via summary] |
| 13 | Components are source files you own (implied by copy-paste model) | CONFIRMED | https://magicui.design/docs/installation | shadcn add writes the source into the project. Ownership wording is [inferred] |
| 14 | Registry entries declare their own npm dependencies (e.g. magic-card needs motion) (5, Key API) | CONFIRMED (partly) | https://raw.githubusercontent.com/magicuidesign/magicui/main/apps/www/registry/magicui/border-beam.tsx ; https://raw.githubusercontent.com/magicuidesign/magicui/main/CONTRIBUTING.md | border-beam imports motion/react and uses @/lib/utils. CONTRIBUTING says npm packages go in the registry entry. magic-card itself not re-read [verified] |
| 15 | Skill selection heuristics (hero, CTA, text, background lists) (5, Agent skill) | UNVERIFIABLE | https://raw.githubusercontent.com/magicuidesign/magicui/main/skills/magic-ui/SKILL.md | Summary fetch did not return the heuristics list |

## Missed guidelines

Official guidance the KB does not cover:

1. Manual install baseline: class-based dark mode, Tailwind content paths for app and components, CSS variables for colours and radius, a `cn` helper in lib/utils that uses clsx and tailwind-merge, and icon packages lucide-react or @radix-ui/react-icons. Source: https://magicui.design/docs/installation/manual [verified]
2. Border-beam parent must be `relative` with `overflow-hidden`. Source: https://magicui.design/docs/components/border-beam [verified]
3. Each component page has a CLI tab and a Manual tab with a props table. Read the Manual tab before installing anything that needs keyframes. Source: https://magicui.design/docs/components/shimmer-button [verified]
4. MCP setup uses a separate CLI, `@magicuidesign/cli`, with `install cursor` (also Windsurf, Claude, Cline, Roo-Cline). The shadcn MCP route needs an `@magicui` registry entry in components.json pointing at magicui.design/r/{name}.json. Source: https://magicui.design/docs/mcp [verified]
5. Publishing a component to the library: about five files (component in registry/magicui, demo in registry/example, sidebar entry, MDX docs page, two registry entries). Run `pnpm build:registry` and commit the generated artifacts, because CI fails when they are stale. Source: https://raw.githubusercontent.com/magicuidesign/magicui/main/CONTRIBUTING.md [verified]
6. Before a PR: `pnpm check` (lint, typecheck, format, registry-deps), `pnpm build`, Conventional Commit messages. Source: same CONTRIBUTING [verified]
7. border-beam class names use Tailwind v4 syntax, so consumers likely need Tailwind v4. Source: https://raw.githubusercontent.com/magicuidesign/magicui/main/apps/www/registry/magicui/border-beam.tsx [inferred]
8. llms index and full text exist for LLM consumers. Sources: https://magicui.design/llms.txt and https://magicui.design/llms-full.txt [verified]
9. The old v3 docs had a different manual install page, so pre-v4 guidance may be stale. Source: https://v3.magicui.design/docs/installation/manual (seen in search results, not fetched) [inferred]

## Resources

| # | Title | URL | Type | Why useful |
|---|---|---|---|---|
| 1 | Magic UI installation | https://magicui.design/docs/installation | Official docs | Canonical shadcn add flow and import path [fetched] |
| 2 | Magic UI manual installation | https://magicui.design/docs/installation/manual | Official docs | Tailwind config, globals.css, keyframes and packages needed without the CLI [fetched] |
| 3 | Magic UI MCP server | https://magicui.design/docs/mcp | Official docs | Cursor, Claude and other IDE setup, plus shadcn MCP route [fetched] |
| 4 | Border Beam component | https://magicui.design/docs/components/border-beam | Component doc | Props table, parent-container requirement, motion-based animation [fetched] |
| 5 | Shimmer Button component | https://magicui.design/docs/components/shimmer-button | Component doc | Typical CTA component, props table [fetched] |
| 6 | Magic UI LLM index | https://magicui.design/llms.txt | Index for LLMs | Single-file index of docs pages for AI-assisted use [fetched] |
| 7 | magicuidesign/magicui | https://github.com/magicuidesign/magicui | Repository | Source for the docs site and registry; README links to docs [fetched] |
| 8 | CONTRIBUTING.md | https://raw.githubusercontent.com/magicuidesign/magicui/main/CONTRIBUTING.md | Contributor guide | Five-file component pattern, registry build and CI checks [fetched] |
| 9 | Magic UI agent skill (SKILL.md) | https://raw.githubusercontent.com/magicuidesign/magicui/main/skills/magic-ui/SKILL.md | Agent skill | Official usage rules that the KB section 5 cites [fetched] |
| 10 | border-beam source | https://raw.githubusercontent.com/magicuidesign/magicui/main/apps/www/registry/magicui/border-beam.tsx | Source code | Example of a no-keyframe, motion-based component with inline styles and className override [fetched] |
| 11 | LICENSE.md | https://raw.githubusercontent.com/magicuidesign/magicui/main/LICENSE.md | License | MIT terms with copyright "Magic UI" [fetched] |
| 12 | Magic UI v3 manual installation | https://v3.magicui.design/docs/installation/manual | Archived docs | Old manual setup, useful only to spot stale steps [seen in search results] |

Notes: a skills.sh listing for Magic UI and a Mintlify mirror appeared in search results. Neither was fetched and both are third-party, so they are not included.
