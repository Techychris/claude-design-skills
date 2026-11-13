# Design sources index

Compiled 2026-11-12, then validated online the same day. Every repo below was shallow-cloned and its README, license file and last commit read that day. "Verified" = read from the clone. Deeper notes per repo are in `kb/` (start at `kb/README.md`; validation results in `kb/validation.md`).

Clone paths were session-local. To restore any repo: `git clone --depth 1 https://github.com/<owner>/<repo>`.

## A. Sources behind the user's design skills

| Repo | Last commit | License | Feeds skill(s) | Notes |
|---|---|---|---|---|
| heydamir/unslop | 2026-11-09 | CC BY 4.0 | unslop, design, design-lean | Keep the credit in any adaptation. |
| benjitaylor/skills | 2026-11-04 | no root license; `stageshow/LICENSE` is MIT (Benji Taylor) | design, design-demo | One skill, `stageshow`. App icons are not MIT; brand SVGs carry other licenses (stageshow/NOTICE.md). |
| emilkowalski/skills | 2026-11-12 | MIT | web-motion | 19 skills, including `pick-ui-library`. |
| lottiefiles/motion-design-skill | 2026-05-18 | MIT (Copyright 2025 LottieFiles) | web-motion | Confirmed official LottieFiles repo. Contains one `motion-design` skill with no Lottie-specific content. |
| dylantarre/animation-principles | 2025-12-30 | MIT | web-motion | 144 skills in 12 groups of 12. No skill in it is named `animation-principles`; a skill with that name appeared in a search listing for `dylantarre/design-system-skills` (not pulled, unconfirmed). Credit stays with Dylan Tarre. |
| dammyjay93/interface-design | 2026-06-20 | MIT, Copyright 2026 Damola Akinleye (verified in LICENSE) | interface-design, design, design-lean | Renamed from `claude-design-skill` (confirmed). The user's local `SKILL.md` differs from upstream (not diffed). |
| owl-listener/designer-skills | 2026-09-05 | MIT (MC Dean) | heuristic-evaluation, accessibility-audit, ux-mapping, ux-wireframe | 111 skills in 9 plugins here; the live five collections hold 275 against the README's 273. |
| cuellarfr/design-skills | 2026-09-30 | MIT | ux-mapping | 10 skills, including `journey-mapping`. |
| product-on-purpose/pm-skills | 2026-11-03 | Apache 2.0 | ux-mapping | 68 skills; `discover-journey-map` is the one cited. |
| rampstackco/claude-skills | 2026-11-08 | MIT | ux-mapping | 109 skills; `journey-mapping` is the one cited. |
| bluzir/claude-code-design | 2026-04-20 | no LICENSE file; README says MIT, package.json says ISC | ux-wireframe | Treat as unlicensed. Ideas only, do not copy text. 19 skill folders. |
| nexu-io/open-design | 2026-11-12 | Apache 2.0 | ux-wireframe | 169 SKILL.md under `skills/` (562 repo-wide). `wireframe-sketch` is a design template under `design-templates/`, not a skill. 531 MB. |
| markdown-viewer/skills | 2026-10-06 | CC BY 4.0 | ux-wireframe | Its `wireframe` skill was removed on 2026-04-11 (commit 2da9334); the skills.sh listing is stale. Last version recovered from commit `02052ea` (2026-03-26): SKILL.md plus four examples; no license of its own, links to a missing `../drawio/` folder. |

Other credits in the skills, not repos pulled: Anthropic `frontend-design` (Apache 2.0, in /mnt/skills/public); Kalbach, *Mapping Experiences*; Polaine, Løvlie and Reason, *Service Design*.

## B. UI libraries from the user's screenshot

| Library | Repo | Last commit | License file |
|---|---|---|---|
| shadcn/ui | shadcn-ui/ui | 2026-11-11 | yes (MIT) |
| Base UI | mui/base-ui | 2026-11-12 | yes (MIT) |
| Radix | radix-ui/primitives | 2026-10-14 | yes (MIT) |
| Sonner | emilkowalski/sonner | 2026-08-10 | yes (MIT) |
| Vaul | emilkowalski/vaul | 2025-10-03 (unmaintained per README) | yes (MIT) |
| cmdk | pacocoursey/cmdk | 2025-10-28 | yes (MIT) |
| NumberFlow | barvian/number-flow | 2026-09-20 | yes (MIT) |
| Magic UI | magicuidesign/magicui | 2026-11-12 | yes (MIT) |
| 21st.dev | serafimcloud/21st | 2025-05-28 (stale) | yes (MIT) |
| RareUI | Codewithswappy/RareUI | 2026-04-07 | yes (MIT) |
| Beautiful UI (beautifului.dev) | none found | n/a | site says MIT; built by Turbo |
| Aceternity UI | none found | n/a | n/a |

Repo paths for items other than RareUI were inferred from the library names; each cloned successfully. Online validation confirmed the Sonner, NumberFlow, Magic UI and RareUI repos against their sites. cmdk's site (cmdk.paco.me) redirects to github.com/dip/cmdk, which has the same HEAD as pacocoursey/cmdk. 21st.dev's repo is public and self-identifies; the site doesn't link back. Vaul's site could not be fetched. Aceternity UI is by Manu Arora; its components are served from a registry (`https://ui.aceternity.com/registry/{name}.json`), and the `github.com/aceternity` org holds starters such as `saasternity`, not the components.

The screenshot also listed a `pick-ui-library` skill: it is `skills/pick-ui-library` inside emilkowalski/skills.

See also: `design-skill-repos.md`, `design-ui-libraries.md`, and the `kb/` folder.
