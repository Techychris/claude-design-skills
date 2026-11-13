# shadcn/ui: rule verification and resources

Checked 2026-11-12 against the official docs at ui.shadcn.com, plus upstream docs at radix-ui.com and base-ui.com.
Local rules compared: `kb/ui-core.md` section 1 and the shadcn skill rules (`skills/shadcn/rules/`: styling, forms, composition, icons, base-vs-radix) and `skills/shadcn/SKILL.md`.

Verdicts: CONFIRMED, CONTRADICTED, STALE, UNVERIFIABLE. Tags: [verified] = a fetched page says it; [inferred] = deduced.
Method notes: the GitHub raw paths for theming, dialog, field and input-group returned client errors, so the ui.shadcn.com pages were used instead. Several docs pages are Base UI variants; the Radix variants are under `/docs/components/radix/`. Page content was read through a summarising fetch, so exact wording was not checked; claims are paraphrased.

---

## Verdict table

| # | Local rule (file) | Verdict | Decided by | Tag | Note |
|---|---|---|---|---|---|
| 1 | Use semantic color tokens, not raw palette classes (styling.md) | CONFIRMED | https://ui.shadcn.com/docs/theming | verified | Docs build all components on tokens with paired `-foreground` tokens. Docs also offer raw palette colors as an install-time option (`--no-css-variables`), so "never raw" is a skill policy, not a docs rule. |
| 2 | Built-in variants before custom styling (styling.md) | CONFIRMED (variants exist); preference UNVERIFIABLE | https://ui.shadcn.com/docs/components/button | verified | Button lists default, outline, secondary, ghost, destructive, link; sizes include xs, sm, lg, icon variants. |
| 3 | `className` for layout only, not colors or type (styling.md) | UNVERIFIABLE | none fetched that states it | - | Policy rule. |
| 4 | No `space-x-*` / `space-y-*`; use `gap-*` (styling.md, SKILL.md) | UNVERIFIABLE | https://ui.shadcn.com/docs/components/field | verified | Field docs use `gap-6` on FieldGroup, but the docs do not forbid `space-y`. |
| 5 | Use `size-*` when width equals height (styling.md) | UNVERIFIABLE | none | - | Spinner docs size the icon with `size-*` utilities, which fits the rule but does not state it. |
| 6 | Use `truncate` shorthand (styling.md) | UNVERIFIABLE | none | - | Tailwind utility; no shadcn page fetched covers it. |
| 7 | No manual `dark:` color overrides; use tokens (styling.md) | CONFIRMED (principle) | https://ui.shadcn.com/docs/theming | verified | Dark mode works by overriding the same tokens under `.dark`. The dark-mode page itself is a stub that links framework guides, so the "no dark:" ban is not stated there. |
| 8 | Use `cn()` for conditional classes (styling.md) | UNVERIFIABLE | none | - | Not fetched. |
| 9 | No manual `z-index` on overlays (styling.md) | UNVERIFIABLE | none | - | Not stated on any fetched page. |
| 10 | Use `shimmer` and `scroll-fade` utilities, no custom keyframes (styling.md) | UNVERIFIABLE | none | - | The utilities do not appear in any fetched page. |
| 11 | Forms use `FieldGroup` + `Field` (forms.md) | CONFIRMED | https://ui.shadcn.com/docs/components/field | verified | Field page presents FieldGroup stacking Field components. |
| 12 | `Field orientation="horizontal"` for settings pages (forms.md) | CONFIRMED (option exists); "settings pages" use INFERRED | https://ui.shadcn.com/docs/components/field | verified | Orientation is vertical, horizontal or responsive; docs pair horizontal with FieldContent. |
| 13 | `FieldLabel className="sr-only"` for hidden labels (forms.md) | UNVERIFIABLE | none | - | Not stated. |
| 14 | Option sets use `ToggleGroup`; count is 2 to 7 (forms.md) | CONFIRMED (use ToggleGroup for option sets); the 2 to 7 count UNVERIFIABLE | https://ui.shadcn.com/docs/components/toggle-group | verified | Docs state no option limit. Local files conflict: SKILL.md and forms.md "Choosing controls" say 2 to 5, forms.md "Option sets" says 2 to 7. STALE / internal inconsistency. |
| 15 | ToggleGroup `spacing={2}` in examples (forms.md) | CONFIRMED, with a change | https://ui.shadcn.com/docs/components/toggle-group | verified | The docs say the spacing default changed from 0 to 2 on 2026-05-17; `spacing={0}` makes items connected. The local example is consistent with the new default. |
| 16 | `InputGroup` contains `InputGroupInput` / `InputGroupTextarea`, not raw `Input` (forms.md) | CONFIRMED | https://ui.shadcn.com/docs/components/input-group | verified | InputGroupInput is described as the replacement for Input in input groups. Docs show no raw Input example. |
| 17 | Buttons inside inputs: `InputGroup` + `InputGroupAddon` with a `Button` (forms.md) | CONTRADICTED (the component in the example) | https://ui.shadcn.com/docs/components/input-group | verified | The addon wrapper is confirmed. The official examples put `InputGroupButton` inside the addon, and the rule's example uses a plain `Button`. Fix the example. |
| 18 | Validation: `data-invalid` on `Field`, `aria-invalid` on the control (forms.md) | CONFIRMED | https://ui.shadcn.com/docs/components/field | verified | Docs say the Field attribute switches the whole block to an error state; aria-invalid goes on the input. |
| 19 | Disabled: `data-disabled` on `Field`, `disabled` on control (forms.md) | UNVERIFIABLE | https://ui.shadcn.com/docs/components/field | verified | Field page does not mention data-disabled. |
| 20 | `FieldSet` + `FieldLegend` for grouped checkboxes and radios (forms.md) | CONFIRMED | https://ui.shadcn.com/docs/components/field | verified | FieldSet renders a fieldset that usually contains a FieldLegend and FieldGroup. |
| 21 | Items inside their Group: `SelectItem` in `SelectGroup` (composition.md) | CONFIRMED for Select; other components UNVERIFIABLE | https://ui.shadcn.com/docs/components/radix/select | verified | Radix Select example wraps items in SelectGroup. The table extending this to Dropdown, Menubar, Command, etc. was not checked. |
| 22 | `asChild` (radix) or `render` (base) for custom triggers (base-vs-radix.md) | CONFIRMED (mechanism) | https://www.radix-ui.com/primitives/docs/guides/composition and https://base-ui.com/react/components/dialog | verified | Radix `asChild` replaces the default element with the child. Base UI Dialog.Trigger has a `render` prop. The shadcn radix dialog example itself does not use asChild. |
| 23 | Base: `<Button render={<a href>} nativeButton={false}>` for links (base-vs-radix.md) | CONTRADICTED | https://ui.shadcn.com/docs/components/button | verified | Button docs say not to use `render` for links and to use `buttonVariants` on a plain `<a>`. The `nativeButton={false}` advice for non-button triggers is supported by https://base-ui.com/react/components/dialog, so only the Button-as-link example is wrong. |
| 24 | Base `Select` requires an `items` prop (base-vs-radix.md) | CONFIRMED | https://ui.shadcn.com/docs/components/select | verified | Base example passes an items array to Select. |
| 25 | Radix `Select` uses inline JSX items and `SelectValue placeholder` (base-vs-radix.md) | CONFIRMED | https://ui.shadcn.com/docs/components/radix/select | verified | Radix example writes items inline and sets a placeholder on SelectValue. |
| 26 | ToggleGroup `type` (radix) vs `multiple` (base) (base-vs-radix.md) | UNVERIFIABLE | https://ui.shadcn.com/docs/components/toggle-group | verified | Radix example uses type="single". Base props are deferred to Base UI docs, which were not fetched. |
| 27 | Dialog, Sheet, Drawer always need a Title (composition.md) | UNVERIFIABLE (recommended, not required) | https://www.radix-ui.com/primitives/docs/components/dialog and https://base-ui.com/react/components/dialog | verified | Radix describes Title as the accessible name announced on open; Base UI recommends explicit title and description. Neither says it is strictly required. shadcn dialog docs show DialogTitle in the example but say nothing about accessibility. |
| 28 | Full Card composition (CardHeader, CardTitle, CardDescription, CardContent, CardFooter) (composition.md) | CONFIRMED (structure); "do not dump into CardContent" UNVERIFIABLE | https://ui.shadcn.com/docs/components/card | verified | Composition shows CardHeader containing title, description and action; content and footer are siblings. |
| 29 | Button has no `isPending`/`isLoading`; compose with Spinner + data-icon + disabled (composition.md) | CONFIRMED | https://ui.shadcn.com/docs/components/button and https://ui.shadcn.com/docs/components/spinner | verified | Button docs document no loading prop and say to render a Spinner inside the button. Spinner uses data-icon before or after the label. |
| 30 | `TabsTrigger` inside `TabsList` (composition.md) | CONFIRMED (structure) | https://ui.shadcn.com/docs/components/tabs | verified | Composition puts triggers in TabsList. The docs do not say "never directly in Tabs". |
| 31 | Avatar always needs `AvatarFallback` (composition.md) | UNVERIFIABLE | https://ui.shadcn.com/docs/components/avatar | verified | Fallback appears in every example; the docs do not say it is required. |
| 32 | Toast: Base uses `toast`, Radix/Aria use `sonner` (composition.md, SKILL.md) | CONFIRMED (mapping) | https://ui.shadcn.com/docs/components/toast and https://ui.shadcn.com/docs/components/radix/sonner | verified | Toast page is the Base UI toast; Sonner page is the Radix variant and requires a Toaster in the root layout. |
| 33 | Base toast call: `toast.add({ title })` (composition.md) | CONFIRMED | https://ui.shadcn.com/docs/components/toast | verified | Docs show toast.add with title, description, type and actionProps. |
| 34 | Radix toast examples: `toast.success`, `toast.error`, `toast` with action (composition.md) | UNVERIFIABLE (call forms) | https://ui.shadcn.com/docs/components/radix/sonner | verified | Docs show plain `toast(...)` and list Success/Error variants; the `.success` and `.error` call forms and action example were not seen. |
| 35 | Callouts use Alert; empty states use Empty (composition.md) | Empty: CONFIRMED (composition); Alert: UNVERIFIABLE | https://ui.shadcn.com/docs/components/empty | verified | Empty composition: EmptyHeader (EmptyMedia variant icon, EmptyTitle, EmptyDescription) and EmptyContent. Alert page not fetched. |
| 36 | Use Separator, Skeleton, Badge instead of custom markup (composition.md) | UNVERIFIABLE | none | - | Pages not fetched. |
| 37 | Overlay selection table: Dialog, AlertDialog, Sheet, Drawer, HoverCard, Popover (composition.md) | UNVERIFIABLE | none | - | Guidance table; no fetched page states it. |
| 38 | Icons in Button use `data-icon="inline-start"` or `"inline-end"` (icons.md) | CONFIRMED | https://ui.shadcn.com/docs/components/button | verified | Docs say to add the attribute for correct spacing. |
| 39 | No sizing classes on icons inside components (icons.md) | UNVERIFIABLE (tension with Spinner docs) | https://ui.shadcn.com/docs/components/button and https://ui.shadcn.com/docs/components/spinner | verified | Button docs give no icon sizing rules. Spinner docs say to change size with a `size-*` utility, so "never size" is stricter than the docs. |
| 40 | Pass icon components, not string keys (icons.md) | UNVERIFIABLE | none | - | Generic React practice; not a shadcn doc statement. |
| 41 | Use the project's configured `iconLibrary` (icons.md, SKILL.md) | UNVERIFIABLE | none | - | Not checked against docs. |
| 42 | Chat: MessageScroller owns streaming follow and jump-to-latest (chat.md, SKILL.md) | CONFIRMED (behaviour); "do not write your own hook" INFERRED | https://ui.shadcn.com/docs/components/message-scroller | verified | Docs say autoScroll on the provider keeps streamed replies in view, and MessageScrollerButton jumps to the end and is inert when there is nothing to scroll. |
| 43 | Chat: Message, Bubble, Trace, Marker, Attachment composition (chat.md) | UNVERIFIABLE | none | - | Only MessageScroller was fetched. |
| 44 | CLI commands in SKILL.md (info --json, search, docs, view, add --dry-run/--diff, apply --only, preset decode/url/open/resolve) | CONFIRMED | https://ui.shadcn.com/docs/cli | verified | All listed subcommands and flags appear in the CLI docs. `--overwrite` also exists; the "never without approval" rule is policy. |
| 45 | Skill install and scope (SKILL.md, KB section 1) | CONFIRMED (install and scope); rule-file names UNVERIFIABLE | https://ui.shadcn.com/docs/skills | verified | Docs give `pnpm dlx skills add shadcn/ui` and say the skill covers CLI, theming, dark mode, registry and MCP. Docs do not list the rule files by name. |
| 46 | Registry must be stated explicitly; ask the user (SKILL.md) | UNVERIFIABLE | none | - | Policy rule. |
| 47 | Named presets nova, vega, maia, lyra, mira, luma (SKILL.md) | UNVERIFIABLE | none | - | Not checked against the docs. |
| 48 | Local rules say all components use semantic tokens with paired foreground tokens (KB section 1, theming) | CONFIRMED | https://ui.shadcn.com/docs/theming | verified | See row 1. |

