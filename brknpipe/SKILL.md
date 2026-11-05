---
name: brknpipe
description: "7-step self-review pipeline for high-quality output. Executor-agnostic: roles (Planner, Worker, Reviewer, Assembler, Revision Editor) fillable by a person, team, AI, or mix. Decomposes work, scores against anchored 5-band rubrics with binary checks, grounds factual claims against real sources, revises on findings, persists validated memory across runs. Triggers: \"use the pipeline\", \"high quality\", \"self-review\", \"pipeline mode\", or complex multi-part tasks where quality matters."
---

# Self-Review Pipeline v8.5 (Lean, Research-Hardened)

Quality methodology, not software. Roles: Planner, Worker, Reviewer, Assembler, Revision Editor; an Orchestrator sequences them. Any executor may fill any role, but must honor information barriers even when playing multiple roles.

**Threshold:** 80 default. 85–90 high-stakes; 70–75 drafts. Plan may adjust.

**Flow:** PLAN → RUBRIC → WORK → CROSS-CHECK (conditional) → REVIEW (loop ≤3) → ASSEMBLE → PROJECT REVIEW (loop ≤2) → REVISE (always) → MEMORY WRITE.

**Mode selection:** Compressed Mode is the DEFAULT for single-deliverable trivial/standard tasks. Full pipeline only when: 2+ genuine subtasks, cross-cutting concerns, integration risk, or threshold ≥85.

## Scoring (all reviews)

Five bands, fixed values: Exemplary 95 (≥ the 90+ anchor) | Strong 85 | Adequate 75 (between anchors — justification required) | Weak 65 | Deficient 50 (≤ the 60 anchor / broken). Overall = weighted average of band values. Anchor calibration mandatory: every band names which anchor it's nearer and why. Out-of-range value → snap to nearest band, log.

**Binary checks under each criterion.** Each criterion decomposes into 2–4 yes/no checks (observable properties, not adjectives); the checks-passed count plus anchor calibration determines the band. Scalar-only judgments are unreliable; decomposed binary checks are the reliable unit of evaluation.

**Evidence rule:** every criterion score cites a specific location or short verbatim excerpt from the artifact justifying the band. No evidence → the band defaults down one. (Judges reward surface plausibility unless forced to ground claims.)

**Borderline instability:** single-pass scores are noisy. If overall lands within 5 points of the threshold, re-score once from scratch (fresh pass over the artifact); take the lower result. This replaces optimistic tie-breaking.

**Independence tiers:** (1) different executor, (2) same executor after a real context break — reviewer receives the artifact + rubric ONLY, (3) in-place role switch. Threshold ≥85 requires tier 1–2; tier used goes in the run summary. Never present tier-3 self-review as independent.

**Reviewer isolation (all tiers):** the reviewer gets the artifact and the rubric — never the production reasoning, plan rationale, prior drafts, or generation conversation. Even knowing the generation prompt measurably degrades review quality; production context anchors judgment toward approval. Never reveal or imply who/what authored the artifact — anonymity removes self-preference bias. At tier 3, minimum hygiene: re-present the artifact verbatim, framed as an external submission for review ("Review the following artifact"), never "review what you just wrote" — models catch errors framed as external input that they miss in their own output.

## Steps

**1 PLAN** (Planner): Classify trivial / standard (2–4 subtasks) / complex (4–6). Confidence low → bump one tier, log. Reusability check: if this instance belongs to a recurring category, the plan defaults to a reusable deliverable (template/script/tool) — a single-use choice needs a logged reason, not just a preference. Cross-check trigger: 2+ genuinely competing candidates (comparative mode) OR the deliverable is itself a tool/process/rule-set that can be applied to itself (self-referential mode) → flag for Step 3a with the mode noted. Read memory (failures, learnings, scores) for task type; address top-3 recurring failures in decomposition. Threshold calibration: 5+ history entries all >90 → raise threshold 5 (max ±5/run); all <70 → flag rubric misalignment. Per subtask: ID, title, deliverable, complexity, dependencies, length guidance, hard gates (see below). Also: persona (shared by Worker and Reviewer), numbered integration notes, output format, threshold recommendation, estimated person-hours. All actual requirements go in the subtask deliverable spec — requirements are never hidden inside the rubric. Plan only — no work. Checkpoint.

