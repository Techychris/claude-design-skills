# UI core knowledge base: shadcn/ui, Base UI, Radix Primitives

> Online validation 2026-11-12: corrections from `kb/validation.md` are applied below.

Built 2026-11-12 from local clones. Repos were read only.
Tags: [verified] = read in the source, README or config during this run. [inferred] = deduced from names or nearby code, not read directly.

Source paths:
- shadcn/ui: /home/claude/shadcn-ui/ui
- Base UI: /home/claude/mui/base-ui
- Radix Primitives: /home/claude/radix-ui/primitives

---

## 1. shadcn/ui

### Purpose
- README: "A set of beautifully designed components that you can customize, extend, and build on." [verified]
- Components are added to the user's project as source code through the CLI, not installed as a runtime dependency. [verified, skills/shadcn/SKILL.md]

### Structure
- `apps/v4/`: documentation site (Next.js `app/`, `content/docs/`). [verified]
- `apps/v4/registry/`: authored registry. `bases/base/` (Base UI), `bases/radix/` (Radix), `bases/aria/` (a third base, React Aria; its `ui/` list was not enumerated). Also `styles/style-*.css` (luma, lyra, maia, mira, nova, rhea, sera, vega) and `new-york-v4/` (legacy). [verified]
- `apps/v4/registry/bases/*/ui/`: the generated-from-source component files. Generated output (`__index__.tsx`, `public/r/`) is not hand-edited per the registry README. [verified]
- `packages/shadcn/`: the `shadcn` CLI (commands, preset, registry, templates). [verified]
- `packages/registry/`: `@shadcn/registry`, the client library behind the CLI. [verified]
- `packages/react/`: `@shadcn/react`, described as "Unstyled components for React." [verified]
- `skills/`: two skill folders, `shadcn/` and `migrate-radix-to-base/`. [verified]

### Component inventory
- Radix base (`apps/v4/registry/bases/radix/ui/`), 63 registry files at clone HEAD dd41d19 (the live docs index lists 66 entries, a different measure): accordion, alert-dialog, alert, aspect-ratio, attachment, avatar, badge, breadcrumb, bubble, button-group, button, calendar, card, carousel, chart, checkbox, code-block, collapsible, combobox, command, context-menu, dialog, direction, drawer, dropdown-menu, empty, field, hover-card, input-group, input-otp, input, item, kbd, label, marker, menubar, message-scroller, message, native-select, navigation-menu, pagination, popover, progress, questionnaire, radio-group, resizable, scroll-area, select, separator, sheet, sidebar, skeleton, slider, sonner, spinner, switch, table, tabs, textarea, toggle-group, toggle, tooltip, trace. [verified]
- Base base (`bases/base/ui/`): the same 63 files plus `toast.tsx` (64 total). Radix base uses `sonner`; Base base uses `toast` and also keeps `sonner`. [verified]
- Chat primitives (`message-scroller`, `message`, `bubble`, `attachment`, `marker`, `trace`) and `questionnaire`, `code-block`, `item`, `empty` are shadcn-level compositions, not wrappers of a single upstream primitive. [inferred from names and the chat rules]

### Install and usage
Install a component (CLI README):
```bash
npx shadcn@latest add alert-dialog
```
- Project setup: `npx shadcn init`. Apply a preset to an existing project: `npx shadcn apply --preset <code>`. [verified, packages/shadcn/README.md]
- The READMEs contain no component usage snippet. A usage example is in section 2 (Base UI) and section 3 (Radix), checked online against base-ui.com and radix-ui.com.

### Key concepts
- Project config lives in `components.json`. Fields include `base` (`radix` or `base`), `style` (e.g. `radix-nova`), `tailwindVersion`, `iconLibrary`, and `aliases`. Read them with `npx shadcn@latest info --json`. [verified, skills/shadcn/SKILL.md]
- Registry items are served as JSON, e.g. `https://ui.shadcn.com/r/styles/<style>/<component>.json`. [verified, skills/migrate-radix-to-base/SKILL.md]
- Composition differs by base: Radix uses `asChild`, Base UI uses `render`. [verified, skills/shadcn/rules/base-vs-radix.md]
- Theming: semantic color tokens (`bg-primary`, `text-muted-foreground`) defined in the style CSS files. Raw palette classes are disallowed by the skill. [verified, skills/shadcn/SKILL.md; style-*.css exist]
- Accessibility rules enforced by the skill: `DialogTitle`/`SheetTitle`/`DrawerTitle` always present; `aria-invalid` on the control plus `data-invalid` on `Field`; `Avatar` always has `AvatarFallback`. [verified, SKILL.md]

