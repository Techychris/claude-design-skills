# Motion skills knowledge base

Built 2026-11-12 from local clones under /home/claude. Repos were only read; this file is the only output.
Tags: [verified] = checked in the file; [inferred] = from names, structure or other files.
Clone HEADs: emilkowalski/skills f7ce8c0; lottiefiles/motion-design-skill f9a8a04; dylantarre/animation-principles 8359713; benjitaylor/skills 299140f. All four worktrees were clean.

Rule line refs are file:line. Rules are paraphrased.

---

## 1. emilkowalski/skills

Path: /home/claude/emilkowalski/skills
Purpose: Opinionated animation and UI-polish skills for agents, written from the author's product work. The README says they aim to steer agents away from common animation mistakes. [verified]

Structure: skills/<name>/SKILL.md, with some folders holding extra files (RECIPES.md, STANDARDS.md, AUDIT.md, API.md, CATALOG.md, PICKER.md, PLAN-TEMPLATE.md). Root: README.md, ui-cheatsheet.md, performance-cheatsheet.md, LICENSE, a 0-byte stray file named .pl. [verified]

Inventory (19 skills):
- animate: build one animation, choosing trigger, tool, properties, curve, duration
- animate-expo: same for React Native / Expo (gestures, sheets, haptics)
- animation-performance: keep motion inside the frame budget; find dropped-frame causes
- animation-vocabulary: map a vague motion description to its exact term
- apple-design: Apple-style fluid, physical motion translated for the web
- ask-sonner: setup and recipes for the Sonner toast library
- break-ui: feed worst-case data to UI and report what breaks
- choreograph: coordinate several elements that move together
- emil-design-eng: main philosophy skill for polish and animation decisions
- find-animation-opportunities: read-only search for where motion helps, and where not to add it
- gestures: drag, swipe and sheet interactions that track the finger
- improve-animations: read-only audit of a codebase's motion, with plans for other agents
- learn-taste: turn session design corrections into rules in DESIGN.md
- mobile-native: CSS and meta fixes so a web app feels installed on phones
- pick-ui-library: curated library picks per frontend task (explicit invocation only)
- prototype: several versions of one UI piece behind a switcher (explicit invocation only)
- remove-animations: subtract motion the interface does not need
- review-animations: strict review of motion code; default is to flag (disable-model-invocation)
- write-swift: modern Swift guidance (value types, concurrency, testing)

Rules (all [verified]):
1. Remove or never add motion on keyboard-triggered actions and on things seen tens to hundreds of times a day. emil-design-eng/SKILL.md:73-77
2. Entering UI uses ease-out (NN/g, M3 decelerate). For exits Emil prefers ease-out too, but Material 3 uses accelerate curves (emphasized-accelerate cubic-bezier(0.3, 0, 0.8, 0.15)) and NN/g allows ease-in for exits; pick one per project. emil-design-eng/SKILL.md:97-98, :121
3. Keep UI animations short: NN/g gives 100-500 ms overall (most 100-400), about 100 ms for simple feedback, 200-300 ms for modal-scale changes; M3 medium tokens are 250-400 ms. emil-design-eng/SKILL.md:135
4. Do not animate from scale(0); start around 0.9-0.97 with opacity (unsourced taste value; neither Apple HIG nor M3 states it). emil-design-eng/SKILL.md:215-219; animate/SKILL.md:86
5. Popovers scale from their trigger; modals stay centred. emil-design-eng/SKILL.md:234-241
6. Pressable elements shrink slightly (about 0.97, unsourced taste value) on :active, with a short transition. emil-design-eng/SKILL.md:201-213
7. For interruptible UI use CSS transitions, not keyframes, because keyframes restart from zero. emil-design-eng/SKILL.md:269-271
8. Animate only transform and opacity; never use transition: all. emil-design-eng/SKILL.md:479; animation-performance/SKILL.md:36
9. Gate hover effects behind hover:hover and pointer:fine. Reduced motion keeps opacity and colour and drops movement. emil-design-eng/SKILL.md:529-557
10. Use springs for gesture-driven motion, since they keep velocity when interrupted. emil-design-eng/SKILL.md:149-195
11. Slow the deliberate phase (hold, press) and snap the response on release. emil-design-eng/SKILL.md:589-591
12. Review findings go in one markdown table, not before/after lines. review-animations/SKILL.md:88-90; emil-design-eng/SKILL.md:40

