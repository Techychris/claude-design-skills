# Full mode

Read this only in Full mode. The review barrier, stopping rules, token rules, and run summary in SKILL.md apply. The Full-mode cycle budgets below govern retries. Full mode adds subtasks, weighted rubrics, assembly, and a project-level review.

**Flow:** PLAN → RUBRIC → WORK → BREAK-IT (code) → SUBTASK REVIEW (≤2 cycles) → ASSEMBLE → PROJECT REVIEW (≤2 cycles, with in-budget revisions) → SELECT RESULT → SUMMARY

## 1. Plan

- Classify one to three subtasks as standard or four or more as complex. For large work, group related subtasks to keep ownership clear.
- For each subtask, record: ID, title, deliverable spec, dependencies, length guidance, and hard gates.
- Every requirement goes in the deliverable spec. The rubric only checks requirements; it never adds hidden ones.
- Write numbered integration notes for the assembler, the output format, the pass mark, and the reviewer role.
- **Cross-check flag (optional heuristic).** Use the optional comparative check when there are two or more competing candidates. Check each against the others' gates and checks. For a rule-set edit, follow the shared nonrecursive rule in SKILL.md.

**Hard gates beyond tests:**
- *Grounding:* a claim tagged verified needs a real lookup trail, or the gate fails. If a second try can't satisfy it, downgrade the claim to estimated or assumed and disclose that.
- *Precision:* flag vague terms ("roughly", "should be safe") where an exact figure is knowable.

## 2. Rubric

- Write a subtask rubric and a project rubric, each with 3–5 criteria whose weights sum to 100.
- Give each criterion 2–4 yes/no checks that name observable properties: "every claim has a source", not "well-sourced".
- Take checks from the user's stated requirements, word for word where possible.
- Assign each scored size or mechanism check to a named criterion before work. Mark any unweighted observation diagnostic.
- For docs and analysis, add a mechanism check: does the core causal claim give the reason behind the symptom, or stop at the symptom? (This is a heuristic, not tested.)
- **Score** = Σ (criterion weight × share of its checks passed). For rubric scores within 5 points of a pass mark of 85+, score once more independently within the same cycle and keep the lower result. This planned calibration is the only repeat scoring of unchanged work. A rubric passes when its unrounded score meets the pass mark and all explicitly critical checks pass. Independent tests use their own verdict.
- If memory holds a rubric that passed for this task type, reuse and refine it.

## 3. Work

- Workers see their deliverable spec, the outputs of their dependencies, and any memory warnings. They don't see the rubric's weights or checks.
- Use the claim tags from SKILL.md step 2.
- For docs and analysis, ask "why" once more on the core causal claim before calling the subtask done.

## 4. Subtask review

- Run hard gates and break-it tests first, once per cycle. A failed required gate or confirmed break-it failure blocks judgment. Route the output to revision if a cycle remains. A selected version needs passing evidence for every required check, including previously failed break-it tests.
- If the work is off-task, the score is 0: restate the deliverable and send it back.
- Once gates pass, apply the rubric and record failed checks. For code at 85+, use the independent-tests verdict from SKILL.md step 6. Any fallback rubric is diagnostic only when independent verification is required.
- A pass ends this subtask review. On a first failure, give the worker localized findings and the prior artifact. Review the revision in fresh context against the same check IDs and prior runnable tests.
- Run at most two cycles per subtask across the whole run, including targeted project rework. If both fail, advance a labeled partial with remaining failures.

## 5. Assemble

- Put the subtasks in order and harmonize terms.
- Resolve clashes against the shared spec and interface checks. Flag unresolved clashes. Keep the best gate-passing version by required checks, then by score, then the earlier version. Label any non-passing fallback partial.
- Follow the integration notes.
- Add no new claims. Transitions and cross-references are fine; new assertions are not.
- Output the deliverable, its ownership map, and `assembly_flags` limited to observable locations and conflicts.

## 6. Project review

- Run project hard gates before judgment on the assembled version. Record a pass for every required gate on the exact selected version before returning it as complete. A failed or unavailable required gate blocks completion. Failure consumes a project cycle. Skip judgment on a failed or unavailable gate.
- For judgment review, provide only the assembled deliverable, spec, rubric, pass mark, ownership map, and sanitized `assembly_flags`.
- At 85+, also require independent tests for any public code integration surface. Provide its public interface, spec, and execution target. Use the nonempty, completed suite and all-tests-pass criteria from SKILL.md step 6.
- Review how the parts fit together, not the quality of each subtask.
- Route each localized note to one or more named subtasks or the integration owner. Log an invalid note as unresolved. Retry only with changed work and budget remaining.
- Run at most two project cycles. Rerun targeted subtasks and affected dependents within budget, then reassemble and retest. Select the best candidate under the same rules as for assembly.
- If a criterion was clearly the wrong measure, record `rubric_critique` for next time (via memory, if it's on).

## 7. Apply findings

Apply findings before the next available cycle. After the budget is exhausted, select a previously checked version and report unresolved findings. Mark the selected version complete only if its required gates and components pass, its project rubric passes, and its independent integration tests pass when required. Return a partial result for any failed requirement or unavailable required gate. If those checks have no known failure and required review is missing or inconclusive, report verification pending. Keep each judgment tied to the version reviewed.

## Errors

- **Unusable worker output:** retry once; this doesn't count as a cycle.
- **No usable output at all:** stop and return the best partial result with notes.
- **Cross-check with no clear winner:** keep both and ask the user to decide.

## Extra summary line (Full mode)

```
Subtasks {n} ({x}/{n} first-pass) | reviews {subtask, version, method, result} | project {version, rubric score, independent test result if required} | cycles: sub max {n}, proj {n} | regressions caught: {n} | cross-check: {comparative|self-ref|skipped}
```
