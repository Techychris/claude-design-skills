---
name: "design-lean"
description: "Use instead of the built-in design skill to build, polish (unslop) or review UI: landing pages, sites, dashboards, app screens. Same craft rules, run as a gated workflow with a faster gate script. Faux product UI goes to design-demo."
---

# Design (lean)

Interface work in three modes, run as a sequence of gates. Each gate has a pass condition, the evidence it leaves, a cap on retries and what happens on failure. Faux product UI (hero demos, bento tiles, cursor walkthroughs) is the `design-demo` skill, which loads this one for its rules.

**Why this skill exists.** A model's default UI is the average of every UI it has seen: centered headline with a label above it, a row of icon cards, soft gradients, one radius and one grey shadow on everything. Intent lives in prose but code generation pulls from patterns, so writing "warm and specific" still emits the template. Every choice therefore traces to a written decision and gets checked. If another model given a similar prompt would produce substantially the same screen, the work has failed. Removing slop is half the job; a clean screen that could belong to any product is the next template.

**What outranks this skill.** (1) A real brand, written spec or named visual direction: follow it exactly, even where it asks for something this skill calls a default; list each conflict in the report with the one-line change that would apply the rule. A violet-to-blue gradient, sparkles or glow count as slop even in a logo unless the user says they are brand. (2) `.design/system.md` (or legacy `.interface-design/system.md`): read it first; those decisions are made; flag drift. (3) This skill, for everything left open.

---

# Workflow

## G0 Route

Ask in order; the first yes decides.

1. Findings only, no changes? → **Review**
2. Faux product UI as an illustration? → load `design-demo`
3. Existing UI whose features, content and section order must stay? → **Polish**
4. Anything else, including a redesign that may change content or structure → **Build**

Surface: **page** (read and scrolled: landing, marketing, portfolio, event, org site; leans on hero, copy, imagery, section rhythm) or **app screen** (worked in: dashboard, admin, settings, tables, inbox, tools; leans on hierarchy, density, states, tokens). A product site that shows its app is a page; app fragments on it follow app-screen rules.

## Gate register

| Gate | Pass condition | Evidence left | Cap | On fail at cap |
| --- | --- | --- | --- | --- |
| G1 Direction | Name-removed test passes; the person confirms, or a skip rule applies | Direction block | 2 exploration rounds | Take the strongest option, mark it an assumption in the report |
| G2 Plan review | Each place a similar prompt would land the same is revised; `.design/decisions.md` written | decisions.md | 1 revision | Proceed; list the remaining defaults in the report |
| G3 Component | `gate.js --only <name>` passes at 1440 and 390, and the component follows decisions.md or logs an exception | One gate-log line | 2 fix attempts per check | Log it as an open issue with its cause; continue only if nothing else depends on it |
| G4 Page | Full `gate.js` run passes; the four tests and the judgment checklist pass | Gate totals, desktop and phone screenshots | 3 render rounds | Report what still fails |
| G5 Report | Every field of the report template filled or marked none | The report | — | — |
| R1 Findings (Review) | Each finding has a criterion, location, severity and concrete fix | Findings list | — | Drop findings without evidence |

Build runs G1–G5. Polish runs G1, then G4 and G5: its passes cut across the whole screen, so it gates once at the end instead of per component. Review runs G0 and R1.

**Skip rules for the G1 wait:** the person said to just do it; a brand or spec already fixes the direction; a single small component inside an existing design.

