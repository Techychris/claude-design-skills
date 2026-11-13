# Vaul: verification and resources

Run date: 2026-11-12. Scope: verify section 2 (vaul) of `kb/ui-components.md` against official docs and repo sources, and list resources.

Method and limits:
- Official docs site vaul.emilkowal.ski could NOT be fetched: the fetch tool reported robots_disallowed. Vaul's own docs are therefore UNVERIFIABLE from the docs site; the verdicts below rely on the repo, source and npm page.
- The repo README is only an unmaintained notice; it has no usage docs.
- Source read from raw.githubusercontent.com (main branch): package.json, src/index.tsx. Line numbers come from a model-summarised fetch, so treat them as approximate.
- The npm page was fetched but truncated before the full usage example.
- Radix Dialog facts come from a third-party mirror of the Radix docs (mintlify), not from radix-ui.com.
- Tags: [verified] = read in this run from the cited URL; [inferred] = deduced.

## Verdict table

| # | KB claim (section 2) | Verdict | Deciding evidence | Note |
|---|---|---|---|---|
| 1 | Purpose: drawer on any edge, built on Radix Dialog, with snap points and drag-to-dismiss | CONFIRMED | package.json (runtime dep @radix-ui/react-dialog ^1.1.1); src/index.tsx (snapPoints, direction, Handle drag behaviour) | [verified]. KB says purpose comes from package.json and source, which is still the only evidence. |
| 2 | Install with `npm install vaul` | CONFIRMED | https://www.npmjs.com/package/vaul (install line) | [verified] |
| 3 | Minimal usage: Drawer.Root, Trigger, Portal, Overlay, Content | UNVERIFIABLE | npm page snippet truncated after Drawer.Overlay; docs site blocked | Structure is consistent with the export object, but no official example was read. |
| 4 | Drawer.Root props: open, onOpenChange | UNVERIFIABLE | Not re-checked in this run | |
| 5 | `direction`: top, bottom, left, right | CONFIRMED | src/index.tsx (direction type union; default bottom; controls drag axis and close threshold) | [verified] |
| 6 | `snapPoints` with `activeSnapPoint` and `setActiveSnapPoint` | CONFIRMED in part | src/index.tsx (snapPoints in the union types and default fadeFromIndex) | activeSnapPoint and setActiveSnapPoint not read directly. |
| 7 | `modal`, `nested` and `NestedRoot` | CONFIRMED in part | src/index.tsx (NestedRoot renders Root with nested set; nested skips position restoration on close) | modal not re-checked. |
| 8 | `dismissible`, `shouldScaleBackground`, `handleOnly` | CONFIRMED | src/index.tsx (shouldScaleBackground default false; handleOnly default false; Content returns early from pointer handlers when handleOnly is true; dismissible affects Handle at last snap point) | [verified] |
| 9 | Dependencies: peer react and react-dom 16.8 to 19; runtime @radix-ui/react-dialog ^1.1.1 | CONFIRMED | https://raw.githubusercontent.com/emilkowalski/vaul/main/package.json | [verified] |
| 10 | Ships style.css | CONFIRMED | package.json (files list includes style.css); src/index.tsx imports './style.css' | [verified] |
| 11 | Component inventory: Root, NestedRoot, Trigger, Portal, Overlay, Content, Handle, Close, Title, Description | CONFIRMED in part | src/index.tsx (NestedRoot, Handle, Title and Description re-exported from Radix) | Trigger, Portal, Overlay, Content and Close were not read in this run. |
| 12 | License MIT | CONFIRMED | package.json (license MIT); https://github.com/emilkowalski/vaul | [verified] |
| 13 | Maintenance: unmaintained, no near-term work planned | CONFIRMED | https://raw.githubusercontent.com/emilkowalski/vaul/main/README.md (notice); https://github.com/emilkowalski/vaul (repo shows the same notice, author says it is a hobby project) | Notice says the author may return someday. KB wording is close enough. |
| 14 | Pin the version if you depend on it | INFERRED | General advice; not stated in the repo | Keep as an inference. |
| 15 | Passing `snapPoints` requires `fadeFromIndex` in the types | CONTRADICTED | src/index.tsx (DialogProps is an intersection with a union. WithFadeFromProps requires both snapPoints and fadeFromIndex. WithoutFadeFromProps makes snapPoints optional and fadeFromIndex typed never. Passing snapPoints alone type-checks.) | KB is wrong: fadeFromIndex is required only in the fade variant. The runtime default is the last snap point index. [verified; type reading from a summarised fetch, confirm with tsc if it matters] |
| 16 | `handleOnly` limits dragging to the handle | CONFIRMED | src/index.tsx (only Drawer.Handle starts a drag when handleOnly is true) | KB marked behaviour inferred; now verified. |
| 17 | Radix Dialog is a hard dependency, so Radix drift can affect it | INFERRED | package.json shows the runtime dependency and the ^1.1.1 range, so drift is possible | Still an inference. |
| 18 | Snap points, drag-to-dismiss, handle (section purpose) | CONFIRMED | src/index.tsx (Handle click cycles snap points; drag closes a dismissible drawer) | [verified] |
| 19 | Accessibility (not in KB): Title and Description | CONFIRMED in part | src/index.tsx (Title and Description are Radix re-exports, with no warning logic of its own); Radix mirror says Title is required for accessibility | Radix requirement from a third-party mirror, not radix-ui.com. Description is optional per the same mirror. Missed in KB. |
| 20 | Accessibility: Handle | CONFIRMED | src/index.tsx (Handle renders with aria-hidden true) | A keyboard or screen-reader user cannot reach the handle as a control. Missed in KB. |
| 21 | Styling / CSS (not in KB) | CONFIRMED | npm page describes Vaul as an unstyled drawer component; src/index.tsx imports style.css; package.json includes it in files | Missed in KB. |
| 22 | Background scaling (not in KB) | CONFIRMED | src/index.tsx (shouldScaleBackground targets the element matching a data attribute for the wrapper; setBackgroundColorOnScale default true) | The consumer must mark the wrapper; exact markup not read. Missed in KB. |
| 23 | Nested drawers need NestedRoot inside a parent drawer (not in KB) | CONFIRMED | src/index.tsx (NestedRoot throws if not inside another drawer) | Missed in KB. |
| 24 | Direction default and fadeFromIndex default (not in KB) | CONFIRMED | src/index.tsx (direction defaults to bottom; fadeFromIndex defaults to last snap point index) | Missed in KB. |
| 25 | Vaul can replace a Dialog on tablet and mobile (not in KB) | CONFIRMED | https://www.npmjs.com/package/vaul (description) | Design guideline; see missed list. |

