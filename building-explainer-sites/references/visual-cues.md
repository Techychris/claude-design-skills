# Visual cues: guiding the eye

Every cue works by sparing the reader effort, and backfires when used as decoration. Status labels follow `evidence.md`: **[V]** verified against a primary source, **[S]** secondary source only, **[U]** unverified, **[C]** convention, **[E]** inferred.

## Contents
- Animation
- Icons
- Typography and font size
- Color
- Spacing
- Hierarchy and depth

## Animation

- **Transitions help with tracking.** In Heer & Robertson's 2007 experiments (24 participants), animated transitions significantly beat instant cuts for tracking objects between chart states, for every transition type tested. They also improved estimates of value changes for scatter plots, grouped bars, and donut charts, but not stacked bars. [V]
- **Keep staging simple.** Simple staging was significantly preferred and usually lowered tracking error, but it was worse for timestep scatter plots. Heavy one-thing-at-a-time staging was significantly worse only for donut charts. [V]
- **Timing.** Data transitions ran 1.25 s and 2 s; the authors recommend about a full second per stage. [V] UI feedback is much shorter: NN/g recommends 100–500 ms for most UI animation (about 100 ms for toggles, 200–300 ms for modals). [S]
- **Animation is rarely the active ingredient.** Tversky, Morrison & Bétrancourt (2002) concluded that most successes of animation come from extra information or procedures, not animation itself. Animations fail when they are:
  - too fast or complex;
  - fleeting, gone before the reader can compare;
  - conceived of as continuous when people think in discrete steps;
  - distracting. [V]
- **Highlighting cues help learning.** Signaling meta-analysis: retention g = 0.53, transfer g = 0.33. [V] Reported moderator values (color g = 0.39, blinking −0.47, text signaling 0.68/0.48) come from a summary only. [S]
- **Why it works.** Heer & Robertson attribute the benefit to object constancy: the eye follows each mark instead of re-matching marks after a cut. [S]
- **Rules.**
  - Pause and replay controls.
  - Honor `prefers-reduced-motion`.
  - Auto-moving content longer than 5 s needs a pause control (WCAG 2.2.2).
  - Nothing blinks.

## Icons

- **Labels help a lot with meaning.** Leung, McGrenere & Graf (2011): 36 participants, 60 icons drawn from a pool of 149.
  - Labels raised identification from 95→98% (younger) and 82→90% (65+).
  - Labels raised interpretation from 52→86% (younger) and 38→71% (65+). [V]
- **Semantic distance matters most.** Icons whose picture is closely tied to their meaning were interpreted far better: 80% vs 41% for older adults, about 84% vs 51% pooled. [V]
- **Concrete, simple icons search faster.** Goetz & Neider (2023): icons high in concreteness improved search, and higher visual complexity slowed identification. [V] The claim that color and shape distinctiveness speeds search is not confirmed in the paper. [U]
- **Rule.** Label every icon, at least on first use.

## Typography and font size

- **Font choice is individual.** Wallace et al. (2022), 352 adults, each reading 5 of 16 fonts:
  - Readers were 35% faster in their fastest font than their slowest (314 vs 232 WPM), and 14% faster than in their preferred font (275 WPM).
  - Comprehension was about 90% in all conditions.
  - The preferred font was the fastest only 20% of the time, and the slowest 20% of the time. [V]
- **Size has a floor.** Legge & Bigelow (2011): reading runs at maximum speed across about a 10-fold range, from about 0.2° to 2° of x-height.
  - Speed drops sharply below the critical print size of about 0.2°.
  - Newspaper and book text sits around 0.23–0.24°. [V]
  - Why: below the critical size, neighboring letters crowd each other and fewer letters are recognized per glance. [V]
- **Font-size math (CSS px are logical, not physical).** [E]
  - 13–14" laptop at default scaling, read at 50 cm: 16px gives about 0.18–0.19° x-height, *below* the 0.2° floor. 20px gives about 0.23°.
  - Phone (~393 px wide) at 32–36 cm: 16px gives about 0.23–0.26°.
  - Rule: 16px is the mobile floor; use 18–20px for desktop long-form.
- **Older and dyslexic readers.**
  - Adults averaging about 70 found 14pt more legible, faster, and preferred over 12pt (Bernard, Liao & Mills 2001). [V]
  - In Rello et al. (2013), 28 readers with dyslexia did best at 18pt (CSS points), with no further gain at 22 or 26pt. Line spacing had no effect. [V]
- **Line length.**
  - Longer lines are often read faster.
  - Dyson & Haselgrove (2001) found 55 characters per line gave the highest comprehension and was read faster than 25 characters per line. [V]
  - Shaikh (2005) found no comprehension difference across 35–95 characters per line. [S]
  - The 45–75 character range (66 ideal) is typographic convention (Bringhurst). [C]
  - Default to about 55–75 characters.
