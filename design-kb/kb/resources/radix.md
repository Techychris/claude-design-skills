# Radix Primitives: official-docs verification and resources

Checked 2026-11-12 against radix-ui.com, github.com/radix-ui/primitives and the npm registry. Checks cover KB `ui-core.md` sections 3 and 4 (Radix rows). No local clone was modified.
Verdicts: CONFIRMED = official source says the same. CONTRADICTED = official source says otherwise. STALE = was true, now outdated. UNVERIFIABLE = no official source found in this run, or the source is local-only.
Tags: [verified] = read on an official page this run. [inferred] = deduced, not read on a page.

Note on the docs site: the Radix pages fetched are the official docs at radix-ui.com/primitives/docs. The philosophy page could not be fetched (client error), so its five principles remain unchecked.

---

## Verdict table

### Section 3 (Radix Primitives)

| # | KB claim | Verdict | Deciding URL | Note |
|---|---|---|---|---|
| 3.1 | Low-level UI library focused on accessibility, customization and developer experience (README) | CONFIRMED | https://github.com/radix-ui/primitives ; https://www.radix-ui.com/primitives/docs/overview/introduction | Repo page and intro page both say this. [verified] |
| 3.2 | Five principles: Accessible, Functional, Interoperable, Composable, Customizable (philosophy.md) | UNVERIFIABLE | https://www.radix-ui.com/primitives/docs/overview/philosophy | The philosophy page failed to fetch (client error). Local-only check. |
| 3.3 | Components follow WAI-ARIA guidance and are tested across browsers and assistive technology | CONFIRMED (WAI-ARIA); test coverage named only in general terms | https://www.radix-ui.com/primitives/docs/overview/accessibility | Page names no specific browsers or screen readers. [verified] |
| 3.4 | `@radix-ui/react-dialog` version 1.3.1 | CONFIRMED | https://registry.npmjs.org/@radix-ui/react-dialog/latest | npm latest is 1.3.1. The Dialog docs page itself shows 1.2.0, so the docs page is behind the registry. |
| 3.5 | Meta package `radix-ui` version 1.8.1 | UNVERIFIABLE | https://www.radix-ui.com/primitives/docs/overview/introduction | Introduction recommends the meta package but gives no version. Registry not queried for this package. |
| 3.6 | Monorepo: pnpm workspaces plus changesets | CONFIRMED (pnpm); changesets UNVERIFIABLE | https://github.com/radix-ui/primitives | Repo README says to install pnpm and run pnpm install. Changesets not mentioned on the fetched pages. |
| 3.7 | Consumer install is `npm install radix-ui` | CONFIRMED | https://www.radix-ui.com/primitives/docs/overview/introduction | The intro recommends the radix-ui meta package and also per-package installs. Radix's own README gives only the dev setup. |
| 3.8 | Import line `import { Dialog } from "radix-ui"` | CONFIRMED | https://www.radix-ui.com/primitives/docs/components/dialog | Same import line on the Dialog page. |
| 3.9 | Dialog export aliases: Root, Trigger, Portal, Overlay, Content, Title, Description, Close | CONFIRMED | https://www.radix-ui.com/primitives/docs/components/dialog | Same part list on the Dialog page. |
| 3.10 | `asChild` is implemented by Slot: clones its child, child props win, `on*` handlers compose | PARTIAL: asChild basics CONFIRMED; merge details UNVERIFIABLE | https://www.radix-ui.com/primitives/docs/guides/composition | The guide says Radix passes the props and behaviour the child needs. It does not describe the merge order or handler composition. Source-only. |
| 3.11 | `data-state` marks open/closed on dialog elements | CONFIRMED | https://www.radix-ui.com/primitives/docs/components/dialog ; https://www.radix-ui.com/primitives/docs/guides/styling | Dialog page lists data-state open/closed on Trigger, Overlay and Content. Styling guide names data-state as the recommended hook. [verified] |
| 3.12 | Behaviour lives in internal blocks (focus-scope, focus-guards, dismissable-layer, presence, portal, popper, roving-focus) | UNVERIFIABLE | n/a | The docs do not name these internals. Local-only. |
| 3.13 | Unstyled by design: no default CSS; consumer supplies styling | CONFIRMED | https://www.radix-ui.com/primitives/docs/overview/introduction ; https://www.radix-ui.com/primitives/docs/guides/styling | Intro says components ship without styles. Styling guide says primitives have no functional or presentation styles, e.g. Dialog Overlay does not cover the viewport by default. |
| 3.14 | MIT license | CONFIRMED | https://github.com/radix-ui/primitives | Repo page says MIT. |
| 3.15 | Copyright line "(c) 2022 WorkOS" in LICENSE | UNVERIFIABLE (exact line) | https://github.com/radix-ui/primitives | Repo page shows "WorkOS, 2022 to present". The LICENSE file itself was not fetched. |
| 3.16 | Dialog: Portal wraps Overlay and Content; Overlay is a sibling of Content | CONFIRMED | https://www.radix-ui.com/primitives/docs/components/dialog | Page describes Portal wrapping both, and Overlay as a sibling of Content. |
| 3.17 | Structure: `packages/react` (one package per component), `packages/core`, `internal/`, `apps/`, `e2e/` | UNVERIFIABLE online | n/a | Local-only facts about the clone. |
| 3.18 | Public component list (32 packages) | UNVERIFIABLE | https://www.radix-ui.com/primitives/docs/overview/introduction | Introduction does not list components. Directory names not checked online. The docs add a Form and a Visually Hidden utility; the KB already lists them. |

