---
name: "web-motion"
description: "Use when asked to animate web UI, add or tune transitions, fix janky or laggy animation, handle prefers-reduced-motion, review or audit motion, or name an effect. Covers CSS, WAAPI, Motion, GSAP, three.js/WebGL and custom elements."
---

# Web Motion for UI Components

One skill for deciding whether something should move, how it should move, and whether it moves well. It merges three MIT-licensed sources (credits at the end) and settles the places where they disagree, so you don't have to.

**Scope:** motion on web interfaces. That covers component states, entrances and exits, gestures, scroll, page transitions, and 3D scenes in three.js. It does not cover video, Lottie authoring, or React Native. §13 adds a short set of principles for building reusable components, beyond their motion.

**The bar:** motion has to *feel* right, not just run. An animation that works but feels sluggish, scales from the wrong point, fires too often, or drops frames counts as a regression.

**Why the small details matter:** users rarely notice any single one, and that is the point. When something behaves exactly as they assumed, they move on without thinking about it. Many small correct details add up to an interface people like without knowing why, and when most software works well enough, that feel is what sets a product apart. Taste here is a trained skill, not a preference: study interfaces that feel right, reverse engineer their motion, and work out why it works.

---

## Pick the mode

| The user wants… | Mode | Output |
| --- | --- | --- |
| "Animate this", "add a transition", "make it feel alive" | **Build** | Working code that passes the Review standards on first try |
| "Review my animation", a diff or a component | **Review** | Findings table + tiered verdict + Block/Approve |
| "Audit our motion", "what should animate?", "too much animation" | **Audit** | Add / Reduce / Remove lists + verdict |
| "What's this effect called?", "how do I describe…" | **Explain** | Name the technique, one sentence on its mechanism, a minimal snippet, and when not to use it |

Building always passes through the **Gate** first. A Gate verdict of "don't animate" is a success, not a dodge. **Build output:** state the Gate verdict and the purpose, the personality, then the code (including the reduced-motion variant), then any limitations.

---

## 1. The Gate: should this animate at all?

Answer in order. Stop at the first "no".

**1. Frequency.** How often will a user see it?

| Frequency | Decision |
| --- | --- |
| 100+ times/day (keyboard shortcuts, command-palette toggle) | **No animation. Ever.** |
| Tens of times/day (hover, list navigation, tab switches) | Remove or drastically reduce |
| Occasional (modals, drawers, toasts, dropdowns) | Standard animation |
| Rare / first-time (onboarding, success, celebrations) | Delight allowed |

**Never animate actions triggered by keyboard shortcuts** (⌘K, shortcut-driven toggles, list navigation). Repeated hundreds of times a day, the animation makes them feel delayed. A dialog opened with Enter on its button animates like any click. Raycast has no open/close animation at all, which is the right call for something opened hundreds of times a day.

**2. Purpose.** Name one, or don't build it:
- **Feedback:** the interface heard the user (press scale, toggle).
- **State indication:** something changed (morphing button, check draw-in).
- **Spatial consistency:** where it came from and where it goes (toast enters and exits the same edge).
- **Preventing a jarring change:** something appearing or disappearing abruptly would feel broken.
- **Attention / staging:** guiding the eye to the one thing that matters now.
- **Explanation:** showing how something works (marketing and onboarding only).
- **Delight:** only at the rare/first-time tier.

**3. Function.** Data the user is reading or acting on (tables, charts in a work tool, form values) should not move for style.

**4. Budget.** Can it stay inside the duration and frame budget below? If not, simplify or drop it.

---

## 2. Personality: pick once per product

Choose **one** archetype and apply it to about 90% of motion. A specific moment may borrow another one (say, a corporate dashboard with a playful success state).

| Archetype | Use for | Signature easing | Overshoot | Component duration scale |
| --- | --- | --- | --- | --- |
| **Crisp** (default for product UI) | dashboards, SaaS, admin, dev tools, finance | `--ease-out` | 0–3% | 1.0× |
| **Playful** | consumer, social, onboarding, creative tools | spring `bounce: 0.2–0.3` | 10–20% | 1.0× |
| **Premium** | editorial, luxury, portfolios, marketing pages | `cubic-bezier(0.4, 0, 0.2, 1)` | 0% | 1.3–1.6×, **marketing/rare surfaces only** |
| **Energetic** | games, sports, music, events | `cubic-bezier(0.16, 1, 0.3, 1)` (expo-out) | 15–30% | 0.8× |

**Brand motion identity** is three constants. Write them as tokens (§4):
1. One signature easing for about 80% of motion.
2. A duration palette (fast / base / slow).
3. One consistent entrance pattern.

Cohesion beats correctness of any single curve. The motion should match the component's look and the product's tone.

---

## 3. Build: decisions in order

### 3.1 Pick the cheapest tool that works

