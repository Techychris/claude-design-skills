---
name: brknpipe
description: "Self-review pipeline for work that has to be right. Plans the work, runs mechanical checks (tests, builds, schemas) first, tries to break code with targeted tests, then has a reviewer that sees only the artifact, spec, and checks evaluate it (independent tests for high-stakes code, checklist or weighted rubric otherwise), and applies the findings. Light mode by default, even for high stakes; Full mode for multi-part work or when requested. Triggers: \"use the pipeline\", \"brknpipe\", \"self-review\", \"pipeline mode\", or complex multi-part deliverables where the user asks for a reviewed, high-stakes result."
---

# brknpipe v9.1.1

A review method, not software. A person, a model, or a mix can fill any role; use a fresh context via subagents whenever available, and in same-session fallback enforce neutral framing and report `by same-session` (framing mitigates bias, not context).

**Core idea:** outside checks (tests, builds, validators) are the most reliable signal, so they run first and can end the run. Judgment review covers only what they can't check, and it costs tokens, so Light mode runs it once at most (Full mode caps it at 2 cycles per stage).

## Pick a mode

Mode depends on the **shape** of the work. Stakes set the pass mark and who reviews; they never change the mode.

**Light (default).** Use it for any single deliverable, including high-stakes ones, and when the user just says "use the pipeline".

**Full.** Use it only when the work has 2+ genuine subtasks, or there's integration risk across parts, or the user explicitly asks for Full mode. Read `references/full-pipeline.md` before starting. Don't load it in Light mode.

**Pass mark:** 80 by default; 85–90 for high stakes; 70–75 for drafts or teaching. A pass mark of 85+ uses an independent reviewer (step 6; independent tests for code) and, in Full mode, a close-call re-score within 5 points.

## Light mode

1. **Plan, in one line.** Task type (`code`, `docs`, `analysis`, `content`, `review`, or `mixed`), pass mark, length/mechanism targets (if applicable), and the hard gates you'll run. List every requirement in the work spec itself; never hide requirements in the review checks.
2. **Do the work.** In prose (and prose parts of `mixed` tasks), tag factual claims *verified* (you looked it up this run), *estimated*, or *assumed*; an untagged claim counts as assumed. Code doesn't use tags: its evidence is the tests.
3. **Run the hard gates.** Any property a tool can check is a gate: tests pass, it builds, the schema validates, links resolve, counts and formats match. If a gate fails, fix and re-run, up to 3 times.
4. **Try to break it (code only).** Read the spec, not your own reasoning, and list the edge cases it implies: boundaries, empty and zero inputs, case and whitespace, ordering, mutation of inputs, error paths. Write 3–8 small tests aimed at them and run them.
   - When a test fails, first check its expected value against the spec. A wrong expectation is a test fix, not a finding.
   - If a rule can't be observed through the public interface (an internal allocation, say), don't write a test that can't tell right from wrong. List it as `untested: <rule>` and check it by reading.
5. **Early exit (code).** If the work is code, every gate and break-it test passes, and the pass mark is under 85, stop here. Skip the review and the revision. Prose always gets the review, because gates rarely cover its requirements. In Full mode, `<85` code subtasks may early-exit Subtask Review, but Project Review still runs.
6. **One review.** Pick one kind:
   - **Code with a pass mark of 85+: independent tests** *(project heuristic)*. A separate reviewer gets the spec and the path to the artifact's interface. It doesn't read the code. It writes its own tests from the spec, or a small reference version to compare against on ≥100 generated inputs *(heuristic floor)*, then runs them. Each failure is a finding. There's no rubric score; `review` = tests passed / tests run. Without subagents, a same-session reviewer has already seen the code, so use the checklist review instead.
   - **Everything else: a checklist review.** Write 3–6 yes/no checks taken from the work spec (including any spec-stated length check). Score = share of checks passed, out of 100. At a pass mark of 85+, use ≥7 checks (or a weighted rubric) if 1-check tolerance is desired.
