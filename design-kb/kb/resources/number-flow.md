# NumberFlow: verification of kb/ui-components.md section 4, and resources

Checked 2026-11-12 against official sources (GitHub repo page, docs site number-flow.barvian.me and its /vanilla page, the React source file and package.json on raw.githubusercontent.com, and a machine-readable docs digest at context7.com). Tags: [verified] = read in this run; [inferred] = deduced. Verdicts: CONFIRMED / CONTRADICTED / STALE / UNVERIFIABLE.

Source notes:
- The GitHub README could not be read: the raw README URLs on the main and master branches returned pages that did not include the README sections. Install and props were checked against the docs site, the docs digest, and the React source instead.
- https://number-flow.barvian.me/react returned a client error. The npm page for @number-flow/react returned a client error. Both are listed as seen in search only.
- The docs digest (context7) and the docs site disagree on whether `ensure` exists and on the docs' React-only scope. See the table.
- The docs site says `continuous` is the only plugin; the digest says it is one example. The vanilla page documents only `continuous`.

## Verdict table

| # | KB claim (section 4) | Verdict | Deciding URL | Tag | Note |
|---|---|---|---|---|---|
| N1 | Animated number; digits animate between values; core is a framework-agnostic web component `number-flow`; wrappers for React, Svelte, Vue | CONFIRMED (core and React/Vue/Svelte listed); UNVERIFIABLE (Svelte and Vue versions) | https://github.com/barvian/number-flow ; https://number-flow.barvian.me/vanilla | [verified] for the package list; versions not checked | Repo page says it is for React, Vue, Svelte and TS/JS. Vanilla page imports the `number-flow` package. |
| N2 | Install: `npm install @number-flow/react`; no install command in docs or README | CONFIRMED (package name, version 0.6.2); VERIFIED (docs page has no install snippet) | https://raw.githubusercontent.com/barvian/number-flow/main/packages/react/package.json ; https://npmjs.com/package/@number-flow/react | [verified] package.json version 0.6.2; install-command absence not checked (README not read) | The vanilla page shows `import 'number-flow'` and an esm.sh URL, but no npm command. Do not say the docs have no install command until the README is read. |
| N3 | Default export; `<NumberFlow value={count} />` | CONFIRMED | https://github.com/barvian/number-flow (packages/react/src/NumberFlow.tsx) ; https://context7.com/websites/number-flow_barvian_me/llms.txt?tokens=10000 | [verified] | Default export is a forwardRef component. |
| N4 | `format` example with `{ style: 'percent' }` | CONFIRMED | https://context7.com/websites/number-flow_barvian_me/llms.txt?tokens=10000 | [verified] | format takes standard Intl options. |
| N5 | Key props: value, format, locales, prefix, suffix, willChange, isolate, onAnimationsStart, onAnimationsFinish | CONFIRMED | https://raw.githubusercontent.com/barvian/number-flow/main/packages/react/src/NumberFlow.tsx ; https://context7.com/websites/number-flow_barvian_me/llms.txt?tokens=10000 | [verified] | All present in the Props type. |
| N6 | `respectMotionPreference` default true | CONFIRMED | https://number-flow.barvian.me/vanilla ; https://context7.com/websites/number-flow_barvian_me/llms.txt?tokens=10000 | [verified] | Setting it false animates even for users who prefer reduced motion. |
| N7 | Animation respects prefers-reduced-motion by default | CONFIRMED | https://number-flow.barvian.me/vanilla | [verified] | Same source as N6. |
| N8 | `NumberFlowGroup` coordinates several numbers | CONFIRMED | https://raw.githubusercontent.com/barvian/number-flow/main/packages/react/src/NumberFlow.tsx ; https://context7.com/websites/number-flow_barvian_me/llms.txt?tokens=10000 | [verified] | Exported as a named export. Docs say to wrap numbers that affect each other's position. |
| N9 | React dependency peers ^18 \|\| ^19; Svelte ^4 \|\| ^5; Vue ^3 | CONFIRMED (React, Svelte, Vue; verified on npm 2026-11-12) | https://raw.githubusercontent.com/barvian/number-flow/main/packages/react/package.json | [verified] for React | The React package.json peers are react and react-dom ^18 \|\| ^19. Svelte and Vue package.json files were not fetched. |
| N10 | Runtime dependencies: `esm-env`, and `number-flow` for the React package | CONFIRMED | https://raw.githubusercontent.com/barvian/number-flow/main/packages/react/package.json | [verified] | Dependencies are esm-env ^1.1.4 and number-flow (workspace). |
| N11 | `continuous` plugin makes transitions pass through intermediate digits | CONFIRMED | https://number-flow.barvian.me/vanilla | [verified] | Docs say it has no effect when `trend` is 0. |
| N12 | Component inventory: NumberFlow, NumberFlowGroup, web-component element | CONFIRMED | https://raw.githubusercontent.com/barvian/number-flow/main/packages/react/src/NumberFlow.tsx | [verified] | Exports NumberFlowElement, NumberFlow (default), NumberFlowGroup. |
| N13 | React wrapper starts with `'use client'` | CONFIRMED | https://raw.githubusercontent.com/barvian/number-flow/main/packages/react/src/NumberFlow.tsx | [verified] | First line of the file. |
| N14 | License MIT | CONFIRMED | https://github.com/barvian/number-flow | [verified] | Repo page summary states MIT. LICENSE file not opened. |
| N15 | Maintenance: active, last commit 2026-09-20 (unverified), changesets for releases | UNVERIFIABLE (last npm publish 2026-07-18) | https://github.com/barvian/number-flow | n/a | Commit date not fetched. Repo page showed about 7.7k stars and 10 open issues, which does not confirm the date. |
| N16 | Docs live at number-flow.barvian.me | CONFIRMED | https://github.com/barvian/number-flow ; https://number-flow.barvian.me | [verified] | Repo page links to the docs site. |
| N17 | The 0.0.1 in site/package.json belongs to the docs app | UNVERIFIABLE | none | n/a | Not fetched. |
| N18 | Svelte 0.4.2 and Vue 0.5.2 package versions | VERIFIED | https://registry.npmjs.org/@number-flow/svelte ; https://registry.npmjs.org/@number-flow/vue | [verified] 2026-11-12 | npm latest: @number-flow/svelte 0.4.2, @number-flow/vue 0.5.2; @number-flow/react and number-flow 0.6.2 (2026-07-18). |
| N19 | Gotcha: `prefers-reduced-motion` default (repeat of N7) | CONFIRMED | https://number-flow.barvian.me/vanilla | [verified] | Duplicate of N7. |

