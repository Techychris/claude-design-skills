# Design knowledge base

Built 2026-11-12. Seven Haiku subagents each read local clones of 22 repos and wrote one file; the main session spot-checked them. A second round of eight Haiku subagents then validated the claims online (see `kb/validation.md`: 130 of 162 confirmed, 14 contradicted, 3 stale, 15 unverifiable; self-reported by an earlier subagent round, not reproducible from these files). Corrections are applied in the files below, except `kb/motion.md`, which needed none. Repos with no public source (Beautiful UI, Aceternity UI) are not covered.

A third round (2026-11-12) added `kb/ux-mastery.md`: ten Haiku subagents researched UI/UX foundations on the live web rather than from repos, followed by focused passes on visual hierarchy, iconography, spacing, composition, devices and viewports, and a gap audit of Apple's HIG and the Android and Material docs (including foldables). It uses its own tags (`[verified]`, `[rechecked]`, `[estimated]`, `[assumed]`, `unknown`), defined at the top of that file.

**Evidence tags.** `[experiment]` = peer-reviewed study. `[meta-analysis]` = pooled peer-reviewed studies. `[industry]` = non-peer-reviewed study or report (NN/g, Baymard, UXmatters, IBM report). `[standard]` = W3C, ISO or platform spec. `[convention]` = practitioner rule with no research base. Verified bibliography, DOIs and confidence levels: `kb/references.md` (source of truth where it disagrees with this file).

**Evidence gaps.** No peer-reviewed evidence was found for APCA versus WCAG 2 contrast, vestibular-safe UI animation (ground it in WCAG 2.3.3 and `prefers-reduced-motion`), design-system effectiveness, or foldable and responsive layout (use platform docs). Treat these as `[convention]`.

**Reading the tags.** `[verified]` = read in the cited file. `[inferred]` = the subagent's own deduction. Rules are paraphrased. Where a file says "not read", that part was skipped, so treat the file as a map, not the full contents.

| File | Covers | Lines |
|---|---|---|
| `kb/ux-mastery.md` | UI/UX principles and foundations: perception, heuristics, visual design (hierarchy, spacing, composition, iconography), type and color, accessibility, interaction and motion, IA and writing, research, design systems, devices, viewports and foldables, Apple HIG and Android platform additions, ethics and AI-era UX, learning roadmap | 324 |
| `kb/references.md` | Verified bibliography: papers, standards, DOIs, evidence levels, unverified citations, recommended additions, evidence gaps (source of truth for citations) | n/a |
| `kb/validation.md` | Online validation scorecard, applied corrections, provenance findings, open items | n/a |
| `kb/motion.md` | emilkowalski/skills (19 skills), lottiefiles/motion-design-skill, dylantarre/animation-principles (144 skills; 24 sampled), benjitaylor/skills (stageshow) | 188 |
| `kb/ui-craft.md` | heydamir/unslop, dammyjay93/interface-design, bluzir/claude-code-design, recovered markdown-viewer `wireframe` skill, markdown-viewer/skills (current head) | 196 |
| `kb/ux-research.md` | owl-listener/designer-skills (111 skills, 9 plugins), cuellarfr/design-skills (10 skills) | 206 |
| `kb/pm-brand.md` | product-on-purpose/pm-skills (68 skills), rampstackco/claude-skills (109 skills) | 223 |
| `kb/open-design.md` | nexu-io/open-design (169 skills, 116 templates, 152 design systems) | 133 |
| `kb/ui-core.md` | shadcn/ui, Base UI, Radix Primitives | 202 |
| `kb/ui-components.md` | Sonner, Vaul, cmdk, NumberFlow, Magic UI, 21st.dev, RareUI | 212 |
| `kb/resources/ui-sdk.md` | UI SDK (Vercel, beta): agent-oriented behavior library; install, status, license, accessibility claims, open questions | n/a |

Also in this folder: `claude/design-sources-index.md` (repo, license and skill mapping), `claude/design-skill-repos.md`, `claude/design-ui-libraries.md`. Per-library verification files are indexed in `kb/resources/README.md`.

## Conflicts between sources (pick one per project)