**Unattended runs.** When nobody is there to answer (a scheduled run, the person said they'd check back, or a question went unanswered), don't wait at G1. Take the direction, state it at the top of the report as an assumption with the one line that would change it, and continue. Skip paid image generation and use the next option in Visuals. A Polish run that finds no slop reports its suggested refinements without applying them. Redirecting later should cost one message.

**In Build, one component in progress at a time.** Gate it, log it, then start the next. A failure is fixed now, not collected for the end: problems compound.

---

# Direction

## Intent

Answer before any visual decision; keep it a compact brief.

- **Who is this human?** The actual person: where they are, what they did five minutes ago, what they'll do next.
- **What must they accomplish?** The verb: grade these submissions, find the broken deployment. It decides what leads, what follows, what hides.
- **What should it feel like?** Words that mean something: warm like a notebook, cold like a terminal, dense like a trading floor. "Clean and modern" means nothing.

If the brief doesn't name the subject, propose a concrete subject, audience and primary job and confirm; if context allows a responsible assumption, state it in one line and proceed. Intent is systemic: if the feel is warm, surfaces, text, borders, accents and type are all warm. "It's common" or "it works" is not a reason.

## Domain exploration

Produce all four: **domain** (5+ concepts and metaphors from the subject's world); **color world** (5+ colors from its physical version); **signature** (one element only this product could have, used consistently where it belongs); **defaults to reject** (the three obvious choices, each with its alternative). Name-removed test: read the proposal with the product name removed; if no one could tell what it's for, explore again (cap: 2 rounds).

## Direction block

```
Product:    [what it does, for whom, one sentence]
Character:  [2–3 concrete words, not clean/modern/sleek/minimal/premium]
World:      [place or material it belongs to; sets neutral tint, accent, visuals]
Moments:    [1–2 places that get rich color and detail, chosen from the content]
Signature:  [the one detail only this product has]
Rejecting:  [default → alternative] × 3
```

Show it with a small specimen when rendering is available (real swatches, the type scale in the real face, the signature as a real component), then ask "Does that direction feel right?" (G1).

**Defaults generated design clusters around.** Each is legitimate for some brief but appears regardless of subject; where the brief leaves an axis free, don't spend it here: (1) warm cream near `#F4F1EA` with a high-contrast serif and a terracotta accent near `#D97757`; (2) near-black with one acid-green or vermilion accent; (3) broadsheet hairlines, zero radius, dense newspaper columns; (4) the SaaS-card kit: identical rounded cards, one radius, the same soft grey shadow, gradient washes; (5) template chrome: tracked all-caps eyebrows, `A · B · C` meta strings, `WORD — fragment` labels, tinted near-black for black, monospace data labels, `→` on buttons, violet or indigo accents.

## Decisions file

After direction, write `.design/decisions.md` once: palette tokens and why, type faces and scale and why, depth strategy and why, spacing base and density and why, the signature and where it appears, the three rejected defaults. This replaces re-justifying every component. At G3 the judgment question is one line: does this component follow decisions.md? If it departs, log the exception and its reason in the gate-log line.

---

# Craft rules

Rules marked **(gated)** are measured by `gate.js`; the G4 checklist covers only the rest.

## Hierarchy and composition

- One focal point per view: name what the person came to do and make it win by size, contrast, position or space.
- Weight and color do more than size. One 14px size holds three tiers: value 600 primary, label 500 secondary, meta 400 muted.
- Density is a decision in pixels, chosen up front and repeated: tool panels 12–16 padding feel tight; 24 feels like a brochure.
- Breathe unevenly: tight inside a group, looser between groups.
- Proportions speak: a 280px sidebar says navigation serves content; 360 says they're peers.
- Restraint: about 60/30/10 neutral, secondary tone, accent. Spend boldness in one place, then remove one accessory.

## Spacing

- Every margin, padding, gap and fixed height is a multiple of 4 (gated); a 2px nudge inside small controls is fine.
- Equal things are equal: one row height and gap per list, one padding per card set; symmetrical padding unless content demands otherwise.
- Things line up: icons in one column, labels on one baseline, numbers right-aligned.
- Pages: sections 80–128 apart on desktop, clearly more than any gap inside a section. Apps: page padding 24–32.

## Color

- One neutral ramp tinted toward the world for background, surfaces, borders and text; one hue across surfaces, shifting only lightness. In apps surfaces stay near-neutral and content carries color.
- Four text roles: primary, secondary, muted, disabled.
- One accent in the chrome, used rarely: the primary action, selection, the one number that matters. Inside the chosen moments color can be rich if each color means something. A real brand color becomes the accent and leaves the surfaces.
- Contrast 4.5:1 for body text and accent-with-text, 3:1 for large text (gated).
- Semantic colors carry meaning only, toned to the palette, slightly desaturated on dark. Running text in full ink.
- Colors come from tokens, never raw values in component CSS (gated).
- No hue-to-hue gradients on surfaces, gradient text, colored glows or shadows, radial washes, blobs or neon borders. A gradient is allowed only as a tone shift within one neutral, or a neutral scrim under text on a photo.

## Surfaces, borders and depth

- One depth strategy: borders only (technical, dense), subtle shadows (approachable), layered shadows (premium), or surface-tone shifts.
- Elevation is quiet. Dark: each step a couple of points of lightness (page → card → raised) plus hairlines. Light: resting `0 0 0 1px rgba(0,0,0,.06), 0 1px 2px rgba(0,0,0,.05)`, floating `0 8px 24px rgba(0,0,0,.06)`. Dark lift: `0 0 0 1px rgba(255,255,255,.08)`.
- Hairlines: primary text color at 6–10% opacity (12% on dark), in a small progression: divider, standard, emphasis, focus ring.
- Sidebar: same as the page or one step deeper on dark, separated by a hairline, never a different hue. Popovers one level above their parent. Inputs slightly darker than their surroundings.

## Typography

- Type carries the personality. One family is normal, two the limit and clearly distinct; a display face only for large headlines. A real brand font stays.
- Step a ratio: about 1.2 dense UI, 1.25 most product UI, 1.333 expressive pages. Five sizes per page at most.
- Weights 400 and 500; 600 for figures and rare emphasis; 700–900 only if a brand spec says so.
- Sentence case everywhere; no uppercase tracked labels, no italic emphasis, no single headline word set apart by italic, bold or color.
- Letter spacing 0 under 16px, about −0.02em from 40px, −0.03em from 56px. Body line height about 1.5, serif body slightly more. Line length 45–75 characters.
- Numbers: tabular figures (gated), one format throughout.
- `text-wrap: balance` on headings, `pretty` on body; `-webkit-font-smoothing: antialiased` on the root.

## Icons

Emoji used as icons or decoration become line icons from one set (the project's own, else lucide), 16 or 18px, stroke 1.5, in their text role's color, same box width per row, 8–10px from the label. Drop icons that add nothing; a category that needs color gets a status dot.

## Copy

- Write from the person's side (they manage notifications, not webhook config); describe, don't sell.
- Headlines say what the product does for whom, using facts on the page. If a competitor's name still fits, rewrite.
- Buttons say what happens ("Save changes"); an action keeps its name through the flow ("Publish" → "Published").
- Errors say what happened and how to fix it, without apology. Empty states invite the next action.
- Active voice, plain verbs; no exclamation marks, greeting headlines, hype words (supercharge, seamless, unlock, magic, game-changing) or `AI-powered` everywhere. Short labels (`Search`). A change names its comparison (`+12% vs last month`). No trailing period on headlines, labels, buttons or toasts.
- Never invent proof: no customers, quotes, reviews, logos or statistics. Sample content where the brief leaves gaps is fine and goes in the report to confirm.

## Structure means something

Outlines, borders, numbering, eyebrows and dividers encode information. `01 / 02 / 03` only for a real sequence. Badges like `PRO`, `New ✨` go unless they carry meaning, then become quiet text. Counts and meta are quiet text, not pills.

## Layout: pages

- The hero opens with the most characteristic thing in the subject's world, in its most fitting form. A big number with a small label and a gradient only if it's truly best.
- First screen answers the visitor's first question in large type, carries the `h1`, one primary action and at most one secondary.
- Strongest heroes: one scene image edge to edge with the headline on its calm part, or an asymmetric split with the visual at least half. Centered stacks only for short heroes without a visual.
- Navigation: wordmark, the existing links, one button; log in as a text link. No floating pills or glass.
- Each section: a heading, a different composition from its neighbors, its full content. No dead bands. The footer is a designed close, not a sitemap.
- Small screens: stack in reading order and recompose; no text under 11px; no horizontal scroll (gated).

## Layout: app screens

- Real proportions: shell fills the viewport, sidebar 240–280, content fluid and capped near 1440–1600, top bar 56–64. Never a narrow centered column.
- Vary sizes: compact stats above one wide chart, never a row of identical cards. The main chart takes at least two thirds of the width and 280–360 height.
- Stat cards: label, figure, change with its comparison; no filler sparklines or icons; no figure repeated elsewhere.
- Pick the expression that tells the data's story: hero number, inline stat, delta, progress bar or gauge.

## Components and states

- Native HTML first (`<button>`, `<a>`, `<input>`, `<dialog>`, `<details>`), never `<div onClick>`. Stateful widgets (select, combobox, dialog, popover, tooltip, menu, tabs, date picker) use a trusted headless primitive (Radix, React Aria, Ark, Headless UI or the platform's). Hand-rolled ones owe the full contract: arrow keys, Enter, Escape, focus trap and return, ARIA roles and state, click-outside, scroll lock.
- The project's design system first; extract a component on the second real reuse; semantic tokens (`bg-card text-muted-foreground`), not literals.
- Every control has default, hover, active, focus (visible ring) and disabled; every data view has loading, empty and error. Hover, focus and empty states are gated.
- Concentric radius: inner = outer − padding, minimum 4, where padding is smaller than the outer radius (gated). Radius scale (gated): 4 or 6 keycaps and tags, 8 or 10 buttons and inputs, 12, 14 or 16 cards, 14, 16 or 20 panels. Buttons are square-ish or fully round, decided once.
- Hit areas at least 24×24, and 44×44 at touch widths (gated); extend small controls with a pseudo-element; never overlap.
- Active rows: a small surface step with a hairline, not a glow. Keyboard shortcuts as small keycaps. Optical alignment where geometric centering looks off.
- Charts: muted grid and labels, one accent per chart, neutral steps for other series; line for trend, bars for comparison, stacked bar or list for share, progress for goals.
- Images: 1px inset outline at 10% black (light) or white (dark); fixed dimensions and real alt text (gated).
- Logo: the product name in the main family plus a simple flat mark; no gradient wordmark or sparkle tile.

## Visuals

- One dominant image beats six small ones; usually one visual, in the hero. No blobs, orbs, nebulas, floating cubes, glowing grids, brains, robots or holograms.
- Order of preference: the project's own pictures; generated, if an image tool exists; drawn in code from the subject; type and color alone. Never a placeholder icon or abstract shape. App screens rarely need generated images.
- Image prompt: write the subject as one plain sentence, then subject; simple setting; light and palette (name the page background); one style; composition with calm space for text; exclusions (no text, letters, logos, UI, watermark); aspect at twice display size. Add texture in code, not in the prompt.
- Before any paid generation, show prompt, model and size and ask. Run once, judge, change the prompt instead of rerolling.
- A cropped, working interface fragment is the strongest picture a software page has; build it with `design-demo`.
- WebP or AVIF at 2x, edges matched to the page color, nothing over a headline.

## Motion

Motion is felt, not watched. (Demo storytelling motion follows `design-demo` instead.)

- Repeated many-times-a-day actions get none; occasional surfaces (menus, modals, toasts) get standard motion; ambient motion never.
- On load, at most one orchestrated moment: a short fade with a 6–12px rise, staggered 40–60ms over at most six items.
- Easing (gated, exactly these): entering and interactive `cubic-bezier(0.22, 1, 0.36, 1)` or `cubic-bezier(0.23, 1, 0.32, 1)`, one per project; across the screen `cubic-bezier(0.77, 0, 0.175, 1)`; drawers and sheets `cubic-bezier(0.32, 0.72, 0, 1)`; constant motion `linear`. Keyword easings fail; never `ease-in`.
- Durations (gated range 100–500ms): hover 100–150; press 100–160; tooltips 125–200; menus 150–250; card, list and modal entrances 200–300; drawers and sheets 300–500; up to 500 only for the one on-load moment.
- Press feedback `scale(0.97)` on `:active`. Nothing appears from `scale(0)`: start at 0.95 and opacity 0. Popovers scale from their trigger, modals from center.
- Transition only named properties (gated): color, background, border, opacity, transform. Never `transition: all`, width, height, top, left or margins.
- No pulse, ping, shimmer, breathing glows, floating, parallax, bouncy springs or `hover:scale` on cards. Respect `prefers-reduced-motion`: keep opacity and color, drop travel.

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

On light, "raised" is a step darker than the card. Inputs sit slightly darker than their surface: "deepest" on dark, "raised" on light. Semantic: positive `#4cc38a` dark / `#16a34a` light; negative `#e5484d` dark / `#dc2626` light. Muted text only for meta and captions.

**Accent:** a real brand color, or one from the world (warm: amber, coral, ember; cool: cobalt, teal, sky; natural: moss, sage). At most about 10% of a page, far less in app chrome. Avoid purple-blue unless the brand is purple.

**Buttons:** hero 44–48 tall, nav 32–36 (44 at touch widths), side padding 16–20. Primary on light: primary-text fill with white text, or the accent; on dark, off-white with dark text. Secondary: raised surface with a hairline.

**Type scale (product UI):** labels and meta 12/16/400; secondary and captions 13–14/20/400; body and nav 14–16/20–24/400–500; wordmark 16–18/1/500–600; hero subhead 18–20/28–30/400, max 36rem; card figures 28–32/1/500–600 tabular; page title 28–36/1.15/400–500; hero headline 56–72 desktop, 36–44 phone, 1.02–1.08, 400–500. Pages may push the headline larger; page body text is 16–20px.

**Type starting points:** precise and technical: Geist or IBM Plex Sans (their mono only for real code and figures); warm and human: Instrument Sans, DM Sans, Figtree (Instrument Serif or Newsreader for hero headlines); editorial: Instrument Sans with Newsreader, Instrument Serif or Fraunces; playful and bold: Space Grotesk, Bricolage Grotesque. A starting point, not a default.

---

# Modes

## Build

1. **Read the project and brief:** stack, existing tokens and components, `.design/system.md`, brand assets, which images really exist. Plan only around assets you have.
2. **Direction** → G1.
3. **Plan:** palette as 4–6 named hex values; typefaces and roles; a one-sentence layout concept with an ASCII wireframe and alignment; three or four principles specific to this brief. Write decisions.md.
4. **Review the plan** → G2: mentally run a similar prompt; wherever you'd land in the same place, revise and say what changed.
5. **Build one component at a time** → G3 each: tokens first as CSS custom properties, then the focal element at desktop and phone width, then each section with real content, then states, then motion. A design that needs animation to look finished isn't finished.
6. **Page check** → G4, then **report** → G5, then offer to save decisions to `.design/system.md`.

## Polish

Keeps the product: features, content and section order stay; every size, color, word and image becomes deliberate.

1. **Look:** find the files that render the screen; screenshot at desktop and phone width. Only a live URL: rebuild it as one static HTML file and say in the report it's a redesign for the site's owner. Only a screenshot: rebuild it as static HTML first and treat that as the original.
2. **Audit:** walk the slop signs below; one line per sign with its location.
3. **Decide depth.** Heavy (many signs across color, type, icons, copy): full process. Light (a few signs): fix only what the audit found, take direction from the existing brand, keep palette, type, layout and visual; bigger ideas go in the report. None: say so and suggest two or three refinements with exact values; apply them only if the person agrees.
4. **Direction** → G1 (show the audit with the direction block). Light depth takes its direction from the brand and skips the wait.
5. **Nine passes in order,** each finished across the whole screen before the next: spacing, color, icons, copy, type, layout, details, visuals, motion. Mark components with `data-component` during the spacing pass so G4 can check them.
6. **Page check** → G4, comparing against the audit and re-running forms, menus and links so polish didn't break function. **Report** → G5.

Don't rename the product (keep a real logo; redraw a slop logo flat), change features, content or order unless asked, invent features, claims or data, or replace removed decoration with new decoration (glass, grain, noise, neon, bento).

**Signs of slop:**
- **Surfaces and color:** purple-blue or violet-pink gradients; gradient text; colored glows and shadows; radial washes and blurred blobs; neon borders; glass cards with colored shadow; many near-identical text tints; everything highlighted.
- **Type:** 800–900 headings; uppercase tracked labels; too many sizes and weights; mixed number formats; negative tracking on small text; italic emphasis; one accent word in a headline.
- **Icons:** emoji as nav, labels or status (🏠 📥 🚀 💰 ⚠️ 📈 🔥 ✨); emoji in pills and counts; icons in many sizes and colors or off their column.
- **Spacing:** arbitrary values (13, 7, 11, 31); rows of different heights or gaps; groups closer to neighbors than to their own items; uneven sibling padding.
- **Copy:** greeting headlines; exclamation marks; changes without a reference; wordy placeholders; hype words; trailing periods on short strings; fake-looking data (`$123,456`, `[X]`); unsourced social proof.
- **Components:** glowing pills for counts and plans; PRO/New/Beta badges everywhere; everything a full pill; rainbow or glowing chart bars; every chart in accent shades; sparklines on every stat card; equal cards side by side; gradient-tile logo with sparkle; decorative tags.
- **Pages:** pill badge above the headline (`✨ Introducing X 2.0`); a headline that fits any product; shimmer; floating blobs and glowing lines; everything stacked and centered; three or more hero buttons; emoji feature cards with vague lines; a visual on every section.
- **Visuals:** glossy 3D blobs, chrome shapes, nebulas; robots and brains for AI; text or fake UI baked into images; hard image edges on a different background.
- **Motion:** pulse, ping, breathing glows on things that aren't live; `transition-all`; `hover:scale`; bouncy springs; elements flying in from different directions; animated layout properties.
- **Template look** (what cleaned-up screens fall back to): pure grey page, Inter, white text and the old brand color on one button for a warm product; a generic hero visual; the same layout and palette as every other product.

## Review

Findings, not fixes, unless asked. Render or screenshot what you review; judge what people see.

1. **Scope:** which screens and task flows, which user, which devices.
2. **Walk the tasks** as a new user, then an experienced one. When the page runs, mark components and run `gate.js`; each failing check is evidence.
3. **Usability, Nielsen's 10:** visibility of system status; match with the real world; user control and freedom; consistency and standards; error prevention; recognition over recall; flexibility and efficiency; aesthetic and minimalist design (use the slop signs here); error recovery; help and documentation.
4. **Accessibility, WCAG 2.2 (POUR):** *perceivable*: text alternatives, captions, adaptable structure (headings, landmarks, reading order), contrast 4.5:1 text and 3:1 large text and UI parts, no meaning by color alone. *Operable*: everything works by keyboard with a visible focus not hidden by sticky bars; no traps; enough time; nothing flashes more than three times a second; targets at least 24×24 (44 touch); dragging has a single-pointer alternative. *Understandable*: readable language, predictable behavior, consistent help, labels and instructions, errors identified with suggestions, no redundant entry, accessible authentication. *Robust*: semantic HTML, name/role/value on every control, ARIA only where HTML can't, status messages announced. Check static and interactive states; say what you tested with and what you couldn't; recommend testing with real assistive technology and disabled users.
5. **R1 Findings:** each has the heuristic or WCAG criterion (number and name), location, description, severity, who is affected and a concrete recommendation (code for accessibility fixes). Severity: 4 critical, blocks a task or access, fix before release; 3 major, significant difficulty, fix soon; 2 minor, inconvenience with a workaround; 1 cosmetic or beyond compliance; 0 not a problem (only when disputing a suspected issue). Real tasks over edge cases.
6. **Priorities:** the three changes that would help most. Note that one reviewer finds a fraction of the issues; three to five find most; nothing replaces real users.

---

# Component gate (G3 and G4)

## Mark components

Put `data-component="<type>"` on each component's root and give it a `data-name`. A data view whose content changes gets `data-dynamic` and `data-states="empty"` (add `loading error` for async data); each state's element carries `data-state="empty" data-state-for="<view id>"`, even while hidden. A demo stage gets `data-stage`; the gate skips it.

| Type | Use for | Adds to the universal checks |
| --- | --- | --- |
| `button` | Buttons, button-styled links | Height ≥32; hover, focus, Enter changes the page |
| `link` | Text and nav links | Hover and focus; links inside a sentence skip target size |
| `input` | Text, search, number, date | A real label, not only a placeholder |
| `checkbox` | Checkboxes, radios, switches | The label counts as the target |
| `select`, `tabs` | Menus, comboboxes, tab lists | Name, focus, hover; a tab list is checked through its active tab |
| `control` | Anything custom and interactive | Name, focus, hover, Enter changes the page |
| `nav` | Navigation regions | A `<nav>` landmark |
| `table`, `list`, `chart` | Data views | Header `scope` on tables; with `data-dynamic`, an empty state that exists |
| `status` | Toasts, live results | A live region |
| `image` | The `<img>` itself | `alt`, `width` and `height` |
| `card`, `stat`, `block` | Static containers, figures, sections | Universal checks only |

**Universal checks, at 1440 and 390:** contrast (faded text is blended, not skipped); 4px grid on padding, vertical margins, and gaps of flex and grid containers; radius scale; concentric radius; transitions only on named properties with a named curve, 100–500ms; no raw color values in stylesheet rules or inline styles; fits the viewport; tabular figures on numbers. Interactive types add: accessible name, focusable, visible focus change, hover change (desktop), target ≥24px, ≥44px at touch widths. Each component is checked on its own elements only; a nested component's defect fails that component, not its parents. SVG text isn't measured; the run says how many labels it skipped so you check them in a screenshot.

## Get and run the script

Don't retype it. Extract it from this file (its base directory is shown when the skill loads):

```bash
mkdir -p .design && python3 - "<base directory>/SKILL.md" <<'PY'
import re, sys
for name, code in re.findall(r"`{3}js\n// file: (\S+)\n(.*?)`{3}", open(sys.argv[1]).read(), re.S):
    open(".design/" + name, "w").write("// file: " + name + "\n" + code); print("wrote .design/" + name)
PY
node -e "require('playwright')" 2>/dev/null || (npm i -D playwright && npx playwright install chromium)  # skip the install when Playwright already resolves
```

```bash
node .design/gate.js page.html --only "<data-name>"   # G3: one component, about 1–5 s
node .design/gate.js page.html                          # G4: every component
node .design/gate.js page.html --json .design/gate.json --widths 1440,768,390
```

Exit 1 means a component failed; 2 means nothing matched. For a dev server, gate the production build too. Reading results: "works by keyboard" only proves Enter changed the page, so confirm it was the right change; a hover with a `transition-delay` of 250ms or more reads as missing. Never report a gate as passed if the script didn't run; with no browser, say so and fall back to screenshots and the checklist.

**Gate log:** one line per component, e.g. `PASS button "Publish" 14/14` or `PASS card "Pricing" 7/7 exception: 20 padding, matches hero`.

```js
// file: gate.js
// Component gate v2. Usage: node gate.js <url-or-html> [--widths 1440,390] [--only name,id,type:button] [--json out.json]
// Checks every element marked data-component="<type>" in headless Chromium. Exit 1 if any fail, 2 on bad usage.
// --only gates just the named components (data-name, id or type:<type>): use it per component, the full run once at the end.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const argv = process.argv.slice(2);
const opt = (k, d) => { const i = argv.indexOf('--' + k); return i < 0 ? d : argv[i + 1]; };
const target = argv[0];
if (!target || target.startsWith('--')) { console.error('Usage: node gate.js <url-or-html> [--widths 1440,390] [--only a,b,type:button] [--json out.json]'); process.exit(2); }
const url = /^https?:|^file:/.test(target) ? target : 'file://' + path.resolve(target);
const widths = opt('widths', '1440,390').split(',').map(Number);
const only = opt('only', '').split(',').map((s) => s.trim()).filter(Boolean);
const jsonOut = opt('json', null);

const INTERACTIVE = ['button', 'link', 'input', 'checkbox', 'select', 'tabs', 'control'];
const RADII = [0, 4, 6, 8, 10, 12, 14, 16, 20];
const EASES = ['cubic-bezier(0.22, 1, 0.36, 1)', 'cubic-bezier(0.23, 1, 0.32, 1)', 'cubic-bezier(0.77, 0, 0.175, 1)', 'cubic-bezier(0.32, 0.72, 0, 1)'];
const MOTION_PROPS = ['color', 'background-color', 'border-color', 'opacity', 'transform', 'box-shadow', 'outline-color', 'text-decoration-color'];

const rgb = (c) => { const m = c && c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const [r, g, b, a = 1] = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return [r, g, b, a]; };
const lum = ([r, g, b]) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
// Text at partial opacity is blended over its background before measuring, instead of being skipped.
const ratio = (fg, bg, op) => { const f = rgb(fg), b = rgb(bg); if (!f || !b) return 99; const a = f[3] * op; const mix = [0, 1, 2].map((i) => f[i] * a + b[i] * (1 - a)); const [h, l] = [lum(mix), lum(b)].sort((x, y) => y - x); return (h + 0.05) / (l + 0.05); };

// Runs in the page. Collects every marked component's facts in one round trip.
function collect({ RADII, EASES, MOTION_PROPS }) {
  const FOCUSABLE = '[tabindex="0"], a[href], button:not([tabindex="-1"]), input, select, textarea';
  const bgOf = (n) => { for (; n; n = n.parentElement) { const b = getComputedStyle(n).backgroundColor; if (!/rgba\(0, 0, 0, 0\)|transparent/.test(b)) return b; } return 'rgb(255, 255, 255)'; };
  const literal = /#[0-9a-f]{3,8}\b|rgba?\(|hsla?\(/i;
  const COLOR_PROPS = ['color', 'background-color', 'background', 'border-color', 'border', 'box-shadow', 'outline-color', 'fill', 'stroke'];
  return [...document.querySelectorAll('[data-component]')].map((e, index) => {
    const type = e.dataset.component, cs = getComputedStyle(e), r = e.getBoundingClientRect();
    const visible = !!(r.width || r.height) && cs.visibility !== 'hidden' && !e.closest('[data-stage]');
    // Own elements: this component and descendants not owned by a nested component, outside SVG, and not UA-internal option rows.
    const own = [e, ...e.querySelectorAll('*')].filter((n) => (n === e || n.closest('[data-component]') === e) && !n.closest('svg, [data-stage]') && !/^(OPTION|OPTGROUP)$/.test(n.tagName));
    const id = e.dataset.name || e.id || (e.getAttribute('aria-label') || e.textContent || type).trim().replace(/\s+/g, ' ').slice(0, 32);
    const self = /^(A|BUTTON|INPUT|SELECT|TEXTAREA)$/.test(e.tagName) || e.tabIndex >= 0 || e.getAttribute('role') === 'tab'; // roving-tabindex tabs reach focus by arrow keys
    const tgt = self ? e : (e.querySelector('[role=tab][aria-selected=true]') || e.querySelector(FOCUSABLE));
    const name = (e.getAttribute('aria-label') || (e.getAttribute('aria-labelledby') || '').split(' ').map((x) => document.getElementById(x)?.textContent || '').join(' ') ||
      (e.labels && [...e.labels].map((l) => l.textContent).join(' ')) || e.getAttribute('alt') || e.getAttribute('title') || e.textContent || '').trim();
    const texts = own.filter((n) => [...n.childNodes].some((c) => c.nodeType === 3 && c.textContent.trim()) && getComputedStyle(n).visibility !== 'hidden')
      .map((n) => { const s = getComputedStyle(n); let op = 1; for (let p = n; p; p = p.parentElement) op *= +getComputedStyle(p).opacity; return { fg: s.color, bg: bgOf(n), fs: parseFloat(s.fontSize), fw: +s.fontWeight, op, t: n.textContent.trim().slice(0, 20) }; })
      .filter((t) => t.op > 0.01);
    const offGrid = [], badRadius = [], concentric = [], motion = [], literals = [];
    own.forEach((n) => {
      const s = getComputedStyle(n);
      const box = ['paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'marginTop', 'marginBottom'];
      if (/flex|grid/.test(s.display)) box.push('rowGap', 'columnGap'); // gap only means something on flex and grid containers
      for (const p of box) { const v = parseFloat(s[p]); if (v > 2 && v % 4) offGrid.push(`${p}=${s[p]}`); }
      const rad = parseFloat(s.borderTopLeftRadius), circle = rad >= Math.min(n.offsetWidth, n.offsetHeight) / 2 - 1;
      if (rad > 0 && !RADII.includes(Math.round(rad)) && !circle) badRadius.push(Math.round(rad));
      const p = n.parentElement;
      if (n !== e && p && e.contains(p) && rad > 0 && !circle) { const ps = getComputedStyle(p), pr = parseFloat(ps.borderTopLeftRadius), pad = Math.min(parseFloat(ps.paddingTop), parseFloat(ps.paddingLeft)); if (pr > 0 && pad > 0 && pad < pr && rad > Math.max(4, pr - pad) + 2) concentric.push(`${Math.round(rad)}>${pr}-${pad}`); }
      if (parseFloat(s.transitionDuration) > 0) {
        s.transitionProperty.split(',').map((x) => x.trim()).forEach((q) => { if (!MOTION_PROPS.includes(q)) motion.push('prop ' + q); });
        s.transitionTimingFunction.split(/,(?![^(]*\))/).map((x) => x.trim()).forEach((f) => { if (!EASES.includes(f) && f !== 'linear') motion.push('ease ' + f); });
        s.transitionDuration.split(',').map(parseFloat).forEach((d) => { if (d * 1000 < 100 || d * 1000 > 500) motion.push('dur ' + d + 's'); });
      }
      const st = n.getAttribute('style') || ''; // inline styles count too
      st.split(';').forEach((decl) => { const [k, ...v] = decl.split(':'); const val = v.join(':'); if (k && COLOR_PROPS.includes(k.trim().toLowerCase()) && literal.test(val) && !/var\(/.test(val)) literals.push(`inline ${k.trim()}`); });
    });
    for (const sheet of document.styleSheets) { let rules; try { rules = sheet.cssRules; } catch { continue; }
      for (const rule of rules) { if (!rule.selectorText) continue; let hit = false; try { const sel = rule.selectorText.replace(/:(hover|active|focus-visible|focus|checked|disabled)/g, ''); hit = own.some((n) => n.matches(sel)); } catch {} if (!hit) continue;
        for (const prop of COLOR_PROPS) { const v = rule.style.getPropertyValue(prop); if (v && literal.test(v) && !/var\(/.test(v)) literals.push(`${rule.selectorText} ${prop}`); } } }
    const tag = e.tagName.toLowerCase();
    const labelBox = (e.labels && e.labels[0]) ? e.labels[0].getBoundingClientRect() : (tgt && tgt !== e ? tgt.getBoundingClientRect() : r);
    const inlineInText = tag === 'a' && cs.display === 'inline' && e.parentElement && e.parentElement.textContent.trim().length > e.textContent.trim().length + 10;
    const numeric = own.filter((n) => n.children.length === 0 && /\d/.test(n.textContent) && /^[\d\s$%.,:–\-ampmMonTueWedThuFriSatSunNovOctDecJanfbt]+$/.test(n.textContent.trim())).map((n) => getComputedStyle(n).fontVariantNumeric);
    const svgText = [...e.querySelectorAll('svg text')].filter((t) => t.closest('[data-component]') === e).length;
    return { index, type, id, name, visible, w: Math.round(tgt && tgt !== e ? labelBox.width : Math.max(r.width, labelBox.width)), h: Math.round(tgt && tgt !== e ? labelBox.height : Math.max(r.height, labelBox.height)), texts, offGrid, badRadius, concentric, motion, literals: [...new Set(literals)],
      focusable: !!tgt, delegated: !!tgt && tgt !== e, inlineInText, tag, role: e.getAttribute('role'), dataName: e.dataset.name || '', elId: e.id || '',
      hasLive: !!(e.getAttribute('aria-live') || e.querySelector('[aria-live],[role=status]') || e.closest('[aria-live]')),
      scope: tag === 'table' ? [...e.querySelectorAll('th')].every((t) => t.getAttribute('scope')) : true, numeric, svgText,
      states: (e.dataset.states || '').split(/\s+/).filter(Boolean).map((s) => ({ s, ok: !!document.querySelector(`[data-state="${s}"][data-state-for="${e.id}"]`) })),
      dynamic: e.hasAttribute('data-dynamic'), imgOk: tag === 'img' ? e.hasAttribute('alt') && e.hasAttribute('width') && e.hasAttribute('height') : true,
      left: r.left, right: r.right, scrollOver: e.scrollWidth > e.clientWidth + 1 && tag !== 'table' && cs.overflowX === 'visible' };
  });
}

const selected = (c) => !only.length || only.some((o) => o === c.dataName || o === c.elId || o === c.id || o === 'type:' + c.type);

(async () => {
  const browser = await chromium.launch();
  const rows = []; const t0 = Date.now();
  for (const w of widths) {
    const page = await browser.newPage({ viewport: { width: w, height: 900 }, hasTouch: w < 600 });
    await page.goto(url); await page.waitForTimeout(400);
    const all = (await page.evaluate(collect, { RADII, EASES, MOTION_PROPS })).filter((c) => c.visible && selected(c));
    for (const info of all) {
      const checks = []; const add = (k, ok, d = '') => checks.push({ k, ok, d });
      const isInter = INTERACTIVE.includes(info.type);
      const lowC = info.texts.filter((t) => ratio(t.fg, t.bg, t.op) < ((t.fs >= 24 || (t.fs >= 18.66 && t.fw >= 700)) ? 3 : 4.5));
      add('contrast', !lowC.length, lowC.map((t) => `${t.t} ${ratio(t.fg, t.bg, t.op).toFixed(2)}`).join('; '));
      add('4px grid', !info.offGrid.length, info.offGrid.slice(0, 3).join(' '));
      add('radius scale', !info.badRadius.length, info.badRadius.join(','));
      add('concentric radius', !info.concentric.length, info.concentric.join(' '));
      add('motion rules', !info.motion.length, [...new Set(info.motion)].slice(0, 3).join(' '));
      add('tokens only', !info.literals.length, info.literals.slice(0, 2).join(' | '));
      add('fits viewport', info.left >= -1 && info.right <= w + 1 && !info.scrollOver);
      if (info.numeric.length) add('tabular figures', info.numeric.every((v) => /tabular-nums/.test(v)));
      if (isInter) {
        add('accessible name', !!info.name);
        add('keyboard focusable', info.focusable);
        add('target ≥24px', info.inlineInText || (info.w >= 24 && info.h >= 24), `${info.w}×${info.h}`);
        if (w < 600 && !info.inlineInText) add('touch target ≥44px', info.w >= 44 && info.h >= 44, `${info.w}×${info.h}`);
        if (info.focusable) {
          // Interact with the focusable element itself: the component, or for tab lists and wrappers, its active focusable child.
          const handle = await page.evaluateHandle(({ i }) => { const e = document.querySelectorAll('[data-component]')[i]; const F = '[tabindex="0"], a[href], button:not([tabindex="-1"]), input, select, textarea'; return /^(A|BUTTON|INPUT|SELECT|TEXTAREA)$/.test(e.tagName) || e.tabIndex >= 0 || e.getAttribute('role') === 'tab' ? e : (e.querySelector('[role=tab][aria-selected=true]') || e.querySelector(F)); }, { i: info.index });
          const el = handle.asElement();
          const style = () => el.evaluate((e) => [e, ...(e.labels || [])].map((n) => { const s = getComputedStyle(n); return [s.outlineStyle, s.outlineWidth, s.boxShadow, s.backgroundColor, s.color, s.borderColor, s.textDecorationLine, s.textDecorationLine === 'none' ? '' : s.textDecorationThickness].join('|'); }).join('||'));
          await page.mouse.move(0, 0); await page.keyboard.press('Escape'); const base = await style();
          await page.keyboard.press('Shift'); await el.focus(); await page.waitForTimeout(250); const foc = await style(); await el.evaluate((e) => e.blur()); await page.waitForTimeout(250);
          add('focus visible', foc !== base);
          if (w >= 600) { await el.hover().catch(() => {}); await page.waitForTimeout(250); const hov = await style(); await page.mouse.move(0, 0); add('hover state', hov !== base); }
          if (['button', 'control'].includes(info.type) && info.tag !== 'a') {
            await el.focus();
            await page.evaluate(() => { window.__gateMut = false; const o = new MutationObserver(() => { window.__gateMut = true; o.disconnect(); }); o.observe(document.body, { subtree: true, childList: true, attributes: true, characterData: true }); });
            await page.keyboard.press('Enter'); await page.waitForTimeout(150);
            const changed = await page.evaluate(() => window.__gateMut).catch(() => true);
            add('works by keyboard', changed);
            if (changed) { await page.goto(url); await page.waitForTimeout(300); } // reload only when the page changed
          }
        }
      }
      if (info.type === 'input') add('label, not just placeholder', !!info.name);
      if (info.type === 'button') add('height ≥32', info.h >= 32, `${info.h}`);
      if (info.type === 'table') add('header scope', info.scope);
      if (['table', 'list', 'chart'].includes(info.type) && info.dynamic) add('empty state exists', info.states.some((s) => s.s === 'empty' && s.ok), info.states.map((s) => s.s + (s.ok ? '' : ' missing')).join(','));
      if (info.type === 'status') add('announced (live region)', info.hasLive);
      if (info.type === 'image') add('alt + fixed size', info.imgOk && info.tag === 'img', info.tag === 'img' ? '' : 'mark the <img> itself');
      if (info.type === 'nav') add('landmark', info.tag === 'nav' || info.role === 'navigation');
      rows.push({ w, type: info.type, id: info.id, pass: checks.every((c) => c.ok), n: checks.length, fails: checks.filter((c) => !c.ok).map((c) => c.k + (c.d ? ` (${c.d})` : '')), svgText: info.svgText });
    }
    await page.close();
  }
  await browser.close();
  const failed = rows.filter((r) => !r.pass);
  for (const r of rows) console.log(`${r.pass ? 'PASS' : 'FAIL'}  ${String(r.w).padEnd(5)} ${r.type.padEnd(8)} ${r.id.slice(0, 32).padEnd(32)} ${r.n - r.fails.length}/${r.n}${r.fails.length ? '  ✗ ' + r.fails.join('; ') : ''}`);
  const tally = {}; failed.forEach((r) => r.fails.forEach((f) => { const k = f.split(' (')[0]; tally[k] = (tally[k] || 0) + 1; }));
  const svg = rows.filter((r) => r.w === widths[0] && r.svgText);
  console.log(`\n${rows.length - failed.length}/${rows.length} component checks passed in ${((Date.now() - t0) / 1000).toFixed(1)}s${only.length ? ` (only: ${only.join(', ')})` : ''}`);
  if (Object.keys(tally).length) console.log('Failing checks: ' + Object.entries(tally).map(([k, v]) => `${k} ×${v}`).join(', '));
  if (svg.length) console.log(`Not checked: ${svg.reduce((a, r) => a + r.svgText, 0)} SVG text labels in ${svg.map((r) => r.id).join(', ')}; check them in a screenshot`);
  if (!rows.length) console.log('No components matched. Mark components with data-component, or check --only.');
  if (jsonOut) fs.writeFileSync(jsonOut, JSON.stringify({ url, widths, only, rows }, null, 2));
  process.exit(failed.length ? 1 : rows.length ? 0 : 2);
})();
```

---

# Page check (G4)

Render and look, at most three rounds: screenshot desktop and phone, critique, fix the top problems, look again. Run the full gate.

- **Swap test:** swap your typeface for the usual one and your layout for a template; where nothing would change, you defaulted. Swap in another product's name; if the screen still fits, push copy, visual and signature harder.
- **Squint test:** blurred, hierarchy still reads and nothing jumps out.
- **Signature test:** point to the places the signature appears.
- **Token test:** read the CSS variables aloud; they belong to this product (`--ink`, `--parchment`), not a template (`--gray-700`).

Judgment checklist (what the gate can't measure):
- [ ] Direction followed throughout; decisions.md exceptions are justified
- [ ] One focal point per view; groups tight inside, looser between
- [ ] One tinted neutral ramp, four text roles, one accent used rarely
- [ ] No hue gradients, gradient text, glows, colored shadows, blobs or emoji
- [ ] Type fits the character; weights 400–600; sentence case; five sizes at most
- [ ] Copy: no exclamation marks, greeting headlines, hype words or unverified claims
- [ ] Every state present: active, disabled, loading, error (hover, focus, empty are gated)
- [ ] First screen composed as a whole; no dead band; a real visual or product preview
- [ ] Reduced motion respected; no bouncy or ambient motion
- [ ] Tab order follows reading order; existing flows still work
- [ ] SVG labels the gate skipped are legible in the screenshot

---

# Report (G5)

```
Mode and surface:
Direction: [the block, or "taken from brand"; "assumption" if unconfirmed]
Decisions: .design/decisions.md [exceptions logged: n]
Gate: [n/n passed at 1440 and 390; open issues with cause]
Not checked: [SVG labels, widths, flows you couldn't run]
Changes: [Polish: a few lines per pass; Build: sections built]
Image prompts written: [or none]
Sample content to confirm: [or none]
Unverified claims found: [or none]
Brand conflicts: [rule, spec, one-line change; or none]
Review only: findings by severity, then the top three changes
```

Then offer to save to `.design/system.md`: direction and feel, depth strategy, spacing base and density, type scale and weights, palette tokens, and component patterns used twice or more with their values (e.g. `Button primary: 36 h · 12/16 pad · 8 radius · 14/500`). When it exists, hold to it and flag drift.

# Working style

Don't announce modes or narrate process; lead with the recommendation and its reasoning. If an inline rendering tool exists, show directions and components (swatches, type scale, before and after) rather than describing them; reasoning stays in the text. Keep updates short.

---

Built from: frontend-design (Anthropic, Apache 2.0); unslop by Damir Sokolovsky (@heydamir, https://github.com/heydamir/unslop), CC BY 4.0, condensed and adapted; interface-design by Damola Akinleye (MIT); heuristic-evaluation and accessibility-audit from Designer Skills by MC Dean (MIT); restructured as a gated workflow from the Anthropic design skill. Keep this credit in any copy or adaptation.