Summary: CONTRADICTED on rows 17 and 23; STALE / internal conflict on row 14 (the 2 to 5 vs 2 to 7 count); the rest are CONFIRMED or UNVERIFIABLE as marked.

---

## Missed guidelines (in official docs, absent or thin in the KB)

Theming tokens [verified, theming]
- Each surface token pairs with a `-foreground` token; the `background` suffix is dropped from names (`primary` pairs with `primary-foreground`).
- Theme tokens are defined under `:root` (light) and `.dark` (dark). The list covers app background, card, popover, primary, secondary, muted, accent, destructive, border, input, ring, `chart-1` to `chart-5`, sidebar tokens and `radius`.
- Radius: `--radius` is the base; `radius-sm` through `radius-4xl` derive from it with calc(), so one change rescales the whole set.
- Adding a custom color: define it under both `:root` and `.dark`, then expose it to Tailwind with `@theme inline` using a `--color-` prefix. Then utilities like `bg-<name>` and `text-<name>-foreground` work.
- Base colors are an init or preset option: Neutral, Stone, Zinc, Mauve, Olive, Mist, Taupe.
- `components.json` has `tailwind.cssVariables` true by default. Setting `--no-css-variables` at install generates raw palette classes (for example `bg-zinc-950`); switching later means reinstalling components.