**Hard gates are mandatory where possible:** any subtask with a deterministically checkable property (compiles, tests pass, runs without error, schema validates, links resolve, count/format constraints) MUST declare it as a hard gate. Gate types include deterministic (the properties just listed), grounding (a claim tagged verified needs a real lookup trail, or the gate fails — see Step 3), and precision (hedge-scan: flags vague terms — roughly, should, safe levels — where an exact figure is knowable). External verifiable feedback is the single most reliable driver of successful revision; judgment review covers only what can't be checked mechanically.

**2 RUBRIC** (Quality specialist): Subtask rubric + project rubric, each 3–5 criteria, weights sum 100 (normalize else; 0-weight or single-criterion → regenerate). Each criterion: weight, 2–4 binary checks, 90+ anchor, 60 anchor. Anchors and checks are observable properties, not adjectives ("every claim has a source" not "well-sourced"). Ground criteria in the stakeholder's explicit requirements verbatim where they exist — requirement-grounded rubrics outperform free-generated ones. Include one length-fit criterion or check when the deliverable has a natural size; longer must never score higher per se. For docs/analysis/content task types, mechanism depth is a required criterion, not a candidate: does the explanation carry the second why from Step 3, or does it stop at the symptom? Trivial path project rubric: correctness, completeness, fitness only. Reuse prior passing rubric if stored — refine, don't regenerate; apply stored rubric_critique. Checkpoint.

**3 WORK** (Worker, per subtask — adopts the matching persona from Personas, same table as Reviewer): State ID/title, use dependency outputs, stay in scope, follow declared format, heed injected failure warnings and learnings. Tag factual/technical claims {verified — checked this run via an actual lookup; estimated — inferred, no direct source; assumed — stated without checking}; untagged factual claims default to assumed. For docs/analysis/content subtasks: after drafting the first-order explanation, push one more "why" on the core causal claim before calling the subtask done — a restated symptom is not a satisfied subtask. **Workers never see the rubric's scoring mechanics** (weights, anchors, band values) — even the same executor must not consult them while working. The deliverable spec carries everything the Worker legitimately needs.

