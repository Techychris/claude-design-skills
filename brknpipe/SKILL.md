---
name: brknpipe
description: "Self-review pipeline for work that has to be right. Plans the work, runs mechanical checks (tests, builds, schemas) first, tries to break code with targeted tests, then has a reviewer that sees only the artifact and the spec check it (independent tests for high-stakes code, yes/no checks otherwise), and applies the findings. Light by default, including high-stakes single deliverables. Full for multiple subtasks, integration risk, or explicit selection. Triggers: \"use the pipeline\", \"brknpipe\", \"self-review\", \"pipeline mode\", or complex multi-part deliverables where the user asks for a reviewed, high-stakes result."
---

# brknpipe v9.1.1

A review method. A person, model, or mix can fill each role. Independent review requires a fresh context. Same-session review limits what is re-presented but retains prior context.

**Core idea:** outside checks (tests, builds, validators) are the most reliable signal, so they run first and can end the run. Judgment review covers what mechanical gates cannot check. Use one Light review and the explicit Full-mode limits.

## Pick a mode

Honor an explicit mode first. Otherwise use Full for two or more genuine subtasks or integration risk, and Light for all other work. Stakes set the pass mark and reviewer.

**Light (default).** Use it for a single deliverable that does not meet the Full criteria, including high-stakes work.

**Full.** Use it for two or more genuine subtasks, integration risk, or an explicit Full request. Read `references/full-pipeline.md` before starting. Don't load it in Light mode.

**Pass mark:** Use the specified mark. Otherwise use 85 for high stakes, 75 for drafts or teaching, or 80 for standard work. At 85+, use a separate reviewer as described below. Keep checklist scores and independent test counts distinct.

## Light mode

1. **Plan, in one line.** Task type, pass mark, and the hard gates you'll run. List every requirement in the work spec itself; never hide requirements in the review checks.
2. **Do the work.** In prose, tag factual claims *verified* (you looked it up this run), *estimated*, or *assumed*; an untagged claim counts as assumed. Code doesn't use tags: its evidence is the tests.
3. **Run the hard gates.** Any property a tool can check is a gate: tests pass, it builds, the schema validates, links resolve, counts and formats match. After the initial attempt, allow up to three reruns on changed work. If required gates remain failed or unavailable, return `gate_failed` with the best partial and skip judgment review.
4. **Try to break it (code only).** Read the spec, not your own reasoning, and list the edge cases it implies: boundaries, empty and zero inputs, case and whitespace, ordering, mutation of inputs, error paths. Write 3–8 small tests aimed at them and run them.
   - When a test fails, first check its expected value against the spec. A wrong expectation is a test fix, not a finding.
   - If a rule can't be observed through the public interface (an internal allocation, say), don't write a test that can't tell right from wrong. List it as `untested: <rule>` and check it by reading.
5. **Early exit (code).** If every code gate and break-it test passes and the pass mark is under 85, stop here and skip review and revision. Otherwise carry confirmed break-it failures into revision. Unresolved failures block the final pass. Prose with passing gates gets one checklist review.
6. **One review.** Pick one kind:
   - **Code with a pass mark of 85+: independent tests.** A separate reviewer gets the spec and the path to the artifact's interface. It doesn't read the code. It writes its own tests from the spec, or a small reference version to compare against on many generated inputs, then runs them. Each failure is a finding. Record passed and executed counts. Pass independent verification only when at least one test ran, the suite completed, and every test passed. Zero tests or tool errors are inconclusive. A checklist fallback cannot establish independent verification.
   - **Everything else: a checklist review.** Write 3–6 yes/no checks taken from the user's stated requirements, plus one size check if the deliverable has a natural length. Score = 100 × passed / total. Compare the unrounded score to the pass mark and report both the count and score. A checklist passes when the score meets the mark and every explicitly critical check passes.
7. **Apply the findings once.** Make the smallest change per finding; leave untouched sections alone. The artifact must not grow more than 10% unless a finding needs it. Re-run gates and all applicable prior tests, including independent tests, after any edit. Reuse the independently authored suite for the rerun. Keep the earlier review tied to its original version. A failed required check yields a partial result. A required check without current evidence yields verification pending. If a gate is unavailable, return a partial and list that gate. Report unresolved items and stop.
8. **Summary.** Report gate status for the delivered version, review result for the reviewed version, and any verification still needed.

## The review barrier (both modes)

- For checklist review, provide the artifact, spec, checks, and pass mark. For independent code tests, provide the spec, public interface and execution target, and withhold implementation source. Pass only the allowed fields in a fresh context when independence is required. Exclude plans, earlier drafts, authorship, reasoning, and conversation history.
- Never say or imply who wrote the artifact.
- Each failed check gets one localized note and a concrete change. Include the observable evidence that makes the check fail. Write nothing for passed checks. A finding with no location is dropped.
- The reviewer adopts the matching senior specialist role (for example, staff backend engineer, senior counsel). A role doesn't add expertise the reviewer lacks; mark the review low-confidence instead.

**Who reviews.**
- **Pass mark 85+, or Full mode:** a separate reviewer. In Claude Code that's a subagent (the Agent tool), given file paths only. If a separate reviewer is unavailable, use the applicable checklist or rubric in the same session and label the context `same-session`. Where independence is required, this fallback can supply findings only. Report the outstanding verification.
- **Otherwise:** review in the same session, with the same framing. A subagent's startup costs more than the review.
- **If the reviewer fails** for a technical reason (rate limit, tool or API error), retry once without consuming a review cycle. On a second failure, use the unavailable-reviewer fallback and report the deviation.

## Stopping rules

- Stop when a revision moved no check from fail to pass. Another pass yields nothing.
- Stop when cycles run out, and report the best version and what still fails. Don't regenerate from scratch to chase the score.
- Stop early if the same required gate fails on two consecutive attempts with the same confirmed cause and no actionable fix remains.
- Never repeat judgment on unchanged work with the same checks, except for Full mode’s specified borderline re-score. An explicit meta-audit may use different checks on fixed source rules. In either mode disable nested self-audits, preserve inner limits, and record the outer-pass count separately. For a rule-set edit, include one nonrecursive trace against its own rules.

## Token rules

- Print only: the one-line plan, each review's score with its failed-check notes, the deliverable, the revision log, and the summary. Keep rubrics and drafts in scratch.
- Put the fixed text first in every review prompt (instructions, then checks), and the artifact last, so repeat reviews reuse the prompt cache.
- Keep the reviewer on a strong model. Better feedback is what makes fixes land. Save effort in planning and assembly instead.
- A claim tagged *verified* with no real lookup is a fabricated verification, and gets reported as a deviation.

**Deviations:** explain deviations in the summary. Cycle caps, final gate status, and independence labels are binding. A result missing any required verification cannot be marked complete.

## Run summary (always)

```
brknpipe {light|full} | delivered {version} {complete|partial|verification pending} | gates {passed}/{required} | break-it {passed}/{executed}|n/a | reviewed {version}|skipped | review {score}/{pass mark} or {passed}/{executed} independent tests or skipped | outcome {pass|fail|inconclusive|skipped} | context {separate|same-session|n/a} | untested {rules|none}
Findings applied: {n} | still failing: {none|list} | claims: {v} verified / {e} estimated / {a} assumed|n/a (code) | deviations: {none|list} | memory: {used|off}
```

## Reference files

- `references/full-pipeline.md`: subtasks, rubric weights, assembly, project review. Full mode only.
- `references/memory.md`: optional memory across runs. Off unless explicitly enabled by the user or project configuration.
- `references/evidence.md`: the research behind these rules, with links. Read it before weakening a rule.
