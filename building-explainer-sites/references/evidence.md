# Evidence register

Every factual claim the skill relies on, with status and source. Before quoting a figure to a user, find it here and keep its status.

**Status key**

| Status | Meaning |
|---|---|
| Verified | Confirmed against the primary source |
| Secondary | Only seen in a summary or secondary source |
| Unverified | Not confirmed; don't present as fact |
| Convention | Practitioner convention, not an experimental finding |
| Inferred | Derived by calculation or reasoning from verified findings |

## Contents
- Explorables and interaction
- Animation
- Icons
- Typography and font size
- Color
- Spacing
- Hierarchy and depth
- Learning science
- Web platform

## Explorables and interaction

| Claim | Status | Source |
|---|---|---|
| Explorables let readers test claims instead of trusting or distrusting blindly | Verified | Victor 2011, worrydream.com/ExplorableExplanations |
| Explorables guide attention to specific phenomena, unlike isolated widgets | Verified | Victor 2011 |
| Most widgets leave readers in a sandbox; explanation should work without interacting; alternate prose and explorables | Verified | Red Blob Games, redblobgames.com/x/2306-educ432 |
| Explorables suit systems and cause-and-effect; question first; gating; homework problems; conclude by using knowledge | Verified | Nicky Case 2014, blog.ncase.me/explorable-explanations |
| ~15% clicked a prominent button in a couple of 2015 NYT graphics; non-clickers didn't ignore the graphic | Verified | Gregor Aisch, vis4.net/blog/in-defense-of-interactive-graphics |
| "Assume no one will ever see" a tooltip or rollover | Secondary | Archie Tse, Malofiej 2016 talk, via summaries |
| Limited empirical evaluation of interactive articles exists | Verified | Hohman et al. 2020, doi:10.23915/distill.00028 |
| Active-reading instrumentation of 50,000+ sessions | Verified (scope); interaction fraction not retrieved | Conlen, Kale & Heer 2019, doi:10.1111/cgf.13720 |
| Explorables mainly benefit people who already understand the concept (critique) | Verified (as a quoted opinion) | Red Blob Games notes |

## Animation