### Section 4 (how the three relate), Radix rows

| # | KB claim | Verdict | Deciding URL | Note |
|---|---|---|---|---|
| 4.1 | Radix is the upstream dependency of shadcn's Radix base (`from "radix-ui"`) | UNVERIFIABLE (shadcn fact) | n/a | Outside official Radix docs. The `radix-ui` import line itself is CONFIRMED (3.8). |
| 4.2 | Swap `asChild` for `render` when migrating | CONFIRMED (as a counterpart) | https://base-ui.com/react/utils/use-render | Base UI page calls render the counterpart to Radix asChild. This is a Base UI page; the Radix side is 3.10. |
| 4.3 | Rename parts Content to Popup | CONFIRMED (Radix side) | https://www.radix-ui.com/primitives/docs/components/dialog | Radix uses Content; Base UI uses Popup (see base-ui.md 4.4). |
| 4.4 | Popover Anchor is a Radix-only part | CONFIRMED | https://www.radix-ui.com/primitives/docs/components/popover | Radix Popover lists an optional Anchor; content positions against the Trigger if it is omitted. |
| 4.5 | NavigationMenu Indicator is a Radix-only part | UNVERIFIABLE | not fetched | Navigation Menu page was not opened. |
| 4.6 | Behaviour deltas to check: tabs activation, menu close-on-click, nav-menu delay | UNVERIFIABLE | not fetched | Tabs, Menu and Navigation Menu pages were not opened. |
| 4.7 | Base UI's creators came from Radix (shared authorship, listed in KB section 4 for context) | CONFIRMED as the Base UI project's own claim; not a Radix statement | https://github.com/mui/base-ui | Base UI's README says its creators come from Radix, Floating UI and Material UI. The Radix docs fetched this run do not say this. |

### Concern-by-concern summary (the requested rule areas)