| Need | Tool |
| --- | --- |
| Hover, press, color, class/attribute state toggle | **CSS transition** |
| Entry on mount, no JS state | **CSS `@starting-style`** (fallback: `data-mounted` set after first frame) |
| Predetermined motion that must stay smooth while the page is busy | **CSS animation** (can run off the main thread) |
| Programmatic control, CSS performance, no library | **WAAPI** `element.animate()` |
| Springs, exit animations, layout/shared-element, gesture-driven values | **Motion** (motion.dev, formerly Framer Motion) |
| Scroll-linked effects, parallax | **CSS scroll-driven animations** (`animation-timeline`), gated by `@supports` (§6.1) |
| Complex timelines, scroll-scrubbed sequences | **GSAP** (+ ScrollTrigger) |
| Real lighting, materials, depth, product configurators | **three.js** (or React Three Fiber), per §6.2 |
| Same-document or cross-page view morphs | **View Transitions API** (progressive enhancement; always provide a no-animation fallback) |

If what's needed is a **component** (toast, drawer, dialog, combobox, menu), use a headless primitive (Base UI, Radix, React Aria, native `<dialog>`/`popover`) and animate it. Don't hand-roll a component just to animate it, or you lose focus management and ARIA.

### 3.2 Pick the properties

- **`transform` and `opacity` by default.** They skip layout and paint. `clip-path` and `filter` are acceptable additions, but compositor support varies: Chromium composites `clip-path`, while Firefox (bug 1619465) and Safari still don't. Profile them before relying on them.
- **Swap down a cost tier:**

| Instead of | Animate |
| --- | --- |
| `width` / `height` / `padding` to grow | `scale()` |
| `top` / `left` / `margin` to move | `translate()` |
| `display` / `visibility` swaps | `opacity` (+ `transition-behavior: allow-discrete` for `display`) |
| `box-shadow` | cross-fade a pseudo-element's opacity (always compositable); `filter: drop-shadow()` has no spread/inset and isn't composited in every engine, so profile it |

- **Minimum properties:** one is direct, two is polished, three or more is probably too much.
- **Never `scale(0)`.** Start from `scale(0.9–0.97)` plus `opacity: 0`. Nothing real appears from nothing.
- **Never opacity-only for an *important* state change.** Pair it with a small translate or scale so the change is legible.
- **`transform-origin` at the trigger** for popovers, dropdowns, menus and tooltips (`var(--transform-origin)` in Base UI, `var(--radix-*-content-transform-origin)` in Radix). **Modals are exempt** and stay centered.
- **Percent translates** are relative to the element's own size. `translateY(100%)` hides a drawer whatever its height. Prefer them over hard-coded px.
- **`scale()` scales children too.** Text and icons shrink with a pressed button, which is what press feedback wants. Use it instead of changing size or font size.
- **Never `transition: all`.** List the exact properties.

### 3.3 Easing

| Motion | Easing |
| --- | --- |
| Entering | `--ease-out` (strong ease-out) |
| Exiting | `--ease-out`, shorter duration (see conflict note in §9) |
| Moving/morphing on screen | `--ease-in-out` |
| Hover / color | `ease` or `--ease-out` at ≤150ms |
| Constant motion (spinner, marquee, progress, hold-to-confirm fill) | `linear` |
| Ambient loops (breathing, pulse) | sine in-out: `cubic-bezier(0.37, 0, 0.63, 1)` |

**Never `ease-in` for UI responses.** It delays movement at exactly the moment the user is watching. `ease-out` at 200ms *feels* faster than `ease-in` at 200ms.

**Built-in CSS keywords are weak.** Use strong custom curves on deliberate motion. Find variants at easing.dev or easings.co rather than inventing them.

**Never `linear` for spatial movement.** Linear is only for rotation, progress and time-based fills.

### 3.4 Duration

| Element | Duration |
| --- | --- |
| Hover feedback | 100–150ms |
| Button press / toggle | 100–160ms |
| Tooltip, small popover | 125–200ms |
| Icon state swap | 150–250ms |
| Dropdown, select, menu | 150–250ms |
| Card / list item enter | 200–300ms |
| Modal, dialog | 200–300ms |
| Drawer / sheet (large travel) | 300–500ms (drawer curve) |
| Page / route transition | 250–400ms |
| Marketing, explanatory, celebration | can exceed; still ends before it bores |

**Rules:**
- **Component UI stays under 300ms** unless the travel distance is large (drawers, sheets) or the surface is rare. Anything slower needs a stated reason.
- **Distance scales duration:** for each doubling of travel, add about 25–30% (100px = base, 200px ≈ 1.3×, 400px ≈ 1.6×).
- **Weight scales duration:** heavy surfaces (modals, overlays) sit at the slow end with no overshoot; light ones (badges, tooltips) sit at the fast end and may overshoot 5–15% if the personality allows it.
- **Exit faster than enter:** exits take 50–75% of the entrance duration.
- **Asymmetric where the user is deciding:** deliberate phases are slow (hold-to-delete: 1.5–2s linear) and the system response snaps (release: 200ms ease-out).
- **Perceived speed counts too:** a faster spinner makes loading feel faster, and once one tooltip is open, the next ones open instantly.

### 3.5 Springs

Use springs for gestures, interruptible motion, "alive" elements, and decorative pointer-following.

```js
// Perceptual config (easiest to reason about). Prefer this.
// Transition option objects (pass as `transition={…}` in Motion), not statements.
// `visualDuration` is when the motion visually reaches its target (any bounce settles after it);
// it overrides `duration` and follows the §3.4 budgets.
{ type: "spring", visualDuration: 0.25, bounce: 0 }   // Crisp
{ type: "spring", visualDuration: 0.35, bounce: 0.2 } // Playful

// Physical config, when you need control
{ type: "spring", stiffness: 300, damping: 30 }  // stiff, no visible bounce
{ type: "spring", stiffness: 200, damping: 15 }  // bouncy
```