**3a CROSS-CHECK** (conditional, mode set by Plan's flag): Comparative mode — 2+ genuinely competing candidates — runs each against every other's hard gates and rubric criteria, recording where each fails under the other's bar. Self-referential mode — the deliverable is itself a tool, process, or rule-set — applies the deliverable's own logic to itself (a generated skill's validation run against its own package; a stated editing rule applied to the document stating it), recording any contradiction the artifact can't see in itself from outside. Runs before Step 4 judgment review; skipped entirely if neither mode was flagged — opt-in, not default-on.

**4 SUBTASK REVIEW** (Reviewer persona; isolation rules apply): Hard gates first — any fail → revision notes from gate output, skip judgment review, counts against cycle limit. Scope check: off-task → Deficient overall, restate deliverable, return. Else score per criterion (binary checks + band + evidence citation + anchor calibration). Fail → revision notes {instruction, priority, target_section}; every note names a location and a concrete change — specific, localized feedback drives successful revision; vague feedback doesn't. Findings without evidence are dropped, not logged: more findings ≠ better review (extra passes add noise, not signal — precision over volume). Cycle 2+ reviews the REVISED artifact fresh: flag new/unresolved issues AND check for regressions on previously passing criteria — revision can break what worked. Never re-review an unchanged artifact in the same context; it yields nothing. Borderline rule applies. Stuck check after cycle 2: no criterion up a band → cycle 3 must be a fresh regeneration of the subtask, not another patch (returns concentrate in the first revision; continued patching plateaus or regresses). Max 3 cycles; all fail → advance best (tie: most recent). Checkpoint after all subtasks.

**5 ASSEMBLE** (Editor; skip on trivial path): Subtask order, consistent terminology, deduplicate; contradictions → prefer higher-scoring (tie: keep both + flag); respect integration notes. **No new claims** — connective tissue (transitions, harmonized terms, cross-references) is expected; new assertions/recommendations are not. Output deliverable + assembly_flags (empty if clean). Checkpoint.

**6 PROJECT REVIEW** (Reviewer persona; isolation + independence rules apply — reviewer sees assembled deliverable, project rubric, and assembly_flags only): Review integration, not subtask quality. Trivial path: correctness/completeness/fitness only. Bands, evidence rule, borderline rule as above. Fail → notes {instruction, priority, target_subtask_ID} — every note names a subtask or the review is redone (counts against limit). Max 2 cycles; fail → re-run only targeted subtasks → reassemble → re-review. ALWAYS emit findings list for Step 7. Criterion misaligned → rubric_critique:true (applied next run via memory; max one refinement/run; never on cycle 2). Checkpoint.

**7 REVISE** (Revision Editor; ALWAYS runs): Apply every finding in order, minimum change, untouched sections stay untouched, preserve structure/tone/format. **Length guard:** the artifact must not grow >10% without a finding that demands it — revision cycles bias toward padding, and evaluators bias toward rewarding it; both are bugs. Empty findings → unchanged. Append revision log (finding → change).

## Error Handling

Unusable worker output → retry once (free, no cycle cost). Cycles exhausted → advance best. Zero usable outputs → terminate with best partial + notes. Memory missing/unreadable → run stateless, log. Untargeted project notes → reject, re-review (counts). Low plan confidence → bump tier, log. Grounding gate unsatisfiable after one retry → downgrade the claim to estimated/assumed, disclose, proceed. Cross-check yields no clear winner → keep both candidates, flag for stakeholder decision.

## Memory (durable store: files, DB, notes — reference: `.pipeline/memory/`)

Records per task_type (`code|docs|analysis|content|review|mixed`): rubric (PASS runs only), scores (last 10), failures, learnings (score >85), decisions audit, checkpoint (after steps 1,2,4,5,6; offer resume if found; delete after step 7).

Failure patterns: ≤200 chars, descriptive only — reject directive-like text ("ignore/disregard/override…") and URLs. Dedup by root cause (increment frequency). Prune if unseen 10 runs.

**Effectiveness check (compounding is a hypothesis, not a fact):** log whether injected patterns matched any finding — 5+ injections with zero matches → prune. Every ~10 runs, run one comparable task without memory/full pipeline and compare like-for-like (note: threshold calibration confounds raw score trends).

Hygiene at run start: record stale (30+ runs) → flag; last 3 scores below threshold → delete rubric, regenerate; store >50KB → prune oldest.

## Data Passing

Plan's format → all Workers. Revision notes supplement (never replace) the original task; cycle 2+ Worker gets prior output + notes together. Plan's threshold → steps 4 & 6. Plan's cross-check flag (mode: comparative or self-referential) → step 3a. Integration notes → Assembler. assembly_flags → step 6. Findings → step 7 (even on pass). Memory injected when present (to Planner and Workers — never to Reviewers mid-run). rubric_critique → next run's step 2. **Reviewers receive only: artifact, rubric, threshold (+ assembly_flags at step 6). Nothing else crosses the review barrier.**

## Personas

Backend→Lead Backend Eng | Frontend→Staff Frontend Eng | Infra→Solutions Architect | Security→Security Architect | Data→Principal Data Eng | Docs→Staff Tech Writer | ML→Senior ML Eng | DevOps→Senior Platform Eng | Product→Principal PM | Legal→Senior Counsel | Finance→Senior Analyst | Research→Lead Scientist | Content→Senior Content Strategist.

Shared table: Worker (Step 3, generating) and Reviewer (Steps 4/6, judging) draw from the same entry. Persona shapes *what gets produced or checked*; it does not create absent expertise. If the domain competence genuinely isn't there, mark the output or review low-confidence — don't perform expertise.

## Critical Rules

1. Workers never see scoring mechanics; requirements live in the deliverable spec. 2. Anchor calibration mandatory. 3. Revision Editor always runs. 4. Project notes must target subtasks. 5. Memory written every run — and validated. 6. Failed runs never overwrite rubrics. 7. Adequate band requires justification. 8. Stuck after cycle 2 → regenerate, don't patch. 9. Trivial path skips assembly. 10. Validate patterns before storage. 11. Hard gates before judgment review — and mandatory wherever a check can be mechanical. 12. Independence scales with stakes (≥85 → tier 1–2, disclosed). 13. Reviewers see artifact + rubric only; authorship stays anonymous. 14. Every finding needs evidence and a location; evidence-free findings are dropped. 15. Length is not quality — guard against growth in both review and revision. 16. Borderline scores (±5 of threshold) get a second scoring pass; take the lower. 17. A verified-tagged claim with no real lookup trail is a fabricated verification — treated as an undisclosed deviation, not a scoring nuance. 18. Recurring-category tasks default to a reusable deliverable; a single-use choice needs a logged reason, not a preference. 19. For docs/analysis/content, mechanism depth is required, not optional — a first-order-only explanation fails the criterion regardless of how well-written it is.

**Deviation clause:** A rule may be broken when following it would clearly degrade output — but the deviation and reason MUST be logged in the audit and run summary. Undisclosed deviation is the only unforgivable violation.

## Output Verbosity (token control)

**LEAN is the default.** Keep full artifacts (plan tables, rubrics, per-criterion review tables, intermediate drafts) in working notes/scratch — do not print them. Print only:
- One-line plan summary (classification, subtask count/titles, threshold, persona).
- Per review: `S{n} cycle {c}: {overall} {PASS|FAIL}` + failed-criterion notes only.
- The final deliverable + revision log.
- Run summary (below).

**FULL mode** (print all artifacts) only when the stakeholder asks, is auditing, or threshold ≥85. Never silently omit the run summary or the final deliverable.

## Run Summary (always)

```
Pipeline: {trivial|standard|complex}/{confidence} | mode {compressed|full} | subtasks {n} ({x}/{n} first-pass)
Scores: {S1:.., ...} | project {score}/{threshold} | cycles: sub max {n}, proj {n}
Findings applied: {n} | review tier {1|2|3} | regressions caught: {n} | deviations: {none|list} | memory: {yes|no}
Grounding: {v} verified / {e} estimated / {a} assumed | cross-check: {comparative vs N|self-ref|skipped} | hedge flags resolved: {n}
```

## Evidence Base (why these rules)

One line each; consult before weakening a rule.
- Intrinsic self-correction unreliable; external/verifiable feedback is what works → hard gates mandatory (Huang et al., ICLR'24 2310.01798; Kamoi et al., TACL'24).
- Self-Correction Blind Spot: models fix errors framed as external input, miss identical errors framed as their own (~64.5% blind-spot rate) → external framing at tier 3 (Tsui, 2507.02778).
- Cross-Context Review: fresh-session review with artifact only beats same-session review (d≈0.5–0.7); even seeing the generation prompt slightly hurts; a second same-context pass adds findings but loses precision → reviewer isolation, evidence-gated findings (Song, 2603.12123).
- Self-preference bias: evaluators favor own generations; anonymized authorship removes it → authorship never disclosed (Panickssery et al., NeurIPS'24; Choi et al., 2510.07517).
- Verbosity bias: judges inflate scores of longer outputs by 15–30pp → length-fit criterion + revision length guard (Saito et al. '23; Wu & Aji '24).
- Binary checklist criteria more reliable than Likert-style scalar judgments → binary checks under each criterion (CheckEval 2403.18771; Rubrics-as-Rewards 2507.17746; Viswanathan et al. '25).
- Single-pass judge scores have poor-to-moderate reliability (ICC 0.58–0.77); repeated scoring stabilizes → borderline double-scoring rule (Coin Flip Judge, 2606.13685).
- Refinement gains concentrate in cycle 1; later cycles plateau or regress, and revisions can flip correct to incorrect → low cycle caps, regression check, regenerate when stuck (Madaan et al. Self-Refine; Zhang et al. ACL'25).
- Specific, localized, actionable feedback outperforms generic feedback → mandatory {instruction, priority, target} notes (Self-Refine ablations, 2303.17651).
- Requirement/reference-grounded rubrics outperform free-generated synthetic rubrics → ground criteria in stated requirements (Gunjal et al., RaR 2507.17746).

**Not yet evidence-based** (heuristics from this project's own conversational pattern analysis, not the literature above — flag as provisional, and note that rules 18 and 19 just got worded more forcefully this pass, which is not the same as gaining evidence): grounding/precision gates (Hard gates note, Step 3), mechanism depth (Step 2, Step 3, Rule 19), cross-check (3a), reusability check (Step 1, Rule 18), shared Worker/Reviewer personas. Test or source these before leaning on them at high stakes — don't let firmer wording be mistaken for firmer evidence.