- **Exit easing:** emilkowalski says ease-out for entering and exiting UI; lottiefiles says exits accelerate; dylantarre's `micro-interactions` uses ease-in for a tooltip hide. (`kb/motion.md`)
- **Motion timing:** dylantarre's skills give different micro-interaction bands (100-200 ms vs 50-100 ms immediate), and two lottiefiles tables disagree on the Playful range (150-300 vs 200-400 ms). (`kb/motion.md`)
- **Journey maps:** pm-skills `discover-journey-map` puts service blueprints out of scope; rampstackco `journey-mapping` includes one. (`kb/pm-brand.md`)
- **Name overlaps:** cuellarfr and designer-skills share seven skill names (accessibility-audit, design-critique, ux-writing, design-ops, design-systems, interaction-design, ux-strategy); installing both may collide. (`kb/ux-research.md`)
- **Wireframe tooling:** the recovered markdown-viewer `wireframe` skill uses draw.io; the repo's current `documd-visuals` package advises against it. (`kb/ui-craft.md`)
- **Form validation timing:** Baymard says validate inline on blur; GOV.UK says validate only on submit. (`kb/ux-mastery.md`, sections 7 and 13)
- **Research sample sizes:** these are NN/g's rules: 5 qualitative, at least 20 quantitative, 15 per group for card sorting, 39 for eyetracking. (`kb/ux-research.md`)
- **Miller's 7 vs 4 and other contested "laws":** see the table in `kb/ux-mastery.md` section 2.
- **Icon stroke by size:** one guide uses 1 px at 16 px and 1.5 px at 24 px; another calls 2 px the 24 px convention. (`kb/ux-mastery.md`, iconography)

## Licensing flags

- **bluzir/claude-code-design:** no LICENSE file; the README says MIT and `package.json` says ISC. Treat as unlicensed until confirmed.
- **Recovered `wireframe` skill:** no license in the folder; the parent repo is CC BY 4.0. It was removed upstream on 2026-04-11, and its origin could not be verified online. Don't assume the same terms.
- **heydamir/unslop and markdown-viewer/skills:** CC BY 4.0, so keep the credit line in adaptations.
- **benjitaylor/skills (stageshow):** MIT for the code, but app icons are not MIT, and some brand SVGs carry other licenses (see `kb/motion.md`).
- **nexu-io/open-design:** Apache 2.0 overall; per-directory licenses inside the skills and design systems were not checked.
- **UI SDK (vercel-labs):** Apache-2.0 per its README; in beta under Vercel's beta terms. (`kb/resources/ui-sdk.md`)

## Facts corrected by online validation

- open-design: `od mcp install` covers 19 rows (18 distinct agents); the Docker basic-auth claim is removed; 169 SKILL.md files under `skills/`.
- bluzir: 19 skill folders, not 20.
- designer-skills: README says 273 skills; the live five collections hold 275.
- pm-skills: plugin.json says 2.35.0, latest release is v2.34.0. rampstackco lint CI runs, but doesn't check the headings or category drift.
- cmdk: cmdk.paco.me redirects to github.com/dip/cmdk (same HEAD as pacocoursey/cmdk).
- Skill credit: the `animation-principles` credit stays with Dylan Tarre; the validation subagent's suggestion to credit MC Dean was checked and rejected.

## Known gaps

- dylantarre: only 24 of 144 skills were sampled, and only their first lines. A skill literally named `animation-principles` is likely in `dylantarre/design-system-skills`, which was not pulled.
- Most skill bodies in designer-skills, open-design and rampstackco were not read; front matter and group-level inventories only.
- Archived status of repos and CI run results could not be checked (GitHub API blocked).
- Two one-minute scheduled reminders were created by mistake by subagents. They have already fired and do nothing, but may still show in the scheduled tasks list.
- Clone paths in the files (`/home/claude/...`) were session-local. Re-clone with `git clone --depth 1 https://github.com/<owner>/<repo>`.
- `kb/ux-mastery.md` gaps are listed in its section 15 and in the "Not covered" lines of each section: dated legal items to re-check, Material 3 pages that did not load (layout, spacing, icons, breakpoints, motion tokens, predictive back, navigation rules), Apple iOS margins and the iPad, visionOS and watchOS pages, and uncovered topics such as dark-mode palettes, component API design, jobs-to-be-done, tablet usage and cross-device continuity. Its sources were fetched by Haiku agents; only the DOJ Title II and FTC items and the Apple iPhone Duo page were re-checked by the main session.
- `kb/resources/ui-sdk.md`: UI SDK is in beta; adapter versions, last-commit date, accessibility behavior, bundle size and the canonical repo path (`vercel-labs/ui` vs `vercel-labs/ui-sdk`) are unconfirmed.

_Validated 2026-11-12 against primary sources; see validation-reports/._