### Skill 1: shadcn (skills/shadcn/SKILL.md, 296 lines)
- Run CLI through the project's package runner (`npx`, `pnpm dlx`, or `bunx --bun`) and read `info --json` before writing code.
- Check registries (`npx shadcn@latest search`) before writing custom UI; use built-in variants before custom styles.
- Layout: `flex` + `gap-*`, never `space-x-*`/`space-y-*`; `size-*` for equal width and height; `cn()` for conditional classes.
- Forms: `FieldGroup` + `Field`; `ToggleGroup` for 2 to 7 options; `FieldSet` + `FieldLegend` for grouped checkboxes/radios.
- Structure: items inside their Group (`SelectItem` in `SelectGroup`); `TabsTrigger` inside `TabsList`; `Button` has no `isPending`/`isLoading`.
- Use `asChild` (radix) or `render` (base) for custom triggers; check `base` first.
- Icons: `data-icon="inline-start"` or `"inline-end"` in buttons; no sizing classes on icons; pass icon components, not string keys.
- Presets: never decode or build preset URLs by hand; use `npx shadcn@latest preset decode|url|open|resolve`.
- Rule files: `rules/styling.md`, `forms.md`, `composition.md`, `icons.md`, `chat.md`, `base-vs-radix.md`. Also `cli.md`, `mcp.md`, `registry.md`, `customization.md`, `design-system*.md`.

### Skill 2: migrate-radix-to-base (skills/migrate-radix-to-base/SKILL.md, 173 lines, plus 9 reference files)
- Preflight: `shadcn info --json`, detect package manager from lockfile, require a clean git tree, work on a branch, run a baseline build before changing dependencies.
- Install `@base-ui/react` next to Radix; remove Radix packages only after the last component migrates.
- Golden-pair first: fetch the base variant by URL and use `git merge-file` (radix golden as ancestor) to replay customizations. Never bulk `--overwrite`.
- Legacy styles (new-york, new-york-v4, default) get classification only; their look is kept and class renames applied to the user's own file.
- Hard rules: leave cmdk, vaul, sonner, input-otp, react-day-picker and recharts untouched; no Base UI counterpart for AspectRatio (use CSS aspect-ratio), Label (native `<label>`), VisuallyHidden (`sr-only`), Direction (`direction` prop on DirectionProvider).
- Behaviour changes are flagged, never silently patched (tabs activation, menu close-on-click, nav-menu 50ms delay).
- Mandatory leftover sweep: `grep -n "radix-ui\|@radix-ui"` on every migrated file, even ones that merged cleanly.
- Reports go to `.migration/<component>.md`, one per component, with no index file; "N wrappers remain on Radix" is derived from disk.

### License
- MIT, `LICENSE.md`, "Copyright (c) 2023 shadcn". [verified]
- Skills are inside the same repo, so they fall under MIT. [inferred]

---

## 2. Base UI (/home/claude/mui/base-ui)

### Purpose
- README: "From the creators of Radix, Floating UI, and Material UI, Base UI is an unstyled UI component library for building accessible user interfaces." [verified]
- Package README: "a library of unstyled React components. You gain complete control over your app's CSS and accessibility features." [verified]
- Package `@base-ui/react` version 1.9.0. [verified, packages/react/package.json]

### Structure
- `packages/react/` (`@base-ui/react`): `src/` has one folder per component plus `internals/`, `use-render/`, `merge-props/`, `utils/`, `types/`. [verified]
- `packages/utils/`: second package, MIT. [verified]
- Top level: `examples/`, `playground/`, `test/`, `scripts/`, `GLOSSARY.md`, `CHANGELOG.md`, `AGENTS.md`, `CLAUDE.md`, `skills-lock.json`. [verified by listing]
- Exports use per-component subpaths, e.g. `./button`, `./dialog`. [verified, package.json exports]

### Component inventory (39 folders in packages/react/src)
accordion, alert-dialog, autocomplete, avatar, button, checkbox, checkbox-group, collapsible, combobox, context-menu, dialog, drawer, field, fieldset, filter-dropdown, form, input, menu, menubar, meter, navigation-menu, number-field, otp-field, popover, preview-card, progress, radio, radio-group, scroll-area, select, separator, slider, switch, tabs, toast, toggle, toggle-group, toolbar, tooltip. [verified]
Non-component modules: csp-provider, direction-provider, merge-props, use-render, unstable-use-media-query. [verified]

### Install and usage
```bash
npm install @base-ui/react
```
(packages/react/README.md) [verified]

