# Quality pipeline for agent deliverables

The base pipeline is the **brknpipe** skill. It used to be copied here, and the copy drifted out of date, so this file now holds only what changes when the deliverable is an agent design, prompt, or implementation.

**How to run it:**
1. Load the brknpipe skill and follow it as written: mode selection, scoring, reviewer isolation, the cycle caps, and the run summary.
2. Add the hard gates, rubric criteria, persona, and threshold below on top of it.

**If brknpipe isn't installed:** tell the person, then run a short version: check the hard gates below one by one (each is a yes/no), score the three rubric criteria below as pass/fail with a quoted line of evidence each, fix what failed once, and report what was checked and what wasn't. Don't present that as the full pipeline.

## Agent-Specific Additions (for reviewing agent designs/implementations)

When the deliverable under review is an agent architecture, prompt, or implementation (not general content), add these to the base pipeline above:

**Additional hard gates (Step 1, declare per subtask where applicable):**
- Agent terminates — no unbounded loop; a max-iteration or stop condition is defined and reachable.
- Tool/function calls are declared with correct schemas and actually invoked in a dry run or trace, not just described.
- Error paths are handled — a failed tool call or malformed input doesn't crash the run or silently proceed with bad state.
- For multi-node (graph) designs: every edge has a defined trigger condition; no orphan nodes; shared state schema is consistent across nodes.

**Additional rubric criteria to consider (Step 2), beyond the default 3–5:**
- **Pattern fit**: does the chosen pattern (prompt chaining / routing / parallelization / orchestrator-workers / evaluator-optimizer / autonomous agent) match the task's actual control needs, per the pattern table in this skill's SKILL.md — not over- or under-engineered for what's needed.
- **Blast radius appropriateness**: for autonomous-agent designs specifically, is the autonomy level justified by the ability to tolerate mistakes (i.e., checked against the "use when" column, not just chosen because it's more flexible)?
- **Context management**: for loop-based single-agent designs, is there a plan for context growth over long runs (summarization, truncation, or explicit scope limit) rather than an unbounded accumulating transcript?

**Reviewer persona addition** (extends the persona table above):
- Agent/Orchestration → **Senior Agent Systems Engineer**

**Threshold guidance for teaching/learning contexts:** when this pipeline is invoked during a mentoring session (see main SKILL.md's guided-discovery build methodology) rather than a production delivery, default the threshold to 70–75 rather than 80 — the goal is a working, understandable first agent, not a polished production system. Raise to 80+ only once the person is iterating on something they intend to ship.
