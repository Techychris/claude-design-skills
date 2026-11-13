# RareUI (Codewithswappy/RareUI): verification and resources

Checked 2026-11-12 against official sources: rareui.in and its docs, the GitHub repo (README, CONTRIBUTING.md, LICENSE, packages/cli source and package.json). Pages were read through WebFetch summaries, so statements are paraphrased. The Next.js installation page was first requested at the wrong URL (/docs/installation/nextjs, 404); the correct page is https://rareui.in/docs/installation/install-nextjs (200; plain create-next-app, Node 18.17+). `install-tailwind` and `add-utilities` also exist (200) and were not read. Tags: [verified] = read in this run; [inferred] = deduced.

Scope: KB `kb/ui-components.md`, section 7 (codewithswappy/rareui).

## Verdict table

| # | KB rule (section) | Verdict | Deciding URL | Note |
|---|---|---|---|---|
| 1 | Install example `npx rareui add liquid-metal` (7, Install) | CONFIRMED | https://github.com/Codewithswappy/RareUI (README) ; https://rareui.in/docs/installation/cli | Docs also show pnpm dlx, yarn dlx and bunx variants, and use @latest [verified] |
| 2 | CLI form `npx rareui add [component-name]` (7, Key API) | CONFIRMED | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/packages/cli/src/index.ts ; https://rareui.in/docs/installation/cli | Bin name `rareui`, the add subcommand takes the name [verified] |
| 3 | CLI accepts kebab-case or PascalCase names (7, Install) | CONFIRMED | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/packages/cli/src/index.ts | Help text lists both forms. The normalisation code was not read [verified] |
| 4 | `init` creates components.json (7, Key API) | CONFIRMED | https://rareui.in/docs/installation/cli | Docs say init creates components.json and sets import aliases. The `add` command help does not mention writing components.json [verified] |
| 5 | Copy-paste is an alternative to the CLI (7, Purpose) | CONFIRMED | https://github.com/Codewithswappy/RareUI ; https://rareui.in/docs/installation/cli | CLI is described as optional, and the code can be copied from docs [verified] |
| 6 | Requires React 19 and Next 16 (7, Gotchas) | WRONG (the claim that the README says "not strict"); "requires" is overstated | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/README.md | README lists React 19, Next.js 16, Tailwind CSS 4 and Framer Motion 12 under "Tech Stack" and states no hard requirement; CLI docs say it targets React/Next.js with Tailwind [verified 2026-11-12] |
| 7 | Built for React and Next with Tailwind (implied by section 7) | CONFIRMED | https://rareui.in/docs/installation/cli | Docs say the CLI targets React and Next.js projects using Tailwind, and other frameworks are not yet supported [verified] |
| 8 | Gotcha: README example `liquid-metal` does not match the file name LiquidMetal.json (7, Gotchas) | VERIFIED (not a gotcha for the CLI) | https://rareui.in/docs/installation/cli ; https://raw.githubusercontent.com/Codewithswappy/RareUI/main/packages/cli/src/index.ts | The documented canonical name is lowercase hyphenated, and the CLI accepts both forms per its help text. `public/r/LiquidMetal.json` exists and `liquid-metal.json` is 404, but add.ts converts kebab-case to PascalCase and matches case-insensitively, so `add liquid-metal` works; the mismatch only matters if you fetch https://rareui.in/r/liquid-metal.json (404) vs /r/LiquidMetal.json (200) by hand [verified add.ts 2026-11-12]. Earlier note: the file-name mismatch itself was not checked |
| 9 | Do not install the `.test` registry entries (7, Gotchas) | NUANCE (probably moot) | https://rareui.in/r/index.json | No `.test` entry is in index.json, so `add .` (which reads the index) cannot pull them; guessed `*.test.json` paths 404 [verified 2026-11-12] |
| 10 | Lazy variants exist for heavy components (LiquidMetalLazy, LiquidWaveLazy) (7, Key API) | CONFIRMED | https://rareui.in/r/index.json | Live registry index lists LiquidMetalLazy and LiquidWaveLazy [verified 2026-11-12] |
| 11 | Registry JSON per component under public/r/ (7, Key API) | UNVERIFIABLE | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/CONTRIBUTING.md | Contributing guide says `npm run build:registry` generates the registry, but does not describe the JSON format or path |
| 12 | Site dependencies: React ^19.2, Next ^16.2.1, Tailwind 4, Framer Motion ^12.23, three ^0.181, @number-flow/react ^0.5.10 (7, Dependencies) | CONFIRMED | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/package.json | Root package.json: react ^19.2.0, next ^16.2.1, tailwindcss ^4, framer-motion ^12.23.24, motion ^12.23.24, three ^0.181.2, @number-flow/react ^0.5.10, node >=20.18.0 [verified 2026-11-12] |
| 13 | CLI dependencies: @clack/prompts, commander, execa, fs-extra, chalk (7, Dependencies) | CONFIRMED | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/packages/cli/package.json | Manifest lists these and also chalk ^5.3 with the versions shown [verified] |
| 14 | CLI version 0.1.6, bin `rareui` (7, Dependencies) | CONFIRMED | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/packages/cli/package.json | [verified]. The npm package name is `rareui`; engines node >=18; npm latest 0.1.6, last modified 2025-12-09 (no CLI release in about 11 months) |
| 15 | Site Node >= 20.18.0 (7, Dependencies) | CONFIRMED | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/package.json | Root package.json engines node >=20.18.0 [verified 2026-11-12] |
| 16 | Three.js components add weight (7, Gotchas) | UNVERIFIABLE (inferred) | none | Based on dependency list and component names only |
| 17 | Likely not a drop-in for React 18 (7, Gotchas) | UNVERIFIABLE (inferred) | https://github.com/Codewithswappy/RareUI | Consistent with the React 19 stack in README, but no compatibility statement exists |
| 18 | Lint, typecheck and build before pushing a component (missed by KB) | (missed) | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/CONTRIBUTING.md | See Missed guidelines |
| 19 | License MIT, 2025, Swapnil Kalambe (7, Maintenance) | CONFIRMED | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/LICENSE | [verified] |
| 20 | Last commit 2026-04-07; moderate activity (7, Maintenance) | UNVERIFIABLE (unverified) | https://github.com/Codewithswappy/RareUI | Commit history not checked (GitHub 403). Changelog page exists on the site, so the project is maintained [inferred] |
| 21 | Changelog at data/changelog.json (7, Maintenance) | VERIFIED (partly) | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/data/changelog.json | data/changelog.json exists: 6 versions, latest 1.5.0 dated Apr 07 2026 (matches). Commit history itself unverifiable; about 7 months with no changelog entry |
| 22 | Component inventory: 41 files in public/r/ (7, Component inventory) | NUANCE | https://rareui.in/r/index.json | Live registry index.json lists 23 components (AnimatedTab, Book3D, FloatingNavigation, GlassShimmerButton, ImageExpandTestimonial, LiquidButton, LiquidMetal(+Lazy), LiquidTooltip, LiquidWave(+Lazy), LoadingSpinner, MagneticScatterText, Neumorphism3DButton, ParticleCard, PremiumButton, PremiumProfileCard, RetroPixelButton, SoftButton, SoundText, ToastTabs, VaporSmokeText, WordMagnet). The GitHub description says "100+ Free, Open Source React UI Components", inflated vs 23 installable. The 41-file count is not reproducible (tree not listable) |
| 23 | Components are typed and support light and dark mode (missed by KB) | CONFIRMED | https://github.com/Codewithswappy/RareUI ; https://raw.githubusercontent.com/Codewithswappy/RareUI/main/CONTRIBUTING.md | README says typed and light and dark; contributing rules require typed props and both themes [verified] |