Dark mode [verified, dark-mode page is a stub]
- The dark-mode page only links framework guides (Next.js, Vite, Astro, Remix, TanStack Start). Next.js guide at https://ui.shadcn.com/docs/dark-mode/next was linked but not fetched. Theme provider details are therefore UNVERIFIABLE here.

Accessibility [verified where noted]
- Radix Dialog: Title announced on open; can be visually hidden by wrapping in Visually Hidden with asChild; Description optional, and removed by omitting it and passing `aria-describedby={undefined}` [verified, radix dialog page].
- Base UI Dialog: explicit title and description recommended for accessible labels [verified, base-ui dialog page].
- Field: data-invalid switches the whole field block into error state; aria-invalid goes on the control [verified, field page].
- Button: loading state via Spinner inside the button, not a prop [verified, button page].

Do / don't from the docs [verified]
- Do not use Button with `render` for a link; use `buttonVariants` on a plain `<a>` [button page].
- Use InputGroupButton (not Button) for buttons inside InputGroupAddon [input-group page].
- Use `spacing={0}` on ToggleGroup for connected items [toggle-group page].
- Put a Toaster in the root layout for Sonner or Base toast [sonner and toast pages].
- Base Select: pass an items array to Select; Radix Select: inline items, placeholder on SelectValue [select pages].