- **Good typography and mood.** Larson et al. (2006): 4 of 10 readers given good typography solved the candle problem versus 0 of 9 given poor typography. A second creativity test showed no difference. Good typography also produced better relative subjective duration (time felt shorter). Don't quote minute values. [V for direction, U for magnitudes]
- **Line height.** 1.4–1.6 is convention. [C] WCAG 1.4.12 requires the layout to survive user overrides up to line-height 1.5.
- **Give readers control.** Since no single font or size is best for everyone, offer size controls where practical.

## Color

- **Contrast.** WCAG sets 4.5:1 for body text and 3:1 for large text, UI parts, and meaningful graphics (SC 1.4.3, 1.4.11). [V]
  - The 4.5:1 figure is 3:1 × 1.5: 20/40 vision, typical around age 80, carries about a 1.5× contrast-sensitivity loss.
  - 7:1 targets 20/80 vision. [V]
- **Lightness, not hue, drives legibility.** The exception is long-wavelength colors (reds) on dark backgrounds, which are hard for people with protanopia: avoid red on black. [V]
- **Color blindness.** About 8% of men and 0.4–0.5% of women of European ancestry have red-green color vision deficiency. Deuteranomaly is the most common type. [V]
- **Light vs dark mode.**
  - Dark text on light performed better for ages 18–33 and 60–85, more so at small sizes (Piepenbrock 2013). [S, via NN/g]
  - There was no difference in daylight conditions (Dobres 2017). [S]
  - Readers with cloudy ocular media read faster in dark mode (Legge 1985, small CRT-era study). [S]
  - Default to light, honor `prefers-color-scheme`, and offer a toggle.
- **Color as a learning cue.** Color-coding concepts consistently across text and visuals is the same idea as signaling. Always pair color with a word, shape, or position.

## Spacing

- **Letter spacing for dyslexia: mixed evidence.**
  - Zorzi et al. (2012): 94 dyslexic children (74 in Experiment 1, 20 in Experiment 2). Extra letter spacing (+2.5pt on 14pt) about halved errors and raised speed by about 0.3 syllables/s, roughly 10–20% depending on the comparison. Reading-level-matched controls showed no significant gain. [V]
  - Stagg & Kiss (2021) found speed gains in both dyslexic (13%) and non-dyslexic (5%) students. [V]
  - Łuniewska et al. (2022) found no effect on accuracy, comprehension, or speed. [V]
  - Rule: offer wider spacing as a user setting, not a default.
- **Extremes hurt everyone.** Wallace, Dobres, Bylinskii & Sawyer (2022 conference abstract), 215 adults: the tightest and loosest letter spacing (−0.1 em, 0.4 em) and word spacing (−0.2 em, 1.5 em) reduced speed, comprehension, and preference. [V]
- **Margins aid comprehension, not speed.**
  - Chaparro et al. (2004): text with good white space was read *more slowly* but comprehended better. Leading affected preference only. [V]
  - A 2005 follow-up found no speed or comprehension difference between enhanced and poor layouts, but satisfaction was 5.50 vs 3.25 and 90% preferred the enhanced layout. [V]
- **Proximity groups things.** Items placed close together are seen as a group (Gestalt proximity; review: Wagemans et al. 2012, *Psychological Bulletin*). [U, not re-checked]
  - Space related items tightly and groups loosely.
  - A heading sits closer to its own section than to the one above.

## Hierarchy and depth

- **Headings shape scanning.** NN/g eyetracking ranks scanning patterns from worst to best: F-pattern, spotted, layer-cake, commitment.
  - Aside from reading almost every word, the layer-cake pattern (scanning headings, then reading the relevant section) is by far the most effective.
  - Full reading (commitment) gives the best comprehension.
  - The F-pattern is a symptom of unstructured text. [V]
- **Scanners land on** links, bold words, numbers, and bulleted lists. Style only what matters. [V]
- **Weak signifiers cost time.** NN/g (Moran 2017), 71 participants, 9 sites: pages with weak clickability cues took 22% longer and drew 25% more fixations. On one site, 86% (25/29) followed the expected path with strong cues versus 50% (12/24) with weak ones. [V] The study tested weak signifiers, not flat design as such.
- **Looks don't make pages more usable.**
  - Kurosu & Kashimura (1995) found beauty correlated with *apparent* usability (r = .589). [V]
  - Grishin & Gillan (2019) found no effect of aesthetics on perceived usability (SUS) with real use, and Alharoon & Gillan (2020) replicated the null. [V]
  - Treat aesthetics as a first impression at most.
- **Rule.** Depth (shadows, raised styling) goes only on interactive things, so it keeps its meaning.
