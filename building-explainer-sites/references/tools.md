# Tools and exemplars

Prefer plain HTML, CSS, and a small amount of JavaScript. Add a library only when it does substantial work. Maintenance status changes; check a library's latest release before adopting it.

## Default stack

| Need | Choose | Notes |
|---|---|---|
| Page and prose | Semantic HTML + CSS | Works with JS off; easiest to audit |
| Components and state | Plain JS, or Svelte 5 / SvelteKit | Svelte is actively maintained, MIT |
| Custom charts and marks | D3 v7 | Stable, infrequent releases, ISC |
| Scroll triggers | Native `IntersectionObserver` | Scrollama is a thin wrapper with no release since 2022 |
| Animation | CSS transitions; Motion (MIT) or GSAP 3 for complex timelines | GSAP and all its plugins are free, including commercial use, under GreenSock's own license (not open-source) |
| Math animation for video | Manim Community | Python; no official web port |
| Quick dashboards or data notebooks | Observable Framework | Near maintenance-only |

## Avoid for new work

Keep these for reading existing projects only:

- **Idyll:** archived, "no longer active" per its Open Collective page.
- **Distill template:** unmaintained. Distill.pub has been on hiatus since 2021.
- **Apparatus (aprt.us):** a dormant research project.
- **Mafs:** dormant.
- **Observable Plot:** no release in about 20 months; fine for static charts but not a long-term dependency.

## Learning tools

- **Polypad** (polypad.amplify.com, formerly Mathigon): hosted and free, but proprietary.
- Red Blob Games' "incremental interactivity" Observable demo shows the right workflow: start from a static SVG diagram and add interactivity step by step.

## Exemplars worth studying

The descriptions below are general characterizations, not re-verified.

| Exemplar | What it does well |
|---|---|
| Bartosz Ciechanowski (ciechanow.ski) | Progressive 2D/3D explorables, reset controls, color-linked prose, rotatable 3D |
| Nicky Case (ncase.me) | Systems explorables framed as small games; questions posed before answers |
| Red Blob Games (redblobgames.com) | Pages that read fine untouched; incremental interactivity; prose and explorables alternate |
| Distill.pub archive | Peer-reviewed interactive ML articles. *Communicating with Interactive Articles* (Hohman, Conlen, Heer & Chau 2020) synthesizes the design space |
| The Pudding (pudding.cool) | Responsive scrollytelling with stacked mobile fallbacks |
| NYT / The Upshot | Scroll-first annotation; essential labels shown, not hidden in tooltips |
| Seeing Theory, 3Blue1Brown | Visual-first math intuition |