| Area | Verdict | Deciding URL |
|---|---|---|
| Styling hooks (className, plain CSS, CSS-in-JS, extending) | CONFIRMED | https://www.radix-ui.com/primitives/docs/guides/styling |
| Data attributes (data-state; no others documented in the styling guide) | CONFIRMED for data-state; no other attributes are documented | https://www.radix-ui.com/primitives/docs/guides/styling ; https://www.radix-ui.com/primitives/docs/components/popover |
| Render composition (asChild requirements) | CONFIRMED (basics): spread props, forward refs, keep accessible, trigger stays focusable | https://www.radix-ui.com/primitives/docs/guides/composition |
| asChild Slot merge details | UNVERIFIABLE | n/a |
| Accessibility (WAI-ARIA, labels and descriptions supplied by developer) | CONFIRMED | https://www.radix-ui.com/primitives/docs/overview/accessibility |
| Focus (automatic focus trap in modal Dialog; Escape returns focus to Trigger; onOpenAutoFocus / onCloseAutoFocus on Popover content) | CONFIRMED | https://www.radix-ui.com/primitives/docs/components/dialog ; https://www.radix-ui.com/primitives/docs/components/popover |
| Portals (renders into document.body by default; container prop) | CONFIRMED | https://www.radix-ui.com/primitives/docs/utilities/portal |
| Animation (data-state with CSS keyframes; forceMount for JS libraries; exit delays unmount) | CONFIRMED | https://www.radix-ui.com/primitives/docs/guides/animation |
| SSR (server rendering supported; React 18+ generates ids on server; below 18 hydration delays screen reader use) | CONFIRMED | https://www.radix-ui.com/primitives/docs/guides/server-side-rendering |
| Portal and SSR mount timing | UNVERIFIABLE | https://www.radix-ui.com/primitives/docs/utilities/portal (page does not address SSR) |

---

## Missed guidelines

Official guidance that `ui-core.md` does not record. Each has a URL fetched this run.

1. Styling: primitives ship with no functional styles; e.g. Dialog Overlay does not cover the viewport until you add styles. Source: https://www.radix-ui.com/primitives/docs/guides/styling
2. Styling: any CSS-in-JS library works; the examples use styled-components. Extending a primitive means wrapping it in a forwardRef component. Source: https://www.radix-ui.com/primitives/docs/guides/styling
3. asChild: when you pass your own component, it must spread received props onto its DOM node and forward its ref (Radix may need the ref to measure). Source: https://www.radix-ui.com/primitives/docs/guides/composition
4. asChild: changing the element is allowed, but the trigger must stay focusable and respond to pointer and keyboard input, so a plain div would break it. Source: https://www.radix-ui.com/primitives/docs/guides/composition
5. asChild: nesting is supported, e.g. a tooltip trigger wrapping a dialog trigger wrapping a custom button. Source: https://www.radix-ui.com/primitives/docs/guides/composition
6. Animation: keep an element mounted during its exit by using the data-state attribute and CSS keyframes; forceMount hands mount control to a JavaScript library. Source: https://www.radix-ui.com/primitives/docs/guides/animation
7. Animation: the JS-library example uses forceMount with asChild so the library decides when Overlay and Content appear and disappear. Source: https://www.radix-ui.com/primitives/docs/guides/animation
8. Dialog: the Title is the accessible title announced on open; hide it visually with Visually Hidden rather than removing it. Source: https://www.radix-ui.com/primitives/docs/components/dialog
9. Dialog: Description is optional; to remove it, drop the element and pass aria-describedby set to undefined on Content. Source: https://www.radix-ui.com/primitives/docs/components/dialog
10. Dialog: Escape closes the dialog and returns focus to the Trigger; focus is trapped automatically in a modal dialog. Source: https://www.radix-ui.com/primitives/docs/components/dialog
11. Popover: Content accepts onOpenAutoFocus and onCloseAutoFocus; the Anchor part is optional. Source: https://www.radix-ui.com/primitives/docs/components/popover
12. Portal: the default target is a new div appended to body; the container prop changes the mount point. Source: https://www.radix-ui.com/primitives/docs/utilities/portal
13. SSR: below React 18, ids for ARIA are assigned during hydration, so screen reader users cannot interact until the bundle loads; React 18 or later generates them on the server. Source: https://www.radix-ui.com/primitives/docs/guides/server-side-rendering
14. SSR: the guide names Next.js, Remix and Gatsby as supported frameworks. Source: https://www.radix-ui.com/primitives/docs/guides/server-side-rendering
15. Accessibility (developer duties): supply labels, accessible names and descriptions for custom controls; keep focus behaviour logical as the app changes (e.g. an AlertDialog focuses its Cancel button on open). Source: https://www.radix-ui.com/primitives/docs/overview/accessibility
16. Accessibility: keyboard support is described as basic and follows WAI-ARIA practice; Tabs and Dialog are named as needing the most care. Source: https://www.radix-ui.com/primitives/docs/overview/accessibility
17. Releases: July 20, 2026 release fixed Dialog ARIA references when Title or Description are not rendered, and made per-primitive subpath imports available. Source: https://www.radix-ui.com/primitives/docs/overview/releases
18. Releases: June and July 2026 contain React 19 fixes (Slot and composed refs, stale handlers on React 19.2). Source: https://www.radix-ui.com/primitives/docs/overview/releases
19. Releases: Portal breaking changes date from 2022 (containerRef renamed to container; data-radix-portal removed); the as-to-asChild switch dates from 2021. Source: https://www.radix-ui.com/primitives/docs/overview/releases
20. Releases: a June 6, 2026 release added nested Slottable support through a render prop. Source: https://www.radix-ui.com/primitives/docs/overview/releases
21. Introduction: Radix Themes is a separate product in the top navigation, not part of the primitives. Source: https://www.radix-ui.com/primitives/docs/overview/introduction
22. Introduction: the meta package is tree-shakeable; if installing per-package, update all Radix packages together to avoid duplicated shared dependencies. Source: https://www.radix-ui.com/primitives/docs/overview/introduction
23. Repo: Chromatic is used for visual regression testing of the components. Source: https://github.com/radix-ui/primitives

