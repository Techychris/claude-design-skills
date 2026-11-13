You are auditing {{N}} single-file HTML designs of the same sample app from ONE viewpoint: {{VIEWPOINT}}.

Method skill(s) to read first and follow: {{SKILL_PATHS}}
Use its severity scale: 4 critical, 3 major, 2 minor, 1 cosmetic, 0 not a problem.

App brief: {{BRIEF}}
Designs (read the full source of each, including the JavaScript):
{{DESIGN_LIST}}
Screenshots (view with Read): {{SHOTS}}
Script results already measured (treat as ground truth, do not repeat them): {{SCRIPT_RESULTS}}

Do NOT edit design files. Do NOT run a browser or install anything.

{{VIEWPOINT_NOTES}}

Write your report to {{OUT_PATH}}. For every finding give: criterion (name and number where the skill uses them), which design, location (selector or function), what is wrong, severity 0-4, who is affected, a concrete fix, and an evidence label:
- confirmed: you traced it in the code or it is in the script results
- observed: you saw it in a screenshot
- inferred: you reasoned it but did not see or trace it
Never report behavior you did not trace. If a sign is absent, write "not present". Do not pad.

End the file with: top 3 fixes per design; which design you would ship and why; what you could not test. Keep it under 120 lines.
Reply with only the file path and 3 lines: the number of findings per design and the single most severe finding.