License: MIT, Copyright (c) 2026 Emil Kowalski. LICENSE:1-3 [verified]. Keep the notice in copied text [inferred: standard MIT term].

Gotchas:
- Rules are written as absolute ("never", "under 300 ms"). They are the author's defaults, not measured thresholds [inferred].
- Conflicts with the other repos on exits: this repo says ease-out for exits; dylantarre/01-by-domain/micro-interactions/SKILL.md:103 uses ease-in for tooltip hide; lottiefiles SKILL.md:44 says exit = accelerate [verified]. Pick one per project.
- Four skills only run when invoked by name: pick-ui-library, prototype, review-animations and learn-taste (frontmatter disable-model-invocation or explicit-only text) [verified].
- animate-expo targets React Native; write-swift targets Swift. Neither applies to web CSS [verified].
- README install is unpinned: `npx skills@latest add emilkowalski/skills` [verified].
- Several skills point to external sites (aiforui.dev, sonner.emilkowal.ski) that are not in this repo [verified].
- The stray .pl file is empty and looks accidental [verified].

---

## 2. lottiefiles/motion-design-skill

Path: /home/claude/lottiefiles/motion-design-skill
Purpose: One implementation-agnostic motion-design skill. It teaches timing, easing, choreography and Disney principles before any code, and says it works with CSS, Framer Motion, GSAP, Lottie and springs. [verified README; SKILL.md:7]

Structure: skills/motion-design/SKILL.md (315 lines) plus 16 support files: director/ (8: philosophy, decision framework, Disney principles, personality, emotion, choreography, narrative, context), patterns/ (4: entrance-exit, state-feedback, ambient, multi-element), reference/ (4: timing-easing tables, property selection, quality checklist, troubleshooting). [verified]

Inventory:
- motion-design: the only skill. Core is an 8-step checklist, motion personalities, duration and easing tables, property guide, common patterns. Depth lives in the subfolders above.

Rules (all [verified] unless marked):
1. Never use linear easing for spatial movement; linear is for spinners and progress bars. SKILL.md:264
2. Never change an important state with opacity alone; pair it with position or scale (unsourced). SKILL.md:265
3. No motion travels more than a third of the screen without an intermediate keyframe (unsourced rule of thumb). SKILL.md:266; director/core-philosophy.md:47
4. Every animation has three layers: primary, secondary, ambient. SKILL.md:267
5. Choose one motion personality per project and apply it consistently. SKILL.md:72
6. Direction sets easing: entrances decelerate, exits accelerate, on-screen movement eases both ends. SKILL.md:44, :140
7. Entrances run slightly longer than exits (NN/g popup about 300 ms in, 200-250 ms out; M3 container transform 300/250). The 30-50% figure is the repo's own; M3 fade uses 150/75. SKILL.md:125
8. Scale duration with distance (principle confirmed by M3; the 100 px / 1.3x numbers are unsourced). M3 tokens: short1-4 = 50/100/150/200 ms; medium1-4 = 250/300/350/400; long1-4 = 450/500/550/600; extra-long1-4 = 700/800/900/1000. SKILL.md:123
9. Reduced motion: remove, reduce or replace movement (MDN, Apple), keep opacity; "halve duration" is the repo's own. Also WCAG 2.2.2 (A): auto-starting motion over 5 s needs pause/stop/hide; WCAG 2.3.3 (AAA): interaction-triggered motion must be disengageable unless essential. Never auto-play loops. director/context-adaptation.md:29
10. Hover feedback under 100 ms (NN/g: simple feedback about 100 ms), press under 150 ms (150 ms ceiling unsourced). SKILL.md:128-129
11. Use the fewest animated properties: one is direct, two polished, three or more risks clutter (unsourced heuristic). SKILL.md:105

