# UI SDK (Vercel): overview and resources

Run date: 2026-11-12, by the main session (no subagent). Pages were read through summarising fetches, so wording is paraphrased and line-level details are unchecked. Tags: `[verified]` = stated on a fetched page (URL given); `[estimated]` = my inference; `unknown` = not on any page read. The library is new and in beta, so expect this file to age quickly.

## What it is

- A library of reusable interaction behaviors that AI agents use to build UIs, made by Vercel; source on GitHub under vercel-labs (canonical repo vercel-labs/ui). [verified: https://ui-sdk.dev/]
- Idea: instead of handing an agent a finished select menu, give it the parts (a popup, a selection model, type-to-find) and let it assemble a select, autocomplete, combobox or a new component. [verified: https://ui-sdk.dev/]
- Over 50 behaviors: keyboard navigation, focus management, selection, popups, drag-and-drop reordering, resizing, canvas pan and zoom, list virtualization, screen reader support. [verified: https://ui-sdk.dev/]
- A ready-made component set built from the same behaviors: color pickers, sliders, tabs, calendars, tree views, toolbars, OTP inputs. [verified: https://ui-sdk.dev/]
- The README says the behaviors handle the ARIA attributes they need. [verified: https://github.com/vercel-labs/ui]

## Install and usage

- React: install `@ui-sdk/react` and `@ui-sdk/core` with your package manager. React 19 or newer. [verified: https://ui-sdk.dev/docs]
- Other adapters named in the README: `@ui-sdk/vue`, `@ui-sdk/svelte`, `@ui-sdk/solid`, `@ui-sdk/web`. All six packages (@ui-sdk/core, react, vue, svelte, solid, web) are at 0.1.0-beta.1, all published 2026-11-12, Apache-2.0 (earlier tag 0.0.0-stage); the `latest` dist-tag points at the beta. Peer deps: react and react-dom >=19 with @types/react >=19.2.10; vue >=3.5 (nuxt ^4/^5 optional); svelte >=5.33; solid-js and @solidjs/web >=2.0.0-rc.14 (Solid 2 RC); web has core only. [verified 2026-11-12: https://registry.npmjs.org/@ui-sdk/react ; https://registry.npmjs.org/@ui-sdk/vue ; https://ui-sdk.dev/docs.md]
- Agent setup: add a note to `AGENTS.md` telling the agent to use the ui-sdk skill when available and to read the bundled `llms.txt` before using the library; for new components the agent searches `core.md` by heading and reads the `rendering.md` beside it. [verified: https://ui-sdk.dev/docs]
- Skill: `npx skills add vercel-labs/ui --skill ui-sdk`. [verified: https://ui-sdk.dev/docs]
- Pages without a build step can load `web.js` and `web.css` from the site (`/web.md` explains it; /web.md returns 200, /web.js answers 307 with the redirect target not followed). [verified: https://ui-sdk.dev/llms.txt]
- Docs map: Core (defining and rendering a primitive, styling, composing behaviors, API reference, platform/text/date utilities, behaviors for focus, selection, dragging, lists, trees, transitions, popups and canvases, testing), Agents (agent bridge, WebMCP, skills), Guides, and one `llms.txt` per framework combining its Rendering page with every component reference. [verified: https://ui-sdk.dev/llms.txt]
- The Compose Behaviors guide builds a star rating from shared state and keyboard navigation. Installing and rendering code beyond the package names: not read.

## Status, license, activity

- **Beta.** The README says the framework, APIs, docs and behavior may change before general availability, under Vercel's beta terms. [verified: https://github.com/vercel-labs/ui]
- **License: Apache-2.0.** [verified: same URL]
- Repo snapshot at fetch time (counts drift): 446 commits on `main`, 649 stars, 14 forks, 1 open issue, 2 open pull requests; only collaborators can open issues or PRs. Last-commit date, contributors and release versions: unknown (blank in the capture). [verified: same URL]
- **Canonical repo is github.com/vercel-labs/ui** (npm `repository` field on every @ui-sdk/* package and the docs landing link; `vercel-labs/ui-sdk` is an alias). [verified 2026-11-12: https://registry.npmjs.org/@ui-sdk/react]

## Accessibility

- Claimed: keyboard, focus, selection, dismissal, popups, drag and drop, and ARIA handling are built into the behaviors. [verified as a claim: https://github.com/vercel-labs/ui]
- The docs landing page gives no detailed accessibility approach; the closest mention is a Field component connecting a form control to its label, description and validation errors. [verified: https://ui-sdk.dev/docs]
- Not audited: no component was tested with a screen reader, keyboard or WCAG checks. Do not assume parity with Radix or Base UI without testing.

## Where it fits relative to the KB [estimated]

- `kb/ui-core.md` covers component primitives (Radix, Base UI) that a human or agent composes through slots or `render`. UI SDK sits one layer lower, at behavior level, and is written to be read by agents (bundled `llms.txt`, a skill, `AGENTS.md` instructions).
- Its "faster and cheaper agents" claim is the site's own and has no evidence on the pages read. [verified as a claim]
- Open questions worth testing before adopting: stability during beta, how its ARIA output compares with Radix and Base UI, bundle size, and whether the component set is production-ready. All unknown.

## Resources

1. **UI SDK site** - https://ui-sdk.dev/ - official landing page.
2. **Docs landing** - https://ui-sdk.dev/docs - install, skill setup, status.
3. **llms.txt index** - https://ui-sdk.dev/llms.txt - map of the per-section and per-framework `llms.txt` files (core, agents, guides, React, Vue, Svelte, Solid, Web Components).
4. **GitHub repo** - https://github.com/vercel-labs/ui - README, license, status (canonical path; see above).
5. Search note: a web search for UI SDK returned only unrelated products (Vercel's AI SDK, UI2, v0 SDK), so beware mixing up names; this is not the AI SDK.

_Validated 2026-11-12 against primary sources; see ../../validation-reports/._