- Keep bounce at 0–0.3. Use bounce only for drag-release, playful surfaces and celebrations. Errors and premium surfaces get no bounce.
- Springs keep velocity when interrupted, while keyframes restart from zero. Use them for anything the user might reverse mid-motion.
- For pointer-tracking effects, pass the value through `useSpring` instead of binding it raw, and only for decorative effects.

### 3.6 Interruption and exit

- **Transitions, not keyframes,** for anything triggered rapidly (toasts, toggles, anything the user can fire twice a second). Transitions retarget from the current value.
- **Exit the way it entered.** A toast that rises from the bottom leaves through the bottom, which makes swipe-to-dismiss feel obvious.
- **Never block input** while decorative motion plays (stagger, ambient, celebration).
- Handle invisible edge cases: pause timers when the tab is hidden, keep hover state across gaps between stacked items, and use pointer capture during drag.

### 3.7 Accessibility (ships with every animation)

- **`prefers-reduced-motion: reduce` means fewer and gentler animations, not zero.** This is how you meet WCAG 2.3.3 (Animation from Interactions, AAA): motion triggered by interaction can be disabled unless it is essential. That is standards guidance; no peer-reviewed study of vestibular-safe UI animation was found. Keep opacity and color fades that help comprehension. Remove translation, scale, auto-scroll, zoom and large rotation. **Parallax is the exception: turn it off entirely** (§6.1).
- **Gate hover motion** with `@media (hover: hover) and (pointer: fine)`, because touch fires false hovers on tap.
- **Auto-starting motion that lasts more than 5s needs a pause, stop or hide control** (WCAG 2.2.2). That includes any decorative repeating loop, whatever the length of one cycle. Loading indicators during a wait the user can't skip count as essential and are exempt. Never flash more than 3 times in any one second (2.3.1).
- **Focus:** never animate the focus ring away. Move focus into a dialog only after it is interactable, not after the animation ends. Return focus on close.
- **Announce state changes** that motion conveys (success, error, item added) through an ARIA live region or native semantics. Motion alone is not information.
- Users must be able to finish the task with every animation disabled.
- **Input parity:** press and hold must work from the keyboard (Space/Enter, with keydown/keyup for hold). Drag must have a single-pointer or button alternative (WCAG 2.5.7).

```css
/* Place after the base rules. Cover every state that sets a transform. */
@media (prefers-reduced-motion: reduce) {
  .toast, .toast[data-removed] { transform: none; transition: opacity 150ms ease; }
}
```

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
// Motion: const reduce = useReducedMotion();
```

Avoid a global `* { transition-duration: 0.01ms !important }` kill switch as your *only* strategy. It strips comprehension-aiding fades and is all-or-nothing. (0.01ms rather than 0 is used so end events still fire.) Write per-component reduced variants.

---

## 4. Tokens: write these first

```css
:root {
  /* Easing */
  --ease-out:    cubic-bezier(0.23, 1, 0.32, 1);    /* entrances, exits, responses */
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);   /* on-screen moves and morphs */
  --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);    /* iOS-like sheet/drawer */
  --ease-ambient: cubic-bezier(0.37, 0, 0.63, 1);   /* loops */

  /* Duration palette (Crisp). Scale per personality, §2 */
  --dur-instant: 100ms;  /* hover */
  --dur-fast:    150ms;  /* press, tooltip, toggle, exits */
  --dur-base:    200ms;  /* dropdown, popover, list item */
  --dur-slow:    300ms;  /* modal, larger surfaces */
  --dur-travel:  450ms;  /* drawer/sheet */

  /* Choreography */
  --stagger: 40ms;
}
```

Tokens set once at `:root` are cheap. **Values that change per frame** (drag distance, scroll progress) must **not** be inherited custom properties on a parent, because every descendant recalculates style each frame. Write `transform` directly on the moving element.

---

## 5. Choreography (multiple elements)

- **Lead with the hero.** The most important element moves first or most. Supporting elements are subtler in every dimension.
- **One shared origin or direction.** Mixed entrance directions read as chaos.
- **Stagger:** 30–80ms between items, and the **total cascade** (the last item's start delay) **stays under 500ms**. Cap the index so that holds: `transition-delay` (or `animation-delay`): `calc(min(var(--i), 6) * var(--stagger))` (6 × 80ms = 480ms), with `--i` set per item. Past the cap, animate the container instead.
- **One easing family** across a staggered group. Vary only the start time.
- **Shared triggers:** elements reacting to one event start within 50ms of each other and originate from the trigger.
- Leave 100–200ms of stillness before the next motion beat.
- **Layers:** primary (the action), secondary (shadow or icon reacting), ambient (background life). Components usually need only **primary**, occasionally secondary. Ambient belongs on marketing and hero surfaces, never in a work UI.
- **List items entering and leaving:** when an item's height animates together with its opacity, tune the two by eye. There is no formula; adjust until removal shows neither a gap nor a double fade.

---

## 6. Recipes

```css
/* Button press: any pressable */
.btn { transition: transform var(--dur-fast) var(--ease-out); }
.btn:active, .btn.pressed { transform: scale(0.97); } /* .pressed: set on pointerdown, for iOS where :active needs a touch listener */
```

```css
/* Popover / dropdown / menu: origin-aware. `data-starting-style`/`data-ending-style` and
   `--transform-origin` come from Base UI. Elsewhere, use @starting-style plus a JS exit class,
   and set the origin from the trigger's side. */
