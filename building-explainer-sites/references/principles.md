# Principles of explorable explanations

## Contents
- Why explorables exist
- Guide, don't sandbox
- Readable without interaction
- How few readers interact
- Topics that suit interaction
- Question before answer
- Safe, legible experimenting
- Learning-science effects to use
- The expert trap

## Why explorables exist

Bret Victor's 2011 essay *Explorable Explanations* argued that ordinary reading environments let readers form questions and imagine alternatives, but give them no way to explore or verify either. Readers end up trusting the author blindly or distrusting blindly. Interactivity closes that gap by letting readers check claims themselves.

## Guide, don't sandbox

- Victor separates explorables from isolated widgets: an explorable deliberately directs attention to specific phenomena inside the simulation.
- Red Blob Games: most interactive widgets leave readers to work things out alone. Pair every explorable with prose that says what to look for.

## Readable without interaction

- The explanation must work as plain text. Interaction is optional enrichment (Red Blob Games).
- Alternate prose and explorables.
- Never put essential information behind a click or hover. Gregor Aisch (NYT graphics) put it this way: if some information is crucial, don't make the user click or hover to see it, because 15% of readers aren't nobody.
- Archie Tse (NYT, Malofiej 2016) gave a related rule: if you make a tooltip or rollover, assume no one will ever see it.

## How few readers interact

The widely repeated "only 10–15% of NYT readers interact" figure is narrower than it sounds. Gregor Aisch measured the share of readers who clicked one prominent button in a couple of 2015 NYT graphics, and found about 15%. He stresses that the other 85% didn't ignore the graphic; they just didn't click the button.

Hohman, Conlen, Heer and Chau (2020, Distill) note there is limited empirical evaluation of interactive articles, partly because publishers don't share metrics. Conlen, Kale and Heer (2019, Computer Graphics Forum) instrumented three interactive articles across more than 50,000 reader sessions.

**Design implication:** expect a minority to interact. Interaction must reward the curious without penalizing everyone else.

## Topics that suit interaction

- Explorables work best for systems, models, and networks of cause and effect (Nicky Case, 2014 workshop notes).
- Not everything benefits from interaction (Red Blob Games). A list of facts, a definition, or a single comparison is usually better as prose, a table, or a static chart.
- Tversky, Morrison and Bétrancourt (2002): the most promising uses of animation are real-time changes and reorientations in time and space.

## Question before answer

From Nicky Case's 2014 workshop notes:
- Withholding the explanation for a moment can make it land harder.
- Embed small "homework problems."
- Gate advanced sections, explicitly or implicitly, so readers don't reach material before they have the background.
- End with something that makes the reader use what they learned.

## Safe, legible experimenting

These come from Bartosz Ciechanowski's essays, as described in a design review:
- an undo or reset appears once the reader starts changing things;
- each concept is color-coded the same way in text and visuals;
- 3D content can be rotated so readers get their bearings.

## Learning-science effects to use

| Effect | Size | Status | Use it as |
|---|---|---|---|
| Signaling (highlighting, cues) | g = 0.53 retention, 0.33 transfer; 103 studies, N = 12,201 | Verified: Schneider, Beege, Nebel & Rey 2018 | Highlight the one change that matters; reserve emphasis |
| Retrieval practice | g = 0.61 overall | Verified: Adesope, Trevisan & Sundararajan 2017 | Prediction prompts, quick checks with feedback |
| Temporal/spatial contiguity | g = 0.74 (as cited by Cromley & Chen 2025) | Verified: Noetel et al. 2022 umbrella review lists it among the largest benefits | Put labels on the figure, beside the thing they name; narrate while it moves |
| Coherence (cut extraneous material) | median d = 0.86, supported in 23 of 23 tests | Verified: Mayer & Fiorella chapter | Remove decorative detail, background music, tangents |
| Segmenting | small to medium effects (Rey et al. 2019, 56 investigations); non-significant within Mayer's own lab (0.19, Cromley & Chen 2025) | Mixed | Break long animations into reader-paced steps |
| Design matters more for system-paced media than self-paced | qualitative | Verified: Noetel et al. 2022 | Websites are self-paced; still apply the principles, but expect smaller gains than in video |

Tversky et al. (2002) found that most apparent successes of animation came from extra information or procedures (interactivity, prediction), not from animation itself. They recommend:
- slow and clear motion;
- schematic rather than realistic visuals;
- arrows or highlights on the critical change;
- learner control over pace (stop, start, replay, zoom).

## The expert trap

A criticism quoted in Red Blob Games' notes: explorables don't scale and often mainly benefit people who already understand the concept. Test with a reader new to the topic, and check that they can state the takeaway afterward.