License: MIT, Copyright (c) 2025 LottieFiles. LICENSE:1-3; SKILL.md frontmatter license MIT, version 1.0.0 [verified].

Gotchas:
- Exit easing conflicts with emil-design-eng (ease-out for exits) [verified; see section 1].
- Duration tables disagree: the Playful archetype gives 150-300 ms (SKILL.md Motion Personality table), while the Joy row of the emotion map gives 200-400 ms [verified].
- Premium and Gentle float share one curve, (0.4, 0, 0.2, 1) [verified, SKILL.md easing table]. Fine, but the archetypes are not separate in practice [inferred].
- Despite the name, no Lottie-specific API or file-format content exists in the tree; Lottie is only named in the README and the SKILL.md description (SKILL.md:7) [verified].
- The quality checklist and rules are design judgment with no tests or examples to run [inferred].

---

## 3. dylantarre/animation-principles

Path: /home/claude/dylantarre/animation-principles
Purpose: A marketplace of 144 Claude Code skills. Each applies Disney's 12 animation principles to one context: domain, thinking style, role, skill level, animation type, emotion, UI element, industry, tool, time scale, principle focus or problem type. [verified README; CLAUDE.md]

Structure: skills/<group>/<skill>/SKILL.md, 144 files, 12 groups of 12 skills. Each group includes one universal-* fallback. [verified]. docs/ holds rendered copies (145 .md files incl. index.md). CLAUDE.md says skills/ is canonical. [verified]. CONTRIBUTING.md, CHANGELOG.md (1.0.0, 2024-12-30), .github templates. No build or test commands. [verified CLAUDE.md]

Inventory (group level; no per-skill list):
- 01-by-domain: product domains (web motion, micro-interactions, games, mobile, video, data viz, 3D, presentations, brand, accessibility, universal fallback)
- 02-by-thinking-style: how to reason about motion (timing, anticipation, physics, rhythm, spatial, problem diagnosis)
- 03-by-role-persona: job roles (motion designer, frontend developer, PM, teacher, UX researcher, etc.)
- 04-by-skill-level: beginner to master, plus troubleshooting, quick-start, teaching others
- 05-by-animation-type: entrances, exits, loops, hover, scroll, loading, state changes
- 06-by-emotional-outcome: feelings the motion should create (calm, joy, trust, urgency, etc.)
- 07-by-ui-element: buttons, modals, forms, cards, lists, toasts, navigation and similar
- 08-by-industry: fintech, healthcare, e-commerce, education, gaming, travel and similar
- 09-by-tool-framework: CSS, Framer Motion, GSAP, Lottie, Rive, React Spring, Anime.js and similar
- 10-by-time-scale: instant (0-100 ms) through dramatic (2000 ms+) and continuous loops
- 11-by-principle-focus: one deep dive per principle (squash, arc, timing, staging and so on)
- 12-by-problem-type: performance, accessibility, debugging, motion sickness, UX friction and similar

Sample read: 24 of 144 skills (two per group, mostly the first 14-30 lines). Rules below come from that sample.

