---
name: "design"
description: "Build, polish (unslop) or review any UI: landing pages, sites, dashboards, app screens. Also faux product UI: hero demos, feature-card stills, bento grids and cursor walkthrough animations. Deliberate direction, craft rules and tokens, plus Nielsen usability and WCAG 2.2 audits."
---

# Design

One skill for interface work, in four modes. Pick the mode first, then the surface, then follow that mode's run. The direction, craft rules and tokens are shared by all four.

| Mode | Use when | Run |
| --- | --- | --- |
| **Build** | A new page, screen, component or redesign | Direction → plan → review the plan → build → check |
| **Polish** | Existing UI looks generic, sloppy or AI-made ("unslop", "clean up", "make it look designed") | Look → audit → decide depth → direction → nine passes → check |
| **Demo** | Faux product UI: a hero or feature-card illustration of an app, a bento grid, a mocked screen, an animated cursor walkthrough, even if no one says "faux UI" | Plan → look → story → start from a gold → screen → choreograph → rehearse |
| **Review** | Findings only: a usability review, an accessibility audit, or both | Scope → walk the tasks → findings with severity → priorities |

| Surface | What it is | Leans on |
| --- | --- | --- |
| **Page** | Read and scrolled: landing, marketing, product site, portfolio, event, org site | Hero, copy, imagery, section rhythm |
| **App screen** | Worked in: dashboard, admin, settings, tables, inbox, tools | Hierarchy, density, states, tokens |

A product site that shows its app is a page; the app fragments on it follow app-screen rules inside.

## The problem this skill exists for

A model's default UI is the average of every UI it has seen: centered headline with a little label above it, a row of icon cards, soft gradients, the same radius and grey shadow on everything. Nothing in it is wrong and nothing in it was decided. It happens because intent lives in prose while code generation pulls from patterns: you can write "warm and specific" and still emit the template, so every choice has to be checked against the intent, not just stated. If another model given a similar prompt would produce substantially the same screen, the work has failed. The fix is not "different for its own sake" but different because the design came from *this* subject, *this* person and *this* task.

Defaults hide in what feels like infrastructure. Typography is the design, not a container for it. Navigation is the product (where you are, where you can go). A number on screen means something to the person reading it. Token names like `--ink` and `--parchment` describe a world; `--gray-700` and `--surface-2` describe a template.

Removing slop is half the job. A clean screen that could belong to any product is the next template. Every run ends with a screen only this product could have.

## Existing brand or design spec wins

If the product has a real brand or written spec (logo, colors, typefaces, weights), or the brief names a visual direction, follow it exactly, even when it asks for something this skill calls a default. Where a rule here conflicts with the spec, keep the spec and list the conflict in the report as a decision for the user, with the one-line change that would apply the rule. A violet-to-blue gradient, sparkles or glow count as slop even in a logo unless the user says they are brand.

If `.design/system.md` (or a legacy `.interface-design/system.md`) exists in the project, read it first: those decisions are made. Hold to its values.

---

# Direction (all modes)

## Intent

Answer these before any visual decision. Keep it a compact working brief.

- **Who is this human?** The actual person, not "users". Where are they, what did they do five minutes ago, what will they do next?
- **What must they accomplish?** The verb: grade these submissions, find the broken deployment, find the next chapter meeting. It decides what leads, what follows, what hides.
- **What should it feel like?** In words that mean something. "Clean and modern" means nothing. Warm like a notebook, cold like a terminal, dense like a trading floor, calm like a reading app.

If the brief does not say what the subject is, propose one concrete subject, audience and primary job, and confirm. If context allows a responsible assumption, state it in one line and proceed. Use what you already know about the client's preferences as a hint.

Intent is systemic: if the feel is warm, surfaces, text, borders, accents and type are all warm. For every choice you must be able to say why. "It's common" or "it works" means you defaulted.

## Domain exploration

Produce all four before proposing a direction:

- **Domain:** five or more concepts, metaphors and words from the subject's world. Territory, not features.
- **Color world:** five or more colors that exist in the physical version of this world (its materials, light, objects).
- **Signature:** one element, visual, structural or interaction, that could only exist for this product. One, not five, used consistently where it belongs.
- **Defaults to reject:** the three obvious choices for this kind of interface, visual and structural, each with its alternative.

Test: read the proposal with the product name removed. If no one could tell what it is for, explore further.

## Direction block

Write this, show it, and (when rendering is available) show a small specimen: real swatches, the type scale in the real face, the signature as a real component.

```
Product:    [what it does, for whom, one sentence]
Character:  [2–3 concrete words, not clean/modern/sleek/minimal/premium]
World:      [place or material it belongs to; sets neutral tint, accent, visuals]
Moments:    [1–2 places that get rich color and detail, chosen from the content]
Signature:  [the one detail only this product has]
Rejecting:  [default → alternative] × 3
```

Then ask "Does that direction feel right?" and wait before building or editing. Skip the wait when the user said to just do it, when a brand or spec already fixes the direction, or for a single small component inside an existing design.

## Calibration: what generated design clusters around

Each is legitimate for some brief, but they appear regardless of subject, so treat them as defaults, not choices. Where the brief leaves an axis free, don't spend that freedom here:

1. Warm cream background (near `#F4F1EA`) with a high-contrast serif and a terracotta or clay accent (near `#D97757`).
2. Near-black background with one acid-green or vermilion accent.
3. Broadsheet layout: hairline rules, zero radius, dense newspaper columns.
4. The SaaS-card kit: identical rounded cards, one radius everywhere, the same soft grey shadow, gradient washes.
5. Template chrome: tracked ALL-CAPS eyebrows above headings, `A · B · C` meta strings, `WORD — fragment` labels, tinted near-black standing in for black, monospace data labels, `→` appended to buttons, violet or indigo accents.

---

# Craft rules (all modes)

## Hierarchy and composition

- **One focal point per view.** Name the thing the person came to do, then make it win through size, contrast, position or space. Demote everything else deliberately.
- **Weight and color do more hierarchy work than size.** One 14px size holds three tiers through weight and color: value 600 primary, label 500 secondary, meta 400 muted. Use size, weight and color together, never size alone.
- **Density is a decision in pixels.** Choose it up front and repeat the same numbers: tool panels 12–16 padding feel tight; 24 feels like a brochure.
- **Breathe unevenly.** Tight inside a group, looser between groups. Same card size, gap and density everywhere is the sound of no one deciding.
- **Proportions speak.** A 280px sidebar says navigation serves content; 360 says they are peers. If you can't say what a proportion means, change it.
- **Restraint.** About 60/30/10: dominant neutral, secondary tone, roughly 10% accent. Hierarchy through space and tone before lines. Spend boldness in one place, keep the rest quiet, then remove one accessory.

## Spacing

- Every margin, padding, gap and fixed height is a multiple of 4 (scale below). A 2px nudge inside small controls is fine. Replace one-offs like `mt-[13px]`.
- Equal things are equal: one row height and gap per list, one padding per card set. Padding is symmetrical unless content demands otherwise.
- Things line up: icons in one column, labels on one baseline, numbers right-aligned.
- Pages: sections 80–128 apart on desktop, clearly more than any gap inside a section. Apps: page padding 24–32.

## Color

- One neutral ramp tinted toward the world; background, surfaces, borders and text all come from it. Keep one hue across surfaces and shift only lightness. In apps, surfaces stay near-neutral and content carries the color; pages can tint surfaces further.
- Text roles: primary, secondary, muted, plus disabled. Two roles is too flat.
- One accent in the chrome, used rarely: the primary action, selection, the one number that matters. Inside the chosen moments, color can be rich as long as each color means something. A real brand color becomes the accent and leaves the surfaces.
- Contrast: body text and accent-with-text reach 4.5:1, large text 3:1. Darken the accent or put dark text on it if not.
- Semantic colors carry meaning only, toned to the palette and slightly desaturated on dark.
- Running text in full ink. A page set in soft grey reads unfinished.
- No hue-to-hue gradients on surfaces, gradient text, colored glows or shadows, radial washes, blobs or neon borders. A gradient is allowed only as a small tone shift within one neutral, or a neutral scrim under text on a photo.

## Surfaces, borders and depth

