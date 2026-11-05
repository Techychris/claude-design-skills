# Accessibility for explorables (WCAG 2.2)

These criteria are the hard rules. They are normative, from WCAG 2.2.

## Contents
- Criteria that matter most
- Patterns
- What the audit can and can't check

## Criteria that matter most

| SC | Level | Requirement | Explainer-specific note |
|---|---|---|---|
| 1.1.1 Non-text content | A | Text alternative for non-text content | Every explorable and chart gets a prose or table equivalent next to it |
| 1.4.1 Use of color | A | Color is not the only means of conveying information | Pair color with a word, shape, or position |
| 1.4.3 Contrast (minimum) | AA | Text ≥ 4.5:1; large text ≥ 3:1 | Large text means ≥ 24px regular or ≥ 18.66px bold |
| 1.4.11 Non-text contrast | AA | UI components and meaningful graphics ≥ 3:1 | Slider tracks, chart marks, focus rings |
| 1.4.12 Text spacing | AA | No loss of content when users set line-height 1.5, paragraph spacing 2em, letter spacing 0.12em, word spacing 0.16em | Avoid fixed-height text boxes |
| 2.1.1 Keyboard | A | All functionality operable by keyboard | Draggable points need arrow-key equivalents |
| 2.2.2 Pause, stop, hide | A | Auto-moving content lasting more than 5 s can be paused | Looping simulations need a pause button |
| 2.3.3 Animation from interactions | AAA | Motion triggered by interaction can be disabled | Honor `prefers-reduced-motion` |
| 2.4.7 Focus visible | AA | Keyboard focus indicator is visible | Don't remove outlines without replacing them |
| 2.4.11 Focus not obscured | AA | Focused item not hidden by sticky headers or overlays | Check sticky scrollytelling graphics |
| 2.5.8 Target size (minimum) | AA | Pointer targets ≥ 24×24 CSS px, with spacing exceptions | 44×44 is the AAA level (2.5.5) |
| 4.1.2 Name, role, value | A | Controls expose name, role, state | Prefer native `<input type="range">` and `<button>` |
| 4.1.3 Status messages | AA | Status changes announced without moving focus | Use `aria-live="polite"` on readouts |

## Patterns

**Slider with announced value and static equivalent:**
```html
<label for="rate">Interest rate</label>
<input type="range" id="rate" min="0" max="10" step="0.5" value="5">
<output id="rate-out" for="rate" aria-live="polite">5%: balance doubles in about 14 years</output>
<p class="static-equivalent">At 5%, a balance doubles in about 14 years; at 10%, about 7.</p>
```

**Reset control:** a real `<button type="button">Reset</button>` that restores the initial state and announces it through the live region.

**Reduced motion in JavaScript:**
```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const duration = reduce ? 0 : 1000;   // data transition ≈1 s per stage
```

**Draggable points:** make each point focusable (`tabindex="0"`, `role="slider"`, `aria-valuenow`) and move it with the arrow keys.

**Charts:**
- Put an accessible summary sentence before the chart.
- Offer a data table, in a `<details>` element or adjacent.
- Don't rely on hover tooltips; label key values directly.

## What the audit can and can't check

`scripts/audit.py` checks:
- text contrast against the nearest opaque background;
- body font size and characters per line;
- horizontal overflow;
- target size;
- JS-off content;
- reduced-motion transitions;
- image alt text;
- heading order;
- console errors.

Manual checks:
- keyboard order and usefulness;
- focus visibility;
- contrast of text over images or gradients;
- non-text contrast of chart marks;
- quality of alt text and static equivalents;
- whether the reduced-motion version still teaches;
- text-spacing override (test with a bookmarklet or user stylesheet).

For deeper automated checks, add axe-core (`@axe-core/playwright`) and Lighthouse. Their rule IDs change between versions, so check current docs.
