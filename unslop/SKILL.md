---
name: "unslop"
description: "Polish or redesign a UI so it stops looking AI-generated: audit the slop, set a direction from the product, fix it in nine passes. Use for unslop, polish, clean-up or de-AI requests."
---

# Unslop

Adapted from unslop by Damir Sokolovsky (@heydamir, https://github.com/heydamir/unslop), licensed CC BY 4.0. This version condenses the original SKILL.md and its references (signs, tokens, visuals) into one file, drops the story-video recorder and the reference images, and adds a rule for screens built to an existing brand or design spec. Keep this credit in any copy or adaptation.

Vibecoded UI fails in predictable ways. Every surface glows, every label has an emoji, spacing is whatever got typed that day, and the copy shouts. Unslopping fixes the craft and keeps the product. Features, content and section order stay. What changes is that every size, color, word and image becomes deliberate.

Removing slop is half the job. A clean screen that could belong to any product is the next template. Every run ends with a screen only this product could have.

Slop spreads color and effects over the chrome (backgrounds, buttons, borders, labels). Craft keeps the chrome quiet and puts the richness into one or two moments of content, like a rendered object, a chart drawn with care or an image from the product's world.

Work like a designer doing a redline pass, one layer at a time, across the whole screen.

## What good looks like

- **One bright element.** Each screen has one polished thing that carries the color and craft. Everything around it is quiet.
- **Quiet chrome.** Navigation, buttons and text use tinted neutrals and one accent. Nothing glows.
- **A clear idea.** You can say in one sentence what the visual shows and why it belongs to this product.
- **Text on calm space.** Headlines sit on space left empty for them, short and specific, with one primary and one secondary action.
- **Real product, real material.** Previews look like the real app with plausible data.

## Run it

1. **Look at the screen.** Find the files that render it. Render it and take a screenshot if you can (Playwright, a browser tool), so you judge what people see, not only the code.
   - Only a link to a live site: save or rebuild the page as one static HTML file and work on that copy. Say in the report that the result is a redesigned page to hand to whoever owns the site.
   - Only a screenshot: rebuild it as one static HTML file first and treat that as the original.
2. **Audit.** Go through the Signs list below and write every sign you find, one line each, with where it lives.
3. **Decide how much to change.**
   - **Heavy slop** (many signs across color, type, icons, copy): full process.
   - **Light slop** (mostly designed, a few signs): polish mode. Fix only what the audit found, take the direction from the existing brand, keep palette, type, layout and visual. Bigger ideas go in the report as suggestions.
   - **No slop:** say so and suggest two or three small refinements with exact values. Apply only if the user agrees.
4. **Set the direction and stop.** Write the five Direction lines. Show the audit and direction and wait for an answer before editing. Skip the wait when the user said to just do it, or in polish mode when a brand or design spec already fixes the direction.
5. **Fix in nine passes, in order.** Finish each pass across the whole screen before the next. Spacing first, copy before type and layout, visuals and motion last.
6. **Check.** Run the checklist, render again, compare with the audit. Fix anything left.
7. **Report** the direction, a few lines per pass, any image prompt written, and any conflicts with the brand (see below).

Keep a run quick: render to check at most three times. When the screen has behavior (forms, flows), re-run the flows after the passes so polish doesn't break function.

### Existing brand or design spec

If the product has a real brand or a written design spec (logo, colors, typefaces, weights), it wins over the generic rules here. Where a rule below conflicts with it (for example the spec chose an 800-weight display face, or a gold primary button in dark mode), keep the spec and list the conflict in the report as a decision for the user, with the one-line change that would apply the rule. A violet-to-blue gradient, sparkles or glow are slop even in a logo unless the user says they are brand.

## Direction

Five short lines, derived from what the product does and who it is for, never from what is trending.

- **Product.** What it does and for whom, in one plain sentence.
- **Character.** Two or three concrete words, like `calm, exact, a little warm`. Not clean, modern, sleek, minimal or premium.
- **World.** The place or material the product belongs to (a note app near paper and ink, a monitoring tool near instruments and night shifts). Sets the neutral tint, the accent and the visual.
- **Moments.** One or two places where the screen gets rich color and detail, chosen from what the product shows.
- **Signature.** One small detail only this product would have, used consistently. One, not five.

## 1. Spacing

- Everything on a 4px grid. Margins, paddings, gaps, fixed heights are multiples of 4. A 2px nudge inside small controls is fine.
- Same thing, same size: one row height and gap per list, one padding per card row.
- Space shows grouping: smaller inside a group than between groups.
- Things line up: icons in one column, labels on one line, numbers right-aligned in one column.
- Padding follows density: compact panels ~16, cards 20 to 24, page edges 24 to 32.
- Navigation rows 32 to 36 tall with 2 to 4 between; section labels 24 above, 8 below.
- Replace one-off values like `mt-[13px]` with scale steps.

## 2. Color

- One neutral ramp tinted toward the world. Background, surfaces, borders, text all from it.
- In apps and dashboards surfaces stay near-neutral; the content carries the color. Landing pages can tint surfaces further.
- Three text roles: primary, secondary, muted.
- One accent in the chrome, used rarely: primary action, selection, the one number that matters.
- Inside the moments color can be rich, as long as each color means something.
- A real brand color becomes the accent and leaves the surfaces.
- Accent with text on it reaches 4.5:1; darken it or use dark text if not.
- On dark themes the primary button can be an off-white with dark text.
- Semantic colors carry meaning only, toned to the palette.
- Remove hue gradients on surfaces, gradient text, colored glows and shadows, radial washes, blobs, neon borders.
- Borders are hairlines: primary text color at 6 to 10% opacity.
- Depth: on dark, surface steps and hairlines; on light, small soft neutral shadows.
- A gradient only as a small tone shift inside one neutral, never hue to hue.

## 3. Icons

- Every emoji used as an icon or label decoration becomes a line icon from one set (the project's, else lucide).
- One size and stroke: 16 or 18px, stroke 1.5.
- Icons take their text role's color, never their own.
- Same icon box width in every row, fixed 8 or 10 gap to the label.
- Drop icons that add nothing. Categories that need color get a small status dot.

## 4. Copy

- Headlines say what the product does for whom, using facts already on the page.
- No exclamation marks in interface text.
- No greeting headlines like `Welcome back, Name! 👋`; the title names the context.
- Short labels: `Search`, not `Search anything...`.
- A change says what it compares to: `+12% vs last month`.
- Headlines, labels, buttons, captions and one-sentence messages end without a period. Paragraphs of several sentences keep theirs.
- No hype words (supercharge, seamless, unlock, magic, revolutionize, game-changing), no `AI-powered` everywhere.
- Unverifiable claims (`Loved by 10,000+ teams`, `10x faster`): ask; make quiet and specific if real, remove otherwise. List them in the report.
- Mock data looks real: plausible numbers and names.
- Badges like `PRO`, `New ✨`, `Beta 🚀` go unless needed, then quiet text.

## 5. Type

- Type fits the character; keep a real brand font. One interface family plus at most one partner (a mono for figures, or a display face for large headlines).
- A few sizes, weights 400 and 500, 600 for rare emphasis. No 700 to 900 headings (unless a brand spec says so; see above), no gradient text.
- Hierarchy from size and color, not weight.
- Sentence case everywhere; no uppercase tracked labels.
- No negative letter spacing on small text.
- Numbers use `tabular-nums` and one format.
- No italic for emphasis.

## 6. Layout

- Keep sections and their order; inside a section alignment and proportions may change.
- Apps keep real app proportions: shell fills the viewport, sidebar 240 to 280, content fluid, capped ~1440 to 1600. Never shrink an app into a narrow centered column.
- Strongest landing hero: one scene image edge to edge, subject on one side, headline on the calm part, product view rising from the bottom edge.
- Without a scene: asymmetric split (visual at least half) or text over a large product view. Centered stacks only for short heroes with no visual.
- Long headlines align left.
- One primary action, at most one secondary.
- Quiet navigation: logo, existing links, one button; log in as a text link.
- Compose the first screen as a whole with no dead empty band (watch grid cells stretched to a taller neighbor).
- On small screens stack in reading order; simplify dense previews instead of zooming them; no text under 11px.

## 7. Details

- Nested radius: inner = outer minus padding, never below 4. Controls 8 to 10, cards 12 to 16, panels 14 to 20. Not everything is a pill.
- Counts and meta become quiet text, not pills.
- Keyboard shortcuts become small keycaps.
- Charts on a muted grid with muted mono labels; one main chart clearly biggest; one accent per chart; type fits the data (trend = line, comparison = bars, share = stacked bar or list, goal = progress bar).
- Stat cards are numbers: label, figure, change with comparison. No sparklines or icons to fill them. Don't repeat a figure already shown elsewhere on the screen.
- Vary sizes: not a row of identical cards. Compact stats above one wide chart, or a wide chart beside a narrow list.
- Active state: small surface step with a hairline, not a gradient glow.
- Hover and focus states exist inside the palette, with a visible focus ring.
- Logo: product name in the main family plus a simple flat mark. No gradient wordmark or sparkle tile.
- The signature detail appears where it belongs and nowhere else.

## 8. Visuals

- Remove decorative filler: glossy blobs, orbs, nebulas, floating cubes, glowing grids, brains, robots.
- Dashboards and app screens rarely need generated images; their moments come from the product (a careful chart, figures set well, real content, a status that feels alive). Physical things like a payment card are usually better built in code.
- A landing hero gets a visual that shows something true. First choice with an image tool: a wide scene from the world with calm space for text. Without one, a coded preview of what the page already promises, carrying one moment.
- Write the subject as one plain sentence first. If you can't, it isn't clear yet.
- Styles that work: painted background art; a cinematic photo of one object; soft matte 3D; a studio-lit product object; light and optics on a dark field; engraving or print only when the whole page lives in that style; a code treatment (glyphs, dots, duotone) in the page palette.
- What fails: asking a model for grain or paper texture (it bakes in a checker pattern; add texture in code), a print style on one image of an otherwise plain modern page, busy collages, purple-blue glossy abstractions.
- Prompt recipe, in order: subject sentence; simple setting; light and palette (name the page background color); one style; composition (where the subject sits, calm space for text); exclusions (no text, letters, logos, UI, watermark); aspect ratio at twice display size.
- Before any paid generation, show the prompt, model and size and ask. Run once, judge, change the prompt rather than rerolling. Save into project assets.
- No image tool: say so, offer to connect one, otherwise leave an empty slot of the right size (plain surface step, no text) and put the prompt in the report.
- On the page: WebP or AVIF at 2x, real alt text, edges masked into the page color, fixed dimensions, no parallax.

## 9. Motion

- Remove looping motion on things that aren't live (pulse, ping, shimmer, breathing glows, floating, parallax).
- Remove `transition-all`, bouncy springs, `hover:scale` on cards.
- Keep motion that explains: quick color or surface change on hover, tiny scale down on press (0.97 to 0.98), menus fade and rise a few pixels, changed numbers tween.
- Transition only color, background, border, opacity, transform, named explicitly. Never width, height, top, left, margins or large blurs.
- One easing curve, `cubic-bezier(0.22, 1, 0.36, 1)`. Durations: hover/press 120 to 180ms, menus 160 to 220ms, entrances 300 to 500ms, stagger 40 to 60ms over at most six items.
- At most one entrance on load: a short fade and 6 to 12px rise.

## Signs of slop (audit list)

Surfaces and color
- Purple-blue or violet-pink gradients on backgrounds, cards, buttons, active nav → one neutral surface
- Gradient text in headings, numbers, logo → solid primary text
- Colored glows and drop-shadows, glowing pills → remove; depth from surface steps and hairlines
- Radial washes, blurred blobs behind content → remove
- Neon or high-contrast colored borders → hairline at 6 to 10%
- Many near-identical tints for text → three text roles
- Everything highlighted → one accent used once or twice per screen
- Glass cards with inner highlight and colored shadow → plain raised surface with hairline

Type
- Headings at 800 or 900 → 400 to 500, size for hierarchy (brand spec excepted)
- UPPERCASE TRACKED LABELS → sentence case
- Too many sizes and weights → a few sizes, weights 400 and 500
- Mixed number formats → one format, tabular figures
- Negative tracking on small text → zero or slightly positive
- Italic for emphasis → color or weight

Icons
- Emoji as nav icons, label decoration, status (🏠 📥 🚀 💰 ⚠️ 📈 🔥 🔒 ✉) → one line icon set or nothing
- Emoji inside pills and counts → plain number
- Icons in many sizes and colors → one size, one stroke, text-role color
- Icons nudged off the column → same icon box width every row
- ✨ for anything AI → remove

Spacing
- Arbitrary values (13px, 7px, 11px, 31px) → 4px-scale steps
- Rows with different heights or gaps → one height, one gap
- Groups closer to neighbours than to their own items → tighter inside, looser between
- Uneven padding in sibling cards → one padding
- Big gap above a section, cramped below → balanced rhythm

Copy
- Greeting headlines → page or period as the title
- Exclamation marks → plain statement
- Changes without a reference → `+12% vs last month`
- Wordy placeholders → `Search`
- Hype words → what the thing actually does
- Trailing periods on labels, buttons, captions, toasts → none
- Fake-looking data (`$123,456`, `[X]`) → plausible numbers

Components
- Glowing pills for counts, plans, shortcuts, status → quiet text or keycap
- PRO / New ✨ / Beta 🚀 everywhere → remove or one quiet text badge
- Everything a full pill → radius by size, nested radius math
- Rainbow, glowing or pill bars; uppercase day labels → one or two series, muted grid, one highlight
- Every chart in shades of the accent → neutral steps, accent on the one thing that matters
- Sparklines or mini bars on every stat card → number, label, change
- Equal cards side by side with the same content → one main block, compact stats, varied widths
- Gradient-tile logo with sparkle, glossy orb mark → product name as text plus a flat mark
- Decorative tags on rows that carry no status (an "Event" chip on every event) → remove

Landing pages and heroes
- Pill badge above the headline (`✨ Introducing X 2.0`) → remove, or a quiet text link if real news
- Headline that fits any product → what this product does for whom
- Shimmer on the headline → solid text
- Floating blobs, orbs, grids, glowing lines → plain background or one real visual
- Everything stacked and centered → asymmetric split or text over a large product view
- Three or more buttons, chips or avatars under them → one primary, at most one secondary
- Unsourced social proof → ask, then quiet and specific, or remove
- Feature cards with emoji, bold title, vague line → fewer features, concrete copy

Visuals
- Glossy 3D blobs, chrome shapes, purple nebula → the product or one concrete metaphor
- Robots, brains, circuits, holograms for AI → remove or show what the AI produces
- Text or fake UI baked into an image → real text in the page
- Image with a hard edge on a different background → matched background, soft mask
- A visual on every section → one, usually the hero

Motion
- Pulse, ping, breathing glows on non-live things → static
- `transition-all`, `hover:scale` → color or surface step, tiny press scale
- Bouncy springs → one ease-out curve
- Everything flying in from different directions → one short fade and rise
- Animating width, height, top, left → transform and opacity

Template look (not slop, but what cleaned-up screens fall back to)
- Pure grey page, Inter, white text, old brand color on one button, for a warm or bright product → ramp tinted toward the world, accent from it
- Headline that still fits after swapping the product name → use this product's nouns
- Empty-box or generic hero visual → coded preview or image from the world
- Every product getting the same layout, type, palette → let the direction choose

## Tokens

Spacing scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128.
- Inside a control 4 to 12; between related items 2 to 8; between groups 12 to 24; between sections 32 to 64 (landing 80 to 128).
- Row heights: 32 compact, 36 default, 40 to 44 touch.
- Hero: 96 to 128 from nav to headline on desktop, 48 to 64 on mobile.

App layout: sidebar 240 to 280; page padding 24 to 32; content capped ~1440 to 1600; top bar 56 to 64; main chart at least two thirds of content width and 280 to 360 tall.

Neutral ramps (apps and dashboards: graphite or similarly grey; landing pages: tint matching the world; warm = paper, wood, food, craft; ink = night, sky, water, technical).

| Dark role | Graphite | Warm | Ink |
| --- | --- | --- | --- |
| Deepest (sidebar) | #0f0f10 | #12110f | #07080d |
| Page | #141415 | #161513 | #0b0d14 |
| Card | #19191b | #1c1a18 | #11141c |
| Raised (active row, input) | #232325 | #262421 | #1a1e28 |
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

Hairlines: primary text at 8%. Muted text only for meta and captions, near 4.5:1 on its surface. Semantic: positive #4cc38a dark / #16a34a light; negative #e5484d dark / #dc2626 light.

Accent: keep a real brand color; otherwise take it from the world (warm: amber, coral, ember; cool: cobalt, teal, sky; natural: moss, sage). Avoid purple-blue unless the brand is purple. Covers a few percent of the screen.

Buttons: hero 44 to 48 tall, nav 32 to 36, side padding 16 to 20. Primary on light: primary text color fill with white text, or the accent. Secondary: raised surface with hairline.

Type families by character:
| Character | Interface | Optional partner |
| --- | --- | --- |
| Precise, technical, calm | Geist, Inter, IBM Plex Sans | Geist Mono, IBM Plex Mono, JetBrains Mono |
| Warm, friendly, human | Instrument Sans, DM Sans, Figtree | Instrument Serif or Newsreader for the hero headline |
| Editorial, crafted | Inter or Instrument Sans | Newsreader, Instrument Serif, Fraunces for headlines |
| Playful, bold | Space Grotesk, Bricolage Grotesque | a mono for small labels |
A display serif belongs to large headlines only, never labels or buttons.

Type scale:
| Use | Size | Line height | Weight |
| --- | --- | --- | --- |
| Small labels, meta, counts | 12 | 16 | 400 |
| Secondary text, captions | 13 to 14 | 20 | 400 |
| Body, nav items | 14 to 15 | 20 to 22 | 400 to 500 |
| Logo wordmark | 16 to 18 | 1 | 500 to 600 |
| Hero subhead | 18 to 20 | 28 to 30 | 400, max 36rem wide |
| Card figures | 28 to 32 | 1 | 500, tabular |
| Page title | 28 to 36 | 1.15 | 400 to 500 |
| Hero headline | 56 to 72 desktop, 36 to 44 mobile | 1.02 to 1.08 | 400 to 500 |
Letter spacing 0 under 16px; -0.02em from 40px; -0.03em from 56px.

Radius: keycap, tag, small button 4 to 6; row, input, button 8 to 10; card 12 to 16; panel or window 14 to 20. Inner = outer minus padding, minimum 4.

Icons: lucide, 16 or 18px, stroke 1.5, muted or secondary color, 8 to 10px gap.

Depth: dark, surface steps plus hairline (active row may take `inset 0 1px 0 rgba(255,255,255,0.12)`); light, `0 1px 2px rgba(0,0,0,0.05)` small, `0 8px 24px rgba(0,0,0,0.06)` floating.

## Do not

- Rename the product. Keep a real logo; redraw a slop logo flat (wordmark alone, or a simple glyph in one solid color).
- Change what the product is, its features, content or section order, unless asked. Meaningless placeholder content may become meaningful.
- Replace removed decoration with new decoration, or swap one trend for another (glass, grain, noise, neon, bento).
- Invent features, claims or data.
- Fall back to the same look for every product.

## Checklist

- [ ] Direction written (or taken from the brand spec) and every pass follows it
- [ ] Every spacing value on the 4px scale; equal things equal
- [ ] Icons, labels, numbers each in one aligned column
- [ ] One tinted neutral ramp, three text roles, one accent with enough contrast
- [ ] No hue gradients, gradient text, glows, colored shadows, color blobs
- [ ] No emoji left in the interface
- [ ] One icon set, one size and stroke
- [ ] Type fits the character; weights 400 to 600; no uppercase tracked labels, italic emphasis or negative tracking on small text
- [ ] No exclamation marks, no trailing periods on short strings, no greeting headline, no unverified claims
- [ ] Numbers in one format with tabular figures
- [ ] Nested radii add up
- [ ] A hero has a real visual or product preview with a moment, never filler or a labeled placeholder
- [ ] First screen composed as a whole, no dead empty band
- [ ] No looping or bouncy motion; one easing curve; no animated layout properties
- [ ] Existing flows still work after the passes
- [ ] Brand-spec conflicts listed in the report
- [ ] Template check: swap in another product's name; if the screen still fits, push the copy, visual and signature harder