## Missed guidelines

Each item comes from the docs site, the docs digest, or the React source, unless marked otherwise.

1. `digits` sets per-position maximums, which suits clocks and countdowns. It is not reactive: changing it after mount does not apply. [verified: docs digest]
2. `trend` sets digit spin direction: always up, always down, or by the sign of the change (the default). `continuous` has no effect when `trend` is 0. [verified: docs digest and vanilla page]
3. `animated={false}` turns off animations and finishes any that are running. Use this for an instant update, not the reduced-motion setting. [verified: vanilla page]
4. `respectMotionPreference={false}` animates even for reduced-motion users. Treat this as an override that needs a reason. [verified: vanilla page]
5. `isolate` has no effect inside a NumberFlowGroup. [verified: docs digest]
6. Timing props: `transformTiming` for layout, `spinTiming` for digit spins (falls back to transformTiming), `opacityTiming` for fades. Each takes an effect-timing object. [verified: docs digest]
7. Styling: the element exposes `::part` hooks (the suffix is one example). Part styling only applies in browsers with Declarative Shadow DOM. Use the feature-detection snippet that sets a `data-supports-dsd` attribute on the root, and add a fallback for older browsers, which may briefly show unstyled content. [verified: vanilla page and docs digest]
8. CSS custom properties: `--number-flow-mask-height` (default 0.25em) sets the edge-fade height and the top and bottom padding; `--number-flow-mask-width` (default 0.5em) sets the fade width. [verified: vanilla page]
9. Spin spacing is controlled by `line-height` (default 1; examples use 0.85). Use `font-variant-numeric: tabular-nums` to keep digit widths fixed during transitions. Changing the digit font size is hard because of the technique. [verified: vanilla page; the font-size remark from docs digest]
10. CSP: pass `nonce` for the inline style elements. For a hash-based policy, hash the exported `styles` strings. [verified: vanilla page and docs digest]
11. SSR: the React component renders its inner HTML on the server (empty in the browser) and sets `suppressHydrationWarning`. On the vanilla path, `renderInnerHTML` takes the same locales, format, prefix, suffix and nonce as the client. [verified: NumberFlow.tsx and vanilla page]
12. Formatting limits: scientific and engineering notation, non-Latin digits, and right-to-left locales are not supported. Compact notation and currency via Intl options do work. [verified: docs digest]
13. `useCanAnimate` reports whether animation is possible, optionally factoring in the motion preference. Use it to skip JS-driven effects. [verified: docs digest; hook name only]
14. Motion for React is recommended for borders and backgrounds, which NumberFlow cannot animate smoothly. The docs also give a spring setting (duration 0.9, bounce 0) that matches NumberFlow's default timing. [verified: docs digest]
15. The React wrapper's `'use client'` directive means it cannot be used inside a Server Component's render directly. Wrap it, or pass it from a client boundary. [inferred from `'use client'` plus standard React rules]
16. The docs site says `continuous` is the only plugin, and the digest names `ensure`. The KB does not mention `ensure`. Check the installed package's plugin exports before documenting it. [inferred from the conflict between sources]

