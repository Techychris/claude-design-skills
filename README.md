# Claude skills

My Claude skills: interface design, UX, writing, documents, diagrams, video and agent work. Each folder is one skill.

<!-- SKILLS-INDEX:START -->
| Skill | Use it for |
| --- | --- |
| [`accessibility-audit`](accessibility-audit/SKILL.md) | Audit an existing interface against WCAG 2.2, producing findings with severity ratings and remediation steps. Use when you have a design or build to assess now. |
| [`agent-architect-mentor`](agent-architect-mentor/SKILL.md) | Use whenever someone wants to design, build, debug, review, or learn about AI agents or agentic systems, or requests a rigorous multi-role self-review… |
| [`brknpipe`](brknpipe/SKILL.md) | 7-step self-review pipeline for high-quality output. Executor-agnostic: roles (Planner, Worker, Reviewer, Assembler, Revision Editor) fillable by a person,… |
| [`building-explainer-sites`](building-explainer-sites/SKILL.md) | Designs, builds, and audits explainer web pages such as explorable explanations, interactive essays, and scrollytelling articles, applying evidence-based… |
| [`design`](design/SKILL.md) | Build, polish (unslop) or review any UI: landing pages, sites, dashboards, app screens. Also faux product UI: hero demos, feature-card stills, bento grids and… |
| [`design-demo`](design-demo/SKILL.md) | Use instead of the built-in design skill's Demo mode for faux product UI: hero or feature-card illustrations of an app, bento grids, mocked screens, animated… |
| [`design-lean`](design-lean/SKILL.md) | Use instead of the built-in design skill to build, polish (unslop) or review UI: landing pages, sites, dashboards, app screens. Same craft rules, run as a… |
| [`design-pipeline`](design-pipeline/SKILL.md) | Take an app idea to a gated, audited single-file HTML prototype with parallel subagents: build 2-3 directions, run the gate and a behavior probe, audit from accessibility, usability and visual viewpoints, verify severe findings in a browser. |
| [`diagram-forge`](diagram-forge/SKILL.md) | Create clean, professional box-and-arrow diagrams (flowcharts, architecture diagrams, control-spectrum/comparison panels, node graphs) as PNG images via a… |
| [`docforge`](docforge/SKILL.md) | Create polished, professionally designed Word documents from a JSON spec — reports, memos, letters, executive briefs, and meeting minutes with real cover… |
| [`heuristic-evaluation`](heuristic-evaluation/SKILL.md) | Run an expert review against Nielsen's heuristics and domain criteria, with severity ratings. Use when you need usability findings without recruiting… |
| [`interface-design`](interface-design/SKILL.md) | Craft-first design for dashboards, admin panels, SaaS apps, settings and data UIs: hierarchy, tokens, states, polish. Not for landing or marketing pages. |
| [`plain-writing`](plain-writing/SKILL.md) | Write or revise prose without AI-writing tells (correctio, padded triplets, purple prose, filler words, generic hedges). Use for any drafted text meant for a… |
| [`remove-ai-tells`](remove-ai-tells/SKILL.md) | Detects and strips recognizable AI-writing tells from drafted text before it goes out to a reader. Covers em dashes, banned filler vocabulary (delve,… |
| [`terse`](terse/SKILL.md) | Write or revise prose without AI-writing tells (correctio, padded triplets, purple prose, filler words, generic hedges). Use for any drafted text meant for a… |
| [`unslop`](unslop/SKILL.md) | Polish or redesign a UI so it stops looking AI-generated: audit the slop, set a direction from the product, fix it in nine passes. Use for unslop, polish,… |
| [`ux-mapping`](ux-mapping/SKILL.md) | Build or review journey maps, service blueprints, experience maps and empathy maps from evidence, with traceable pains and opportunities and a checked visual… |
| [`ux-wireframe`](ux-wireframe/SKILL.md) | Turn a UX opportunity or brief into lo-fi wireframes, with 3+ directions to compare, an annotated spec with states, accessibility and responsive rules, and a… |
| [`video-creator`](video-creator/SKILL.md) | Create narrated videos (MP4) with engaging, natural-sounding AI voiceover — never robotic. Use this skill whenever the user asks to make a video, explainer,… |
| [`web-motion`](web-motion/SKILL.md) | Use when asked to animate web UI, add or tune transitions, fix janky or laggy animation, handle prefers-reduced-motion, review or audit motion, or name an… |
<!-- SKILLS-INDEX:END -->

`terse` and `plain-writing` are the same skill under two names.

## Install

For Claude Code, copy the folders you want into `~/.claude/skills/`. In the Claude apps, add each folder as a skill in your skill settings (zip the folder first if the app asks for a file).

## Keep this repo in sync

`scripts/sync_skills.py` copies every skill you uploaded to your Claude account into this repo and rebuilds the index above. Anthropic's built-in skills are skipped. Run it from a Claude session that has your skills synced:

```bash
python3 scripts/sync_skills.py --dry-run   # see what would change
python3 scripts/sync_skills.py
git add -A && git commit -m "Sync skills" && git push
```

It never deletes a folder. Skills you removed from your account are listed so you can delete them by hand.

## design-lean and design-demo

These two are the Anthropic design skill rebuilt as a gated workflow.

- **Smaller load.** Demo mode is its own skill, so Build, Polish and Review runs load 33% less text.
- **Gate register.** Every gate has a pass condition, the evidence it leaves, a retry cap and an on-fail action. Runs with nobody watching proceed on stated assumptions instead of stalling.
- **Faster gate script.** `gate.js --only <name>` checks one component in 1 to 5 seconds instead of re-checking the whole page (about 20 seconds) after every change.
- **Fewer false failures.** Native selects, roving-tabindex tab lists and containers around a broken child no longer fail. Inline color literals are now caught, and SVG labels the script can't measure are counted and reported.
- **No retyping.** The scripts live inside each SKILL.md and are extracted with one command.
- **One report template** replaces reporting rules that were spread over seven places.

### Use the gate script

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

### Test the gate

`tests/gate-fixture.html` has 13 seeded defects and clean controls. Running the gate on it should give 13 of 30 rows passing. These cases should fail: D1 off-grid padding, D2 low contrast, D3 placeholder-only input, D4 inline color literal, D5 `transition: all`, D6 no focus ring, D7 tabs without a hover change (at 1440 only), D10 image without size and D12 an 18px radius. Everything else should pass, and D11 should be reported as an unchecked SVG label.

```bash
node .design/gate.js tests/gate-fixture.html
```

## Licenses and credits

Eight skills reuse other people's work. Each of those folders has a `THIRD_PARTY_NOTICES.md` with the copyright and license notice for every source it uses, so the notices stay with a folder you copy on its own. [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) at the root lists them all, and the original license files are in [`LICENSES/`](LICENSES/).

| Source | Author | License | Used in |
| --- | --- | --- | --- |
| [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Anthropic | Apache 2.0 | `design`, `design-lean` |
| [unslop](https://github.com/heydamir/unslop) | Damir Sokolovsky | CC BY 4.0 | `unslop`, `design`, `design-lean` |
| [interface-design](https://github.com/Dammyjay93/interface-design) | Damola Akinleye | MIT | `interface-design`, `design`, `design-lean` |
| [Designer Skills](https://github.com/Owl-Listener/designer-skills) | MC Dean | MIT | `heuristic-evaluation`, `accessibility-audit`, `design`, `design-lean` |
| [Stageshow](https://github.com/benjitaylor/skills/tree/main/stageshow) | Benji Taylor | MIT | `design`, `design-demo` |
| [skills](https://github.com/emilkowalski/skills) | Emil Kowalski | MIT | `web-motion` |
| [motion-design-skill](https://github.com/LottieFiles/motion-design-skill) | LottieFiles | MIT | `web-motion` |
| [animation-principles](https://github.com/dylantarre/animation-principles) | Dylan Tarre | MIT | `web-motion` |

`ux-wireframe`, `ux-mapping` and `diagram-forge` credit other projects for ideas only, not text, so they carry no license notice. Their credits are in their SKILL.md files.

`design`, `design-lean` and `design-demo` are also built from Anthropic's design skill, which doesn't state a license. Because of that, and because the repo mixes CC BY 4.0, MIT and Apache 2.0 material, there's no single license for the repo as a whole.
