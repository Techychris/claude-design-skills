# Claude design skills

Two Claude skills for interface work, rebuilt from Anthropic's design skill as a gated workflow.

| Skill | Use it for |
| --- | --- |
| [`design-lean`](design-lean/SKILL.md) | Building, polishing (unslop) or reviewing UI: landing pages, sites, dashboards, app screens |
| [`design-demo`](design-demo/SKILL.md) | Faux product UI: hero illustrations of an app, bento tiles, mocked screens, cursor walkthroughs. Loads `design-lean` for the shared rules. |

## What's different from the original

- **Smaller load.** Demo mode is its own skill, so Build, Polish and Review runs load 33% less text.
- **Gate register.** Every gate has a pass condition, the evidence it leaves, a retry cap and an on-fail action. Runs with nobody watching proceed on stated assumptions instead of stalling.
- **Faster gate script.** `gate.js --only <name>` checks one component in 1 to 5 seconds instead of re-checking the whole page (about 20 seconds) after every change.
- **Fewer false failures.** Native selects, roving-tabindex tab lists and containers around a broken child no longer fail. Inline color literals are now caught, and SVG labels the script can't measure are counted and reported.
- **No retyping.** The scripts live inside each SKILL.md and are extracted with one command.
- **One report template** replaces reporting rules that were spread over seven places.

## Install

Each folder is one skill. For Claude Code, copy the folders into `~/.claude/skills/`. In the Claude apps, add each folder as a skill in your skill settings.

## Use the gate script

The gate checks every element marked `data-component="<type>"` in headless Chromium, at 1440 and 390 pixels wide. Extract it from the skill file:

```bash
mkdir -p .design && python3 - design-lean/SKILL.md <<'PY'
import re, sys
for name, code in re.findall(r"`{3}js\n// file: (\S+)\n(.*?)`{3}", open(sys.argv[1]).read(), re.S):
    open(".design/" + name, "w").write("// file: " + name + "\n" + code); print("wrote .design/" + name)
PY
node -e "require('playwright')" 2>/dev/null || (npm i -D playwright && npx playwright install chromium)
node .design/gate.js page.html --only "<data-name>"   # one component
node .design/gate.js page.html                          # the whole page
```

## Test the gate

`tests/gate-fixture.html` has 13 seeded defects and clean controls. Running the gate on it should give 13 of 30 rows passing. These cases should fail: D1 off-grid padding, D2 low contrast, D3 placeholder-only input, D4 inline color literal, D5 `transition: all`, D6 no focus ring, D7 tabs without a hover change (at 1440 only), D10 image without size and D12 an 18px radius. Everything else should pass, and D11 should be reported as an unchecked SVG label.

```bash
node .design/gate.js tests/gate-fixture.html
```

## Credits

Built from frontend-design (Anthropic, Apache 2.0); unslop by Damir Sokolovsky (https://github.com/heydamir/unslop), CC BY 4.0, condensed and adapted; interface-design by Damola Akinleye (MIT); heuristic-evaluation and accessibility-audit from Designer Skills by MC Dean (MIT); and Stageshow by Benji Taylor (https://github.com/benjitaylor/skills, MIT), as adapted in the Anthropic design skill. Full credits and the Stageshow license notice are at the end of each SKILL.md.

No license file is included. The skills combine material under CC BY 4.0, MIT and Apache 2.0 with Anthropic's design skill, which doesn't state its own license.
