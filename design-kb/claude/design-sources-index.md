# Design sources index

Compiled 2026-11-12, then validated online the same day. Every repo below was shallow-cloned and its README, license file and last commit read that day. "Verified" = read from the clone. Deeper notes per repo are in `kb/` (start at `kb/README.md`; validation results in `kb/validation.md`).

Clone paths were session-local. To restore any repo: `git clone --depth 1 https://github.com/<owner>/<repo>`.

`kb/references.md` is the verified bibliography (papers, standards, DOIs, evidence levels, unverified citations); use it for any research citation.

## A. Sources behind the user's design skills

| Repo | Last commit | License | Feeds skill(s) | Notes |
|---|---|---|---|---|
| heydamir/unslop | 2026-11-09 | CC BY 4.0 | unslop, design, design-lean | Keep the credit in any adaptation, link the licence and note changes (CC BY 4.0). |
| benjitaylor/skills | 2026-11-04 | no root license; `stageshow/LICENSE` is MIT (Benji Taylor) | design, design-demo | One skill, `stageshow`. App icons are not MIT; brand SVGs carry other licenses (stageshow/NOTICE.md). |
| emilkowalski/skills | 2026-11-12 | MIT | web-motion | 19 skills, including `pick-ui-library`. |
| lottiefiles/motion-design-skill | 2026-05-18 | MIT (Copyright 2025 LottieFiles) | web-motion | Confirmed official LottieFiles repo. Contains one `motion-design` skill with no Lottie-specific content. |
| dylantarre/animation-principles | 2025-12-30 | MIT | web-motion | 144 skills in 12 groups of 12. No skill in it is named `animation-principles`; a skill with that name appeared in a search listing for `dylantarre/design-system-skills` (not pulled, unconfirmed). Credit stays with Dylan Tarre. |
| dammyjay93/interface-design | 2026-06-20 | MIT, Copyright 2026 Damola Akinleye (verified in LICENSE) | interface-design, design, design-lean | Renamed from `claude-design-skill` (confirmed). The user's local `SKILL.md` differs from upstream (not diffed). |
| owl-listener/designer-skills | 2026-09-05 | MIT (MC Dean) | heuristic-evaluation, accessibility-audit, ux-mapping, ux-wireframe | 111 skills in 9 plugins here; README says 273 skills across five collections (a 275 count could not be reproduced). |
| cuellarfr/design-skills | 2026-09-30 | MIT | ux-mapping | 10 skills, including `journey-mapping`. |
| product-on-purpose/pm-skills | 2026-11-03 | Apache 2.0 | ux-mapping | 68 skills; `discover-journey-map` is the one cited. |
| rampstackco/claude-skills | 2026-11-08 | MIT | ux-mapping | 109 skills; `journey-mapping` is the one cited. |
| bluzir/claude-code-design | 2026-04-20 | no LICENSE file; README says MIT, package.json says ISC | ux-wireframe | Treat as unlicensed. Ideas only, do not copy text. 20 skills per README tree (19 skill folders by directory count). |
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

Repo paths for items other than RareUI were inferred from the library names; each cloned successfully. Online validation confirmed the Sonner, NumberFlow, Magic UI and RareUI repos against their sites. cmdk's site (cmdk.paco.me) redirects to github.com/dip/cmdk, which has the same HEAD as pacocoursey/cmdk. 21st.dev's repo is public and self-identifies; the site doesn't link back. Vaul's site (vaul.emilkowal.ski) resolves (200) as of 2026-11-12. Aceternity UI is by Manu Arora; its components are served from a registry (`https://ui.aceternity.com/registry/{name}.json`), and the `github.com/aceternity` org holds starters such as `saasternity`, not the components.

The screenshot also listed a `pick-ui-library` skill: it is `skills/pick-ui-library` inside emilkowalski/skills.

See also: `design-skill-repos.md`, `design-ui-libraries.md`, and the `kb/` folder.

## C. Additional sources worth adding (URLs returned 200 on 2026-11-12)

| Source | URL | Why | Licence / note |
|---|---|---|---|
| WAI-ARIA Authoring Practices Guide | https://www.w3.org/WAI/ARIA/apg/ | Keyboard and ARIA patterns Radix, Base UI and UI SDK implement | W3C Software and Document License |
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | Basis for accessibility audits | W3C document licence |
| Material Design 3 | https://m3.material.io | Components, motion, accessibility | Proprietary to Google; ideas only |
| Apple Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines/ | Platform guidance | Apple proprietary; cite, do not copy |
| Nielsen Norman Group | https://www.nngroup.com (heuristics: /articles/ten-usability-heuristics/) | Heuristics behind heuristic-evaluation and design | Proprietary; link |
| Refactoring UI | https://www.refactoringui.com | Hierarchy, spacing, colour | Commercial book; link only |
| Laws of UX | https://lawsofux.com | Laws cited by cuellarfr and owl-listener skills | Attribute Jon Yablonski |
| Inclusive Components | https://inclusive-components.design | Component accessibility write-ups (Heydon Pickering) | Proprietary; link |
| Open Props | https://open-props.style | CSS custom-property tokens; npm open-props 1.7.23 | MIT, Adam Argyle |
| Radix Themes | https://www.radix-ui.com/themes/docs/overview/getting-started | Styled layer over Primitives; @radix-ui/themes 3.3.0 | MIT, WorkOS |
| GOV.UK Design System | https://design-system.service.gov.uk | Evidence-based component guidance | MIT code, OGL content |
| Carbon, Primer, Polaris, Spectrum, Atlassian, Fluent 2 | https://carbondesignsystem.com ; https://primer.style ; https://polaris-react.shopify.com ; https://spectrum.adobe.com ; https://atlassian.design ; https://fluent2.microsoft.design | Public design systems | Carbon Apache-2.0, Primer MIT; check each |
| Design Tokens Community Group | https://www.designtokens.org | Token format standard | W3C community group |
| Every Layout | https://every-layout.dev | Layout primitives | Commercial; link |
| web.dev Learn Design | https://web.dev/learn/design | Free design course | CC BY 4.0 per web.dev |
| Inclusive Design Principles | https://www.inclusivedesignprinciples.org | Short accessibility principles | Attribute |
| shadcn and Base UI llms.txt | https://ui.shadcn.com/llms.txt ; https://base-ui.com/llms.txt | Agent-readable docs (radix-ui.com/llms.txt is 404) | Official docs |

Last-commit dates above could not be re-verified (GitHub returned 403). npm publish dates as proxies: sonner 2026-08-09, @number-flow/react 2026-07-18, radix-ui 2026-10-14, shadcn 2026-10-27, @base-ui/react 2026-10-09. Aceternity authorship ("Manu Arora") and the `github.com/aceternity` org were not confirmed from opened pages. open-design counts: README says 151 design systems.

_Validated 2026-11-12 against primary sources; see ../validation-reports/._