## Missed guidelines

1. Vaul is unstyled. Plan your own visual design and use style.css only for the base behaviour. [verified: npm description; src/index.tsx imports style.css]
2. Positioned as a Dialog replacement on tablet and mobile. Use Dialog for desktop-only flows where edge drawers do not fit. [verified: npm description; the desktop advice is inferred]
3. Title is required for accessibility. Vaul re-exports Radix Title and adds no warning of its own, so a missing Title is a silent accessibility gap in your app. Use a visually hidden Title if the design has none. [verified: src/index.tsx for the re-export; Radix requirement from the third-party mirror]
4. Description is optional. Radix's docs do not say what happens without one. Test in your target browser. [inferred: mirror did not cover warnings]
5. Handle is aria-hidden. Always give keyboard and screen-reader users a second way to change snap point or close. [verified: src/index.tsx; the advice is inferred]
6. Clicking the Handle cycles to the next snap point. At the last snap point a dismissible drawer closes instead. Without snap points, a non-dismissible drawer closes on handle click. Make this clear to users in the design. [verified: src/index.tsx]
7. A press held more than about 250 ms on the handle cancels the click. Pointer-driven handle clicks should be short. [verified: src/index.tsx (time values approximate from a summarised fetch)]
8. shouldScaleBackground is off by default. When it is on, the page element marked as the drawer wrapper is scaled during drag. Mark your page wrapper, or the effect does nothing. [verified: src/index.tsx; the marking requirement is inferred from the selector]
9. With handleOnly, only the Handle starts drags, so drag-to-dismiss needs a visible handle. [verified: src/index.tsx]
10. Nested drawers need NestedRoot placed inside a parent drawer, or it throws. [verified: src/index.tsx]
11. The repo is unmaintained. Pin the exact version, watch for React version gaps (peer range stops at 19), and plan a replacement or fork before you depend on it for new work. [verified: README notice; peer range from package.json; plan is inferred]
12. Radix Dialog is a runtime dependency. Keep Radix and Vaul versions in step during upgrades. [verified: package.json; advice inferred]

## Resources

1. **Vaul GitHub repo** - https://github.com/emilkowalski/vaul - official repo - Holds the unmaintained notice; check issues and open PRs before depending on it.
2. **Vaul README (raw)** - https://raw.githubusercontent.com/emilkowalski/vaul/main/README.md - official README - Contains only the unmaintained notice; useful to confirm status.
3. **Vaul src/index.tsx** - https://raw.githubusercontent.com/emilkowalski/vaul/main/src/index.tsx - source - Handle, NestedRoot, snapPoints and fadeFromIndex types, direction, background scaling, handleOnly.
4. **Vaul package.json** - https://raw.githubusercontent.com/emilkowalski/vaul/main/package.json - manifest - Version 1.1.2, exports, files (including style.css), peer and runtime dependency ranges.
5. **Vaul on npm** - https://www.npmjs.com/package/vaul - registry page - Install line and the author's one-line description (unstyled drawer, Dialog replacement). Usage example is truncated in the fetch.
6. **Vaul docs site** - https://vaul.emilkowal.ski/ - official docs - Not fetchable from here (robots disallowed). Open it in a browser to check snap points, nested and Title examples.
7. **Radix Dialog docs (mintlify mirror)** - https://www.mintlify.com/radix-ui/primitives/components/dialog - third-party mirror of Radix docs (fetched) - Says Title is required for accessibility. Check radix-ui.com for the authoritative version.
8. **Radix primitives philosophy (mintlify mirror)** - https://www.mintlify.com/radix-ui/primitives/concepts/philosophy - third-party mirror (seen in search, not fetched) - Background on the primitive layer Vaul builds on.
9. **Community fork of vaul** - https://github.com/ddaoxuan/vaul - community repo (seen in search, not fetched) - Possible maintained alternative. Not endorsed: check its activity, license and relationship to upstream before use.
10. **vaul-svelte** - https://github.com/neimadt/vaul-svelte - community port (seen in search, not fetched) - Example of porting the drawer pattern to another framework. Not endorsed; check license and activity.
