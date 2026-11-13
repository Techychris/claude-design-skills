---
name: design-pipeline
description: Use to take an app idea to a gated, audited single-file HTML prototype using parallel subagents. Builds 2-3 distinct directions, runs a deterministic gate and a behavior probe, audits from accessibility, usability and visual viewpoints, verifies severe findings in a browser, and produces one merged report. Use when asked to run the design pipeline, compare design directions, or audit designs from several viewpoints.
---

# Design pipeline

Eight stages. Stages 4, 5 and 7 are deterministic or browser-verified; the model audits in stage 6 produce leads, not facts.

| # | Stage | Who | Output | Pass condition |
| --- | --- | --- | --- | --- |
| 1 | Brief | you | `brief.md` | product, user, job, placeholder-data rule written |
| 2 | Directions | you | `directions.md` | 2-3 directions that differ in layout and data shape, not just color or mode |
| 3 | Build | one builder subagent per direction | `dN/index.html` | builder reports its own gate run |
| 4 | Gate | script | `gate-N.txt` | `gate.js` all rows pass at 1440 and 390 |
| 5 | Probe | script | `probe-N.txt` | `probe.js` no FAIL, or each FAIL listed as a finding |
| 6 | Audit | one auditor subagent per viewpoint, in parallel | `audit-<viewpoint>.md` | every finding has criterion, location, severity 0-4, fix, evidence label |
| 7 | Verify | one verifier subagent | `verified.md` | every severity 3-4 finding re-tested in a browser: CONFIRMED, REFUTED or UNTESTABLE |
| 8 | Report | you | `REPORT.md` | merged, de-duplicated, ranked; states what was not tested |

## Rules

- **Subagents use Haiku** unless the user approves a stronger model for a named task.
- **Placeholder data only.** No customer data, policy data, credentials or real names. Owners and requesters are teams or roles.
- **Do not let a builder grade itself.** Re-run the gate and the probe yourself after the build; trust those over the builder's report.
- **Evidence labels:** `confirmed` (script or browser result), `observed` (seen in a screenshot), `inferred` (reasoned from source). Audits that skip the label are rejected.
- **Count a finding once.** Merge duplicates across auditors; record how many auditors raised it.
- **A model finding that a script or browser refutes is dropped and noted.**
- Never edit another stage's output. Fixes are a new build round, then stages 4-5 again.

## Setup

```bash
export NODE_PATH=<dir containing node_modules/playwright>   # headless Chromium
RUN=runs/<app-name>; mkdir -p $RUN/d1 $RUN/d2 $RUN/shots
# gate.js lives inside design-lean/SKILL.md; extract it (see that skill's "Get and run the script"), then:
cp <skill dir>/probe.js $RUN/                    # scripts stay outside the design folders
```

Run scripts with the design path as an argument:

```bash
node $RUN/gate.js  $RUN/d1/index.html > $RUN/gate-1.txt     # exit 1 on any failure
node $RUN/probe.js $RUN/d1/index.html > $RUN/probe-1.txt
```

## Prompt templates

`prompts/builder.md`, `prompts/auditor.md`, `prompts/verifier.md`. Fill the `{{placeholders}}` and pass as the subagent prompt. Auditor viewpoints: `accessibility` (skill: accessibility-audit), `usability` (skill: heuristic-evaluation), `visual` (skills: unslop and design-lean slop signs).

## Known limits

Haiku auditors read source and screenshots; they do not run a browser. The probe covers keyboard focus, dialogs, reflow, reduced motion, names and empty states only. Neither covers screen readers, Safari, Firefox, forced colors or real touch.

## Lessons from the first two runs (Intake Board, Room Board)

- A passing gate and a passing probe do not mean usable. Room Board passed both (161/161, 104/104) and still carried 10 severity 3 problems. Never stop at stage 5.
- Haiku audits held up: 8 of 10 severity 3 findings confirmed in a browser, 0 refuted. Detail slips (a time, a count) are common, so verify numbers before they go in a ticket.
- Every audit finding of severity 3 or higher goes through stage 7. Taste findings stay labelled opinion.
- Re-run the gate and probe yourself; builders reported accurately here, but the rule costs one minute.
- Directions must differ in layout and data shape. The Intake Board pair shared data and copy and the audits said so; the Room Board pair did not have this problem.
- The probe skips the empty-state check when there is no search box. Extend it to drive filter selects, and add booking-style checks (clashes, past times) as app-specific tests the builder must write.
- Builders cannot write their own severity 3 fixes blind. A fix round is a new builder prompt that contains the verified findings, then stages 4 and 5 again.
