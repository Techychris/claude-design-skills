# Online validation of the design KB

Run 2026-11-12 by eight Haiku subagents against live sources: `git ls-remote` (upstream HEAD vs the clone), `npm view`, raw-file and page fetches, web search. GitHub's API and tree pages were blocked in this environment, so "archived" flags and CI run status could not be read. Each subagent also wrote a detailed table (claim, verdict, URL) to its own file; those stay in the session sandbox. This page keeps the summary and every correction that matters.

## Scorecard (162 claims)

| Area | Checked | Confirmed | Contradicted | Stale | Unverifiable |
|---|---|---|---|---|---|
| Motion repos | 20 | 19 | 0 | 0 | 1 |
| UI craft | 20 | 17 | 2 | 1 | 0 |
| UX research | 20 | 18 | 2 | 0 | 0 |
| PM and brand | 19 | 15 | 1 | 1 | 2 |
| open-design | 24 | 21 | 1 | 1 | 1 |
| Core UI libraries | 20 | 15 | 2 | 0 | 3 |
| Component libraries | 20 | 15 | 2 | 0 | 3 |
| Provenance and credits | 19 | 10 | 4 | 0 | 5 |
| **Total** | **162** | **130** | **14** | **3** | **15** |

"Stale" = upstream changed after the clone. Every clone's HEAD matched its upstream at check time, so the stale items are claims, not repos.

## Applied to the KB files

- **open-design:** `od mcp install` covers 19 rows but 18 distinct agents (`copilot` twice); the README prose says "16+ CLIs". Docker basic-auth user removed (undocumented). Version added (0.25.1 on main; latest release v0.26.1). "169 SKILL.md files", not directories. pnpm is pinned, not a minimum.
- **ui-craft:** bluzir has 19 skill folders, not 20. The `wireframe` skill was removed from markdown-viewer/skills on 2026-04-11 (commit 2da9334); no wireframe path exists at head. The README counts for markdown-viewer/skills were recounted and match. The `interface-design` rename from `claude-design-skill` is confirmed.
- **ux-research:** README says 273 skills; the live five collections hold 275 (33 plugins and 76 commands match). `accessibility-audit` is 26 lines, not 27. Added the WCAG AA thresholds (4.5:1, 3:1) and Nielsen's severity wording, both checked against w3.org and nngroup.com.
- **pm-brand:** `lint.yml` does run `lint_skills.py`, but the script doesn't check the headings or category drift listed in the gotchas, so a green CI proves little. One rendered page read 107 skills while the pinned README says 109. pm-skills `plugin.json` says 2.35.0 but the latest release is v2.34.0. Marketplace install commands and licence holders added.
- **ui-core:** the Base UI and Radix usage snippets now match the live docs (import lines and `asChild`/`render` confirmed). A `Positioner` belongs inside `Portal` only for Popover- and Menu-style parts, not Dialog. The shadcn docs list 66 entries against 63 registry files, which are different measures. No official shadcn Radix-to-Base migration page exists; the only online guide is a community discussion.
- **ui-components:** 21st.dev's repo is public (README calls it an open-source registry) but stale since 2025-05-28. NumberFlow's 0.0.1 belongs to the docs site; the package is 0.6.2. Sonner's peer range includes `^19.0.0-rc`. Magic UI's site lists 78 components against 79 registry items. Vaul's `npm install vaul` is confirmed on npm.
- **motion:** no corrections needed. Optional: the LottieFiles install line is `npx skills add LottieFiles/motion-design-skill`.

## Provenance results

| Claim | Verdict | Note |
|---|---|---|
| Dammyjay93 = Damola Akinleye; repo renamed from claude-design-skill | Confirmed | LICENSE says Damola Akinleye; README confirms rename. |
| Owl-Listener maintained by MC Dean | Confirmed | LICENSE and commit author. |
| LottieFiles/motion-design-skill is the official repo | Confirmed | Owned by LottieFiles, MIT. Earlier "unconfirmed" note is resolved. |
| dylantarre/animation-principles is by Dylan Tarre; same owner as design-system-skills | Confirmed | |
| A skill literally named `animation-principles` is in dylantarre/animation-principles | Contradicted | No SKILL.md has that name in the repo. A separate repo, `dylantarre/design-system-skills`, has one (seen in a search listing; its contents were not checked). |
| RareUI, NumberFlow, Sonner, Magic UI repos match their sites | Confirmed | |
| cmdk.paco.me points to pacocoursey/cmdk | Contradicted | The site redirects to github.com/dip/cmdk, which has the same HEAD as pacocoursey/cmdk, so it is likely the same project under another owner name. |
| 21st.dev's repo is serafimcloud/21st | Unverifiable | The repo identifies itself as 21st.dev; the site doesn't link back. |
| Vaul repo matches its site | Unverifiable | The site blocks fetching. |
| Beautiful UI has a public repo | Unverifiable | None found. Site says MIT, built by Turbo (turbodesign.co); the validation file names the copyright holder as Shane Levine. |
| Aceternity UI has a public component repo | Unverifiable | None found; author is Manu Arora. |
| markdown-viewer wireframe still documented live | Contradicted | Removed from the repo; the gitbook page returns 404; the skills.sh listing is stale. The local copy has no verifiable origin. |

## Subagent correction not applied

The provenance subagent said the `animation-principles` skill credited to Dylan Tarre is really MC Dean's (`Owl-Listener/designer-skills/interaction-design/skills/animation-principles`). I checked: that file exists, but the accessibility details the `web-motion` credit cites (pause controls, flash rate) appear in Dylan Tarre's repo (`12-by-problem-type/accessibility-issues`) and not in MC Dean's skill. The credit to Dylan Tarre stands. Which repo holds a skill literally named `animation-principles` (likely `dylantarre/design-system-skills`) is unresolved.

## Still unverified

- Archived status of all repos, and GitHub Actions run results.
- Whether the shadcn CLI behaves as documented (it was not run).
- Vaul's site docs, and the other claims marked UNVERIFIABLE in the table above.

_Validated 2026-11-12 against primary sources; see ../validation-reports/._
