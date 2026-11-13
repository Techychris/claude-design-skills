# Sonner: verification and resources

Run date: 2026-11-12. Scope: verify section 1 (sonner) of `kb/ui-components.md` against official docs and repo sources, and list resources.

Method and limits:
- Official docs site fetched: sonner.emilkowal.ski (homepage only; its sub-pages were not reachable from links on the page).
- Source read from raw.githubusercontent.com (main branch): package.json, src/index.tsx, src/state.ts, src/types.ts, src/styles.css. Line numbers come from a model-summarised fetch, so treat them as approximate.
- GitHub repo page and skills repo/skill pages fetched.
- Fetched content was summarised by a small model, not read raw. Type-level claims were cross-checked where possible, but the "last commit" date could not be read from the page.
- Tags: [verified] = read in this run from the cited URL; [inferred] = deduced.

## Verdict table

Verdicts apply to the claims in ui-components.md section 1. "N/A" rows are KB items that belong to Vaul.

| # | KB claim (section 1) | Verdict | Deciding evidence | Note |
|---|---|---|---|---|
| 1 | Install with `npm install sonner` | CONFIRMED | https://sonner.emilkowal.ski/ (install step); https://github.com/emilkowalski/sonner | [verified] |
| 2 | Minimal usage: mount `<Toaster />` once, call `toast()` from anywhere | CONFIRMED | https://sonner.emilkowal.ski/ (render Toaster once, at the app root; call toast from an event handler) | [verified] |
| 3 | Positioning: `position` prop on `<Toaster>` | CONFIRMED | https://sonner.emilkowal.ski/ (position prop on Toaster); https://raw.githubusercontent.com/emilkowalski/sonner/main/src/types.ts (six position values) | Default is bottom-right per src/index.tsx [verified]. KB omits the default. |
| 4 | Swipe direction depends on position (not in KB) | CONFIRMED | https://sonner.emilkowal.ski/ (page notes swipe-to-dismiss direction changes with position) | Added to section 1 as a rule. |
| 5 | Theming: `theme` is light, dark or system | CONFIRMED | src/types.ts (theme union); src/index.tsx (system reads prefers-color-scheme and listens for changes); src/styles.css (data-sonner-theme selectors) | Default is light per src/index.tsx [verified]. KB omits the default. |
| 6 | Rich colors: `richColors` prop on Toaster | CONFIRMED | https://sonner.emilkowal.ski/ (richColors gives colored styling); src/index.tsx (per-toast richColors overrides the Toaster default) | Per-toast override is not in KB. |
| 7 | Promise toasts: `toast.promise(promise, { loading, ... })` | CONFIRMED | src/state.ts (loading toast created when data.loading is set; success or error replaces it by the same id; unwrap() returns a promise) | Non-ok HTTP responses take the error path [verified]. Not in KB. |
| 8 | Loading toasts never auto-dismiss | CONFIRMED | src/index.tsx (timer effect returns early for type loading, for toast.promise loading state, and for duration Infinity) | Also skips the close button on loading toasts [verified]. |
| 9 | Use `toast.promise` to swap a loading toast for success or error | CONFIRMED | src/state.ts (same-id merge into the loading toast) | [verified] |
| 10 | Toaster props: position, theme, richColors, expand, duration, closeButton, visibleToasts, toastOptions | CONFIRMED | src/types.ts (all eight present) | types.ts also has gap, hotkey, offset, mobileOffset, dir, swipeDirections, icons, customAriaLabel, containerAriaLabel [verified]. |
| 11 | `toast`, `toast.success`, `toast.loading` exist | CONFIRMED in part | src/state.ts (`loading`, `success`, `error`, `info`, `warning` wrap create) | [verified]. toast.success/loading are confirmed; the source line numbers from KB were not re-checked. |
| 12 | Exports `toast`, `Toaster`, `useSonner` | UNVERIFIABLE | Not re-checked in this run (src/index.tsx export line not read directly) | Keep KB note as-is. |
| 13 | Peer deps react and react-dom 18 / 19 / 19 RC; @types/react optional | CONFIRMED | https://raw.githubusercontent.com/emilkowalski/sonner/main/package.json (peerDependencies, peerDependenciesMeta) | [verified] |
| 14 | Exports `./dist/styles.css` | CONFIRMED | package.json (exports map, "./dist/styles.css"; files: dist only) | [verified] |
| 15 | Bundlers need an explicit CSS import (KB: not stated) | UNVERIFIABLE | Sonner site and README do not mention a CSS import step (site fetch) | Still open. The KB claim that the source imports ./styles.css (src/index.tsx:9) was not re-checked. |
| 16 | Version 2.0.8 | CONFIRMED | package.json (version 2.0.8) | [verified] |
| 17 | License MIT | CONFIRMED | package.json (license), GitHub repo | [verified] |
| 18 | Maintenance "Active", last commit 2026-08-10 | UNVERIFIABLE (date); partly consistent | GitHub repo page: not archived, shows 332 commits on main, Releases section empty; commit date not visible in fetch | Do not rely on the KB date without checking `git log` locally. |
| 19 | Keep one `<Toaster />` per app (KB: inferred) | CONFIRMED with a caveat | https://sonner.emilkowal.ski/ (render once, at root); src/index.tsx (one `<ol>` per position; listRef reused across lists, so focus and hotkey track only the last list) | Caveat is new; see missed guidelines. |
| 20 | `ask-sonner` agent skill install command | CONFIRMED | https://github.com/emilkowalski/skills (18 skills, includes ask-sonner); https://skills.sh/emilkowalski/skills/ask-sonner (install command) | Source says the skill is written by the author. [verified] |
| 21 | Accessibility (not in KB) | Missed; now verified | src/index.tsx (section has aria-live polite, aria-relevant additions text, tabIndex -1 on the section, each toast tabIndex 0, Alt+T hotkey focuses list, Escape collapses when focus is in list) | Add to KB section 1. |
| 22 | Styling: CSS theming and reduced motion (not in KB) | Missed; now verified | src/styles.css (data-sonner-theme dark block; data-rich-colors variants; reduced-motion media query turns off toast transitions and loading bar animation; container is position fixed with very high z-index) | Add to KB section 1. |
| 23 | Snap points, handle, nested drawers | N/A | Vaul features | See the Vaul file. |