- **Choose one depth strategy and commit:** borders only (technical, dense), subtle shadows (approachable), layered shadows (premium), or surface-tone shifts.
- **Elevation is whisper-quiet.** On dark, each step is a couple of points of lightness (the dark ramp: page → card → raised) plus hairlines. On light, surfaces stay light and lift with small soft shadows: resting `0 0 0 1px rgba(0,0,0,.06), 0 1px 2px rgba(0,0,0,.05)`, floating `0 8px 24px rgba(0,0,0,.06)`. Dark lift is a single ring `0 0 0 1px rgba(255,255,255,.08)`.
- **Hairlines:** primary text color at 6–10% opacity (up to 12% on dark). Build a small progression: divider, standard, emphasis, focus ring.
- Sidebar: same as the page, or one step deeper on dark, separated by a hairline, never a different hue. Dropdowns and popovers sit one level above their parent. Inputs are slightly darker than their surroundings: they receive content.
- Squint test: blurred, you still see what sits above what, and nothing jumps out.

## Typography

- Type carries the personality. One family is normal, two is the limit, and if two, clearly distinct. A display face belongs to large headlines only.
- Choose faces for the character, not the faces you reach for on every project. A real brand font stays. The table under Tokens is a starting point, not a default.
- Pick a ratio and step it: about 1.2 for dense UI, 1.25 for most product UI, 1.333 for expressive pages. A 14px base at 1.25: 11 · 14 · 16 · 18 · 22 · 28 · 44. Five sizes on a page is the ceiling.
- Weights 400 and 500; 600 for figures and rare emphasis. No 700–900 headings unless a brand spec says so.
- Sentence case everywhere. No uppercase tracked labels, no italic for emphasis, no single word in a headline set apart by italic, bold or color.
- Letter spacing 0 under 16px; about −0.02em from 40px; −0.03em from 56px. Body line height about 1.5; serif body slightly more.
- Line length 45–75 characters, under 80. Long headlines align left.
- Numbers: `font-variant-numeric: tabular-nums`, one format throughout.
- `text-wrap: balance` on headings, `text-wrap: pretty` on body; `-webkit-font-smoothing: antialiased` on the root.

## Icons