| Claim | Status | Source |
|---|---|---|
| Animated transitions beat static for object tracking in every condition (24 participants) | Verified | Heer & Robertson 2007, doi:10.1109/TVCG.2007.70539 |
| Value-change estimates improved for scatter, grouped bars, donut; not stacked bars | Verified | same |
| Simple staging preferred (p < 0.003), usually lower error; worse for timestep scatter; heavy staging significantly worse only for donuts | Verified | same |
| Durations 1.25 s and 2 s; ~1 s per stage recommended | Verified | same |
| Benefit attributed to object constancy | Secondary (authors' interpretation, citing Palmer 1999) | same |
| Animation's successes come from extra information or procedures, not animation per se; failure modes; Congruence and Apprehension principles | Verified | Tversky, Morrison & Bétrancourt 2002, doi:10.1006/ijhc.2002.1017 |
| UI animations mostly 100–500 ms | Secondary | NN/g, Laubheimer 2020 |

## Icons

| Claim | Status | Source |
|---|---|---|
| Labels: identification 95→98% (younger), 82→90% (65+); interpretation 52→86%, 38→71% | Verified | Leung, McGrenere & Graf 2011, doi:10.1080/01449290903171308 |
| Semantic distance: older adults 80% vs 41%; pooled ~84% vs 51% | Verified | same |
| Concrete icons improve search; complexity slows identification | Verified | Goetz & Neider 2023, doi:10.1080/0144929X.2023.2286527 |
| Color and shape distinctiveness speeds icon search | Unverified | (summary only) |
| Icon characteristic norms (concreteness, complexity, meaningfulness, familiarity, semantic distance) | Unverified | McDougall, Curry & de Bruijn 1999 |

## Typography and font size

| Claim | Status | Source |
|---|---|---|
| 352 adults; 35% faster fastest vs slowest font (314 vs 232 WPM); 14% faster than preferred (275 WPM); ~90% comprehension | Verified | Wallace et al. 2022, doi:10.1145/3502222 |
| Preferred font fastest 20% and slowest 20% of the time | Verified | same |
| Critical print size ~0.2° x-height; fluent range ~0.2°–2°; print text ~0.23–0.24° | Verified | Legge & Bigelow 2011, J. Vision 11(5):8 |
| Crowding explains slowdown below critical size | Verified | same |
| 16px ≈ 0.18–0.19° on 13–14" laptops at 50 cm; ≈ 0.23–0.26° on phones at 32–36 cm | Inferred | arithmetic from logical px sizes and x-height ≈ 0.5 em |
| Older adults (~70): 14pt more legible, faster, preferred over 12pt | Verified | Bernard, Liao & Mills, CHI EA 2001 |
| Adults: 12pt faster than 10pt | Secondary | Bernard et al. 2001/2002, Usability News |
| Dyslexic readers (n = 28): 18pt best; no further gain at 22/26pt; line spacing no effect; sizes in CSS points | Verified | Rello et al. 2013, pielot.org/pubs/Rello2013-W4A-SizeMatters.pdf |
| 55 characters per line gave the highest comprehension, read faster than 25 cpl | Verified (abstract) | Dyson & Haselgrove 2001, IJHCS 54:585–612 |
| No comprehension difference across 35–95 cpl | Secondary | Shaikh 2005, Usability News |
| 45–75 characters per line (66 ideal) | Convention | Bringhurst, *Elements of Typographic Style* |
| Line-height 1.4–1.6 | Convention | — |
| Candle problem 4/10 (good typography) vs 0/9 (poor); remote-associates test no difference | Verified | Larson, Hazlett, Chaparro & Picard 2006 |
| Good typography improves relative subjective duration (direction) | Verified | Larson & Picard 2005; numeric values Unverified |

## Color

| Claim | Status | Source |
|---|---|---|
| 3:1 baseline; 20/40 → ~1.5× contrast-sensitivity loss → 4.5:1; 7:1 for 20/80 | Verified | WCAG 2.2 Understanding SC 1.4.3 |
| Red on dark is hard for protanopia; otherwise hue barely affects legibility | Verified | same |
| ~8% of men, ~0.4–0.5% of women (European ancestry) have red-green CVD | Verified | PMC10428128; PMC11748764 |
| Light mode better for ages 18–33 and 60–85, more at small sizes | Secondary | Piepenbrock et al. 2013, via NN/g |
| No polarity difference in daylight conditions | Secondary | Dobres et al. 2017, via NN/g |
| Cloudy ocular media read faster in dark mode | Secondary | Legge et al. 1985 (small, CRT-era) |

## Spacing

| Claim | Status | Source |
|---|---|---|
| Zorzi: 94 dyslexic children (74 + 20); errors about halved; ~0.3 syllables/s faster (≈10–20%) | Verified | Zorzi et al. 2012, doi:10.1073/pnas.1205566109 |
| Critique: effect may not be dyslexia-specific; authors' Bayes-factor reply | Verified | doi:10.1073/pnas.1212877109; doi:10.1073/pnas.1213265109 |
| Speed gains in dyslexic (13%) and non-dyslexic (5%) students | Verified | Stagg & Kiss 2021, doi:10.1016/j.ridd.2021.104065 |
| No effect of inter-letter spacing on accuracy, comprehension, or speed | Verified | Łuniewska et al. 2022, doi:10.1016/j.learninstruc.2021.101576 |
| 215 adults: extreme letter and word spacing reduced speed, comprehension, preference | Verified (conference abstract) | Wallace, Dobres, Bylinskii & Sawyer 2022, J. Vision 22(14):3349 |
| Good white space: slower reading, better comprehension; leading affects preference only | Verified (abstract) | Chaparro, Shaikh & Baker 2004, Usability News 6.2 |
| Enhanced vs poor layout: no speed or comprehension difference; satisfaction 5.50 vs 3.25; 90% prefer enhanced | Verified | Usability News 7.1 (2005) |
| Proximity grouping | Unverified (not re-checked) | Wagemans et al. 2012, *Psychological Bulletin* |

## Hierarchy and depth

| Claim | Status | Source |
|---|---|---|
| Scanning patterns worst to best: F, spotted, layer-cake, commitment; layer-cake "by far the most effective" short of full reading; commitment gives best comprehension | Verified | NN/g, text-scanning-patterns-eyetracking |
| Scanners land on links, bold words, numbers, lists | Verified | same |
| Weak signifiers: 71 participants, 9 sites, 22% longer, 25% more fixations; 86% (25/29) vs 50% (12/24) | Verified | NN/g, Moran 2017 |
| Beauty correlates with apparent usability (r = .589) | Verified | Kurosu & Kashimura, CHI '95 |
| No aesthetics effect on SUS with real use; replicated | Verified | Grishin & Gillan 2019, JUS 14(2); Alharoon & Gillan 2020 |

## Learning science

| Claim | Status | Source |
|---|---|---|
| Signaling: 103 studies, N = 12,201; retention g = 0.53, transfer g = 0.33 | Verified | Schneider, Beege, Nebel & Rey 2018, doi:10.1016/j.edurev.2017.11.001 |
| Signaling moderators: color 0.39, blinking −0.47, text 0.68/0.48 | Secondary | TUM Clearinghouse summary |
| Retrieval practice g = 0.61 overall | Verified | Adesope et al. 2017, doi:10.3102/0034654316689306 |
| Largest multimedia benefits: second-language captions, contiguity, signaling; design matters more for system-paced media | Verified | Noetel et al. 2022, doi:10.3102/00346543211052329 |
| Contiguity g = 0.74; sentence-level coherence 0.63; segmenting 0.19 (n.s.) within Mayer's research | Verified | Cromley & Chen 2025, doi:10.1016/j.edurev.2025.100730 |
| Coherence: 23 of 23 tests, median effect 0.86 | Verified | Mayer & Fiorella, *Cambridge Handbook of Multimedia Learning* |
| Segmenting: small to medium effects (56 investigations) | Verified | Rey et al. 2019, doi:10.1007/s10648-018-9456-4 |
| Position on a common scale is read most accurately (Cleveland & McGill ranking) | Unverified (widely cited) | Cleveland & McGill 1984/1985 |

## Web platform

| Claim | Status | Source |
|---|---|---|
| svh/lvh/dvh: Chrome 108, Firefox 101, Safari 15.4 | Verified | caniuse.com/viewport-unit-variants |
| WCAG 2.2 criteria in `accessibility.md` | Verified | w3.org/TR/WCAG22 |
| Core Web Vitals "good": LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1, at the 75th percentile | Verified | web.dev/articles/vitals |
