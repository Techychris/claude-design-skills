# Validation B: ui-craft.md, ui-core.md, motion.md (checked 2026-11-12)

Scope note: these three files are repo-summary KBs (skills and component libraries), not design-theory references. They hold about 40 checkable factual or normative claims; most of the topics in the brief (8pt grid, line length, APCA, dvh, container queries, foldables, view transitions, scroll-driven animation, WCAG 2.2.2/2.3.3) are absent and are listed under "Missing or misframed". Files were read only, not edited.

Sources opened (all fetched this session):
- M3 = https://raw.githubusercontent.com/material-components/material-components-android/master/docs/theming/Motion.md and .../Color.md
- M1 = https://m1.material.io/layout/metrics-keylines.html (Material 1, flagged by the page as no longer maintained)
- HIG-M = https://developer.apple.com/design/human-interface-guidelines/motion.md
- HIG-A = https://developer.apple.com/design/human-interface-guidelines/accessibility.md
- NNG = https://www.nngroup.com/articles/animation-duration/
- MDN-RM = https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
- BCD = @mdn/browser-compat-data 8.1.9 (https://cdn.jsdelivr.net/npm/@mdn/browser-compat-data/data.json)
- CIU = caniuse database, https://raw.githubusercontent.com/Fyrd/caniuse/main/features-json/<feature>.json
- WCAG 2.5.8 https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html ; 2.5.5 https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html ; 2.3.3 https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html ; 2.2.2 https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html ; 1.4.3 https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html ; 1.4.11 https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html ; 1.4.12 https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html
- WCAG3 = https://www.w3.org/TR/wcag-3.0/
- W-CMP = https://web.dev/articles/stick-to-compositor-only-properties-and-manage-layer-count (last updated 2015)
- W-RAIL = https://web.dev/articles/rail
- BUI = https://base-ui.com/react/handbook/animation
- CSST = https://css-tricks.com/?p=15151 (nested radius)
- UYL = https://useyourloaf.com/blog/iphone-17-screen-sizes/
- AND = https://developer.android.com/guide/topics/ui/accessibility/apps
- npm registry (registry.npmjs.org) and https://endoflife.date/api/nodejs.json

Not verifiable (JS-only pages): m3.material.io motion/dark theme pages, caniuse.com UI, Apple HIG HTML pages (the .md variants worked).

## Claim table

| # | file:section | claim | verdict | correction (exact figures) | source URL(s) |
|---|---|---|---|---|---|
| 1 | ui-craft §1 rule 5 | Spacing on a 4px grid | NUANCE | Valid, but Material 1 uses an 8dp grid for components and a 4dp grid for toolbar icons and type baseline; 4px is the finer unit. KB never mentions the 8pt grid. | M1 |
| 2 | ui-craft §1 rule 6 | Hairline borders at 6 to 10% opacity | NUANCE | Style choice, unsourced. A border that is the only cue for an input or button boundary must reach 3:1 against the adjacent colour (WCAG 1.4.11, AA); 6-10% alpha borders almost never do. Decorative dividers are exempt. | WCAG 1.4.11 |
| 3 | ui-craft §1 rule 7 | One icon set, 16 or 18px, 1.5 stroke | UNSOURCED | House style of one repo, no standard. Touch target must still be sized separately (see #9). M1 pairs a 24dp icon with a 48dp target. | M1 |
| 4 | ui-craft §1 rule 8 | Weights 400/500, no tracked uppercase labels | UNSOURCED | Taste rule; no primary source. | none |
| 5 | ui-craft §1 rule 9 | Nested radius = outer radius minus padding, minimum 4 | VERIFIED | Formula confirmed: inner = outer - gap (20px outer, 5px padding gives 15px). Add: subtract border width too; small radii need optical tuning. "minimum 4" is unsourced. | CSST |
| 6 | ui-craft §1 rule 10 / motion §1 rule 8 | Animate only transform and opacity; no transition: all | VERIFIED | web.dev: "only two properties" are compositor-only (transform, opacity). Caveat: article dates from 2015; layer promotion is needed to skip paint. Base UI's own example transitions transform and opacity. | W-CMP, BUI |
| 7 | ui-craft §2 rule 6 | Dark themes: step surfaces by a few percent lightness | VERIFIED (part) | M3 dark roles use tonal surface containers instead of elevation overlays: neutral4, 10, 12, 17, 22 (lowest to highest). Low-alpha white borders and "shadows do not read" are unsourced. | M3 Color.md |
| 8 | ui-craft §2 rule 7 | Type ratio about 1.2 to 1.333 | UNSOURCED | Design convention; no primary source opened. Apple gives size floors instead: 17 pt default and 11 pt minimum on iOS, 13/10 pt macOS. | HIG-A |
| 9 | ui-craft §3 rule 9 | Mobile hit targets 44px or more | NUANCE | Apple: default 44x44 pt, minimum 28x28 pt (iOS/iPadOS). Android: 48x48dp, with 8dp or more between targets (M1). WCAG 2.5.8 (AA) floor is 24x24 CSS px; 2.5.5 (AAA) is 44x44 CSS px. 44 is fine as a default but is not the AA requirement. | HIG-A, AND, M1, WCAG 2.5.8, 2.5.5 |
| 10 | ui-craft §3 rule 9 | Slide text 24px+, print 12pt+ | UNSOURCED | Repo-specific minimums, no standard. | none |
| 11 | ui-craft §3 commands | Node 20 or newer for scripts | OUTDATED | Node 20 reached EOL 2026-04-30. Node 22 EOL 2027-04-30, Node 24 EOL 2028-04-30, Node 26 became LTS 2026-10-28 (EOL 2029-04-30). chrome-devtools-mcp 1.13.0 still accepts ^20.19.0, ^22.12.0 or >=23. | endoflife.date, npm |
| 12 | ui-craft §3 rule 7 | Pin React 18.3.1 and Babel 7.29.0 | NUANCE | Both versions exist. Current npm latest: react 19.3.1, @babel/standalone 8.1.2; the 7.x line is at 7.29.14. Pinning is deliberate but stale. | npm |
| 13 | ui-craft §4 rule 3 | Canvas: iPhone 375x812, Android 360x800, web 1200/1440 | OUTDATED | 375x812 is the iPhone X-12 mini class. iPhone 17 and 17 Pro are 402x874, Air 420x912, 17 Pro Max 440x956 (points). Android 360x800 unsourced. | UYL |
| 14 | ui-craft §4 rule 2 | Spacing 10/20/40px | NUANCE | Off the 4/8 grid and inconsistent with §1 rule 5 (4px grid). | M1 |
| 15 | motion §1 rule 1 | No motion on tens-to-hundreds-per-day actions | VERIFIED | Apple: "generally avoid adding motion to UI interactions that occur frequently"; "Let people cancel motion." Keyboard-triggered part is unsourced. | HIG-M |
| 16 | motion §1 rule 2 | Entering and exiting UI uses ease-out; ease-in feels slow | NUANCE | Entering: ease-out is right (NN/g). Exiting: M3 uses accelerate curves (emphasized-accelerate cubic-bezier(0.3, 0, 0.8, 0.15); standard-accelerate (0.3, 0, 1, 1)), and NN/g says ease-in or ease-in-out are "sometimes used" for exits though they can feel unresponsive. Emil's exit rule is a house style, not the spec. | M3, NNG |
| 17 | motion §1 rule 3 | Keep UI animations under 300 ms | NUANCE | NN/g: 100-500 ms overall, most 100-400; simple feedback about 100 ms; modal/substantial change 200-300 ms; large movement up to 400 ms; above 500 ms drags. M3 medium tokens run 250-400 ms. Fine for small UI, not a universal cap. | NNG, M3 |
| 18 | motion §1 rule 4 | Never animate from scale(0); start 0.9-0.97 | UNSOURCED | Design opinion. Neither Apple HIG nor M3 states it. | HIG-M, M3 |
| 19 | motion §1 rule 6 | Press scale about 0.97 | UNSOURCED | Taste value. | none |
| 20 | motion §1 rule 7 | Interruptible UI: CSS transitions, not keyframes | VERIFIED | Base UI: transitions "can be smoothly cancelled midway"; keyframes are the alternative. | BUI |
| 21 | motion §1 rule 9 | Gate hover with hover:hover / pointer:fine; reduced motion keeps opacity/colour, drops movement | VERIFIED | hover/pointer media: Chrome 38/41, Firefox 64, Safari 9. MDN: reduced-motion styles may "remove, reduce, or replace" motion, example swaps scaling for an opacity dissolve. Apple: replace x/y/z transitions with fades. | BCD, CIU, MDN-RM, HIG-A |
| 22 | motion §1 rule 10 | Springs for gesture-driven motion | NUANCE | Apple HIG "Motion" page does not mention springs or give durations. HIG-A: for Reduce Motion, tighten springs to reduce bounce. Web springs via CSS linear(): Chrome 113, Firefox 112, Safari 17.2. | HIG-M, HIG-A, BCD |
| 23 | motion §2 rule 1 | Never linear for spatial movement; linear for spinners/progress | VERIFIED | NN/g: linear "usually looks unnatural". M3 keeps linear (0,0,1,1) for "simple, non-stylized motion". | NNG, M3 |
| 24 | motion §2 rule 2 | Never change important state with opacity alone | UNSOURCED | Not in sources opened. WCAG 1.4.1 (colour alone) is related but different. | none |
| 25 | motion §2 rule 3 | No motion over a third of the screen without intermediate keyframe | UNSOURCED | Rule of thumb. | none |
| 26 | motion §2 rule 6 | Entrances decelerate, exits accelerate | VERIFIED | M3: standard-decelerate (0,0,0,1), emphasized-decelerate (0.05,0.7,0.1,1) for enter; standard-accelerate (0.3,0,1,1), emphasized-accelerate (0.3,0,0.8,0.15) for exit; standard (0.2,0,0,1). | M3 |
| 27 | motion §2 rule 7 | Entrances 30-50% longer than exits | NUANCE | NN/g: entry "slightly longer" (popup about 300 ms in, 200-250 ms out, so 20-50%). M3 container transform 300 in / 250 out (20%); M3 fade 150 in / 75 out (100%). No fixed ratio. | NNG, M3 |
| 28 | motion §2 rule 8 | Scale duration with distance: 100 px base, 200 px about 1.3x | NUANCE | Principle verified (M3: "duration should increase as the area/traversal of an animation increases"). The 100px/1.3x numbers are unsourced. M3 tokens: short1-4 = 50/100/150/200; medium1-4 = 250/300/350/400; long1-4 = 450/500/550/600; extra-long1-4 = 700/800/900/1000 ms. | M3 |
| 29 | motion §2 rule 9 | Reduced motion: remove spatial movement, keep opacity, halve duration, no auto-play loops | NUANCE | Direction fits MDN and HIG-A (reduce automatic and repetitive animation; replace with fades). "At least half" is unsourced. KB omits the legal-style hooks: WCAG 2.2.2 (Level A) needs pause/stop/hide for auto-starting moving content over 5 seconds, regardless of the media query; WCAG 2.3.3 (Level AAA) needs interaction-triggered motion to be disengageable unless essential. | MDN-RM, HIG-A, WCAG 2.2.2, 2.3.3 |
| 30 | motion §2 rule 10 | Hover under 100 ms, press under 150 ms | NUANCE | NN/g: simple feedback (checkbox, toggle) about 100 ms, and below 100 ms is near the perception limit. web.dev: respond to input within 100 ms. 150 ms press ceiling unsourced. | NNG, W-RAIL |
| 31 | motion §2 rule 11 | One animated property direct, two polished, three+ clutter | UNSOURCED | Heuristic. | none |
| 32 | motion §3 rule 4 | Keep stretch under about 10% for accessibility | UNSOURCED | No standard. Apple HIG-A advice instead: avoid animating z-depth and blur, replace x/y/z transitions with fades; visionOS: avoid sustained oscillation near 0.2 Hz. | HIG-A, HIG-M |
| 33 | motion §3 rule 5 | 6 frames snappy, 24 frames deliberate | UNSOURCED | 6 frames at 60 fps = 100 ms, 24 frames = 400 ms; consistent with NN/g but not a source. | NNG |
| 34 | motion §3 rule 8 | Stagger sequences of 5 items or fewer | UNSOURCED | Heuristic. | none |
| 35 | motion §1 (perf), §3 rule 10 | Stay inside the frame budget | VERIFIED | web.dev RAIL: each frame should take 10 ms or less to produce (about 6 ms of the 16 ms is browser overhead). Response within 100 ms. | W-RAIL |
| 36 | motion §4 gotchas | Playwright-core about 1.48 | OUTDATED | Latest 1.65.0 (engines node >=20). | npm |
| 37 | motion §4 gotchas | lucide-react pinned to 0.468.0 | OUTDATED | 0.468.0 was published 2024-12-05; latest is 1.72.0. | npm |
| 38 | motion §4 rule 9 | Reduced motion shows the poster still and complete | VERIFIED | Consistent with MDN (remove/replace) and HIG-A (reduce automatic and repetitive animation). | MDN-RM, HIG-A |
| 39 | ui-core §2 | @base-ui/react 1.9.0; §3 radix-ui 1.8.1, react-dialog 1.3.1 | VERIFIED | npm latest today: @base-ui/react 1.9.0, radix-ui 1.8.1, @radix-ui/react-dialog 1.3.1, shadcn CLI 4.23.0. | npm |
| 40 | ui-core guideline check | Base UI prefers CSS transitions; docs have no reduced-motion guidance | VERIFIED | Handbook says "Transitions are recommended over CSS animations" and never mentions prefers-reduced-motion. | BUI |
| 41 | ui-core §3 Radix | Radix animates exits via data-state/forceMount | UNSOURCED | Not re-opened this run. | none |

## Current browser support (2026-11-12) for topics the KB should carry

Data pulled from CIU and BCD; "global" is the caniuse y-share.

| Feature | Chrome/Edge | Firefox | Safari / iOS | Notes |
|---|---|---|---|---|
| Container queries (size) | 105/106 | 110 | 16.0 | CIU global 95.96% |
| dvh/svh/lvh | 108 | 101 | 15.4 | CIU global 96.07% |
| View Transitions, same-document | 111 | 144 | 18.0 | CIU global 93.17% |
| View Transitions, cross-document (@view-transition) | 126 | preview only (not shipped in BCD) | 18.2 | Firefox gap remains |
| View transition types (:active-view-transition-type) | 125 | 147 | 18.2 | |
| Scroll-driven animations (animation-timeline, scroll(), view()) | 115 | 159 | 26 | Now in all three engines; the "Chromium-only" framing is outdated |
| @starting-style | 117 | 129 | 17.5 | |
| transition-behavior (allow-discrete) | 117 | 129 (partial) | 17.4 | |
| CSS linear() easing | 113 | 112 | 17.2 | spring approximation |
| prefers-reduced-motion | 74 | 63 | 10.1 | CIU global 97.35% |
| prefers-reduced-transparency | 118 | flag only | none | |
| light-dark() | 123 | 120 | 17.5 | |
| field-sizing | 123 | 152 | 26.2 | |
| text-wrap: balance | 130 (CIU) | 121 | 17.5 | CIU global 89.33% |
| interpolate-size | 129 | no | preview | |
| Viewport Segments (horizontal/vertical-viewport-segments, env(viewport-segment-*)) | 138 | no | no | foldables; Chromium-only |
| Device Posture (media device-posture, DevicePosture API) | 132 | no | no | Chromium-only |
| CSS anchor positioning | partial in CIU (Chrome 160, Edge 156, Firefox 163 flagged "a") | partial | full in 27 | check notes before relying |

## Missing or misframed

1. WCAG 2.2.2 (A, auto-start moving content over 5 s needs pause/stop/hide) and 2.3.3 (AAA, interaction-triggered motion disengageable) are not cited anywhere; motion.md frames reduced motion only as taste.
2. Target size: only "44px". Needs the AA/AAA split (24 vs 44 CSS px) and platform values (Apple 44 default/28 min, Android 48dp with 8dp gaps).
3. Contrast: nothing on WCAG 1.4.3 (4.5:1 text; 3:1 for 18 pt or 14 pt bold, about 24px/18.5px) or 1.4.11 (3:1 for UI components, focus indicators). APCA status: WCAG 3.0 is a Working Draft dated 10 September 2026 and says the contrast algorithm "is yet to be determined"; it does not replace WCAG 2. Apple HIG names APCA as a popular measure but uses WCAG AA ratios (4.5:1 up to 17 pt, 3:1 at 18 pt or bold).
4. Typography/readability: no line-length, line-height or type-scale guidance. Verified anchor: WCAG 1.4.12 requires content to survive line height 1.5x, paragraph spacing 2x, letter spacing 0.12x, word spacing 0.16x (AA). The 45-75 character measure was not verified against a primary source and should be labelled unsourced if added.
5. Responsive: no breakpoints, container queries, dvh/svh/lvh, safe-area env(), or foldable APIs (see support table).
6. Motion APIs: no View Transitions, scroll-driven animations, @starting-style, CSS linear() springs, or prefers-reduced-motion implementation pattern (e.g. gate animation-timeline and view-transition animations behind the query).
7. Apple HIG motion framing: the HIG "Motion" page gives no durations or easing; it says make motion optional, avoid motion on frequent interactions, let people cancel motion, keep feedback brief. HIG Accessibility lists Reduce Motion tactics (tighten springs, track gestures, avoid z-depth animation, replace x/y/z transitions with fades, avoid blurs). Do not attribute duration numbers to Apple.
8. Material 3 motion tokens are absent; add the table in row 28 and the easing set in row 26.
9. Visual hierarchy: Apple Layout page states order by importance (top and leading side), align, group, progressive disclosure; none of it is in the KB.
10. Conflicts left open in motion.md: exit easing, duration bands (50-100 vs 100-200 ms micro), squash on press. Add the Material/NN/g position as tie-breaker.
11. ui-core has no craft or accessibility numbers; its Gaps list is honest. Radix/Base UI Dialog accessible-name claims were not re-verified here.

## Suggested exact edits (old -> new)

motion.md
1. `2. Entering and exiting UI uses ease-out; ease-in on UI feels slow because it delays the first movement.`
   -> `2. Entering UI uses ease-out (NN/g, M3 decelerate). For exits Emil prefers ease-out too, but Material 3 uses accelerate curves (emphasized-accelerate cubic-bezier(0.3, 0, 0.8, 0.15)) and NN/g allows ease-in for exits; pick one per project.`
2. `3. Keep UI animations under 300 ms.`
   -> `3. Keep UI animations short: NN/g gives 100-500 ms overall (most 100-400), about 100 ms for simple feedback, 200-300 ms for modal-scale changes; M3 medium tokens are 250-400 ms.`
3. `7. Entrances run about 30-50% longer than exits. SKILL.md:125`
   -> `7. Entrances run slightly longer than exits (NN/g popup about 300 ms in, 200-250 ms out; M3 container transform 300/250). The 30-50% figure is the repo's own; M3 fade uses 150/75.`
4. `9. Reduced motion: remove spatial movement, keep opacity, cut duration by at least half, never auto-play loops.`
   -> `9. Reduced motion: remove, reduce or replace movement (MDN, Apple), keep opacity; "halve duration" is the repo's own. Also WCAG 2.2.2 (A): auto-starting motion over 5 s needs pause/stop/hide; WCAG 2.3.3 (AAA): interaction-triggered motion must be disengageable.`
5. `4. Keep stretch under about 10% for accessibility, and give reduced-motion users an instant state change.`
   -> `4. Keep stretch small (the 10% figure is the repo's own, not a standard), and give reduced-motion users an instant or fade-only state change.`
6. `Filming uses playwright-core ~1.48` -> `Filming uses playwright-core ~1.48 (latest is 1.65.0)`
7. `lucide-react is pinned to 0.468.0` -> `lucide-react is pinned to 0.468.0 (Dec 2024; latest is 1.72.0)`

ui-craft.md
8. `Spacing on a 4px grid; replace one-off values like mt-[13px] with scale steps.`
   -> `Spacing on a 4px grid (Material uses 8dp for components, 4dp for icons and type); replace one-off values like mt-[13px] with scale steps.`
9. `Hairline borders at 6 to 10% opacity.`
   -> `Hairline borders at 6 to 10% opacity for decoration only; borders that mark an input or button boundary need 3:1 contrast (WCAG 1.4.11).`
10. `mobile hit targets 44px or more.`
    -> `mobile hit targets 44px or more (Apple 44 pt default, 28 pt minimum; Android 48dp; WCAG 2.5.8 AA floor 24 CSS px, 2.5.5 AAA 44 CSS px).`
11. `Node 20 or newer for the scripts.`
    -> `Node 20.19 or newer for the scripts (Node 20 is EOL since 2026-04-30; prefer Node 22 or 24).`
12. `Pin React 18.3.1 and Babel 7.29.0 with integrity hashes.`
    -> `Pin React 18.3.1 and Babel 7.29.0 with integrity hashes (both are behind current: React 19.3.1, Babel standalone 8.1.2).`
13. `iPhone 375x812, Android 360x800, desktop web 1200 or 1440 wide.`
    -> `iPhone 375x812 (legacy; current iPhone 17 is 402x874), Android 360x800, desktop web 1200 or 1440 wide.`
14. `Spacing: 10px tight, 20px normal, 40px between sections.`
    -> `Spacing: 10px tight, 20px normal, 40px between sections (off the 4/8 grid; prefer 8/16/40 if consistency with the rest of the KB matters).`
15. Dark-theme rule, `Dark themes: step surfaces by a few percent of lightness and use low-alpha white borders; shadows do not read on dark.`
    -> `Dark themes: step surfaces by a few tone points (M3 dark surface containers: neutral 4, 10, 12, 17, 22) and use low-alpha white borders; shadows do not read on dark.`