.popover {
  transform-origin: var(--transform-origin, top center);
  transition: opacity var(--dur-base) var(--ease-out), transform var(--dur-base) var(--ease-out);
}
.popover[data-starting-style], .popover[data-ending-style] {
  opacity: 0; transform: scale(0.96);
}
.popover[data-ending-style] { transition-duration: var(--dur-fast); } /* exit faster */
```

```css
/* Native popover / dialog with @starting-style and discrete display */
/* The destination state's duration wins, so the closed (base) rule holds the faster exit. */
dialog {
  transition: opacity var(--dur-fast) var(--ease-out), transform var(--dur-fast) var(--ease-out),
              display var(--dur-fast) allow-discrete, overlay var(--dur-fast) allow-discrete;
  opacity: 0; transform: scale(0.96);
}
dialog[open] { opacity: 1; transform: none; transition-duration: var(--dur-slow); }
@starting-style { dialog[open] { opacity: 0; transform: scale(0.96); } }
dialog::backdrop {
  background-color: rgb(0 0 0 / 0);
  transition: background-color var(--dur-fast) var(--ease-out),
              display var(--dur-fast) allow-discrete, overlay var(--dur-fast) allow-discrete;
}
dialog[open]::backdrop { background-color: rgb(0 0 0 / 0.5); transition-duration: var(--dur-slow); }
@starting-style { dialog[open]::backdrop { background-color: rgb(0 0 0 / 0); } }
/* Firefox parses allow-discrete but doesn't yet transition `display`, so the exit is instant there
   (an acceptable fallback). `overlay` is Chromium-only; without it the exit drops out of the top layer early. */
```

```css
/* Tooltip: the open delay and `data-instant` (skip the animation once a neighbor is open) come from
   Base UI's JS. Elsewhere, set the delay in your open handler. */
.tooltip { transform-origin: var(--transform-origin, bottom center);
  transition: opacity 125ms var(--ease-out), transform 125ms var(--ease-out); }
.tooltip[data-starting-style], .tooltip[data-ending-style] { opacity: 0; transform: scale(0.97); }
.tooltip[data-instant] { transition-duration: 0ms; }
```

```css
/* Toast: interruptible transition, same edge in and out */
.toast {
  transition: transform var(--dur-slow) var(--ease-out), opacity var(--dur-slow) var(--ease-out);
  @starting-style { transform: translateY(100%); opacity: 0; }
}
.toast[data-removed] { transform: translateY(100%); opacity: 0; transition-duration: var(--dur-fast); }
/* `data-removed` is Sonner's attribute; in your own code, set an exit class and remove the node
   on transitionend. Sonner itself uses 400ms `ease`. Copy that only with the reason written down. */
```

```css
/* Drawer / sheet (`data-closed` stands for whatever closed-state hook your library exposes) */
.drawer { transition: transform var(--dur-travel) var(--ease-drawer); }
.drawer[data-closed] { transform: translateY(100%); visibility: hidden;
  transition: transform var(--dur-slow) var(--ease-drawer), visibility var(--dur-slow); } /* exit ≈ 67%; hidden from AT once closed */
```

```css
/* Accordion: the one sanctioned layout animation. Keep it short. Prefer <details>/<summary>
   when you can; otherwise the closed state's `visibility: hidden` (below) takes hidden content out of the tab order. */
.panel { display: grid; grid-template-rows: 0fr; transition: grid-template-rows var(--dur-base) var(--ease-out); }
.panel[data-open] { grid-template-rows: 1fr; }
.panel > .inner { overflow: hidden; }
.panel:not([data-open]) > .inner { visibility: hidden; transition: visibility var(--dur-base); }
/* Alternative (Chromium-only today): `interpolate-size: allow-keywords` lets you animate height to auto. */
```

```css
/* Hold to confirm: slow and deliberate press, snappy release. The CSS is visual only. Do NOT fire on
   transitionend: the 200ms snap-back on early release ends too, and would trigger the action. Instead,
   on pointerdown or Space/Enter keydown, add .pressed and start a 2s timer that fires the action; on
   pointerup, pointercancel, keyup or contextmenu, clear both. Keep the fill under reduced motion (it shows progress). */