## Resources

| # | Title | URL | Type | Why useful |
|---|---|---|---|---|
| 1 | NumberFlow repo (barvian/number-flow) | https://github.com/barvian/number-flow | Official repo | Source for the React wrapper, packages, changesets, and license. |
| 2 | NumberFlow docs | https://number-flow.barvian.me | Official docs | Primary usage, props, and framework guidance. |
| 3 | NumberFlow vanilla docs | https://number-flow.barvian.me/vanilla | Official docs | Full CSS parts, custom properties, plugins, reduced motion, SSR and nonce details. Read this for styling. |
| 4 | @number-flow/react on npm | https://npmjs.com/package/@number-flow/react | Package registry | Version and peer dependency check. Page did not load in this run; seen in search. |
| 5 | number-flow on jsDelivr (lite.d.ts, 0.6.0) | https://cdn.jsdelivr.net/npm/number-flow@0.6.0/dist/lite.d.ts | Type declarations | Exact prop types for the core lite build. Seen in search, not read. |
| 6 | @number-flow/react package.json on jsDelivr (0.6.0) | https://cdn.jsdelivr.net/npm/@number-flow/react@0.6.0/package.json | Package metadata | Confirms peers and dependencies for that release. Seen in search, not read. |
| 7 | NumberFlow docs digest (context7) | https://context7.com/websites/number-flow_barvian_me/llms.txt?tokens=10000 | Machine-readable docs mirror | Compact summary of props and gotchas. Third-party copy; check against the official docs. |
| 8 | Maxwell Barvian developer spotlight (Codrops) | https://tympanus.net/codrops/?p=86563 | Interview | Background on the author and the design intent. Seen in search, not read. |
| 9 | NumberFlow on 21st.dev | https://21st.dev/@barvian/components/number-flow | Community listing | Shows a copy-paste install path and usage. Third-party. Seen in search, not read. |
| 10 | NumberFlow on Best of JS | https://bestofjs.org/projects/number-flow | Directory | Ranking and related-project list. Seen in search, not read. |
| 11 | @number-flow/react on Socket | https://socket.dev/npm/package/@number-flow/react/overview/0.3.0 | Package analysis | Dependency and supply-chain view for an older release. Seen in search, not read. |
| 12 | Vue usage guide (Made with Vue.js) | https://madewithvuejs.com/go/numberflow-for-vue | Tutorial | Basic Vue usage for the Vue wrapper. Third-party. Seen in search, not read. |

Note: the README now reads "An animated number component for React, Vue, Svelte, and TS/JS." and the docs site returns 200 [verified 2026-11-12]. Missed guidelines also include the `useCanAnimate({ respectMotionPreference })` hook, `animated`, `trend`, `transformTiming` / `spinTiming` / `opacityTiming` props and non-reactive `digits`. Resources 4-6 and 8-12 were seen in search results only. Their content is not verified here. The Svelte and Vue wrapper docs were not found in official sources during this run.

_Validated 2026-11-12 against primary sources; see ../../validation-reports/._