## Missed guidelines

1. CLI flags: `-y` skips prompts, `-o` overwrites, `-c` sets the working directory, `-p` sets the install path. Source: https://rareui.in/docs/installation/cli [verified]
2. `diff` compares local copies with the latest registry versions. Source: https://rareui.in/docs/installation/cli [verified]
3. `add .` installs every component; `add` with no name lists available ones. Source: https://raw.githubusercontent.com/Codewithswappy/RareUI/main/packages/cli/src/index.ts [verified]
4. `add` checks for file conflicts before overwriting and installs required dependencies automatically. Source: same CLI source [verified]
5. Contributing rules: client components with typed props; merge classes with the project `cn` utility; use Framer Motion for animation; no `any`; Tailwind utilities rather than inline styles; no console logs or commented code; WCAG 2.1 AA with ARIA and keyboard support. Source: https://raw.githubusercontent.com/Codewithswappy/RareUI/main/CONTRIBUTING.md [verified]
6. Placement: PascalCase filenames inside a category folder under components/rareui/. Source: same CONTRIBUTING [verified]
7. Pre-PR checks: lint, type-check and build; Conventional Commit style `type(scope): description`; test in Chrome, Firefox and Safari. Source: same CONTRIBUTING [verified]
8. Docs for each component: JSDoc on props and at least two usage examples. Source: same CONTRIBUTING [verified]
9. Framework scope: the CLI supports only React and Next.js with Tailwind; other frameworks are planned.
10. `add` aborts with "components.json not found. Please run npx rareui init first." unless `init` has run; registry base is https://rareui.in/r with `index.json`. Source: https://raw.githubusercontent.com/Codewithswappy/RareUI/main/packages/cli/src/commands/add.ts [verified 2026-11-12] Source: https://rareui.in/docs/installation/cli [verified]