.hold { touch-action: none; user-select: none; -webkit-touch-callout: none; }
.hold .fill { clip-path: inset(0 100% 0 0); transition: clip-path 200ms var(--ease-out); }
.hold.pressed .fill { clip-path: inset(0 0 0 0); transition: clip-path 2s linear; }
```

```js
// Fragment. Drag to dismiss: velocity, not just distance. dy = drag offset (px); sample = the pointer
// position/time from about 100ms before release (velocity since drag start under-reads a late flick).
const velocity = Math.abs(dy - sample.dy) / (performance.now() - sample.t); // px/ms
if (Math.abs(dy) > THRESHOLD || velocity > 0.11) dismiss();
// Plus: damp over-drag past bounds (friction, not a wall), setPointerCapture on start,
// ignore extra pointers once dragging. Always ship a close button too (WCAG 2.5.7).
```

```js
// Programmatic, no library (WAAPI): a reveal entrance
if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const a = el.animate(
    [{ clipPath: 'inset(0 0 100% 0)' }, { clipPath: 'inset(0 0 0 0)' }],
    { duration: 250, easing: 'cubic-bezier(0.23, 1, 0.32, 1)' }
  );
  // The final style lives in CSS, so no fill: 'forwards'; that would pin a stale value over later changes.
}
```

```css
/* Tabs with a clean color change: render a second, aria-hidden copy of the tab list styled as
   active, stacked on top, and clip it to the active tab. Animating the clip changes background and
   text color in one move, which separate color transitions can't match. Set --clip-left/--clip-right
   on .tabs-active itself (not a parent) from the active tab's offsets when the tab changes. */
.tabs-active { position: absolute; inset: 0; pointer-events: none;
  clip-path: inset(0 var(--clip-right) 0 var(--clip-left) round 999px);
  transition: clip-path var(--dur-base) var(--ease-out); }
```

```css
/* Comparison slider: stack two images and clip the top one. While dragging, write the inset
   straight to the element's style (e.g. `inset(0 37% 0 0)`); no extra DOM needed. Back it with a
   real <input type="range"> so it works from the keyboard (WCAG 2.5.7). */
.compare-top { clip-path: inset(0 50% 0 0); }
```

```css
/* Card flip in real 3D, no JS needed for the motion. Under reduced motion, swap faces with an
   opacity fade instead of rotating. */
.card { transform-style: preserve-3d; transition: transform var(--dur-slow) var(--ease-in-out); }
.card[data-flipped] { transform: rotateY(180deg); }
.card > .face { backface-visibility: hidden; }
.card > .back { transform: rotateY(180deg); }
```

**State feedback patterns:**
- **Success:** scale pop (overshoot 5–10%: state feedback stays below the Playful 10–20% used for decorative motion) or a check draw-in (crisp), 300–400ms, announced via a live region.
- **Error shake:** 2–3 horizontal oscillations of ±6–12px, 300–400ms, `--ease-in-out`, **no overshoot**, paired with an error message. Skip it under reduced motion.
- **Loading:** skeletons fade in at 100ms, and spinners use `linear` and spin briskly. Don't show any loader for waits under about 300ms.
- **Scroll reveal:** 8–16px translate plus opacity (or a clip-path inset reveal), once only, `IntersectionObserver` with a negative bottom margin. Don't hide content that's already above the fold. Reduced motion means appear immediately.
- **Reduced motion for every recipe above** (place this block after them): keep opacity and color; set `transform: none` where transform only animates; where it *hides* (closed drawer), use opacity plus visibility; skip clip-path reveals except progress fills; let accordions snap.

```css
@media (prefers-reduced-motion: reduce) {
  .btn:active, .btn.pressed, .popover, .tooltip, dialog, dialog[open],
  [data-starting-style], [data-ending-style] { transform: none; }
  .drawer, .drawer[data-closed] { transform: none; transition: opacity var(--dur-fast) ease, visibility var(--dur-fast); }
  .drawer[data-closed] { opacity: 0; }
  .panel { transition: none; }
  ::view-transition-group(*) { animation: none; }           /* keep the root crossfade, drop movement */
}
```
- **Blur bridge:** when a cross-fade shows two overlapping states, add `filter: blur(2px)` mid-transition. Keep animated blur under 20px (Safari cost).

### 6.1 Parallax and scroll-linked motion

**Gate first.** Parallax is ambient motion: hero, marketing and storytelling pages only, never a work UI. Users rate parallax sites as more fun, but studies find no gain in usability or task time, and in the main Purdue study (Frederick et al., JUS 2015) 2 of 43 users got motion sick. Layers moving at different speeds are a known vestibular trigger, so the default answer for product UI is no.

**Rules:**
- **Use CSS scroll-driven animations**, not scroll listeners. They run on the compositor, while JS listeners run on the main thread and jank.
- **Animate `transform` only**, on a decorative layer. Keep text and controls on the static layer.
- **Crop with `overflow: clip`, never `hidden`.** `view()` follows the nearest scroll container, and `overflow: hidden` creates one that never scrolls, so the animation silently freezes.
- **Keep it small.** Displace the layer by at most about 10% of its own height, and oversize it so its edges never show.
- **Vertical only.** Never move things sideways while the user scrolls vertically, and never zoom, scale or rotate on scroll.
- **Don't take over scrolling** (scroll-jacking, snap-hijacking). The page must scroll at the user's speed.
- **Avoid `background-attachment: fixed`.** It repaints on every scroll and iOS Safari ignores it.
- **Reduced motion means off, not gentler.** The speed difference between layers is the trigger itself, so there is no safe gentle version. Long, motion-heavy pages should also offer an on-page toggle.
- **Support (as of mid-2026):** Chromium 115+ and Safari 26+ (test on 26.5+, which fixed progress bugs at the 0% and 100% edges). Firefox stable still has it behind a flag. Unsupported browsers ignore `animation-timeline`, so the static layout must be correct on its own.

```css
.hero { position: relative; overflow: clip; }  /* clip, not hidden: hidden makes .hero a scroll container, and view() would track it and never move */
.hero-bg { position: absolute; inset: -15% 0; }  /* oversized: ±10% of 130% height stays inside the 15% bleed */
@keyframes parallax { from { transform: translateY(-10%); } to { transform: translateY(10%); } }