---

## Resources

Items are listed only when fetched or seen in a search result this run.

| # | Title | URL | Type | Why useful |
|---|---|---|---|---|
| 1 | Introduction | https://www.radix-ui.com/primitives/docs/overview/introduction | Overview | Install path (radix-ui meta package), unstyled stance, what the library covers. [verified] |
| 2 | Styling | https://www.radix-ui.com/primitives/docs/guides/styling | Guide | Plain CSS, CSS-in-JS and extension patterns; data-state as the styling hook. [verified] |
| 3 | Composition | https://www.radix-ui.com/primitives/docs/guides/composition | Guide | asChild contract: prop spreading, ref forwarding, keeping elements accessible. [verified] |
| 4 | Animation | https://www.radix-ui.com/primitives/docs/guides/animation | Guide | CSS keyframes on data-state, forceMount for JavaScript animation libraries. [verified] |
| 5 | Server-side rendering | https://www.radix-ui.com/primitives/docs/guides/server-side-rendering | Guide | Supported frameworks; React 18 id generation; hydration trade-off. [verified] |
| 6 | Accessibility | https://www.radix-ui.com/primitives/docs/overview/accessibility | Overview | WAI-ARIA position; developer duties for labels and focus. [verified] |
| 7 | Dialog | https://www.radix-ui.com/primitives/docs/components/dialog | Component docs | Parts, data-state hooks, Title and Description guidance, focus behaviour. [verified] |
| 8 | Popover | https://www.radix-ui.com/primitives/docs/components/popover | Component docs | Anchor part, auto-focus handlers, data-side and data-align hooks. [verified] |
| 9 | Portal | https://www.radix-ui.com/primitives/docs/utilities/portal | Utility docs | Portal target and the container prop. [verified] |
| 10 | Releases | https://www.radix-ui.com/primitives/docs/overview/releases | Changelog | Dated changes, including 2026 React 19 fixes and the July 20, 2026 release. [verified] |
| 11 | Form | https://www.radix-ui.com/primitives/docs/components/form | Component docs | Form validation primitive. Seen in search results; not fetched. |
| 12 | radix-ui/primitives (GitHub) | https://github.com/radix-ui/primitives | Repository | Source, MIT license, pnpm dev setup; the repo page shows about 19.2k stars at fetch time. [verified] |
| 13 | Radix Primitives home | https://www.radix-ui.com/primitives | Landing page | Entry point to the docs. Seen in search results; not fetched. |
