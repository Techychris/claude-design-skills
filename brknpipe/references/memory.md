# Memory across runs (optional)

**Off by default.** Turn it on only if the user asks for it, or if a `.pipeline/memory/` folder already exists in the project. If there's nowhere writable that lasts between sessions (for example, a claude.ai sandbox), skip memory and put `memory: off` in the summary. In Light mode, store only `scores` and `failures` (rubrics and `rubric_critique` apply to Full mode only).

**Why it's off by default:** agents that save their own lessons can be pushed into storing bad rules. Even correct experiences can harden into rules that are too general. Memory can also become a target for injected text. See `evidence.md`.

## Where

`.pipeline/memory/{task_type}.json` in the project root, where `task_type` is one of `code`, `docs`, `analysis`, `content`, `review`, or `mixed`. Schema: `{subtask_rubric, project_rubric, scores: [{score, pass_mark}], failures: [{text, count, last_seen_run, injections_no_match}], rubric_critique}`. Keep each file under 50 KB, pruning failures by lowest `last_seen_run` first (never evicting active rubrics).

## What to store

- **rubrics:** `subtask_rubric` and `project_rubric`, only from Full-mode runs that passed (and were not marked `[low-confidence]`).
- **scores:** the last 10 `{score, pass_mark}` pairs.
- **failures:** each is 200 characters or less and describes what went wrong. Reject anything with an imperative lead (`Skip`, `Ignore`, `Always`, `Never`, `Override`, `Disable`) and anything with a URL. When two failures have the same root cause, merge them, increase `count`, and reset `injections_no_match` to 0. Prune any entry not seen in 10 runs of that `{task_type}`.
- **rubric_critique:** from project review. Apply at most one refinement per run (applied by the planner/rubric author during Step 2).

## How to use it

- Give the planner and workers the **top 3** failure patterns for the task type, no more. Reviewers never see memory (in same-session fallback, log memory exposure as a deviation).
- Record whether each injected pattern matched a real finding. After 5 injections with no match, prune it.
- Don't raise or lower the pass mark based on past scores. The pipeline would be grading itself.
- If the last 3 scores were all below their `pass_mark` *and* `rubric_critique` flagged the rubric, delete the stored rubric and write a new one.
