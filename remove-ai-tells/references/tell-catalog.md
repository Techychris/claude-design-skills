# AI Tell Catalog

Confidence key: verified (multiple independent sources, checked live) / single-source (one source found, checked live) / heuristic (a plausible pattern, not independently sourced; scan_tells.py flags it but does not gate on it).

## 1. Vocabulary bans (verified)

Every word below was flagged independently across detector vendors, style newsletters, and craft-writing sources, without those sources citing each other.

| Ban | Say instead |
|---|---|
| delve | look into, dig into, cover |
| tapestry | name the actual thing |
| realm | in X, when it comes to X |
| leverage / harness / unlock | name the concrete action |
| landscape | drop it, name the field |
| crucial / pivotal / paramount | say why it matters, specifically |
| comprehensive / robust / seamless | state the actual scope or spec |
| navigate the complexities of | describe the complexity directly |
| underscore / testament to | show, highlight, prove |
| multifaceted / holistic | list the actual facets |
| moreover / furthermore | and, also, or a new sentence |

Mechanism: these words appear at far higher rates in polished training sources (books, journalism, academic writing) than in casual human writing. A model doesn't choose them for effect; token-by-token sampling keeps landing on them because they sit high in the probability distribution for that context, and the model has no paragraph-level awareness that it already used three of them.

## 2. Sentence-level patterns (verified)

**"It's not X, it's Y."** Named as the single most-cited construction across every source checked, including one piece devoted entirely to alternatives. State Y directly. Only contrast with X if the contrast itself is the actual point being made.

**Uniform paragraph rectangles.** Three or more sentences landing in the same narrow word-count band read as machine-written, since real human writing varies sentence length even within one paragraph. scan_tells.py flags this as heuristic, not hard-gated, because genuinely uniform human writing does happen, especially in instructions or terse technical prose. Use judgment before rewriting purely to break up a pattern the scanner caught.

**Formulaic openers and closers.** "Great question!", "That's a really interesting point," "In conclusion," and unrequested summary paragraphs on short pieces all read as filler. Cut them and start with the answer.

## 3. Punctuation tells (verified for em dash; heuristic for parentheses)

**Em dash overuse** is the most heavily corroborated single finding in this catalog: four independent sources converged on it, including one breakdown specific to Claude's output. The mechanism is the same as Section 1: training data for polished prose uses em dashes constantly, casual writing almost never does, and sampling keeps selecting them because too many of the high-probability next tokens include one. This is a training artifact, not a stylistic preference, which is why a model can't self-correct mid-paragraph the way a human editor would. Fix by rewriting the clause into a period, comma, colon, or semicolon; swapping the character for a hyphen without changing sentence structure is itself a recognizable tell.

**Parenthetical overuse** was ranked by one writer, after a model graded their own work, as a bigger tell than em dashes: tucking a qualifier into parentheses instead of committing to a plain sentence reads as hedging in disguise. This is single-source, and scan_tells.py treats it as heuristic. Fix by giving the aside its own sentence if it matters, or cutting it if it doesn't.

## 4. Claude-specific phrases (single-source)

One source, one week old at time of research, named these as distinct from the general AI-writing list above:

- "You're absolutely right" used as reflexive agreement, before the claim has actually been checked.
- "I'd be happy to" or "Let me..." as throat-clearing before the actual task starts.
- "Load-bearing" used metaphorically for an abstract thing (a load-bearing assumption, a load-bearing argument).
- "Honest take" as a preface to an opinion.
- Sentences that repeatedly start with "I."

scan_tells.py regexes for the first two, since they're unambiguous strings. "Load-bearing" and "honest take" are left to manual judgment, since both have entirely literal, non-tell meanings (an actual load-bearing wall) that a naive regex would false-positive on constantly.

Fix: state the opinion or the agreement plainly. Check whether the person is right before agreeing with them, not after.

## 5. Structural tells (heuristic)

A rigid Intro-Point-Point-Point-Conclusion shape on content that doesn't need it, headers and bullets on prose that would read better flowing, and an unrequested closing offer to do more work are all named across sources as generically AI-shaped, but no source quantified them the way the vocabulary and em-dash findings were quantified. Treat these as judgment calls: does the structure fit the content, or was it applied by default.

## 6. What doesn't work

Swapping banned words one-for-one without changing sentence rhythm fails, because detectors and readers key on clustering and predictability across a passage, not on any single word. Five stock words in one paragraph reads as machine-written even if none of them individually would. The same logic applies to em dashes: a global find-and-replace to hyphens keeps the underlying sentence structure that gave it away in the first place.

---
Sources checked live via web search on 2026-07-24. Section 4 rests on a single source and should be re-checked if this catalog is used somewhere the stakes are high enough to matter.