Workflow guidance from the skills page [verified, skills page]
- The skill loads project context via `shadcn info --json` and checks docs, search or MCP tools before generating code.

Not covered by any fetched page (candidates for follow-up): data-disabled on Field, `cn()` helper, overlay z-index, chart component, sidebar, Next.js dark-mode guide.

---

## Resources

1. shadcn/ui Theming. https://ui.shadcn.com/docs/theming. Type: official docs. Why: the canonical token list, `.dark` overrides, `@theme inline` pattern and radius scale.
2. shadcn/ui Skills. https://ui.shadcn.com/docs/skills. Type: official docs. Why: install command and what the official skill covers, so you can check the local rule set against it.
3. shadcn/ui Field. https://ui.shadcn.com/docs/components/field. Type: official docs. Why: FieldGroup, Field, FieldSet, orientation and data-invalid/aria-invalid usage.
4. shadcn/ui Input Group. https://ui.shadcn.com/docs/components/input-group. Type: official docs. Why: correct sub-components (InputGroupInput, InputGroupAddon, InputGroupButton), which contradicts the local rule example.
5. shadcn/ui Button. https://ui.shadcn.com/docs/components/button. Type: official docs. Why: variants, sizes, data-icon, no loading prop, and the "do not render links as Button" guidance.
6. shadcn/ui Toggle Group. https://ui.shadcn.com/docs/components/toggle-group. Type: official docs. Why: the spacing default change on 2026-05-17 and the missing option limit (the 2 to 7 rule is unsupported).
7. shadcn/ui Message Scroller. https://ui.shadcn.com/docs/components/message-scroller. Type: official docs. Why: autoScroll and jump-to-latest behaviour for the chat rules.
8. shadcn/ui CLI. https://ui.shadcn.com/docs/cli. Type: official docs. Why: confirms every CLI command and flag the SKILL.md uses, including `apply --only` and `preset` subcommands.
9. shadcn/ui llms.txt index. https://ui.shadcn.com/llms.txt. Type: docs index. Why: flat list of every docs URL (forms, registry, components) for a quick re-check.
10. Radix Primitives Composition guide. https://www.radix-ui.com/primitives/docs/guides/composition. Type: official upstream docs. Why: how asChild hands behaviour to the child, the basis of the radix rule.
11. Radix Primitives Dialog. https://www.radix-ui.com/primitives/docs/components/dialog. Type: official upstream docs. Why: Title and Description accessibility behaviour and Visually Hidden usage.
12. Base UI Dialog. https://base-ui.com/react/components/dialog. Type: official upstream docs. Why: render prop on Trigger and Title, and nativeButton for non-button triggers.

Also fetched and useful: https://ui.shadcn.com/docs/components/radix/sonner (Radix toast with Toaster), https://ui.shadcn.com/docs/components/toast (Base toast with toast.add), https://ui.shadcn.com/docs/components/spinner, https://ui.shadcn.com/docs/components/select, https://ui.shadcn.com/docs/components/radix/select.
