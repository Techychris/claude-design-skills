---
name: building-explainer-sites
description: Designs, builds, and audits explainer web pages such as explorable explanations, interactive essays, and scrollytelling articles, applying evidence-based rules for structure, interactivity, animation, typography, color, spacing, accessibility, and testing. Use when the user asks for an explainer, interactive article, explorable, scrollytelling page, visual explanation of a concept for the web, or a review of such a page.
---

# Building explainer sites

An explainer page teaches one idea. The text carries the explanation; interactive parts let readers test their own hunches. Most readers never touch the interactive parts, so nothing essential may depend on them.

This file holds the workflow, the rules, and the checklist. Evidence, figures, and sources live in `references/`. Read a reference file only when its topic comes up.

## Workflow

Copy this progress list and tick items off as you go:

```
Explainer progress
- [ ] 1. Frame: one-sentence takeaway, audience, why this topic suits (or doesn't suit) interaction
- [ ] 2. Write the prose first, complete enough to teach with no interaction
- [ ] 3. Choose at most a few explorables; each answers a question the prose poses
- [ ] 4. Build from templates/explainer-page.html (or the project's own system)
- [ ] 5. Run scripts/audit.py and fix every FAIL
- [ ] 6. Walk the manual checklist below
- [ ] 7. Report what was checked automatically, what manually, and what is untested
```

### 1. Frame

- State the one thing the reader should understand by the end. If you can't, the page isn't ready to build.
- Explorables suit systems, models, and chains of cause and effect. A list of facts gets prose, a table, or a static figure instead.
- Pick the level of interactivity per point. Most points need none.

### 2. Write the prose first

- The page must read fully as text. Each explorable illustrates something the prose already says.
- Headings state each section's point ("Contrast comes from lightness, not hue"), not its topic ("Color"). Someone reading only headings should get the argument.
- Keep explanations schematic. Cut detail that doesn't serve the takeaway.

### 3. Design each explorable

- Pose a question before the explorable ("Guess first: …"), then let the reader check. Prediction before reveal is a strong learning effect.
- Guide attention to the specific thing to notice. Never drop the reader into an open sandbox.
- Give every interactive element a reset control and a visible current state.
- Use one color per concept, in both the prose and the visual.
- Put the static equivalent (a sentence, a table, or a labeled image) next to it, so the point survives without JavaScript or interaction.
- Encode the key quantity by position on a common scale before length, angle, or area.

### 4. Build

Start from `templates/explainer-page.html`. It already does the following:
- prose in HTML, enhanced by JavaScript;
- theme tokens for light and dark;
- reduced-motion handling;
- a reset-able explorable with a text equivalent and `aria-live` output.

If the project has its own design system, apply these rules within it.

For library choices, read `references/tools.md`.

### 5. Audit

Run the bundled audit. Execute it; don't read it into context:

```bash
pip install playwright && python -m playwright install chromium   # once, if missing
python scripts/audit.py path/to/page.html            # or a URL
python scripts/audit.py page.html --json report.json # machine-readable output
```

It renders the page at 320, 390, and 1280 px, plus JS-off, dark, and reduced-motion variants. It reports PASS, WARN, or FAIL for:
- text contrast;
- body font size;
- characters per line;
- horizontal overflow;
- target size;
- reduced-motion handling;
- JS-off content;
- missing alt text;
- heading structure;
- console errors.

Fix every FAIL, then run it again. Treat WARN as a judgment call and say what you decided.

The audit cannot judge comprehension, narrative, correctness, contrast of text over images, or keyboard order. Those are manual.

### 6. Manual checklist

Walk this list after the audit. Items marked (audit) are covered automatically; confirm they passed.

**Structure**
- [ ] Page reads fully with no interaction and with JavaScript off (audit)
- [ ] Headings state each section's point
- [ ] Prose and explorables alternate; no wall of widgets
- [ ] Each explorable has a guiding question; concepts build in order
- [ ] The ending asks the reader to use what they learned

**Interaction**
- [ ] No essential information behind hover, click, or scroll-trigger alone
- [ ] Every interactive element has a reset; controls look operable
- [ ] Keyboard can reach and operate every control; focus is visible
- [ ] Scroll-driven transitions only where the motion itself carries meaning; normal scrolling never hijacked
- [ ] Changing values announced via `aria-live="polite"`

**Visual cues**
- [ ] Body text ≥ 4.5:1 contrast; UI parts and meaningful graphics ≥ 3:1 (audit covers text)
- [ ] Color is never the only signal; no red-on-black
- [ ] Body text ≥ 16px on mobile; 18–20px for desktop long-form (audit)
- [ ] Lines about 55–75 characters on desktop (audit)
- [ ] Every icon has a text label, at least on first use
- [ ] Bold and accent color reserved for what matters; depth (shadows) only on interactive things
- [ ] Related items closer together than separate groups; headings closer to their own section
- [ ] Data transitions ≈1 s per stage (≤2 s total); UI feedback ≤0.5 s; nothing blinks
- [ ] Reduced-motion users get no non-essential motion (audit)
- [ ] Layout survives WCAG 1.4.12 text-spacing overrides

**Testing**
- [ ] Checked on a real phone, not only a resized window
- [ ] Read by someone new to the topic, who can then state the takeaway
- [ ] Links resolve

### 7. Report

Tell the user three things:
- what passed the audit;
- what you checked by hand;
- what remains untested (real phone, a newcomer read-through).

Never present untested items as done.

## Hard rules and soft defaults

Hard rules rest on standards (WCAG 2.2) or replicated evidence. Never break them silently. Soft defaults rest on convention or single studies, so adjust them to the audience and say why.

| Hard rules | Soft defaults |
|---|---|
| Body text ≥ 4.5:1 contrast; UI and graphics ≥ 3:1 | 7:1 contrast for long reading |
| Fully readable without interaction and without JS | 18–20px body for desktop long-form |
| No essential info behind hover or click only | 55–75 characters per line; line-height 1.4–1.6 |
| Keyboard-operable controls, visible focus, targets ≥ 24×24 CSS px | Data transitions ≈1 s per stage |
| Honor `prefers-reduced-motion`; nothing blinks | Light mode default plus a dark option |
| Color never the only signal | Icon labels on first use |
| Survives WCAG 1.4.12 text-spacing overrides | Generous margins (they aid comprehension, not speed) |
| Body text ≥ 16px | Letter-spacing as a user setting, not a default |

## Mobile and scrollytelling

- Plan mobile from the start.
- Keep a scroll-driven sequence only when the transition means something, such as change over time or movement in space. Otherwise stack static figures.
- No click-through steppers and no swipe hijacking.
- Replace hover with visible labels.
- Size scroll steps with `svh` or `lvh`, never `vh` or `dvh`. Those resize as mobile toolbars move.

Details: `references/scrollytelling.md`.

## Reference files

Read only the file the task needs:

- `references/principles.md`: why explorables work, guided vs sandbox, learning-science effects (signaling, contiguity, coherence, retrieval practice), interaction rates, the expert trap.
- `references/visual-cues.md`: animation, icons, typography and font-size math, color, spacing, hierarchy and depth, with figures.
- `references/scrollytelling.md`: The Pudding's mobile rules, viewport units, stacking vs scrolling.
- `references/accessibility.md`: WCAG 2.2 criteria that matter for explorables, with implementation snippets.
- `references/tools.md`: library choices, maintenance status, exemplar explainers worth studying.
- `references/evidence.md`: every factual claim with its status (verified, unverified, convention) and primary source. Check here before quoting a figure to the user.

When you cite a figure to the user, take it from `evidence.md` and keep its status label. Don't upgrade an unverified claim.