Rules (from the sample):
1. Never use linear easing for UI motion; use standard ease curves. 01-by-domain/web-motion-design/SKILL.md:39 [verified]
2. When squashing one axis, keep the volume by expanding the other. 01-by-domain/web-motion-design/SKILL.md:29 [verified]
3. Animate only transform and opacity, because these skip layout and paint. 04-by-skill-level/troubleshooting/SKILL.md:33 [verified]
4. Keep stretch small (the 10% figure is the repo's own, not a standard), and give reduced-motion users an instant or fade-only state change. 03-by-role-persona/accessibility-advocate/SKILL.md:14 [verified]
5. Count frames: a 6-frame action (100 ms at 60 fps) reads as snappy, a 24-frame one (400 ms) as deliberate (unsourced; consistent with NN/g). 02-by-thinking-style/timing-mastery/SKILL.md:18 [verified]
6. Show a loading state at once on action; do not wait for a slow response first. 05-by-animation-type/loading-states/SKILL.md:14 [verified]
7. Before a big move, make a small move the other way. 02-by-thinking-style/anticipation-payoff/SKILL.md:18 [verified]
8. Keep stagger sequences to 5 items or fewer unless the user starts them (unsourced heuristic). 05-by-animation-type/entrance-animations/SKILL.md:73 [verified]
9. Entrances can start at about 95% scale with opacity. 05-by-animation-type/entrance-animations/SKILL.md:12 [verified]
10. Performance check: confirm only transform and opacity animate, and use will-change sparingly. 12-by-problem-type/performance-optimization/SKILL.md:50, :54 [verified]

License: MIT, Copyright (c) 2024 Dylan Tarre. LICENSE:1-3 [verified]. The README badge also says MIT [verified].

Gotchas:
- Frontmatter name mismatch: all 12 skills in 04-by-skill-level use a title-case name such as "Animation Principles - Advanced", not the directory slug. The slug is what CLAUDE.md uses for loading [verified; inferred that this breaks slug-based lookup].
- Edit skills/, not docs/. docs/ is a rendered copy [verified CLAUDE.md].
- Timing bands conflict. web-motion-design gives micro 100-200 ms (SKILL.md:22, :45). micro-interactions gives immediate 50-100 ms and standard 100-200 ms (SKILL.md:45). [verified]
- Squash guidance conflicts. micro-interactions scales Y to 0.95 on press with no width compensation (SKILL.md:29); web-motion-design requires expanding X (SKILL.md:29). [verified]
- Ease-in on tooltip hide (micro-interactions SKILL.md:103) conflicts with emil-design-eng. [verified]
- Each skill restates the 12 principles in the same table and sections, so the content is repetitive and most values are unsourced [inferred from the sample].
- CONTRIBUTING.md asks authors to verify code examples, but the repo has no test or lint step [verified CONTRIBUTING.md:130; CLAUDE.md].
- The "Disney" framing is a label for the classic principle set. The source book is not in the repo [inferred].

---

## 4. benjitaylor/skills

Path: /home/claude/benjitaylor/skills
Purpose: A repo with one skill, stageshow, for making faux product UI (stills, feature cards, cursor demos, bento grids). It includes a React kit, examples and tools that film the result so the agent can check it. [verified README; stageshow/SKILL.md:3-9]

Structure: root AGENTS.md holds the real repo instructions; CLAUDE.md is only `@AGENTS.md`; README.md; .github/assets/stageshow.png. stageshow/ holds: SKILL.md (152 lines), README.md, references/ (15 .md files), kit/ (React parts with per-part CSS; brands/ SVGs), examples/ (71 folders: gold scenes, product studies, specimen sheets), teaching/ (bad/good pairs), playground/ (Vite viewer), scripts/ (film, layout, verification), assets/app-icons.ts, package.json. [verified]

Inventory:
- stageshow (SKILL metadata 1.1.1): the one skill. Parts: references/ for craft, framing, motion, kit API, verify, rehearse, teaching; kit/ to copy into a project; examples/ with a gold table; teaching/ for diagnosing bugs; scripts/ for filming and checks.

Rules (all [verified]):
1. Real words only where the story is; placeholder bars for the rest. stageshow/SKILL.md:24
2. Keep real text to about 3-7 strings per screen. stageshow/SKILL.md:40; references/craft.md:9
3. Copy the closest gold example into the project and adapt it; do not rewrite from a glance. stageshow/SKILL.md:39
4. Plan 3-5 beats and one payoff in 10-16 seconds. Every cursor move needs a cause, and data does not rewind without one. stageshow/SKILL.md:38
5. Design at the display size, about 720x340 for a hero beside copy. stageshow/SKILL.md:36
6. The window or phone fills at least two thirds of the stage and runs off an edge. stageshow/references/framing.md:11; stageshow/SKILL.md:48
7. Use kit parts (Button, Card, Row, Field and so on) instead of look-alike hand-built classes. stageshow/SKILL.md:147
8. Set a poster frame that tells the story alone, since most people see only that frame. stageshow/SKILL.md:42; references/motion.md:39
9. Reduced motion shows the poster still and complete. stageshow/references/rehearse.md:107
10. Build the choreography through the Act API and keep elements mounted so exits animate. stageshow/SKILL.md:41
11. Film with the gate, and watch playback at speed: a contact sheet misses one-frame flashes. stageshow/SKILL.md:42; references/rehearse.md:111
12. Avoid stock-AI tells: sparkles, purple, made-up logos. stageshow/SKILL.md:50

License: stageshow/LICENSE is MIT, Copyright (c) 2026 Benji Taylor [verified]. Third-party notices (stageshow/NOTICE.md, stageshow/kit/brands/SOURCES.md) [verified]:
- App icons in assets/app-icons.ts are not MIT; they remain the products' artwork.
- Brand SVGs: SVGL (MIT), payment-icons (Apache 2.0), Cryptocurrency Icons (CC0), and official Linear, American Express and Circle assets.
- Two Wikipedia-study photos are CC0; authors and sources are in examples/wikipedia/PHOTOS.md.
- No bezel photos are bundled. No CC BY content was found in any of the four repos (grep) [verified].

Gotchas:
- Needs Node 20.19 or later (package.json engines). `npm run dev` starts the viewer; `npm run typecheck` and `npm run check:css` are the checks [verified].
- Do not run a production build while the dev server is running in the same workspace (AGENTS.md) [verified].
- Copy kit/ into your project; it is not an installed package. Keep the relative imports. lucide-react is pinned to 0.468.0 (Dec 2024; latest is 1.72.0) [verified package.json].
- Filming uses playwright-core ~1.48 (latest is 1.65.0) and needs local Chrome or CHROME_PATH [verified README].
- Optional dependency `portless` may be skipped; on macOS/Linux run `npm install --include=optional` [verified README].
- Product studies (Figma, Linear, Slack and others) copy real products' look. The skill says to borrow the interaction, not the identity, and NOTICE disclaims endorsement [verified stageshow/SKILL.md:59; NOTICE.md].
- Version mismatch: SKILL metadata 1.1.1 vs package.json 0.1.0 [verified].
- teaching/ bad halves are never starting points [verified stageshow/SKILL.md:59].
- Install line: `npx skills add benjitaylor/skills --skill stageshow` [verified README].

## 5. Validation additions (2026-11-12)

- Apple HIG "Motion" gives no durations or easing: make motion optional, avoid it on frequent interactions, let people cancel it, keep feedback brief. Reduce Motion tactics (HIG Accessibility): tighten springs, track gestures, avoid z-depth and blur animation, replace x/y/z transitions with fades. Do not attribute duration numbers to Apple.
- Material 3 easing: standard (0.2,0,0,1); standard-decelerate (0,0,0,1); emphasized-decelerate (0.05,0.7,0.1,1); standard-accelerate (0.3,0,1,1); emphasized-accelerate (0.3,0,0.8,0.15); linear (0,0,1,1) for simple non-stylized motion.
- Frame budget (web.dev RAIL): about 10 ms per frame of your own work, respond to input within 100 ms. The compositor-only article dates from 2015.
- Open conflicts above (exit easing, micro duration bands, squash on press): tie-breaker is the Material 3 / NN/g position.
- Reduced-motion pattern: gate animation-timeline and view-transition animations behind prefers-reduced-motion.

Browser support (2026-11-12, caniuse and MDN BCD):

| Feature | Chrome/Edge | Firefox | Safari |
|---|---|---|---|
| Scroll-driven animations (animation-timeline, scroll(), view()) | 115 | 159 | 26 (now in all three engines; "Chromium-only" is outdated) |
| View Transitions, same-document | 111 | 144 | 18.0 |
| View Transitions, cross-document (@view-transition) | 126 | preview only | 18.2 |
| @starting-style | 117 | 129 | 17.5 |
| CSS linear() (spring approximation) | 113 | 112 | 17.2 |
| prefers-reduced-motion | 74 | 63 | 10.1 |


_Validated 2026-11-12 against primary sources; see ../validation-reports/._
