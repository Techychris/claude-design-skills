# Base UI: official-docs verification and resources

Checked 2026-11-12 against base-ui.com, github.com/mui/base-ui and the npm registry. Checks cover KB `ui-core.md` sections 2 and 4 (Base UI rows). No local clone was modified.
Verdicts: CONFIRMED = official source says the same. CONTRADICTED = official source says otherwise. STALE = was true, now outdated. UNVERIFIABLE = no official source found in this run, or the source is local-only.
Tags: [verified] = read on an official page this run. [inferred] = deduced, not read on a page.
Status (2026-11-12): Stable since v1.0.0 (released 2025-12-11, 35 components then; https://base-ui.com/react/overview/releases); latest @base-ui/react 1.9.0 (npm 2026-10-09). The repo README does not say it is stable, so cite the release page. The package was renamed from `@base-ui-components/react` (last 1.0.0-rc.0) to `@base-ui/react`. Peer deps: react and react-dom ^17 || ^18 || ^19 (not React-19-only); date-fns ^4 and @date-fns/tz ^1.2 are also listed as peers (calendar-related; optionality not confirmed) [verified https://registry.npmjs.org/@base-ui/react]. Ships its own Drawer (since v1.3.0), Toast, Autocomplete, Number Field, OTP Field and Meter. shadcn new projects default to Base UI since July 2026 (`shadcn init -b radix` to opt out) [verified https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default]; shadcn Drawer now wraps Base UI Drawer, not Vaul.

Pages fetched this run are the source for every verdict. "Not fetched" means the page was not opened, so the rule stays unchecked.

---

## Verdict table

### Section 2 (Base UI)

| # | KB claim | Verdict | Deciding URL | Note |
|---|---|---|---|---|
| 2.1 | Unstyled, accessible component library (README wording) | CONFIRMED | https://github.com/mui/base-ui ; https://base-ui.com/react/overview/quick-start | Docs say the library is unstyled and that you control CSS. [verified] |
| 2.2 | Package `@base-ui/react` version 1.9.0 | CONFIRMED | https://registry.npmjs.org/@base-ui/react/latest ; https://base-ui.com/react/overview/releases | npm latest is 1.9.0. Release page lists v1.9.0 as newest (Oct 9, 2026). [verified] |
| 2.3 | Install with `npm install @base-ui/react` | CONFIRMED | https://base-ui.com/react/overview/quick-start | Docs show a pnpm command and npm/yarn/bun tabs. Package name matches. [verified] |
| 2.4 | Per-component subpath exports (e.g. `@base-ui/react/dialog`) | CONFIRMED | https://base-ui.com/react/overview/quick-start ; https://base-ui.com/react/components/dialog | Docs import from subpaths. Quick start also says everything ships in one package and is tree-shakable. [verified] |
| 2.5 | Dialog parts: Root, Trigger, Portal, Backdrop, Popup, Viewport, Title, Description, Close, createHandle/Handle | CONFIRMED | https://base-ui.com/react/components/dialog | Same list, plus Dialog.createHandle for detached triggers. [verified] |
| 2.6 | Dialog usage: Root/Trigger/Portal/Popup nesting | CONFIRMED (parts); nesting [inferred] | https://base-ui.com/react/components/dialog | Parts confirmed. Exact nesting order is not shown verbatim in the parts summary. |
| 2.7 | `render` prop takes an element or a function of (props, state) | CONFIRMED | https://base-ui.com/react/handbook/composition ; https://base-ui.com/react/utils/use-render | Both forms documented. [verified] |
| 2.8 | Props are merged, then the element is cloned | UNVERIFIABLE (clone step) | https://base-ui.com/react/handbook/composition | Merge rules are documented (className joined, style merged, handlers chained, render element's handler runs first, refs all kept). The word "cloned" and the internal mechanism are not on any official page. |
| 2.9 | State becomes `data-*` attributes; `true` gives an empty attribute | UNVERIFIABLE (empty-attribute rule) | https://base-ui.com/react/utils/use-render ; https://base-ui.com/react/components/button | useRender says state properties become data attributes and can be remapped with stateAttributesMapping. The empty-attribute rule for `true` is not stated on any fetched page. |
| 2.10 | Button sets `data-disabled` | CONFIRMED | https://base-ui.com/react/components/button | Button docs list data-disabled as the only data attribute. |
| 2.11 | `className` can be a function of component state | CONFIRMED | https://base-ui.com/react/handbook/styling ; https://base-ui.com/react/components/dialog | Styling handbook and dialog page both say className and style accept a function of state. [verified] |
| 2.12 | Focus props `initialFocus` and `finalFocus` on the popup | CONFIRMED | https://base-ui.com/react/components/dialog ; https://base-ui.com/react/components/popover | Both props accept a boolean, a ref, or a function (dialog). Defaults: first tabbable element; return to trigger. |
| 2.13 | ARIA wiring and focus handling sit inside each component (was marked [inferred]) | CONFIRMED (general); per-component audit still open | https://base-ui.com/react/overview/accessibility | Docs say components manage ARIA, roles, pointer interaction, keyboard support and focus. This upgrades the KB tag to [verified] at the general level. |
| 2.14 | `data-open` / `data-closed` / `data-starting-style` / `data-ending-style` exist on overlay parts | CONFIRMED (dialog, popover) | https://base-ui.com/react/components/dialog ; https://base-ui.com/react/components/popover | Not in the KB; listed here because they are the animation hooks. |
| 2.15 | Component inventory: 39 folders in `packages/react/src` | 37 public components VERIFIED; 39-folder count UNVERIFIABLE | https://base-ui.com/llms.txt | llms.txt lists 37 component pages (incl. Drawer, Toast, Autocomplete, Number Field, OTP Field, Meter); utilities: csp-provider, direction-provider, merge-props, use-render. Public docs list 37 components. The KB folder list adds `filter-dropdown` and `radio`, which the public list does not have. They may be internal or unreleased. Local-only check. |
| 2.16 | MIT license | CONFIRMED | https://github.com/mui/base-ui | Repo page says MIT. |
| 2.17 | Copyright line "(c) 2019 Material-UI SAS" | UNVERIFIABLE | https://github.com/mui/base-ui | The LICENSE file was not fetched; the repo page does not show the copyright line. |
| 2.18 | Structure: `packages/react`, `packages/utils`, `GLOSSARY.md`, `AGENTS.md`, etc. | UNVERIFIABLE online | n/a | Local-only facts about the clone. |

### Section 4 (how the three relate), Base UI rows

| # | KB claim | Verdict | Deciding URL | Note |
|---|---|---|---|---|
| 4.1 | Base UI is a separate library from Radix | CONFIRMED | https://github.com/mui/base-ui | Own package and docs site. |
| 4.2 | Base UI creators come from Radix, Floating UI and Material UI | CONFIRMED (as the project's claim) | https://github.com/mui/base-ui ; https://base-ui.com/ | Stated on the repo and home page. |
| 4.3 | Swap `asChild` for `render` | CONFIRMED | https://base-ui.com/react/utils/use-render ; https://base-ui.com/react/handbook/composition | useRender page calls it the counterpart of Radix's `asChild`. [verified] |
| 4.4 | Rename parts (Content to Popup) | CONFIRMED | https://base-ui.com/react/components/dialog ; https://www.radix-ui.com/primitives/docs/components/dialog | Base UI uses Popup; Radix uses Content. |
| 4.5 | Dialog has no Positioner | CONFIRMED | https://base-ui.com/react/components/dialog | Viewport does the positioning container job. |
| 4.6 | Add a Positioner inside Portal only for Popover- and Menu-style parts | UNVERIFIABLE ("only" part) | https://base-ui.com/react/components/popover ; https://base-ui.com/react/components/dialog | Popover uses a Positioner between Portal and Popup. Dialog page says Menu uses one. Tooltip, Select, Preview Card and Combobox were not checked, so "only" is not established. |
| 4.7 | No Base UI counterpart: AspectRatio | CONFIRMED | https://base-ui.com/llms.txt | Not in the public component list. |
| 4.8 | No Base UI counterpart: Label | CONFIRMED (as a standalone component) | https://base-ui.com/react/handbook/forms | Base UI has Field.Label instead. Say "use Field.Label" in the KB. |
| 4.9 | No Base UI counterpart: VisuallyHidden | CONFIRMED | https://base-ui.com/llms.txt | Not in the public component list. |
| 4.10 | No Base UI counterpart: Direction (provider) | WRONG: Direction -> DirectionProvider (react/utils/direction-provider) | https://base-ui.com/react/utils/direction-provider | Base UI ships a DirectionProvider and a useDirection hook (utils). KB section 1 line 66 already says Direction maps to a `direction` prop on DirectionProvider, so section 4 contradicts section 1. |
| 4.11 | No Base UI counterpart: Popover Anchor | CONFIRMED | https://base-ui.com/react/components/popover | Base UI Popover parts list has no Anchor. |
| 4.12 | No Base UI counterpart: NavigationMenu Indicator | UNVERIFIABLE | not fetched | Navigation Menu page was not opened. |
| 4.13 | Known behaviour deltas: tabs activation, menu close-on-click, nav-menu delay | UNVERIFIABLE | not fetched | Tabs, Menu and Navigation Menu pages were not opened. |
| 4.14 | Migration is one wrapper at a time, leaf wrappers first | UNVERIFIABLE (official) | n/a | Not an official Base UI rule. It comes from the shadcn skill. |
| 4.15 | shadcn Base base imports `@base-ui/react/dialog` | UNVERIFIABLE (shadcn fact) | n/a | Outside official Base UI docs; the subpath pattern itself is CONFIRMED (2.4). |

### Concern-by-concern summary (the requested rule areas)

| Area | Verdict | Deciding URL |
|---|---|---|
| Styling hooks (className function, style function) | CONFIRMED | https://base-ui.com/react/handbook/styling |
| Data attributes (per component; `data-disabled`, `data-open`, `data-starting-style`) | CONFIRMED for listed attributes; the general state-to-attribute rule UNVERIFIABLE | https://base-ui.com/react/components/dialog ; https://base-ui.com/react/utils/use-render |
| Render composition (`render` element and function) | CONFIRMED | https://base-ui.com/react/handbook/composition |
| asChild vs render | CONFIRMED (Base UI has no asChild) | https://base-ui.com/react/handbook/composition ; https://base-ui.com/react/utils/use-render |
| Accessibility (ARIA, keyboard, focus done by component) | CONFIRMED; developer duties listed (see Missed guidelines) | https://base-ui.com/react/overview/accessibility |
| Focus (initialFocus, finalFocus, modal trap) | CONFIRMED | https://base-ui.com/react/components/dialog |
| Portals (Portal renders to body by default; container; keepMounted) | CONFIRMED | https://base-ui.com/react/components/dialog |
| Animation (exit animation, data-starting/ending-style) | CONFIRMED for the attributes; the rule that Base UI waits for exits is CONFIRMED with a caveat (it detects CSS animations and Motion animations with opacity) | https://base-ui.com/react/handbook/animation |
| SSR | UNVERIFIABLE: no Base UI SSR page was fetched | not fetched (no SSR page located in search) |

---

## Missed guidelines

Official guidance that `ui-core.md` does not record. Each has a URL that was fetched this run.

1. Styling: CSS variables are exposed (e.g. Popover Positioner's anchor width and available height; Popup size variables) and documented per component. Source: https://base-ui.com/react/handbook/styling
2. Styling: for CSS-in-JS, use the exported data-attribute and CSS-variable name constants instead of hard-coded strings (e.g. Menu item attribute constants). Source: https://base-ui.com/react/handbook/styling
3. Composition: when the render element is a custom component, it must forward its ref and spread received props onto its DOM node. Source: https://base-ui.com/react/handbook/composition
4. Composition: render merging rules differ from `mergeProps`: all refs are kept, and a `preventBaseUIHandler()` call on the event skips Base UI's handlers. Source: https://base-ui.com/react/handbook/composition
5. Composition: change the default element only case by case, because each part already picks a suitable one (e.g. accordion heading level). Source: https://base-ui.com/react/handbook/composition
6. useRender: for React 19 `forwardRef` is unnecessary; React 18 still needs it. Also `stateAttributesMapping` customises the data-attribute mapping; `enabled: false` returns null. Source: https://base-ui.com/react/utils/use-render
7. Button: `nativeButton` defaults to true; set it to false for non-button elements, which then need role and keyboard handling. Links should be styled, not rendered as buttons. Source: https://base-ui.com/react/components/button
8. Dialog: with modal on (or trap-focus), keep a Close control inside Popup so touch screen-reader users can leave. Source: https://base-ui.com/react/components/dialog
9. Dialog: Trigger needs `nativeButton={false}` when rendered as a non-button. Source: https://base-ui.com/react/components/dialog
10. Dialog: `modal` has three values: true (trap focus, lock scroll, block outside pointers), 'trap-focus' (trap only), false. Source: https://base-ui.com/react/components/dialog
11. Animation: prefer CSS transitions over keyframes for open/close, because a transition can reverse mid-way when a popup closes before it finishes opening. Source: https://base-ui.com/react/handbook/animation
12. Animation: Base UI keeps a popup mounted during its closing phase and removes it once its animation ends; `keepMounted` keeps it hidden in the DOM instead. Manual unmounting is available through `preventUnmountOnClose()` and `actionsRef`. Source: https://base-ui.com/react/handbook/animation
13. Animation: Motion integration patterns differ for popups removed from the DOM versus kept mounted; Select uses a mix. Source: https://base-ui.com/react/handbook/animation
14. Animation: Base UI detects CSS animations and Motion animations only when they include opacity; otherwise use manual unmounting. Source: https://base-ui.com/react/handbook/animation
15. Customization: change handlers (onOpenChange, onValueChange, onPressedChange) take an eventDetails argument with a reason, the originating event, and `cancel()` / `allowPropagation()`. Source: https://base-ui.com/react/handbook/customization
16. Forms: each control needs an accessible name (Field.Label or a native label, or aria-label if no visible label); multi-thumb sliders need an aria-label per thumb. Source: https://base-ui.com/react/handbook/forms
17. Forms: validation runs on submit by default; `validationMode` can be blur or change; `validationDebounceTime` delays it; `Field.Error` with `match` gives custom messages per validity state. Source: https://base-ui.com/react/handbook/forms
18. Forms: invalid state is passed through the Field.Root `invalid` prop, and the page does not mention aria-invalid. Source: https://base-ui.com/react/handbook/forms
19. Accessibility (developer duties): supply visible focus indicators (focus-visible styling), colour contrast (APCA suggested), and accessible names for custom controls. Source: https://base-ui.com/react/overview/accessibility
20. Accessibility: the page does not give reduced-motion or screen-reader test guidance for apps built with Base UI. Source: https://base-ui.com/react/overview/accessibility (absence noted, not a rule)
21. Direction: DirectionProvider only changes component behaviour; the app must still set dir or direction on the page. For portaled content use useDirection. Source: https://base-ui.com/react/utils/direction-provider
22. Releases: v1.0.0 stable was released Dec 11, 2025; v1.9.0 is the newest listed release (Oct 9, 2026). Source: https://base-ui.com/react/overview/releases
23. Handbook pages not fetched but listed in the official index: TypeScript, CSP Provider, mergeProps. Source: https://base-ui.com/llms.txt
24. Forms page: Base UI form controls extend native constraint validation and work with React Hook Form and TanStack Form. Source: https://base-ui.com/react/handbook/forms

---

## Resources

Items are listed only when fetched or seen in a search result this run.

| # | Title | URL | Type | Why useful |
|---|---|---|---|---|
| 1 | Styling | https://base-ui.com/react/handbook/styling | Handbook | Style hooks: className and style functions, data attributes, CSS variables; Tailwind, CSS Modules, CSS-in-JS examples. [verified] |
| 2 | Composition | https://base-ui.com/react/handbook/composition | Handbook | The render prop rules: element vs function, prop, class, style, handler and ref merging. [verified] |
| 3 | Animation | https://base-ui.com/react/handbook/animation | Handbook | Transitions vs keyframes, data-starting/ending-style, exit timing, Motion integration. [verified] |
| 4 | Accessibility | https://base-ui.com/react/overview/accessibility | Overview | What Base UI handles and what the developer must still supply (focus indicators, contrast, names). [verified] |
| 5 | Dialog | https://base-ui.com/react/components/dialog | Component docs | Parts, focus props, modal modes, Portal, data attributes, Title and Description guidance. [verified] |
| 6 | Popover | https://base-ui.com/react/components/popover | Component docs | Positioner placement, CSS variables for anchor and available size, focus props. [verified] |
| 7 | Forms | https://base-ui.com/react/handbook/forms | Handbook | Field, Fieldset and Form parts; native and custom validation; accessible naming. [verified] |
| 8 | useRender | https://base-ui.com/react/utils/use-render | Utility docs | Building custom components with the render prop; state to data attributes; React 18 vs 19 refs. [verified] |
| 9 | Customization | https://base-ui.com/react/handbook/customization | Handbook | eventDetails, cancel and allowPropagation; controlled vs uncontrolled. [verified] |
| 10 | Direction Provider | https://base-ui.com/react/utils/direction-provider | Utility docs | RTL behaviour and useDirection for portaled content. [verified] |
| 11 | Releases | https://base-ui.com/react/overview/releases | Changelog | Dated release history; v1.0.0 stable and v1.9.0 latest. [verified] |
| 12 | llms.txt index | https://base-ui.com/llms.txt | Machine-readable index | Full list of docs pages with .md URLs; useful for LLM and tooling access. [verified] |
| 13 | mui/base-ui (GitHub) | https://github.com/mui/base-ui | Repository | Source, MIT license, stated goals; the repo page shows about 11.3k stars at fetch time. [verified] |
| 14 | TypeScript handbook | https://base-ui.com/react/handbook/typescript | Handbook | Typing components and the render prop. Seen in search results; not fetched. |

_Validated 2026-11-12 against primary sources; see ../../validation-reports/._