## Missed guidelines

Official sources only, plus source-level behaviour. Each item is tagged.

1. Default duration is 4000 ms. Precedence: per-toast duration, then Toaster-level duration (duration prop or toastOptions.duration), then the default. [verified: src/index.tsx]
2. Timers pause while the list is expanded, while a toast is being interacted with, and while the document is hidden. Pausing subtracts elapsed time rather than restarting. [verified: src/index.tsx]
3. The close button only shows when the toast is dismissible, has no custom jsx, and is not a loading toast. Default aria-label is "Close toast", overridable with closeButtonAriaLabel. [verified: src/index.tsx; closeButtonAriaLabel is in ToastOptions per src/types.ts]
4. The Toaster list is an aria-live polite region with additions and text announced, and an aria-label that defaults to "Notifications". Use customAriaLabel or containerAriaLabel to localise it. [verified: src/index.tsx; containerAriaLabel and customAriaLabel are in src/types.ts]
5. Default hotkey is Alt+T, which expands the list and moves focus into it. Escape collapses it when focus is inside. The hotkey prop changes it. [verified: src/index.tsx; prop in src/types.ts]
6. Multiple positions create one `<ol>` each, but the listRef is shared, so focus and hotkey logic track only the last list. Prefer one position per app unless you test keyboard focus. [verified: code reading; impact on users is inferred]
7. Default visibleToasts is 3 and default gap is 14 px. [verified: src/index.tsx]
8. Per-toast richColors overrides the Toaster richColors default. [verified: src/index.tsx]
9. Promise errors include non-ok HTTP responses and Error instances, not only rejections. Use toast.promise's unwrap() to keep the original promise result in code. [verified: src/state.ts]
10. Reduced-motion users get no toast transitions or loading-bar animation from the bundled CSS. Any custom animation you add should honour the same media query. [verified: src/styles.css; the custom part is inferred]
11. Toaster container is position fixed with a very high z-index. Check stacking against modals and drawers, such as a Vaul drawer in the same page. [verified: src/styles.css; the conflict is inferred]
12. Do not treat `toast.promise` as a replacement for form validation or inline errors. [inferred: general UX judgement, not in the docs]
13. Sonner's agent skill ask-sonner draws on the author's own guidance and points to the full API reference for prop names, types and defaults. Use it as a quick reference, then confirm against types.ts. [verified: skills.sh page]

## Resources

1. **Sonner docs site** - https://sonner.emilkowal.ski/ - official docs - Install, Toaster placement, position, richColors, and the author's animations course link.
2. **Sonner GitHub repo** - https://github.com/emilkowalski/sonner - official source - Source of truth for behaviour; check issues and tags before upgrading.
3. **Sonner src/index.tsx** - https://raw.githubusercontent.com/emilkowalski/sonner/main/src/index.tsx - source - Timers, hotkey, ARIA region, theme, position and close-button logic.
4. **Sonner src/state.ts** - https://raw.githubusercontent.com/emilkowalski/sonner/main/src/state.ts - source - toast.promise, unwrap, and the same-id update path.
5. **Sonner src/types.ts** - https://raw.githubusercontent.com/emilkowalski/sonner/main/src/types.ts - source types - Full ToasterProps, ToastOptions, ExternalToast. Best reference for prop names.
6. **Sonner src/styles.css** - https://raw.githubusercontent.com/emilkowalski/sonner/main/src/styles.css - source CSS - Data-attribute theming, rich-color variants, reduced-motion rules, container stacking.
7. **Sonner package.json** - https://raw.githubusercontent.com/emilkowalski/sonner/main/package.json - manifest - Version, exports including ./dist/styles.css, peer dependency ranges.
8. **ask-sonner skill repo** - https://github.com/emilkowalski/skills - official agent skills - Repo with 18 skills including ask-sonner; install with `npx skills add emilkowalski/skills`.
9. **ask-sonner on skills.sh** - https://skills.sh/emilkowalski/skills/ask-sonner - skill directory page - Describes what the skill covers and its install command.
10. **Sonner toaster component reference (Tessl)** - https://tessl.io/registry/tessl/npm-sonner/files/docs/toaster-component.md - third-party generated doc (seen in search, not fetched) - Alternate prop listing. Not official: check every default against src/types.ts and src/index.tsx.
