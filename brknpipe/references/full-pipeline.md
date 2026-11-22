# Full mode

Read this only in Full mode. Everything in SKILL.md still applies (with Full-mode scoping noted below): the review barrier, the stopping rules, the token rules, and the run summary. Full mode adds subtasks, weighted rubrics, assembly, and a project-level review.

**Flow:** PLAN → RUBRIC → WORK → HARD GATES & BREAK-IT (code) → SUBTASK REVIEW (≤2 cycles) → ASSEMBLE → PROJECT HARD GATES → PROJECT REVIEW (≤2 cycles) → APPLY FINDINGS → SUMMARY

## 1. Plan

- Classify the task as standard (2–4 subtasks) or complex (4–6). If you're unsure, take the larger size and say so.
- For each subtask, record: ID, title, deliverable spec (including length and mechanism targets where applicable), dependencies, and hard gates.
- Every requirement goes in the deliverable spec. The rubric only checks requirements; it never adds hidden ones.
- Write numbered integration notes for the assembler, the output format, the pass mark, and the reviewer role.
- **Cross-check flag (optional heuristic).** Set it when there are 2+ competing candidates (each is checked against the others' gates and checks during Step 4 before Assembly), or when the deliverable is itself a rule-set or tool (apply it to itself and record any contradictions). It's off by default.

**Hard gates beyond tests *(project heuristics)*:**
- *Grounding:* a claim tagged verified needs a real lookup trail, or the gate fails. A second try uses the 3-retry gate budget (`SKILL.md` step 3) and avoids a `SKILL.md` fabricated-verification deviation if resolved before review; if still unresolved, downgrade to estimated or assumed and disclose it.
- *Precision:* flag vague terms ("roughly", "should be safe") where an exact figure is knowable.

## 2. Rubric

- Write a subtask rubric and a project rubric, each with 3–5 criteria whose weights sum to 100.
- Give each criterion 2–4 yes/no checks that name observable properties: "every claim has a source", not "well-sourced".
- Take checks from the deliverable spec and user's stated requirements, word for word where possible (including spec-stated length and, for docs/analysis, causal-mechanism checks — *project heuristic*).
- **Score** = Σ (criterion weight × share of its checks passed). If the score lands within 5 points of the pass mark and the pass mark is 85+, score once more from scratch using a fresh reviewer and keep the lower result. Below 85, don't re-score.
- If memory holds rubrics that passed for this task type, reuse and refine them, auditing every reused check against the current deliverable spec so no hidden requirements are imported.

## 3. Work

- Workers see their deliverable spec, the outputs of their dependencies, and any memory warnings. They don't see the rubric's weights or checks.
- Use the claim tags from SKILL.md step 2.
- For docs and analysis, ask "why" once more on the core causal claim before calling the subtask done.

## 4. Subtask review

- Run hard gates and break-it tests first. If any gate fails, fix and re-run up to 3 times (matching `SKILL.md` step 3) before spending a judgment-review cycle; if gates still fail, stop and escalate per the stopping rules.
- If the work is off-task, the score is 0: restate the deliverable and send it back (this consumes 1 cycle, distinct from the free retry for unusable output).
- Otherwise, score it and write notes for the failed checks only. For code at a pass mark of 85+, use the independent-tests review from SKILL.md step 6 instead of rubric scoring; propagate any `untested: <rule>` items to Assembly.
- In cycle 2, review the revised artifact fresh. Check for regressions on checks that passed before.
- Run at most 2 cycles. If both fail, advance the best version and record what still fails.

## 5. Assemble

- Put the subtasks in order and harmonize terms.
- Where subtasks contradict each other, keep the higher-scoring one; when scales differ (test ratio vs. weighted rubric), keep both and flag it in `assembly_flags`.
- Follow the integration notes and carry forward any subtask `untested: <rule>` items.
- Add no new claims. Transitions and cross-references are fine; new assertions are not.
- Output the deliverable plus `assembly_flags`, then run project-level hard gates before Project Review.

## 6. Project review

- The reviewer sees the assembled deliverable, the spec, the project rubric, the pass mark, and `assembly_flags` only.
- Review how the parts fit together, not the quality of each subtask.
- Every note must name a subtask ID or `ASSEMBLY` (for assembly-only defects). Drop single notes lacking a location (`SKILL.md` review barrier); if all notes lack a target ID, retry once without spending a cycle (on a second failure, log a deviation and fail the cycle).
- Run at most 2 cycles. On a fail, re-run only the targeted subtasks (or re-assemble for `ASSEMBLY` notes), re-run project hard gates, and re-review.
- If a criterion was clearly the wrong measure, record `rubric_critique` for next time (via memory, if it's on).

## 7. Apply findings

Run this step only if findings remain after Project Review (skip if Cycle 2 passed with 0 findings). Apply them in order, with the smallest change each. Keep the 10% per-step / 15% cumulative word-count growth limit. Re-run project hard gates after edits. Append a revision log mapping each finding to its change.

## Errors

- **Unusable worker output:** retry once; this doesn't count as a cycle.
- **No usable output at all:** stop and return the best partial result with notes.
- **Cross-check:** if `comparative` has no clear winner, keep both and ask the user to decide; if `self-ref` finds unresolvable internal contradictions, log them as Major findings rather than blocking output.

## Extra summary line (Full mode)

```
Subtasks {n} ({x}/{n} first-pass) | scores {S1:.., ...} | project {score}/{pass mark} | cycles: sub max {n}, proj {n} | regressions caught: {n} | cross-check: {comparative|self-ref|skipped} | re-scored: {yes|no}
```