Usage (verified online against https://base-ui.com/react/components/dialog; import line confirmed):
```tsx
import { Dialog } from "@base-ui/react/dialog"

<Dialog.Root>
  <Dialog.Trigger>Open</Dialog.Trigger>
  <Dialog.Portal><Dialog.Popup>...</Dialog.Popup></Dialog.Portal>
</Dialog.Root>
```

Dialog parts (`dialog/index.parts.ts`) [verified]: Root, Trigger, Portal, Backdrop, Popup, Viewport, Title, Description, Close, plus `createHandle`/`Handle`.

### Key concepts
- `render` prop: accepts a React element or a function `(props, state)`; replaces the default tag. Props are merged, then the element is cloned. [verified, internals/useRenderElement.tsx lines 164-195, use-render/useRender.ts]
- State becomes `data-*` attributes: `true` gives an empty attribute, other values are stringified. Example: Button sets `data-disabled`. [verified, internals/getStateAttributesProps.ts; button/ButtonDataAttributes.ts]
- `className` may be a function of state, so styling reacts to component state without extra CSS selectors. [verified, internals/types.ts:48]
- Focus control props exist on the popup, e.g. `initialFocus` and `finalFocus`. [verified, dialog/popup/DialogPopup.tsx:29]
- Accessibility model: ARIA wiring and focus handling sit inside each component. The per-component ARIA logic was not audited in this run. [inferred]

### License
- MIT, `LICENSE`, "Copyright (c) 2019 Material-UI SAS". Packages declare `"license": "MIT"`. [verified]

---

## 3. Radix Primitives (/home/claude/radix-ui/primitives)

### Purpose
- README: "a low-level UI component library with a focus on accessibility, customization and developer experience." [verified]
- `philosophy.md` lists five principles: Accessible, Functional, Interoperable, Composable, Customizable. [verified]
- Accessibility stance: "Components adhere to WAI-ARIA guidelines and are tested regularly in a wide selection of modern browsers and assistive technologies." [verified, philosophy.md]

### Structure
- `packages/react/`: one package per component (59 entries, including helpers and the `radix-ui` meta package). [verified]
- `packages/core/`: `env-check`, `number`, `primitive`, `rect`. [verified]
- `internal/`: `builder`, `test-data`, `test-utils`, `typescript-config`. `apps/`: `ssr-testing`, `storybook`. `e2e/`, `scripts/`, `.changeset/`. [verified]
- Versions read: `@radix-ui/react-dialog` 1.3.1; meta package `radix-ui` 1.8.1. [verified]
- Monorepo: pnpm workspaces plus changesets. [verified, pnpm-workspace.yaml, .changeset/]

### Component inventory (32 public component packages)
accessible-icon, accordion, alert-dialog, aspect-ratio, avatar, checkbox, collapsible, context-menu, dialog, dropdown-menu, form, hover-card, label, menubar, navigation-menu, one-time-password-field, password-toggle-field, popover, progress, radio-group, scroll-area, select, separator, slider, switch, tabs, toast, toggle, toggle-group, toolbar, tooltip, visually-hidden. [verified from directory names]
Helper and internal packages (not components): arrow, collection, compose-refs, context, direction, dismissable-layer, focus-guards, focus-scope, id, menu, popper, portal, presence, primitive, roving-focus, slot, and `use-*` hooks. [verified]

### Install and usage
- README covers only the repo dev setup: `npm install -g pnpm` then `pnpm install`. The README has no consumer install line. [verified]
- Consumer install: `npm install radix-ui`. [verified online: https://www.radix-ui.com/primitives/docs/overview/introduction recommends it]

Usage (verified online against https://www.radix-ui.com/primitives/docs/components/dialog; import and `asChild` confirmed; the Portal/Content nesting is not shown verbatim on that page):
```tsx
import { Dialog } from "radix-ui"

<Dialog.Root>
  <Dialog.Trigger asChild><button>Open</button></Dialog.Trigger>
  <Dialog.Portal><Dialog.Content>...</Dialog.Content></Dialog.Portal>
</Dialog.Root>
```

Dialog export aliases (`dialog/src/dialog.tsx` lines 653-672): Root, Trigger, Portal, Overlay, Content, Title, Description, Close. [verified]

### Key concepts
- `asChild` is implemented by `Slot`: it clones its single child, merges props so child props win, and composes `on*` handlers so both run. [verified, slot/src/slot.tsx lines 81-88, 144-160]
- `data-state` marks open and closed state on dialog elements, which is the styling hook for consumers. [verified, dialog/src/dialog.tsx:153]
- Behaviour is in internal building blocks: focus-scope, focus-guards, dismissable-layer, presence, portal, popper, roving-focus. Their exact behaviour was not read. [verified names; behaviour inferred]
- Unstyled by design: no default CSS, the consumer supplies all styling. [inferred from the "Customizable" principle]

### License
- MIT, `LICENSE`, "Copyright (c) 2022 WorkOS"; README says "Copyright © 2022-present WorkOS". [verified]

---

## 4. How the three relate

- Radix Primitives is the upstream dependency of shadcn's Radix base (`from "radix-ui"`). [verified, bases/radix/ui/dialog.tsx:5]
- Base UI is a separate library, consumed by shadcn's Base base (`from "@base-ui/react/dialog"`). [verified, bases/base/ui/dialog.tsx:4]
- Same shadcn component names exist in both bases, so a project switches by changing the `base` field and the style prefix (`radix-<style>` to `base-<style>`). [verified, migrate SKILL.md and SKILL.md]
- Migration path (Radix to Base UI):
  1. Install `@base-ui/react` alongside Radix.
  2. Migrate one wrapper at a time, bottom-up (leaf wrappers such as Button first).
  3. Swap `asChild` for `render` (see base-vs-radix.md) and rename parts (Content to Popup). Add a Positioner inside Portal only for Popover- and Menu-style parts; Dialog has no Positioner. [verified: base-ui.com Dialog and Popover pages]
  4. Flip `components.json` to `base-<style>` after the last wrapper, then remove Radix packages. [verified, migrate SKILL.md]
- Parts with no Base UI counterpart: AspectRatio, Label, VisuallyHidden, Popover Anchor, NavigationMenu Indicator. [verified]
- Known behaviour deltas to check by hand: tabs activation, menu close-on-click, nav-menu delay. [verified, migrate SKILL.md]
- The Base UI README says its creators come from Radix, Floating UI and Material UI. This is the project's own claim. [verified as stated]

---

## 5. Licenses at a glance

| Project | License | Copyright line (as read) |
|---|---|---|
| shadcn/ui | MIT | Copyright (c) 2023 shadcn |
| Base UI | MIT | Copyright (c) 2019 Material-UI SAS |
| Radix Primitives | MIT | Copyright (c) 2022 WorkOS |

---

## 6. Gaps

- None of the three READMEs has a component usage snippet. The usage blocks above are inferred from source and match the live docs checked on 2026-11-12.
- Not read: `apps/v4/content/docs/` in shadcn, Base UI `docs` (not in this clone), Radix `e2e/` and `apps/`.
- shadcn rule files were not opened except `rules/base-vs-radix.md`. The rules listed under skill 1 come from the summary in `skills/shadcn/SKILL.md`. The 9 migrate reference files (`universal-patterns.md`, `class-mapping.md`, etc.) were not read.
- The `aria` base in shadcn was not enumerated.
- No official ui.shadcn.com Radix-to-Base migration page was found; the migration steps rest on `skills/migrate-radix-to-base` only (a community discussion is the only online guide).
- No tests or builds were run.

## Guideline check and resources (2026-11-12)

Per-library verdict tables and resources are in `kb/resources/` (`shadcn.md`, `base-ui.md`, `radix.md`).

- **Base UI Direction:** Base UI does ship `DirectionProvider` and `useDirection`, so Direction does have a counterpart; remove it from the "no counterpart" list in section 4 (section 1 already maps it). Base UI has `Field.Label` rather than a standalone Label. [verified online 2026-11-12]
- **Base UI count:** the public docs list 37 components; the repo folders `filter-dropdown` and `radio` are not in the public list. [verified online]
- **Base UI additions:** `nativeButton` must be false for non-button triggers; change handlers receive `eventDetails` with `cancel()`; form validation runs on submit unless `validationMode` is set; prefer CSS transitions over keyframes for open/close; custom render elements must forward refs and spread props. The docs have no reduced-motion guidance.
- **Radix additions:** primitives ship unstyled (the Dialog Overlay does not cover the viewport until styled); `asChild` children must spread props and forward refs; Dialog Title is the accessible name (hide it with Visually Hidden, don't remove it); animate exits with `data-state` keyframes or `forceMount` (unsourced, not re-verified); React 18+ generates ids on the server. The docs page for Dialog shows 1.2.0 while npm latest is 1.3.1.
- **shadcn corrections:** the input-group rule example should use `InputGroupButton`, not `Button`, inside `InputGroupAddon`; the `render`-on-Button link example is wrong, because the docs say to use `buttonVariants` on a plain `<a>`; the `ToggleGroup` option limit is 2-5 in one rule file and 2-7 in another and the docs give no limit. Most style rules (no `space-x/y`, `size-*`, icon sizing, `z-index`) are skill policy that the docs neither state nor forbid.
- **shadcn additions:** each surface token pairs with a `-foreground` token; `--radius` derives the radius scale; add custom colors under `:root` and `.dark` then expose them with `@theme inline`; `--no-css-variables` generates raw palette classes; `ToggleGroup` spacing default changed to 2 on 2026-05-17. The dark-mode docs page is a stub.

Package versions re-checked on npm 2026-11-12: @base-ui/react 1.9.0, radix-ui 1.8.1, @radix-ui/react-dialog 1.3.1, shadcn CLI 4.23.0. Base UI docs recommend CSS transitions over CSS animations and never mention prefers-reduced-motion. The Base UI package was renamed from `@base-ui-components/react`.

_Validated 2026-11-12 against primary sources; see ../validation-reports/._