@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    :root:not([data-motion="reduce"]) .hero-bg {       /* also honors an on-page motion toggle */
      animation: parallax linear both;
      animation-timeline: view();
      animation-range: cover 0% cover 100%;
    }
  }
}
```

### 6.2 3D scenes (three.js / WebGL / WebGPU)

**Gate first.** A decorative 3D hero is ambient motion (marketing and hero surfaces only). A product configurator or explanatory scene earns its place through the Explanation purpose. Ask what the 3D helps the user decide, and what the fallback is when the device can't run it. If neither has an answer, use a still image.

**Renderer (three.js r186, late 2026):**
- **`WebGPURenderer` from `three/webgpu` is the recommended path.** Call `await renderer.init()` before the first frame. It falls back to WebGL 2 automatically, so one code path covers every browser. Firefox stable still lacks WebGPU on Linux, Intel Macs and Android, which is where that fallback runs.
- **Custom shaders go in TSL.** `ShaderMaterial`, `RawShaderMaterial` and `onBeforeCompile` don't work under `WebGPURenderer`; TSL compiles one shader to both WGSL and GLSL. `WebGLRenderer` is still maintained for pure WebGL 2 apps but gets no new features.
- **Pin the three.js version** and import `three` and its addons through one import map, so the WebGPU build and the addons share one copy of the classes.

**Loading:**
- **Paint content first.** Show a static poster (an image or CSS gradient at the canvas's exact size, so nothing shifts), and start the renderer after the main content has painted, or when the canvas nears the viewport.
- **Budget the assets:** glTF with Draco geometry and KTX2 textures, about 1.5MB total for a hero.
- **If WebGPU and WebGL both fail, keep the poster.** Never leave an empty box.
- **Prefer an opaque canvas:** clear to the page's background color and draw glows or gradients into the scene, rather than layering CSS over a transparent canvas. A canvas nothing blends with is the simplest compositing path. (In headless testing, transparent and blended WebGPU canvases rendered white on some runs; this hasn't been confirmed on real GPUs.)

**Render loop:**
- Use `renderer.setAnimationLoop`. **Stop it when the canvas is off-screen** (`IntersectionObserver`) and when the tab is hidden. A static scene renders on demand, only when something changes (`frameloop="demand"` in R3F).
- **Cap the pixel ratio**: `Math.min(devicePixelRatio, 2)`. Rendering at 3× multiplies GPU work for detail nobody sees.
- **Dispose** geometries, materials, textures and the renderer on unmount.
- In R3F, **never call `setState` inside `useFrame`**: mutate refs. drei's `<AdaptiveDpr>` and `<PerformanceMonitor>` lower quality on weak devices.

**Motion inside the scene:**
- **Damp toward targets, frame-rate independent:** `x = THREE.MathUtils.damp(x, target, lambda, dt)` (lambda ≈ 4–8 for UI-like response). Binding values straight to the pointer feels mechanical, the same reason §3.5 uses springs.
- **Ambient motion stays slow and small.** An idle rotation of about 0.1–0.2 rad/s reads as alive; faster reads as a screensaver. No camera flights, zooms or scroll-driven camera moves on decorative scenes, because large camera motion is a vestibular trigger like parallax.
- **Pointer-follow is decorative only.** Gate it to fine pointers and keep the tilt small (a few degrees).

**Accessibility:**
- **CSS `prefers-reduced-motion` doesn't reach the canvas.** Read `matchMedia('(prefers-reduced-motion: reduce)')` in JS, listen for its `change` event, and under reduce stop auto-rotation, drift and pointer-follow: render one still frame. Motion the user drives directly (dragging a configurator model) may stay.
- **A decorative canvas is `aria-hidden="true"`** and holds nothing meaningful; headings and calls to action stay in the DOM over it. A configurator's options are real HTML controls, keyboard-operable, with the current state in text.
- **An auto-rotating scene that runs more than 5s needs a pause control** (WCAG 2.2.2, §3.7).

```js
// Fragment: the loop rules above, framework-free.
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
let onScreen = false, last = performance.now();
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
function frame(now) {
  const dt = Math.min((now - last) / 1000, 0.1); last = now;   // clamp dt after a pause
  if (!reduce.matches) mesh.rotation.y += 0.15 * dt;          // slow ambient spin
  mesh.rotation.x = THREE.MathUtils.damp(mesh.rotation.x, target.x, 6, dt);
  renderer.render(scene, camera);
}
const run = () => renderer.setAnimationLoop(onScreen && !document.hidden && !reduce.matches ? frame : null);
new IntersectionObserver(([e]) => { onScreen = e.isIntersecting; run(); }).observe(canvas);
document.addEventListener('visibilitychange', run);
reduce.addEventListener('change', () => { run(); renderer.render(scene, camera); }); // still frame
```

---

## 7. Performance

**Frame budget:** 16.7ms at 60Hz, **8.3ms at 120Hz**. Design against the smaller one, and judge on a mid-range phone, never a fast laptop.

| Symptom | Likely cause → fix |
| --- | --- |
| Stutters | Animating layout props → `transform`/`opacity` |
| Choppy shadow | `box-shadow` repaint → cross-fade a pseudo-element's opacity (see §3.2) |
| Jank only during navigation/loading | rAF/JS animation on a busy main thread → CSS or WAAPI |
| Motion animation drops frames | Animating a CSS variable (never accelerated) → animate `transform` or Motion's `x`/`y`/`scale`, which current Motion accelerates |
| Hand-rolled animation janks in React | `setState` per frame → write `ref.current.style.transform` or a motion value |
| Drag slows as content grows | Per-frame inherited CSS variable → set `transform` on the element |
| Blur lags (Safari) | Large animated blur → keep it under 20px, 2–5px is usually enough |
| Unexpected things animate | `transition: all` → explicit properties |
| 1px shift at start/end | Layer promotion handoff → `will-change: transform` **on that element only, after you see it** |

Name the cause before changing code. "Added `will-change`, seems smoother" is not a diagnosis. Say which findings you verified from code and which need a real-device recording (DevTools Performance panel plus 4–6× CPU throttle at minimum).

---

## 8. Custom elements and Shadow DOM

Use this section when "web components" means literal custom elements.

- **Tokens cross the shadow boundary.** Inherited custom properties (`--ease-out`, `--dur-base`) pierce shadow roots, so define them on `:root` and consume them inside. Expose overrides as documented custom properties (`--my-popover-duration`).
- **State via host attributes:** `:host([open]) .panel { … }`. Reflect the state to an attribute so consumers can style it too.
- **Expose `::part()`** for animatable internals so consumers can retune motion without forking.
- `@starting-style`, `@media (prefers-reduced-motion)` and `@media (hover: hover)` all work inside shadow styles. Put the reduced-motion variant *inside* the component, not on consumers.
- **Exit animations:** delay `hidden`/removal until `transitionend`/`animationend` (or `el.getAnimations()` → `Promise.all(a.map(x => x.finished))`), with a timeout fallback in case the event never fires. Under reduced motion, use the opacity-only exit, or remove immediately if there is none.
- Dispatch `open`/`close` events at the **start** of a transition and `opened`/`closed` events at the end. Consumers need both.
- Never animate the host's layout box (`width`/`height`) to reveal internals. Animate an internal wrapper with `transform`/`clip-path`.

---

## 9. Where the sources disagree (decisions made)

| Question | Source positions | This skill's rule |
| --- | --- | --- |
| Exit easing | Kowalski: ease-out always, never ease-in. LottieFiles and Material: accelerate (ease-in) on exits. | **Ease-out with a shorter duration** by default. An accelerate curve is allowed only for an element leaving the viewport after a completed dismissal (flick-away), at ≤200ms. Never ease-in on anything the user is waiting to see respond. |
| Modal/page duration | Kowalski: UI under 300ms. LottieFiles: modal 300–400, page 400–600, Premium 350–600. | **Components under 300ms.** Large-travel surfaces (drawers) up to 500ms. Page transitions 250–400ms. The long Premium timings apply to marketing and rare surfaces only. |
| "Always three motion layers" | LottieFiles: critical rule. Kowalski: delete motion when in doubt. | **Primary is required, secondary is optional, ambient only on marketing/hero.** In product UI, extra layers are noise. |
| Hover scale | Tarre: 1.05–1.1 so it's noticeable. Kowalski: subtle, gated. | **Hover rarely needs scale.** Prefer a color/opacity shift. If you scale, 1.02–1.05 on large targets, gated to fine pointers. |
| Squash & stretch, anticipation | Tarre/LottieFiles: apply Disney principles. Kowalski: restraint. | **Playful/Energetic personalities only,** at small amplitude. Never on Crisp/Premium, never under reduced motion. |
| Reduced motion | Tarre: global near-zero kill switch. Kowalski: gentler, not zero. | **Gentler, not zero,** per component (§3.7). Parallax is the one exception: off entirely (§6.1). |
| Stagger | Kowalski: 30–80ms. LottieFiles: total under 500ms. | **Both:** 30–80ms per item *and* a total under 500ms. |
| Motion shorthands (`x`, `y`, `scale`) | Kowalski: run on the main thread, so use a full `transform` string. Motion's performance docs (checked Oct 2026): independent transforms are hardware-accelerated like `transform`; CSS variables are not. | **Shorthands are fine in current Motion.** Animating a CSS variable is what to avoid (§7). On an older Framer Motion version that drops frames, profile first, then try the `transform` string. |

---

## 10. Review mode

**Posture:** senior design engineer, strict about craft. Default to flagging. Approval is earned. Cite `file:line`. Pull exact values from this skill rather than approximating.

**Escalate on sight:**
- `transition: all`
- `scale(0)` entrance, or an important state change that is opacity-only
- `ease-in` on a UI response; weak built-in easing on deliberate motion; `linear` on spatial movement
- Any animation on a keyboard shortcut or 100+/day action
- Component duration over 300ms with no reason; enter and exit at the same speed
- `transform-origin: center` on a trigger-anchored popover
- Keyframes on toasts, toggles or rapidly-triggered elements
- Animating `width`/`height`/`margin`/`padding`/`top`/`left` (except a short accordion)
- Animating a CSS variable (`--x`) on motion that runs while the page is busy
- A per-frame value driven through an inherited CSS variable
- No `prefers-reduced-motion` handling for movement; ungated `:hover` motion
- Everything entering at once, or a cascade over 500ms
- Parallax outside hero/marketing surfaces, parallax by JS scroll listener, `overflow: hidden` between a `view()` subject and the page scroller, horizontal or zoom motion on vertical scroll, or parallax still running under reduced motion
- Mixed personalities or entrance directions within one view
- A 3D render loop that keeps running off-screen, in a hidden tab, or under reduced motion; an uncapped pixel ratio; no static poster or fallback; `setState` inside `useFrame`; meaningful content only inside the canvas
- Motion that conveys state without an accessible announcement; focus lost or trapped mid-animation

**Remedy preference, earliest first:**
1. Delete it.
2. Reduce it (shorter, smaller, fewer properties).
3. Fix the easing.
4. Fix the origin or physicality.
5. Make it interruptible.
6. Move it to the compositor.
7. Make the timing asymmetric.
8. Polish (blur bridge, stagger, `@starting-style`, spring).
9. Accessibility and cohesion.

**Output: two parts, in this order.**

**Part 1. Findings table (required).** One row per issue. Never a "Before:/After:" list.

| Location | Before | After | Why |
| --- | --- | --- | --- |
| `Menu.css:14` | `transition: all 300ms` | `transition: opacity 200ms var(--ease-out), transform 200ms var(--ease-out)` | `all` animates unintended, possibly layout, properties |

**Part 2. Verdict,** grouped by tier with empty tiers omitted:
1. Feel-breaking regressions
2. Should be removed or reduced
3. Performance
4. Interruptibility & timing
5. Origin, physicality & cohesion
6. Accessibility

Close with **Block** (any feel-breaking regression, motion on a keyboard/high-frequency action, `scale(0)`/`ease-in` on UI, an easy-fix non-composited animation, or missing reduced-motion on movement) or **Approve** (none of those, durations and easing within bounds, interruptibility handled, reduced motion and hover gating present). Say which findings need slow-motion or real-device confirmation.

---

## 11. Audit mode

Sweep the codebase (CSS, `motion.`/`animate(`/`gsap.`/`@keyframes`/`transition` usages, component libraries) and return three lists. Every item runs through the Gate.

1. **Remove / reduce.** Motion failing frequency, purpose or function. For each: location, current behavior, the Gate question it fails, and the replacement (often none, or a 100ms opacity fade). Note removal hazards: code awaiting `transitionend`, tests waiting on animations, layout that relied on transform offsets.
2. **Fix.** Motion that should exist but breaks a §10 escalation trigger. Use the Review table format.
3. **Add.** Places where a missing transition causes a jarring change (content popping in, layout jumps, state flips with no feedback, popovers appearing without origin). For each, name the purpose and a recipe from §6.

Also report **kept on purpose** (motion you checked that passes), so the audit shows its coverage. End with the 3–5 highest-impact changes as self-contained tasks any agent could execute, plus a token proposal (§4) if the codebase has none.

---

## 12. Debugging feel

- **Slow it down:** 2–5× duration or the DevTools Animations panel at 10–25%. Check that cross-fades don't show two objects, easing doesn't stop abruptly, the origin is right, and coordinated properties stay in sync.
- **Frame-by-frame** in DevTools for drift between properties.
- **Real devices** for gestures (phone on LAN + Safari/Chrome remote devtools).
- **Fresh eyes the next day.**
- **When unsure whether it feels right, try deleting it.** If nobody misses it, it was noise.

---

## 13. Building components people want to use

Apply when building or reviewing a reusable component or library, not only its motion. These come from building Sonner.

- **Make adoption nearly free.** One setup step and a call from anywhere (`<Toaster />` once, `toast()` anywhere), with no required hooks, context or config.
- **Defaults over options.** Most users never customize, so the default easing, timing and look have to be excellent out of the box.
- **Name it to be remembered.** A distinctive name can beat a descriptive one when the product earns it.
- **Handle edge cases invisibly** (§3.6). Nobody notices them, which is the goal.
- **Ship a docs site people can play with:** live, interactive examples with copy-ready code, so they understand it before installing it.

---

## Credits

Merged and reconciled from:
- **Emil Kowalski, `emilkowalski/skills`** (MIT): animate, review-animations, animation-performance, emil-design-eng. Source of the Gate, the easing/duration bars, the recipes, the performance diagnostics, the review format, the opening rationale and §13.
- **LottieFiles, `motion-design-skill`** (MIT): personality archetypes, brand motion identity, choreography, stagger budgets, distance/weight scaling, state-feedback patterns.
- **Dylan Tarre, `animation-principles`** (MIT): Disney principles mapped to web, accessibility checklist (pause controls, flash rate, focus, announcements).

Additions not in those sources: §6.2 (three.js, from the three.js manual and 2026 WebGPU migration and performance guides), §6.1 (parallax, from the Frederick et al. study, vestibular-accessibility guidance and 2026 browser-support reports), §8 (custom elements), the native `<dialog>` / grid-rows / `interpolate-size` recipes, the View Transitions row, and the §9 conflict resolutions (the Motion-shorthand row checked against motion.dev/docs/performance, Oct 2026).