- Every emoji used as an icon or label decoration becomes a line icon from one set (the project's own, else lucide).
- One size and stroke: 16 or 18px, stroke 1.5, in the color of its text role. Same icon box width in every row, 8–10px gap to the label.
- Drop icons that add nothing. A category that needs color gets a small status dot.

## Copy

Words are design content. Ask what the screen needs to say, then say it plainly.

- Write from the person's side: they manage notifications, not webhook config. Describe what something is or does, don't sell it.
- Headlines say what this product does for whom, using facts on the page. Swap in a competitor's name: if it still fits, rewrite it.
- Buttons say exactly what happens ("Save changes", not "Submit"), and an action keeps its name through the flow: "Publish" leads to "Published".
- Errors say what happened and how to fix it, in the interface's voice, without apology or vagueness. Empty states invite the next action.
- Sentence case, active voice, plain verbs, no filler. No exclamation marks, no greeting headlines (`Welcome back, Name! 👋`), no hype words (supercharge, seamless, unlock, magic, game-changing), no `AI-powered` everywhere.
- Short labels: `Search`, not `Search anything...`. A change names its comparison: `+12% vs last month`. Headlines, labels, buttons and toasts take no trailing period; multi-sentence paragraphs keep theirs.
- Never invent proof: no customers, quotes, reviews, logos or statistics. Ask about unverifiable claims; make them specific if real, remove them if not, and list them in the report. Sample content where the brief leaves gaps is fine, plausible, and listed for the client to confirm.

## Structure means something

Outlines, borders, numbering, eyebrows, dividers and labels encode information; they are not decoration. Use `01 / 02 / 03` only for a real sequence. Badges like `PRO`, `New ✨`, `Beta 🚀` go unless they carry real meaning, then become quiet text. Counts and meta are quiet text, not pills. Remove decorative tags that carry no status.

## Layout: pages

- The hero opens with the most characteristic thing in the subject's world, in the most fitting form: a headline, an image, a live demo, an interactive moment. A big number with a small label and a gradient is the default; use it only if it is truly best.
- First screen answers the visitor's first question in large type, carries the page's `h1`, and has one primary action and at most one secondary.
- Strongest hero: one scene image edge to edge with the headline on its calm part, or an asymmetric split with the visual taking at least half. Centered stacks only for short heroes without a visual.
- Navigation: wordmark, the existing links, one button; log in as a text link. No floating pills or glass.
- Each section has a heading, a different composition from its neighbors, and its full content. No dead empty bands; equal outer margins.
- The footer is a designed close, not a sitemap.
- Small screens: stack in reading order and recompose; no text under 11px; no horizontal scroll.

## Layout: app screens

- Keep real app proportions: shell fills the viewport, sidebar 240–280, content fluid and capped near 1440–1600, top bar 56–64. Never shrink an app into a narrow centered column.
- Vary sizes: compact stats above one wide chart, or a wide chart beside a narrow list, never a row of identical cards. The main chart takes at least two thirds of the content width and 280–360 height.
- Stat cards are label, figure and change with its comparison. No sparklines or icons to fill them; don't repeat a figure shown elsewhere.
- Every pattern has many expressions: a metric can be a hero number, an inline stat, a delta, a progress bar or a gauge. Pick the one that tells this data's story.

## Components and states

**Use what exists before making anything.**
1. Controls: native HTML first (`<button>`, `<a>`, `<input>`, `<dialog>`, `<details>`), never `<div onClick>`. For anything stateful (select, combobox, dialog, popover, tooltip, menu, tabs, date picker), use an accessible headless primitive the ecosystem trusts (Radix, React Aria, Ark, Headless UI, or the platform equivalent) and style it. Hand-roll only as a last resort and then owe the full contract: arrow keys, Enter, Escape, focus trap and return, ARIA roles and state, click-outside, scroll lock.
2. Styling: use the project's design system and conventions first; extract a component on the second real reuse; bind to semantic tokens (`bg-card text-muted-foreground`), not literals (`bg-white text-gray-500`); inline utilities only for genuine one-offs.

**States are not optional.** Every control has default, hover, active, focus (visible ring) and disabled; every data view has loading, empty and error. Missing states are the fastest tell of unfinished work.

**Details.**
- Concentric radius: inner = outer − padding, minimum 4, wherever the padding is smaller than the outer radius (circles exempt). Scale: keycaps and tags 4–6, buttons and inputs 8–10, cards 12–16, panels 14–20. Not everything is a pill; buttons are square-ish or fully round, decided once.
- Hit areas 44×44 for touch (40 minimum); extend small controls with a pseudo-element; never overlap.
- Optical alignment when geometric centering looks off.
- Active rows: a small surface step with a hairline, not a glow. Keyboard shortcuts as small keycaps.
- Charts: muted grid and labels, one accent per chart, neutral steps for the other series, type that fits the data (trend = line, comparison = bars, share = stacked bar or list, goal = progress).
- Images: a 1px inset outline at `rgba(0,0,0,.1)` light or `rgba(255,255,255,.1)` dark; fixed dimensions; real alt text.
- Logo: the product name in the main family plus a simple flat mark. No gradient wordmark or sparkle tile.
- Watch CSS specificity: section and element selectors that cancel each other's padding.

## Visuals

- One dominant image beats six small ones. Usually one visual, in the hero.
- Remove filler: blobs, orbs, nebulas, floating cubes, glowing grids, brains, robots, holograms for AI.
- App screens rarely need generated images; their moments come from the product (a careful chart, figures set well, a status that feels alive). Physical objects like a card are better built in code.
- Order of preference: the project's own pictures; generated, if an image tool exists; drawn in code from the subject (its objects, materials, interface); type and color alone. Never a placeholder icon or abstract shape.
- Write the subject as one plain sentence first. Image prompt recipe: subject; simple setting; light and palette (name the page background); one style; composition with calm space for text; exclusions (no text, letters, logos, UI, watermark); aspect at twice display size. Don't ask a model for grain or paper texture; add texture in code.
- Before any paid generation, show the prompt, model and size and ask. Run once, judge, change the prompt instead of rerolling.
- Previews look like the real app with plausible data. A cropped, working interface fragment is the strongest picture a software page has. Build it in Demo mode.
- WebP or AVIF at 2x, edges matched to the page color, nothing laid over a headline.

## Motion

Motion is felt, not watched. These rules are for the product's own UI. A demo is the exception: its storytelling motion is watched on purpose and follows Demo mode's pace and easing.

- **Should it animate at all?** Actions repeated many times a day (shortcuts, command palette) get none. Occasional surfaces (menus, modals, toasts) get standard motion. Motion that answers an action and shows what changed is welcome; ambient motion is not.
- On load, at most one orchestrated moment: a short fade with a 6–12px rise, staggered 40–60ms over at most six items. No fade-up on every section, no hover transition on every card.
- **Easing, by job.** Entering and interactive motion: `cubic-bezier(0.22, 1, 0.36, 1)`, or web-motion's `--ease-out`, `cubic-bezier(0.23, 1, 0.32, 1)`, which never differs from it by more than 1.1% of the travel; pick one per project. Movement across the screen: `cubic-bezier(0.77, 0, 0.175, 1)`. Drawers and sheets: `cubic-bezier(0.32, 0.72, 0, 1)`. Constant motion (spinners, progress): `linear`. The gate accepts exactly these; keyword easings (`ease`, `ease-out`) fail it even where web-motion allows them. Never `ease-in`.
- Durations (as web-motion §3.4): hover 100–150ms; press 100–160; tooltips 125–200; menus 150–250; card and list entrances 200–300; modals 200–300; drawers and sheets 300–500; up to 500 only for the one on-load moment.
- Press feedback `scale(0.97)` on `:active`. Nothing appears from `scale(0)`: start at 0.95 and opacity 0. Popovers scale from their trigger; modals from center.
- Transition only named properties (color, background, border, opacity, transform). Never `transition: all`, never width, height, top, left or margins. Changed numbers may tween.
- Remove pulse, ping, shimmer, breathing glows, floating, parallax, bouncy springs and `hover:scale` on cards.
- Respect `prefers-reduced-motion`: keep opacity and color, drop travel.

## Quality floor (every build, unannounced)

Responsive to phone width, visible keyboard focus, keyboard-operable controls in reading order, accessible names (visible label or `aria-label`), alt text, 4.5:1 text contrast, reduced motion respected, existing flows still working.

---

# Tokens

**Spacing scale:** 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128. Inside a control 4–12; related items 4–8; between groups 12–24; between sections 32–64 (pages 80–128). Rows 32 compact, 36 default, 40–44 touch. Hero: 96–128 from nav to headline on desktop, 48–64 on phone. Card padding 20–24, compact panels 16.

**Neutral ramps.** Apps: graphite. Pages: tint toward the world (warm = paper, wood, food, craft; ink = night, sky, water, technical).

| Dark role | Graphite | Warm | Ink |
| --- | --- | --- | --- |
| Deepest (inputs) | #0f0f10 | #12110f | #07080d |
| Page | #141415 | #161513 | #0b0d14 |
| Card | #19191b | #1c1a18 | #11141c |
| Raised (active row, hover) | #232325 | #262421 | #1a1e28 |
| Primary text | #ededed | #efe9de | #eef0f5 |
| Secondary text | #a1a1a6 | #aaa398 | #a3a9b8 |
| Muted text, icons | #85858b | #8a847a | #7a8296 |

| Light role | Graphite | Warm | Ink |
| --- | --- | --- | --- |
| Page | #fafafa | #f7f4ee | #f5f7fa |
| Card | #ffffff | #fdfbf7 | #ffffff |
| Raised | #f4f4f5 | #efe9df | #eceff4 |
| Primary text | #171717 | #1f1b16 | #111827 |
| Secondary text | #525252 | #5e554a | #4b5565 |
| Muted text, icons | #737373 | #7b7266 | #6b7487 |

On light, "raised" (active rows, hover) is a step darker than the card. Inputs sit slightly darker than their surface on both themes: "deepest" on dark, "raised" on light.

Semantic: positive `#4cc38a` dark / `#16a34a` light; negative `#e5484d` dark / `#dc2626` light. Muted text only for meta and captions, near 4.5:1 on its surface.

**Accent:** a real brand color, or one from the world (warm: amber, coral, ember; cool: cobalt, teal, sky; natural: moss, sage). At most about 10% of the screen on a page, far less in app chrome. Avoid purple-blue unless the brand is purple.

**Buttons:** hero 44–48 tall, nav 32–36 (44 at touch widths), side padding 16–20. Primary on light: primary-text fill with white text, or the accent. On dark the primary can be off-white with dark text. Secondary: raised surface with a hairline.

**Type scale (product UI):**

| Use | Size | Line height | Weight |
| --- | --- | --- | --- |
| Labels, meta, counts | 12 | 16 | 400 |
| Secondary text, captions | 13–14 | 20 | 400 |
| Body, nav items | 14–16 | 20–24 | 400–500 |
| Wordmark | 16–18 | 1 | 500–600 |
| Hero subhead | 18–20 | 28–30 | 400, max 36rem wide |
| Card figures | 28–32 | 1 | 500–600, tabular |
| Page title | 28–36 | 1.15 | 400–500 |
| Hero headline | 56–72 desktop, 36–44 phone | 1.02–1.08 | 400–500 |

Pages may push the headline larger; body text on pages is 16–20px.

**Type starting points by character:**

| Character | Interface | Optional partner |
| --- | --- | --- |
| Precise, technical, calm | Geist, IBM Plex Sans | Geist Mono or IBM Plex Mono, for real code and figures only |
| Warm, friendly, human | Instrument Sans, DM Sans, Figtree | Instrument Serif or Newsreader for hero headlines |
| Editorial, crafted | Instrument Sans | Newsreader, Instrument Serif, Fraunces for headlines |
| Playful, bold | Space Grotesk, Bricolage Grotesque | none needed |

---

# Component gates

Every component passes its own gate before you build the next one. A failed gate is fixed now, not collected for the end: problems compound, and a page of individually passing components is the only page that passes as a whole.

**Mark components.** Put `data-component="<type>"` on each component's root (types below). Optional `data-name` gives it a readable name in the log. A data view whose content changes (search results, a filtered list, a chart fed by data) also gets `data-dynamic` and `data-states="empty"` (add `loading error` when data arrives asynchronously), and each state's element carries `data-state="empty" data-state-for="<view id>"`, even while hidden.

| Type | Use for | Gate adds to the universal checks |
| --- | --- | --- |
| `button` | Buttons and button-styled links | Height ≥32; hover, focus and keyboard activation |
| `link` | Text and nav links | Hover and focus (links inside a sentence are exempt from target size) |
| `input` | Text, search, number, date fields | A real label, not only a placeholder; hover and focus |
| `checkbox` | Checkboxes, radios, switches | Label counts as the target; hover on the control or its label |
| `select`, `tabs` | Menus, comboboxes, tab lists | Name, focus, keyboard |
| `control` | Anything custom and interactive | Name, focus, hover, and Enter must change something |
| `nav` | Navigation regions | A `<nav>` landmark |
| `table`, `list`, `chart` | Data views | Header `scope` on tables; with `data-dynamic`, an empty state that exists |
| `status` | Toasts, live result panels, inline status | Announced through a live region |
| `image` | Pictures | `alt` plus fixed `width` and `height` |
| `card`, `stat`, `block` | Static containers, figures, sections | Universal checks only; `stat` figures need tabular numbers |

**Universal checks (every component, at 1440 and 390 wide):** text contrast 4.5:1 (3:1 at 24px+ or 18.66px bold); padding, gaps and vertical margins on the 4px grid; radii from the scale; concentric radius (applies when the parent padding is smaller than its radius; circles exempt); transitions only on named properties with a curve Motion names (or `linear` for constant motion) and 100–500ms; no raw color literals in the component's CSS rules (tokens only); fits the viewport without overflow; tabular figures on numbers. Interactive types add: accessible name, keyboard focusable, visible focus change, hover change (desktop), target ≥24px, and ≥44px at touch widths.

**Judgment half of the gate.** The script can't judge intent. Before marking a component done, write its line from Build step 6 (intent, hierarchy, palette, depth, type, spacing, each with a why). A component passes when the script passes and every why is answerable.

**Gate log.** Keep one line per component in working notes and report the totals: `button  See what's on the board  14/14 PASS`. Never report a gate as passed if the script didn't run; if no browser is available, say so and fall back to screenshots and the checklist.

**Run it headless.** Write the script below to `gate.js`, then:

```bash
npm i playwright && npx playwright install chromium   # skip if Playwright is already installed
node gate.js path/to/page.html                         # or a URL; --widths 1440,768,390 to add widths
```

It opens the page in headless Chromium, hovers, focuses, tabs and presses Enter on each marked component, and measures the results. Exit code 1 means a component failed. For a dev server, gate the production build too: bundlers change what ships.

Two checks need care when reading results. Hover is read 250ms after the pointer arrives, so transitions longer than that read as missing. "Works by keyboard" only proves Enter changed the DOM; confirm the change was the right one.

```js
// Component gate. Usage: node gate.js <url-or-html-path> [--widths 1440,390]
// Checks every element marked data-component="<type>" in a real browser.
// Exit code 1 if any component fails. Requires Playwright (require('playwright')).
const { chromium } = require('playwright');
const path = require('path');
const args = process.argv.slice(2);
const target = args[0];
const widths = (args.includes('--widths') ? args[args.indexOf('--widths') + 1] : '1440,390').split(',').map(Number);
const url = /^https?:|^file:/.test(target) ? target : 'file://' + path.resolve(target);

const INTERACTIVE = ['button', 'link', 'input', 'checkbox', 'select', 'tabs', 'control'];
const RADII = [0, 4, 6, 8, 10, 12, 14, 16, 20];
const EASES = ['cubic-bezier(0.22, 1, 0.36, 1)', 'cubic-bezier(0.23, 1, 0.32, 1)', 'cubic-bezier(0.77, 0, 0.175, 1)', 'cubic-bezier(0.32, 0.72, 0, 1)']; // ease-out (this skill, web-motion), ease-in-out, drawer
const MOTION_PROPS = ['color', 'background-color', 'border-color', 'opacity', 'transform', 'box-shadow', 'outline-color', 'text-decoration-color'];

function lum(c) {
  const m = c && c.match(/rgba?\(([^)]+)\)/); if (!m) return null;
  const [r, g, b, a = 1] = m[1].split(/[ ,/]+/).filter(Boolean).map(Number);
  const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
  return { L: 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b), a };
}
const ratio = (a, b) => { const x = lum(a), y = lum(b); if (!x || !y) return 99; const [h, l] = x.L > y.L ? [x.L, y.L] : [y.L, x.L]; return (h + 0.05) / (l + 0.05); };

(async () => {
  const browser = await chromium.launch();
  const rows = []; let failed = 0;
  for (const w of widths) {
    const page = await browser.newPage({ viewport: { width: w, height: 900 }, hasTouch: w < 600 });
    await page.goto(url); await page.waitForTimeout(600);
    const count = await page.$$eval('[data-component]', (e) => e.length);
    for (let i = 0; i < count; i++) {
      const el = (await page.$$('[data-component]'))[i];
      if (!(await el.isVisible()) || await el.evaluate((e) => !!e.closest('[data-stage]'))) continue; // components inside a demo stage are illustration
      const info = await el.evaluate((e, { RADII, EASES, MOTION_PROPS }) => {
        const type = e.dataset.component, cs = getComputedStyle(e), r = e.getBoundingClientRect();
        const id = e.dataset.name || e.id || (e.getAttribute('aria-label') || e.textContent || type).trim().replace(/\s+/g, ' ').slice(0, 32);
        const all = [e, ...e.querySelectorAll('*')].filter((n) => !n.closest('svg, [data-stage]') || n === e); // a demo stage is an illustration, not UI
        const bgOf = (n) => { for (; n; n = n.parentElement) { const b = getComputedStyle(n).backgroundColor; if (!/rgba\(0, 0, 0, 0\)|transparent/.test(b)) return b; } return 'rgb(255, 255, 255)'; };
        const name = (e.getAttribute('aria-label') || (e.getAttribute('aria-labelledby') || '').split(' ').map((x) => document.getElementById(x)?.textContent || '').join(' ') ||
          (e.labels && [...e.labels].map((l) => l.textContent).join(' ')) || e.getAttribute('alt') || e.getAttribute('title') || e.textContent || '').trim();
        const texts = all.filter((n) => [...n.childNodes].some((c) => c.nodeType === 3 && c.textContent.trim()) && getComputedStyle(n).visibility !== 'hidden')
          .map((n) => { const s = getComputedStyle(n); let op = 1; for (let p = n; p; p = p.parentElement) op *= +getComputedStyle(p).opacity; return { fg: s.color, bg: bgOf(n), fs: parseFloat(s.fontSize), fw: +s.fontWeight, op, t: n.textContent.trim().slice(0, 20) }; });
        const offGrid = [];
        all.forEach((n) => { const s = getComputedStyle(n); for (const p of ['paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'rowGap', 'columnGap', 'marginTop', 'marginBottom']) { const v = parseFloat(s[p]); if (v > 2 && v % 4) offGrid.push(`${p}=${s[p]}`); } });
        const badRadius = [], concentric = [];
        all.forEach((n) => { const s = getComputedStyle(n); const rad = parseFloat(s.borderTopLeftRadius); if (rad > 0 && !RADII.includes(Math.round(rad)) && rad < Math.min(n.offsetWidth, n.offsetHeight) / 2 - 1) badRadius.push(Math.round(rad));
          const p = n.parentElement; if (n !== e && p && e.contains(p) && rad > 0) { const ps = getComputedStyle(p), pr = parseFloat(ps.borderTopLeftRadius), pad = Math.min(parseFloat(ps.paddingTop), parseFloat(ps.paddingLeft)); const circle = rad >= Math.min(n.offsetWidth, n.offsetHeight) / 2 - 1; if (!circle && pr > 0 && pad > 0 && pad < pr && rad > Math.max(4, pr - pad) + 2) concentric.push(`${Math.round(rad)}>${pr}-${pad}`); } });
        const motion = [];
        all.forEach((n) => { const s = getComputedStyle(n); if (parseFloat(s.transitionDuration) > 0) { s.transitionProperty.split(',').map((x) => x.trim()).forEach((p) => { if (!MOTION_PROPS.includes(p)) motion.push('prop ' + p); });
          s.transitionTimingFunction.split(/,(?![^(]*\))/).map((x) => x.trim()).forEach((f) => { if (!EASES.includes(f) && f !== 'linear') motion.push('ease ' + f); });
          s.transitionDuration.split(',').map(parseFloat).forEach((d) => { if (d * 1000 < 100 || d * 1000 > 500) motion.push('dur ' + d + 's'); }); } });
        const literals = [];
        for (const sheet of document.styleSheets) { let rules; try { rules = sheet.cssRules; } catch { continue; }
          for (const rule of rules) { if (!rule.selectorText) continue; let hit = false; try { hit = all.some((n) => n.matches(rule.selectorText.replace(/:(hover|active|focus-visible|focus|checked|disabled)/g, ''))); } catch {} if (!hit) continue;
            for (const prop of ['color', 'background-color', 'background', 'border-color', 'border', 'box-shadow', 'outline-color']) { const v = rule.style.getPropertyValue(prop); if (v && /#[0-9a-f]{3,8}\b|rgba?\(/i.test(v) && !/var\(/.test(v)) literals.push(`${rule.selectorText} ${prop}`); } } }
        const tag = e.tagName.toLowerCase();
        const focusable = e.tabIndex >= 0 || ['a', 'button', 'input', 'select', 'textarea'].includes(tag);
        const labelBox = (e.labels && e.labels[0]) ? e.labels[0].getBoundingClientRect() : r;
        const inlineInText = tag === 'a' && cs.display === 'inline' && e.parentElement && e.parentElement.textContent.trim().length > e.textContent.trim().length + 10;
        const numericNodes = all.filter((n) => n.children.length === 0 && /\d/.test(n.textContent) && /^[\d\s$%.,:–\-ampmMonTueWedThuFriSatSunNovOctDecJanfbt]+$/.test(n.textContent.trim())).map((n) => getComputedStyle(n).fontVariantNumeric);
        return { type, id, name, w: Math.round(Math.max(r.width, labelBox.width)), h: Math.round(Math.max(r.height, labelBox.height)), texts, offGrid, badRadius, concentric, motion, literals: [...new Set(literals)],
          focusable, inlineInText, tag, role: e.getAttribute('role'), hasLive: !!(e.getAttribute('aria-live') || e.querySelector('[aria-live],[role=status]') || e.closest('[aria-live]')),
          scope: tag === 'table' ? [...e.querySelectorAll('th')].every((t) => t.getAttribute('scope')) : true, numeric: numericNodes,
          states: (e.dataset.states || '').split(/\s+/).filter(Boolean).map((s) => ({ s, ok: !!document.querySelector(`[data-state="${s}"][data-state-for="${e.id}"]`) })),
          dynamic: e.hasAttribute('data-dynamic'),
          imgAlt: tag === 'img' ? e.hasAttribute('alt') && e.hasAttribute('width') && e.hasAttribute('height') : true,
          right: r.right, left: r.left, scrollOver: e.scrollWidth > e.clientWidth + 1 && !['table'].includes(tag) && cs.overflowX === 'visible' };
      }, { RADII, EASES, MOTION_PROPS });

      const checks = [];
      const add = (k, ok, d = '') => checks.push({ k, ok, d });
      const isInter = INTERACTIVE.includes(info.type);
      // universal
      const lowC = info.texts.filter((t) => t.op > 0.99 && ratio(t.fg, t.bg) < ((t.fs >= 24 || (t.fs >= 18.66 && t.fw >= 700)) ? 3 : 4.5));
      add('contrast', !lowC.length, lowC.map((t) => `${t.t} ${ratio(t.fg, t.bg).toFixed(2)}`).join('; '));
      add('4px grid', !info.offGrid.length, info.offGrid.slice(0, 3).join(' '));
      add('radius scale', !info.badRadius.length, info.badRadius.join(','));
      add('concentric radius', !info.concentric.length, info.concentric.join(' '));
      add('motion rules', !info.motion.length, [...new Set(info.motion)].slice(0, 3).join(' '));
      add('tokens only', !info.literals.length, info.literals.slice(0, 2).join(' | '));
      add('fits viewport', info.left >= -1 && info.right <= w + 1 && !info.scrollOver);
      if (info.numeric.length) add('tabular figures', info.numeric.every((v) => /tabular-nums/.test(v)));
      // interactive
      if (isInter) {
        add('accessible name', !!info.name);
        add('keyboard focusable', info.focusable);
        add('target ≥24px', info.inlineInText || (info.w >= 24 && info.h >= 24), `${info.w}×${info.h}`);
        if (w < 600 && !info.inlineInText) add('touch target ≥44px', info.w >= 44 && info.h >= 44, `${info.w}×${info.h}`);
        const style = () => el.evaluate((e) => [e, ...(e.labels || [])].map((n) => { const s = getComputedStyle(n); return [s.outlineStyle, s.outlineWidth, s.boxShadow, s.backgroundColor, s.color, s.borderColor, s.textDecorationLine, s.textDecorationLine === 'none' ? '' : s.textDecorationThickness].join('|'); }).join('||'));
        await page.mouse.move(0, 0); await page.keyboard.press('Escape'); const base = await style();
        await page.keyboard.press('Shift'); await el.focus(); await page.waitForTimeout(250); const foc = await style(); await el.evaluate((e) => e.blur()); await page.waitForTimeout(250);
        add('focus visible', foc !== base);
        if (!(w < 600)) { await el.hover().catch(() => {}); await page.waitForTimeout(250); const hov = await style(); await page.mouse.move(0, 0); add('hover state', hov !== base); }
        if (['button', 'control'].includes(info.type)) {
          await el.focus();
          await el.evaluate(() => { window.__gateMut = false; const o = new MutationObserver(() => { window.__gateMut = true; o.disconnect(); }); o.observe(document.body, { subtree: true, childList: true, attributes: true, characterData: true }); });
          await page.keyboard.press('Enter'); await page.waitForTimeout(150);
          add('works by keyboard', info.tag === 'a' || await page.evaluate(() => window.__gateMut));
          if (info.tag === 'a') await page.goBack().catch(() => {});
          await page.goto(url); await page.waitForTimeout(300);
        }
      }
      // type-specific
      if (info.type === 'input') add('label, not just placeholder', !!info.name);
      if (info.type === 'button') add('height ≥32', info.h >= 32, `${info.h}`);
      if (info.type === 'table') add('header scope', info.scope);
      if (['table', 'list', 'chart'].includes(info.type) && info.dynamic) add('empty state exists', info.states.some((s) => s.s === 'empty' && s.ok), info.states.map((s) => s.s + (s.ok ? '' : ' missing')).join(','));
      if (info.type === 'status') add('announced (live region)', info.hasLive);
      if (info.type === 'image') add('alt + fixed size', info.imgAlt);
      if (info.type === 'nav') add('landmark', info.tag === 'nav' || info.role === 'navigation');

      const pass = checks.every((c) => c.ok); if (!pass) failed++;
      rows.push({ w, type: info.type, id: info.id, pass, fails: checks.filter((c) => !c.ok).map((c) => c.k + (c.d ? ` (${c.d})` : '')), n: checks.length });
    }
    await page.close();
  }
  await browser.close();
  const seen = new Set();
  for (const r of rows) { const key = r.w + r.type + r.id; if (seen.has(key)) continue; seen.add(key);
    console.log(`${r.pass ? 'PASS' : 'FAIL'}  ${String(r.w).padEnd(5)} ${r.type.padEnd(8)} ${r.id.padEnd(32)} ${r.n - r.fails.length}/${r.n}${r.fails.length ? '  ✗ ' + r.fails.join('; ') : ''}`); }
  console.log(`\n${rows.length - failed}/${rows.length} component checks passed`);
  process.exit(failed ? 1 : 0);
})();
```

# Build mode

1. **Read the project and brief.** Stack, existing tokens and components, `.design/system.md`, brand assets, what imagery truly exists. Plan only around assets you have.
2. **Direction.** Intent, domain exploration, Direction block. Confirm (see Direction for when to skip).
3. **Plan.** A compact token plan: palette as 4–6 named hex values; typefaces and roles; a layout concept in one sentence plus an ASCII wireframe, with alignment; three or four principles specific to this brief.
4. **Review the plan against the brief.** Mentally run a similar prompt: wherever you would land in the same place, the plan is defaulting. Revise those parts and say what changed and why.
5. **Build, still, one component at a time.** Tokens first as CSS custom properties, then the focal element or hero at desktop and phone width, then each section or panel from the plan with real content, then states, then motion. A design that needs animation to look finished isn't finished. Mark each component with `data-component` as you write it and run its gate (see Component gates) before starting the next.
6. **State before each component** (in working notes, not to the user):
   ```
   Intent · Hierarchy (focal element and how it wins) · Palette (and why) · Depth (and why)
   Surfaces · Typography (face, size/weight/color levers) · Spacing (base, density)
   ```
   If you can't give a why for each, you're defaulting.
7. **Check** (see Checks): every component gate passing at 1440 and 390, then the whole-page checks. Then offer to save the decisions.

# Polish mode

Keeps the product: features, content and section order stay. What changes is that every size, color, word and image becomes deliberate.

1. **Look.** Find the files that render the screen. Render it and screenshot at desktop and phone widths when you can. Only a live URL: rebuild the page as one static HTML file and say in the report that it's a redesign to hand to the site's owner. Only a screenshot: rebuild it as static HTML first and treat that as the original.
2. **Audit.** Walk the Signs list below; write every sign found, one line each, with its location.
3. **Decide depth.**
   - Heavy slop (many signs across color, type, icons, copy): full process.
   - Light slop (mostly designed, a few signs): fix only what the audit found, take direction from the existing brand, keep palette, type, layout and visual; bigger ideas go in the report.
   - No slop: say so and suggest two or three refinements with exact values; apply only if the user agrees.
4. **Direction.** Show the audit and Direction block; wait for an answer (same skip rules).
5. **Nine passes, in order,** each finished across the whole screen before the next: spacing, color, icons, copy, type, layout, details, visuals, motion. Each pass applies the matching Craft section.
6. **Check.** Mark the components and run their gates; every one passes. Then run the Checks, render again, compare with the audit, and re-run any flows (forms, menus, links) so polish didn't break function.
7. **Report:** the direction, a few lines per pass, any image prompt written, sample content to confirm, unverified claims found, and brand conflicts.

Don't: rename the product (keep a real logo; redraw a slop logo flat), change features, content or order unless asked, invent features, claims or data, replace removed decoration with new decoration (glass, grain, noise, neon, bento), or give every product the same look.

## Signs of slop (audit list)

- **Surfaces and color:** purple-blue or violet-pink gradients on backgrounds, cards, buttons or nav; gradient text; colored glows and shadows; radial washes and blurred blobs; neon borders; glass cards with colored shadow; many near-identical text tints; everything highlighted.
- **Type:** 800–900 headings; UPPERCASE TRACKED LABELS; too many sizes and weights; mixed number formats; negative tracking on small text; italic emphasis; one accent word in a headline.
- **Icons:** emoji as nav, labels or status (🏠 📥 🚀 💰 ⚠️ 📈 🔥 ✨); emoji in pills and counts; icons in many sizes and colors or off their column.
- **Spacing:** arbitrary values (13, 7, 11, 31); rows of different heights or gaps; groups closer to neighbors than to their own items; uneven sibling padding; big gap above, cramped below.
- **Copy:** greeting headlines; exclamation marks; changes without a reference; wordy placeholders; hype words; trailing periods on short strings; fake-looking data (`$123,456`, `[X]`); unsourced social proof.
- **Components:** glowing pills for counts and plans; PRO/New/Beta badges everywhere; everything a full pill; rainbow or glowing chart bars; every chart in accent shades; sparklines on every stat card; equal cards side by side; gradient-tile logo with sparkle; decorative tags that carry no status.
- **Pages:** pill badge above the headline (`✨ Introducing X 2.0`); a headline that fits any product; shimmer; floating blobs and glowing lines; everything stacked and centered; three or more buttons under the hero; emoji feature cards with vague lines; a visual on every section.
- **Visuals:** glossy 3D blobs, chrome shapes, nebulas; robots and brains for AI; text or fake UI baked into images; hard image edges on a different background.
- **Motion:** pulse, ping, breathing glows on things that aren't live; `transition-all`; `hover:scale`; bouncy springs; elements flying in from different directions; animated layout properties.
- **Template look** (what cleaned-up screens fall back to): pure grey page, Inter, white text and the old brand color on one button for a warm product; a generic hero visual; the same layout and palette as every other product.

# Demo mode (faux product UI)

Miniature product UI: a believable interface, framed in its space, as one still or a short animation in which one thing happens. The viewer recognizes the screen and sees the thing happen. These are authored illustrations, not browser automation: the script draws the cursor pressing and changes the scene. The Craft rules and Tokens still hold; this section adds what a product shot needs and overrides Motion where they differ.

**The one idea:** it reads as a real product, simplified to what the viewer needs, framed with intent, and every motion has a cause.

Five ways it fails:
- **Too much.** Real text in every row, numbers everywhere, everything packed. The more detail, the more it looks generated.
- **Wireframe.** Two gray blobs and a button. Built too small, or stripped of what made it recognizable.
- **Boxed.** A whole window shrunk into a card with even margins: a screenshot pasted in, not a product shot.
- **Flat.** Every object the same weight in the same bordered card. The eye has nowhere to land.
- **Bland.** A gray window with a cursor, whatever the brief said. The brief's look and energy (a blueprint, glass over color, a Dynamic Island, a mascot) are the point; build what it asks for, to these rules.

The fix: a full, structured screen in quiet grays, real words only on what the story is about, placeholder bars for the rest, room to breathe, a crop that puts the eye where the story is. Simplify the words, not the context. An empty corner, a void under a list, rows spread to fill a pane, a window floating on a plate: unfinished, not calm.

**How hard to press.** Build it like a launch page you will be judged on. Then look at the frame as the most exacting designer you know would, the one who screenshots the one wrong thing and sends it back with "what is this?": a dot off its avatar, a unit on its own line, copy touching a card. If you can picture that screenshot, you have found the next fix.

## The Stageshow kit

When it is available, use it: React parts (`Stage`, `Window`, `Phone`, `Row`, `Bar`, `Text`, `Roll`, `Count`, `Collapse`, `Fly`, `Connector` and more, with an `Act` script API), about 70 gold examples and product studies, and `scripts/film.mjs`, which films a contact sheet and flags framing and motion faults. Look for a `stageshow` skill folder or a `kit/` with `stageshow.css` in the project. Otherwise, with network access, install it (`npx skills add benjitaylor/skills --skill stageshow`) or clone `https://github.com/benjitaylor/skills` and work from `stageshow/`. Then its `SKILL.md`, `references/` and the closest gold example are the detailed rules; this section is the summary. Installing it runs that repo's own package scripts, which a sandbox may block. Without the kit, build in plain React or HTML and CSS by the rules below and film with the script under Filming without the kit.

## Run

Most of the quality is decided before any code. Write the plan first: where it sits, the focal object, the action, the payoff, what can be left out.

1. **Medium and place.** Still or animation (loop, once in view, or on hover). The page, its ground, its width. Design at the size it will be seen and show it at 1:1: about 720 × 340 for a hero beside copy, 900 to 1100 wide for a full-width hero, 400 × 300 for a card. Never under about 320 wide for a demo; a bento tile or satellite card may be smaller. Anything that can sit in a phone column gets a compact design at 358 wide: a redesign (closer crop, satellite dropped or stacked), not a squeeze.
2. **Look.** With the product's code or site at hand, take its real tokens, icons, chrome and words. With none, run Direction for it. Pick a fidelity: minimal (all bars), standard (words where they carry meaning, bars elsewhere, the default), realistic (real content everywhere; for hero scale, a named real product, or a still whose subject is a list or page). A brief with a style (kawaii, paper, a poster color) gets that style in full, still built to these rules.
3. **The story.** Pick its shape from what the product is valued for: how it feels to use (a cursor does one satisfying thing and the result appears under its hand), a flow (a few screens told as one continuous object, payoff on the last), or what the system does (the consequence lands somewhere else, the link visible, usually no cursor). Three to five beats and a payoff, 10 to 16 seconds. Between a richer story and a calmer frame, choose the frame.
4. **Start from a gold, then frame it.** With the kit, film the closest gold example and copy its folder as the start; keep its stage size, crop, row and type sizes, spacing and beats, then replace its look and content with the brief's product. A copy that only changes the name is not done. Without the kit, pick a layout from the table below and hold yourself to it the same way. Frame before any motion: film one still at both widths; if it is emptier, flatter or more boxed than it should be, fix the frame first.
5. **The screen.** Count the real strings, usually 3 to 7: a budget for words, not elements. Fit every control's text before it moves. Measure what the cursor touches from the DOM; never hard-code positions.
6. **Choreograph.** Keep what appears mounted and toggle it so exits animate. Animate the relationship, not just the object: a new row carries the rows below it; a resizing surface never stretches its text. Beats overlap, groups stagger, the payoff holds, the loop ends where it began or resets with a visible cause.
7. **Rehearse.** Set the poster frame first: the beat that tells the story on its own, never one caught mid-change, the result left on screen. Then film the loop, not only a still: a contact sheet at the shown width and at 390, and step frame by frame through every press, menu, morph and the loop seam. A still can't show a pop. Fix the largest visible fault first (framing, then hierarchy, then motion, then polish) and re-film. Ask: what does the eye land on first, and is it the result? Is one window, tile or device clearly leading? Any no is the largest fault. A passing script is necessary, not sufficient. Hand over with a short note: the gold or layout you started from, what you changed, what you did not check.

## Framing

- **One hero object, at most one or two satellites** (a receipt, a phone, a detail card) that carry the point. Keep what identifies the product: a title, the real chrome, the rows that give the action a reason. Logo and nav are optional.
- **Crop only filler.** The payoff, the action, what the cursor touches and every real word stay whole. A placeholder action the crop would slice is removed, not sliced. A button, chip or shadow sliced by the stage edge is the usual fault.
- **Crop 10 to 40% of the hero off stage.** The window or phone fills at least two thirds of the stage's width and runs off an edge. The stage masks everything (`overflow: hidden`).
- **The page is the ground.** On a white or dark page, no plate behind the window and no window whole with air on four sides; that floats. Unframed (whole, centered, an even margin at least as deep as the shadow) only when the developer asks.
- **One gutter,** measured in the final crop: every edge distance matches it, a full gutter or well past. Crossing it by under 24px or stopping a few pixels short is a mistake.
- **Satellites straddle the hero's edge, about half outside,** over chrome (a sidebar, header or margin), never over content. Two satellites are two kinds and sizes (a card and a notification at true size), never two equal cards stacked. Anchored UI (popover, menu, toast) is not a satellite: it sits where the product puts it.
- **A window keeps its device's shape:** whole at 1.25:1 or wider; bled, what shows is at least square. Fix by crop, never by squashing.
- **What the story opens stays in frame,** a gutter from every edge on every frame; place the trigger so the overlay has room. No dead corners at rest or anywhere in the loop.
- **Start flat and frontal.** Depth from shadow, z-order, scale and opacity; tilt only where it earns its keep (a loose pile of paper), perspective only when asked.
- **Phones:** a satellite phone starts at 40% of the window's visible width and at least 220px; let it run off the bottom rather than shrink. Notifications stay at true iOS proportion and are never cut. A phone cropped at the top loses its status bar and nav bar together. Never draw a status bar or home indicator by hand; take the frame from the kit or a real reference.

| Layout | Hero | Use for |
| --- | --- | --- |
| Pinned, bottom bleed | Inset 8–12% left, right and top; 15–35% past the bottom | Feature cards and bento tiles |
| Corner bleed | Inset 10% top and left; 15–35% past right and bottom; satellite on the left or bottom edge | Heroes beside copy |
| Stage with gutters | Inset 8–20% each side on a colored stage, off the bottom | Brand moments |
| Satellite focus | Hero cropped hard; a large satellite (30–40% of hero width) carries the story | One small thing: a notification, a receipt, a diff |
| Wide hero | A 900–1100px window at 1:1, off the bottom; realistic fidelity | Homepage heroes at full width |
| Device pair | Desktop 75–80% wide, off the bottom; phone straddling the right edge, a third outside | Cross-device stories |
| Many of one | A grid of one thing off every edge; one tile in focus by depth, the only one with words | Scale shown as repetition |
| Fade crop | Window inset top and sides, masked out over its last third, filler only under the fade | When an edge would cut the window at an arbitrary line |
| Close-up | The whole window at 1.3–1.6x, chrome and all, the subject row whole | A card about one control |
| Panel over product | A settings panel over the product's margin, one neutral leader to what it changed | A setting and its effect |
| Opposite corners | Copy bottom-left; the product hung from the top-right corner | Bento tiles with a line of copy |

A bento grid is one set: one hero tile, then a window, a stat, an object and a diagram, each a different kind; plan the grid before any tile.

## The still frame

- **Restraint.** Real strings on the title, the thing acted on, what is typed, the result; the rest is bars. Bars are filler at the edges; bars where the eye lands read unfinished. Where the story touches a list, two or three real rows. In a small surface a row is one line: avatar, name, value. Placeholder widths vary row to row (60, 45, 70, 52). Label and value match: both words or both bars. One number gets to be big. Say the feature's signal once, not in header, satellite and every row.
- **Keep the domain's signature content:** album art, thumbnails, avatars (each named avatar its own color). Swapped out, it is a generic list.
- **No masthead for a fictional name** and no product name on screen unless the brief leans on it and the real product would show it there. A faux app's title is a `div`, never `h1` to `h6`: the demo lives inside someone's page outline.
- **Type:** real 11 to 15px UI sizes, scaled by the stage, never 7px. Small text line height at least 1.3. Monospace only for code, identifiers and aligned numbers.
- **Spacing:** words keep a 12px inset from any window, card, panel or hovered-row edge (never under 8); bars may bleed, words do not. Row padding 12px, 8 for a dense list. A title over its subtitle sits 4 to 6px apart. A button keeps 8px or more from the field above it. No near-tangents: edges 1 to 3px apart read as accidents; align exactly or part by at least 8.
- **Optical centering:** center a label on its letters (`text-box: trim-both cap alphabetic`) in pills, buttons and avatars. A centered amount centers its digits, with the currency sign hung outside at `right: 100%`.
- **Icons come from a set, never your hand:** the product's own pack first, else one set chosen on purpose (SF-style for Apple chrome, Material Symbols for Android, else Phosphor, Iconoir, Radix, Tabler, Heroicons or Lucide), one size (14–16px) and stroke per scene, filled at 14px and under. Emoji are content, never icons. Other products' logos are their real marks in original proportions, never a look-alike.
- **AI features:** no sparkle, wand or star and no purple as the AI color; show what the AI does (the question sent, thinking, the answer streaming in with its height, sources last). The product's own icon is fine even if it is a sparkle.
- **No invented logo:** a letter in a colored square is not a mark. Use the real mark or a plain text wordmark.
- **Color:** one neutral family for window, sidebar and cards; five inks and one accent to start. Don't outline the hero with an accent ring to point at it; lift it the way the product would. Nothing translucent overlaps. On dark, depth comes from a lighter surface, not shadow.
- **Chrome:** a desktop app gets its real chrome; browser chrome only when the browser is part of the picture. Never draw platform chrome from memory; look at the real app or a screenshot. Sidebar columns run the full height of their window. A messaging app on an iPhone keeps Messages' conventions unless the brief gives it a look.

## Demo motion

Storytelling motion (the cursor, rolls, flights, staggered dependents) follows these rules instead of the Motion section and web-motion's 300ms component budget, 50ms shared-trigger rule, 30–80ms stagger and 500ms cascade cap. UI feedback inside the demo (hover, press, a toggle, a toast) keeps those rules and the product's own timing.

- **Two curves.** Travel `cubic-bezier(0.45, 0, 0.1, 1)`, timed by distance: a longer trip takes longer, and a move reads by its overlap with the next beat. Arrival from nowhere `cubic-bezier(0.25, 0.8, 0.25, 1)` over 0.8 to 1s. Stagger groups in reading order 40 to 80ms apart, 80 to 120ms between grid tiles.
- **Open on a finished screen that works as a still.** The cursor rests on empty surface between beats, near its next move, never on an unused control. No cursor move you can't explain; with no cursor, no stand-in (no wandering focus ring or spotlight). The elements decide the cursor's kind: I-beam over text, hand over links, arrow on native app buttons, resize on edges.
- **Every change moves.** Change only what changed: roll the changed span of text and slide what follows by its measured width; numbers roll last digit first. A button keeps one slot for all its states. Typed text becomes a chip in place.
- **Nothing pops.** Everything has an entrance and stays mounted until its exit finishes. Solid things (windows, phones, cards) arrive by moving, never fading through. Cards and pills arrive whole from just above; a toast enters and leaves through the screen edge it is anchored to. Content arrives after its container. A popup is sized before its first frame and holds the edge it opened from.
- **One object, one trip, ending in its final place:** open the room, measure the slot, then fly. Landings decelerate over the last third, no bounce. After motion nothing moves: the handoff frame matches in size, place and look.
- **Drags:** keep the grab offset, the others make room continuously, the drop snaps to a measured slot. A text selection sits under the I-beam.
- **The payoff is visible at the shown size and arrives full,** never a blank surface for a quarter second. It holds about 2s before the exit; nothing sits still more than three seconds.
- **Loops:** a reset removes what the loop added as one thing, with a seen cause (undo, clear, close), as a reverse stagger around an anchor, or snapped while hidden. Data never rewinds in view. A loop never plays a navigation backwards. No dead air at the seam: the next action begins within about a second of the exit.
- **Playback:** any demo that plays on its own for more than 5s in total, a loop of any cycle length or a once-in-view story, gets a visible, keyboard-operable Pause control beside it (WCAG 2.2.2). Pause when the demo is off screen or the tab is hidden. Pausing stops the script's clock and freezes only the animations on the stage (`document.getAnimations().filter((a) => stage.contains(a.effect?.target))`); freezing every animation in the document also freezes the host page's controls mid-press.
- **Reduced motion** shows the poster frame, with Play as an opt-in.

Component gates apply to real, interactive UI. A demo's stage is an illustration: put `data-stage` on its root and the gate skips it and every component inside it (its easing and decorative controls would fail on purpose). Gate the host page's own controls, Pause included.

## Faults that come back every round

Check these before handing over:
- Content that swaps instead of moving
- Gray bars where the eye lands
- A plate behind the window, or a window floating with air on four sides
- Empty bands, and controls or shadows cut by the stage
- Stock AI and made-up logos: sparkles, purple, a letter in a colored square
- Busy rows and uneven insets
- Long holds, and a reset with no cause
- A selection that isn't under the I-beam
- A status bar or home indicator drawn by hand
- A centered amount centered together with its sign

## Filming without the kit

Write the script below to `film.js`. It shoots one element at a fixed interval and lays the frames out at 2x as one contact sheet, so a loop reads as one image. It films the first `.frame`, the wrapper that holds the stage; put that class on it or pass `--select`. Read every sheet you make. Frames run left to right: compare neighbors in a row, and the last of a row with the first of the next, before calling a change a jump.

```bash
node film.js page.html --width 1440 --every 600 --count 20 --out loop.png   # the whole loop
node film.js page.html --width 390 --every 700 --count 16 --out phone.png   # the compact design
node film.js page.html --start 1600 --every 100 --count 10 --out beat.png   # one beat; a shot takes 100 to 200ms, so read the timestamps
node film.js page.html --reduce --still --out poster.png                    # what reduced motion shows
```

```js
// Film a demo: shoot one element at a fixed interval and lay the frames out as one contact sheet.
// Usage: node film.js <url-or-html-path> [--select .frame] [--width 1440] [--every 500] [--count 20]
//                     [--start 0] [--still] [--reduce] [--out sheet.png]
// Prints page errors and console warnings. Requires Playwright (require('playwright')).
const { chromium } = require('playwright');
const path = require('path');
const args = process.argv.slice(2);
const USAGE = 'Usage: node film.js <url-or-html-path> [--select .frame] [--width 1440] [--every 500] [--count 20] [--start 0] [--still] [--reduce] [--out sheet.png]';
const opt = (k, d) => { const i = args.indexOf('--' + k); if (i < 0) return d; const v = args[i + 1]; if (v === undefined || v.startsWith('--')) { console.error(USAGE); process.exit(2); } return v; };
const has = (k) => args.includes('--' + k);
const target = args[0];
if (!target) { console.error(USAGE); process.exit(2); }
const url = /^https?:|^file:/.test(target) ? target : 'file://' + path.resolve(target);
const sel = opt('select', '.frame'), width = +opt('width', 1440), every = +opt('every', 500);
const count = has('still') ? 1 : +opt('count', 20), start = +opt('start', 0), out = opt('out', 'sheet.png');

(async () => {
  let browser;
  try {
  browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width, height: 900 }, deviceScaleFactor: 2, reducedMotion: has('reduce') ? 'reduce' : 'no-preference' });
  const logs = [];
  page.on('pageerror', (e) => logs.push('pageerror: ' + e.message));
  page.on('console', (m) => { if (['error', 'warning'].includes(m.type())) logs.push(m.type() + ': ' + m.text()); });
  await page.goto(url);
  const el = page.locator(sel).first();
  if (!(await el.count())) { console.error(`No element matches ${sel}; pass --select`); if (logs.length) console.error(logs.join('\n')); process.exitCode = 1; return; }
  await el.scrollIntoViewIfNeeded();
  await page.waitForTimeout(start);
  const shots = []; const t0 = Date.now();
  for (let i = 0; i < count; i++) {
    const wait = t0 + i * every - Date.now(); if (wait > 0) await page.waitForTimeout(wait);
    shots.push({ t: Date.now() - t0 + start, png: (await el.screenshot()).toString('base64') });
  }
  // Lay the frames out at true size (2x) in a grid sized to fit, then screenshot the grid.
  const box = await el.boundingBox();
  const cols = count === 1 ? 1 : box.width >= 600 ? 2 : 3;
  const sheet = await browser.newPage({ deviceScaleFactor: 2, viewport: { width: Math.ceil(cols * (box.width + 16) + 16), height: 600 } });
  await sheet.setContent(`<body style="margin:0"><div id="s" style="display:inline-grid;padding:16px;background:#e4e6ea;font:12px system-ui;gap:16px;grid-template-columns:repeat(${cols},${box.width}px)">` +
    shots.map((s) => `<figure style="margin:0"><figcaption style="color:#3c3c46;margin-bottom:6px">${s.t} ms</figcaption><img style="display:block;width:${box.width}px" src="data:image/png;base64,${s.png}"></figure>`).join('') + '</div></body>');
  await sheet.locator('#s').screenshot({ path: out });
  console.log(`${out}: ${shots.length} frame(s) of ${sel} at ${width}px${has('reduce') ? ', reduced motion' : ''}`);
  if (logs.length) { console.log(logs.join('\n')); process.exitCode = 1; }
  } catch (e) { console.error('film.js: ' + e.message.split('\n')[0]); process.exitCode = 1; }
  finally { await browser?.close(); }
})();
```

# Review mode

Findings, not fixes, unless the user asks for fixes too. Run one or both parts. Render or screenshot what you review; judge what people see.

**Scope:** which screens and task flows, which user, which devices. Walk each task as a new user, then as an experienced one. When you can run the page, mark its components and run the component gates; each failing check is evidence for a finding.

## Usability: Nielsen's 10 heuristics

1. Visibility of system status: people know what is happening.
2. Match with the real world: the system speaks the user's language.
3. User control and freedom: easy undo and exit.
4. Consistency and standards: follow conventions.
5. Error prevention: stop problems before they happen.
6. Recognition over recall: options are visible.
7. Flexibility and efficiency: shortcuts for experienced users.
8. Aesthetic and minimalist design: nothing irrelevant. (Use the Signs list for visual findings here.)
9. Error recovery: errors are recognized, explained and recoverable.
10. Help and documentation: help where it's needed.

## Accessibility: WCAG 2.2 (POUR)

- **Perceivable:** text alternatives, captions, adaptable structure (headings, landmarks, reading order), contrast 4.5:1 text and 3:1 large text and UI parts, no meaning by color alone.
- **Operable:** everything works by keyboard with a visible focus that isn't hidden behind sticky bars; no traps; enough time; nothing flashes more than three times a second; targets at least 24×24 (44 for touch); dragging has a single-pointer alternative.
- **Understandable:** readable language, predictable behavior, help in the same place on every page, labels and instructions on inputs, errors identified with suggestions, no redundant entry, accessible authentication.
- **Robust:** correct semantic HTML, name/role/value on every control, ARIA only where native HTML can't do it, status messages announced.

Check static and interactive states, across devices and browsers. Automated checks catch a fraction; say what you tested with (keyboard, screen reader, contrast checker) and what you couldn't, and recommend testing with real assistive technology and with disabled users where possible.

## Findings

One scale for both parts:

| Severity | Meaning |
| --- | --- |
| 4 Critical | Blocks a task or blocks access entirely; fix before release |
| 3 Major | Significant difficulty; fix soon |
| 2 Minor | Inconvenience with a workaround |
| 1 Cosmetic / enhancement | Polish, or beyond compliance |
| 0 | Not a problem (record only when disputing a suspected issue) |

Each finding: heuristic or WCAG criterion (number and name), location, description, severity, who is affected, and a concrete recommendation (with a code example for accessibility fixes). Focus on real tasks over edge cases. End with the three changes that would help most. Note that one reviewer finds a fraction of the issues; three to five independent reviewers find most, and nothing replaces testing with real users.

---

# Checks (Build and Polish, before showing)

Render and look, at most three rounds: screenshot desktop and phone, critique, fix the top problems, look again.

- **Swap test:** swap your typeface for the usual one and your layout for a template. Where nothing would change, you defaulted. Swap in another product's name: if the screen still fits, push the copy, visual and signature harder.
- **Squint test:** blurred, hierarchy still reads and nothing jumps out.
- **Signature test:** point to the specific places the signature appears.
- **Token test:** read the CSS variables aloud; they should belong to this product.

Checklist:
- [ ] Direction written (or taken from the brand) and followed throughout
- [ ] Every spacing value on the 4px scale; equal things equal; aligned columns
- [ ] One tinted neutral ramp, text roles, one accent with enough contrast
- [ ] No hue gradients, gradient text, glows, colored shadows or blobs
- [ ] No emoji in the interface; one icon set, size and stroke
- [ ] Type fits the character; weights 400–600; sentence case; no italic emphasis or negative tracking on small text
- [ ] No exclamation marks, trailing periods on short strings, greeting headlines or unverified claims
- [ ] Tabular figures in one format; nested radii add up
- [ ] Every state present: hover, focus, active, disabled, loading, empty, error
- [ ] First screen composed as a whole; no dead empty band; a real visual or product preview, never filler
- [ ] Motion: only the curves Motion names (Demo motion's two inside a `data-stage`), no bouncy motion, no animated layout properties, reduced motion respected; auto-playing loops, other than spinners and progress, only in a demo with a Pause control
- [ ] Every component gate passes at 1440 and 390, demo stages excluded (log totals in the report)
- [ ] Quality floor met; existing flows still work
- [ ] Brand conflicts, sample content and unverified claims listed in the report

# Working style

- Don't announce modes or narrate process. Lead with the recommendation and its reasoning.
- If an inline rendering tool exists, show directions and components rather than describing them: swatches, the type scale, before and after side by side. The widget shows the visual only; reasoning stays in the text. Match the host's theme variables. Rendering shows craft; it doesn't replace it.
- Keep updates short; don't paste long design monologues.
- After finishing, offer to save the decisions to `.design/system.md`: direction and feel, depth strategy, spacing base and density, type scale and weights, palette tokens, and component patterns used twice or more with their values (for example `Button primary: 36 h · 12/16 pad · 8 radius · 14/500`). When it exists, hold to it and flag drift.

---

Built from: frontend-design (Anthropic, Apache 2.0); unslop by Damir Sokolovsky (@heydamir, https://github.com/heydamir/unslop), CC BY 4.0, condensed and adapted; interface-design by Damola Akinleye (MIT); heuristic-evaluation and accessibility-audit from Designer Skills by MC Dean (MIT); Demo mode condensed and adapted from Stageshow by Benji Taylor (https://github.com/benjitaylor/skills, MIT). Keep this credit in any copy or adaptation.

Stageshow notice: Copyright (c) 2026 Benji Taylor. Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.