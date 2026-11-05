# Scrollytelling and mobile

Main source: The Pudding, *Responsive scrollytelling best practices* (Russell Samora, 2017). Its advice is still sound; its CSS details have been updated below.

## Plan mobile from the start

- Designing mobile-first forces the experience down to essentials.
- Designing desktop-first is fine if you plan how each step scales down before building.

## Scroll it or stack it

Keep a scroll-driven sequence only when the transition itself carries meaning: change over time, or movement through space.

Stack static figures instead when:
- heavy animation would hurt performance;
- each step works as a standalone figure;
- mobile needs a different chart type;
- time is short.

## Never take over the browser

- No click-through steppers. They hide content behind clicks.
- No swipe or tap navigation that overrides normal scrolling.

## Touch

- Replace hover interactions with visible labels or annotations.
- Make required interactions obvious controls, so readers don't trigger them while scrolling.
- Targets must be at least 24×24 CSS px (WCAG 2.5.8).

## Pacing

Mobile wears readers out faster. Use a few steps, make the point, and stop.

## Implementation

- Separate chart setup from drawing; on resize, update rather than rebuild.
- **Viewport units:**
  - `vh` jumps as mobile toolbars appear and hide.
  - Use `svh` (toolbars shown) or `lvh` (toolbars hidden). Both stay fixed.
  - Avoid `dvh` for scroll steps; it resizes as the toolbars move, which reintroduces the jump.
  - Support: Chrome 108, Firefox 101, Safari 15.4.
- **Scroll triggers:**
  - Prefer native `IntersectionObserver`. Scrollama wraps it but has had no release since 2022.
  - GSAP ScrollTrigger is free, including commercial use, under GreenSock's own license (not OSI).
- **Reduced motion:**
  - When `prefers-reduced-motion: reduce` is set, swap animated transitions for instant state changes.
  - Keep the step content.

```css
.step { min-height: 80svh; }          /* stable on mobile */
@media (prefers-reduced-motion: reduce) {
  * { transition: none !important; animation: none !important; }
}
```

```js
const io = new IntersectionObserver((entries) => {
  for (const e of entries) if (e.isIntersecting) showStep(+e.target.dataset.step);
}, { rootMargin: '-45% 0px -45% 0px' });   // fires when a step crosses mid-screen
document.querySelectorAll('.step').forEach((el) => io.observe(el));
```

## Fallback

Each step's text must still make sense with the graphic absent, for JS-off readers, screen readers, and readers who scroll fast.