7. **Apply the findings once.** Make the smallest change per finding; leave untouched sections alone. The artifact must not grow more than 10% by word count vs. the pre-revision draft unless a finding needs it. Re-run the gates. Then stop, even if a check still fails, and say which one.
8. **Summary** (below).

## The review barrier (both modes)

- The reviewer sees the artifact, the spec or stated requirements, the checks, and the pass mark. It never sees the plan, drafts, reasoning, memory, or a summary of the conversation. A reviewer given the conversation loses most of the isolation gain (preprint; see `evidence.md`).
- Never say or imply who wrote the artifact.
- Each failed check gets one note: where it is, and the concrete change. Write nothing for passed checks. A finding with no location is dropped.
- The reviewer adopts the matching senior specialist role *(project heuristic)* (for example, staff backend engineer, senior counsel). A role doesn't add expertise the reviewer lacks; mark the review `[low-confidence]` in the summary instead.

**Who reviews.**
- **Pass mark 85+, or Full mode:** a separate reviewer. In Claude Code that's a subagent (the Agent tool), given file paths only. Where subagents don't exist (claude.ai), review in the same session, re-presenting the work as "Review the following artifact", and report `by same-session` in `review:`. Never present a same-session review as independent.
- **Otherwise:** review in the same session, with the same framing. A subagent's startup costs more than the review.
- **If the reviewer fails** for a technical reason (rate limit, tool or API error), retry once; that doesn't count as a cycle. If it fails again, review in the same session (degrading 85+ code from independent tests to checklist per step 6) and log it as a deviation.

## Stopping rules

- Stop when a revision moved no check from fail to pass. Another pass yields nothing. In Full mode, zero-delta stops the current subtask (advancing the best version) or project stage, not prior completed subtasks.
- Stop when cycles run out, and report the best version and what still fails. Don't regenerate from scratch to chase the score.
- A run that looks headed for failure early (gates keep failing on the same cause) stops and reports to the user, instead of spending more cycles. In Full mode, this stops the failing subtask (or aborts globally only if downstream dependents are blocked).
- Never re-review an unchanged artifact, except on a protocol-error retry (`full-pipeline.md`) or a close-call re-score (using a fresh reviewer).

## Token rules

- Print only: the one-line plan, each review's score with its failed-check notes, the deliverable, `assembly_flags` (Full mode), the revision log (when revisions ran), and the summary. Keep rubrics and drafts in scratch.
- Put the fixed text first in every review prompt (instructions, then shared rubric/checks, then subtask-specific spec), and the artifact last, so repeat reviews reuse the prompt cache.
- Keep the reviewer on a strong model when subagents are used. Better feedback is what makes fixes land. Save effort in planning and assembly instead.
- A claim tagged *verified* with no real lookup is a fabricated verification, and gets reported as a deviation (unless caught and resolved by the Full-mode grounding gate before review).

**Deviations:** a rule may be broken when following it would clearly make the output worse. Log the rule and the reason in the summary. An unlogged deviation is the one thing that isn't allowed.

## Run summary (always)

```
brknpipe {light|full} | gates {passed}/{total} | break-it {n tests, n failed|n/a} | untested: {none|rules} | review {score}/{pass mark} {PASS|FAIL|skipped} [low-confidence] | review: {independent tests|checklist|rubric|mixed} by {subagent|same-session}|skipped
Findings applied: {n} | still failing: {none|list} | claims: {v} verified / {e} estimated / {a} assumed|n/a (code) | deviations: {none|list} | memory: {used|off}
```
*(In Full mode, line 1 reports project-level `gates`/`break-it`/`untested` rollups and the project review score; subtask scores appear on the Full-mode summary line.)*

## Reference files

- `references/full-pipeline.md`: subtasks, rubric weights, assembly, project review. Full mode only.
- `references/memory.md`: optional memory across runs. Off unless the user asks for it or `.pipeline/memory/` already exists.
- `references/evidence.md`: the research behind these rules, with links. Read it before weakening a rule.
