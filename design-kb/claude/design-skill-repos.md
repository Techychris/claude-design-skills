# Design skill repos: what each contains

Compiled 2026-11-12 from the cloned repos (names and descriptions read from each SKILL.md front matter). Licenses and dates: `design-sources-index.md`. Deeper per-repo rules: `kb/`.

## emilkowalski/skills (19 skills, MIT)
animate, animate-expo, animation-performance, animation-vocabulary, apple-design, ask-sonner, break-ui, choreograph, emil-design-eng, find-animation-opportunities, gestures, improve-animations, learn-taste, mobile-native, pick-ui-library, prototype, remove-animations, review-animations, write-swift.
- `pick-ui-library`: picks a library per frontend task (command menus to cmdk, toasts to Sonner). Explicit invocation only.
- `learn-taste`: turns a session's design corrections into rules.
- `break-ui`: stress-tests UI with worst-case data.

## heydamir/unslop (1 skill, CC BY 4.0)
`unslop`: audits AI-looking UI, sets a direction from the product, then fixes in nine passes. Has `examples/`, two helper scripts (`snapshot.mjs`, `story.mjs`) and tests.

## benjitaylor/skills (1 skill)
`stageshow`: faux product UI as stills or cursor demos. Has `references/`, a copyable React `kit/`, 71 example folders, `teaching/`, and filming scripts. Needs Node 20.19+.

## lottiefiles/motion-design-skill (1 skill, MIT)
`motion-design`: one SKILL.md plus 16 support files (director/, patterns/, reference/). No Lottie-specific content.

## dylantarre/animation-principles (144 skills, MIT)
Disney's 12 principles applied in 12 groups of 12: domain, thinking style, role, skill level, animation type, emotion, UI element, industry, tool, time scale, principle focus, problem type.

## dammyjay93/interface-design (MIT)
Product-UI skill (dashboards, admin, SaaS; not marketing pages) with slash commands `design-review` and `design-deslop`, and a saved-decisions file `.interface-design/system.md`. The pre-commit hook uses BSD `sed` syntax.

## markdown-viewer/skills (CC BY 4.0)
Head: one package, `documd-visuals`. The `wireframe` skill (draw.io XML wireframes with web, iOS, Android and dashboard examples) was removed in April 2026 and recovered from an older commit.

## Large collections
- owl-listener/designer-skills: 111 skills in 9 plugins (design-research 14, design-systems 11, ux-strategy 12, ui-design 19, interaction-design 22, prototyping-testing 10, design-ops 9, designer-toolkit 7, visual-critique 7).
- cuellarfr/design-skills: 10 skills: accessibility-audit, design-critique, design-elevation, design-ops, design-systems, interaction-design, journey-mapping, ux-research, ux-strategy, ux-writing.
- product-on-purpose/pm-skills: 68 skills across discover, define, develop, deliver, measure, iterate, foundation, two sprint tool families and utilities.
- rampstackco/claude-skills: 109 stack-agnostic skills in 16 groups (brand, design, content, SEO, product, research and more).
- nexu-io/open-design: 169 skills in `skills/` (562 SKILL.md repo-wide), 116 design templates, 151 design systems (README), 12 craft rule files.
- bluzir/claude-code-design: 20 skills plus starter components and Chrome DevTools MCP; no license file.

CC BY 4.0 repos (unslop, markdown-viewer) also require a link to the licence and a note of changes in adapted skills. bluzir count: 20 skills per its README tree (a directory count gave 19 folders).

_Validated 2026-11-12 against primary sources; see ../validation-reports/._