## Resources

| # | Title | URL | Type | Why useful |
|---|---|---|---|---|
| 1 | RareUI home | https://rareui.in | Official site | Overview, install methods and stack as the project describes it [fetched] |
| 2 | RareUI docs | https://rareui.in/docs | Official docs | Sidebar of components by category; useful for checking what is documented [fetched] |
| 3 | RareUI CLI installation | https://rareui.in/docs/installation/cli | Official docs | init, add, diff, runner variants and flags [fetched] |
| 4 | Codewithswappy/RareUI | https://github.com/Codewithswappy/RareUI | Repository | README with stack list, copy-paste and CLI usage, license [fetched] |
| 5 | RareUI CLI source | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/packages/cli/src/index.ts | Source code | Ground truth for flags, name handling and add behaviour [fetched] |
| 6 | RareUI CLI package manifest | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/packages/cli/package.json | Manifest | npm name, version, bin and CLI dependencies [fetched] |
| 7 | CONTRIBUTING.md | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/CONTRIBUTING.md | Contributor guide | Component file rules, review checklist, commit style [fetched] |
| 8 | LICENSE | https://raw.githubusercontent.com/Codewithswappy/RareUI/main/LICENSE | License | MIT terms, copyright Swapnil Kalambe, 2025 [fetched] |
| 9 | RareUI changelog | https://rareui.in/changelog | Changelog | Release history for version checks [linked from fetched site page] |
| 10 | GitHub discussions | https://github.com/Codewithswappy/RareUI/discussions | Support | Where the project directs questions [linked from fetched site page] |

Notes: the correct Next.js page is https://rareui.in/docs/installation/install-nextjs (200). install-tailwind and add-utilities also exist (200); read them to close the setup gap (global CSS, keyframes, aliases). The mintlify.wiki mirror (former resource 11) is dead (404) and was removed. Registry rows 9 to 16 and 20 to 22 were rechecked against rareui.in/r/index.json and the root package.json on 2026-11-12.

_Validated 2026-11-12 against primary sources; see ../../validation-reports/._
