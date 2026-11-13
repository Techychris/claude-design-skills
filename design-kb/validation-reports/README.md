# KB validation, 2026-11-12

Five independent subagents checked the KB against primary sources (W3C, NN/g, Apple HIG, Material 3, MDN, npm, official docs and repos). Corrections with a cited source were applied. Claims without a source were softened or tagged "(unsourced)", not deleted.

| Report | Scope | Checked | Verified | Wrong | Outdated/Dead | Nuance | Unsourced |
|---|---|---|---|---|---|---|---|
| A-core-ux.md | ux-mastery, validation | 61 | 45 | 1 | 1 | 8 | 6 |
| B-craft-motion.md | ui-craft, ui-core, motion | 41 | 12 | 0 | 4 | 12 | 13 |
| C-research-pm.md | ux-research, pm-brand, open-design, README | 45 | 26 | 0 | 0 | 11 | 8 |
| D-libraries.md | ui-components + 7 library docs | 72 | 55 | 2 | 3 | 8 | 4 |
| E-sources.md | remaining resources + claude/ docs | 67 | 40 | 4 | 5 | 18 | 0 |

## Known limits
- GitHub HTML, API and feeds returned 403, so every "last commit" date and repo file count is unverified. npm publish dates were used as a proxy.
- Not checked: Gestalt, Jakob's and Tesler's laws, cognitive-load models, Norman's principles, Material elevation, Baymard checkout stats, eye-tracking studies. NN/g's "5 users" page and m3.material.io did not load.
- Versions and browser support were true on 2026-11-12 and will drift.
