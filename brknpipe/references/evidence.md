# Evidence behind the rules

Each line gives the rule and the source behind it. Read this before weakening a rule.

**How these were checked:** each source was looked up on 2026-11-20 through its arXiv, proceedings, or docs page, at the level of the abstract and summary, not the full text. Papers marked *preprint* hadn't been peer-reviewed. Figures are as reported by the authors.

## Outside checks first; early exit

- Without outside feedback, models don't reliably correct their own reasoning, and sometimes get worse. [Huang et al., ICLR 2024](https://arxiv.org/abs/2310.01798)
- The review reports gains from reliable external feedback and limited evidence for prompt-only self-correction on general tasks. [Kamoi et al., TACL 2024](https://aclanthology.org/2024.tacl-1.78)
- In self-repair of code, feedback quality is the bottleneck. Expert human feedback fixed 1.58× as many programs as GPT-4's own feedback. Feedback from a stronger model also helped. This is why the reviewer stays on a strong model. [Olausson et al., ICLR 2024](https://arxiv.org/abs/2306.09896)
- Self-correction run on answers that were already right can flip them to wrong. This is why a clean run skips revision. [Zhang et al., ACL 2025](https://aclanthology.org/2025.acl-long.1314/)

## Break-it tests

- When an attacker model plants bugs that survive the current tests and a defender model improves the tests, the tests catch more bugs than baseline methods. The light version here: test the spec's edge cases. [ADIT, ICLR 2026](https://iclr.cc/virtual/2026/10021096); [AdverTest, preprint](https://arxiv.org/abs/2602.08146)

## The review barrier

- The current abstract reports F1 of 28.6% for fresh-context review and 21.7% for a second same-session review in its benchmark. Treat the measured gap as task-specific. Across runs, the study found no statistically significant advantage over a single same-session review or a context-aware subagent. *Preprint, one author, not reproduced.* [Song, 2603.12123](https://arxiv.org/abs/2603.12123)
- Models fix errors framed as outside input that they miss in their own output (a 64.5% blind-spot rate, measured on 14 open models without step-by-step reasoning). [Tsui, 2507.02778](https://arxiv.org/abs/2507.02778)
- Evaluators recognize and favor their own outputs, which is why authorship is never stated. [Panickssery et al., NeurIPS 2024](https://arxiv.org/abs/2404.13076)
- Anthropic's docs describe subagents as starting in their own context window, without the parent conversation. [Claude Code docs](https://code.claude.com/docs/en/sub-agents)

## Yes/no checks, notes on failures only

- Breaking an evaluation into yes/no questions improves agreement between evaluator models and lowers variance. [CheckEval, 2403.18771](https://arxiv.org/abs/2403.18771)
- Rubrics grounded in requirements and written as checklists work as reliable reward signals. [Gunjal et al., Rubrics as Rewards, 2507.17746](https://arxiv.org/abs/2507.17746)
- Pairwise judge preferences can vary across repeated trials. The 85+ and ±5-point re-score settings are local policy, without a validated cutoff here. *Preprint.* [Yagubyan, 2606.13685](https://arxiv.org/abs/2606.13685)

## One review pass; stopping rules

- Extra review rounds raised recall by 0.08 but brought 62% more false positives, cutting precision from 0.30 to 0.20. *Preprint.* [Song, 2603.16244](https://arxiv.org/abs/2603.16244)
- For code review, one thorough prompt was more cost-effective than a multi-agent setup. *Preprint.* [2610.13668](https://arxiv.org/pdf/2610.13668)
- A comparison reported higher token spend and lower scores for its five-agent configuration. Verify per-run spend and matched-budget results before claiming a fold difference. *Preprint.* [2607.26922](https://arxiv.org/pdf/2607.26922)
- Accuracy usually peaks at a middling token spend and then levels off. *Preprint.* [2604.22750](https://arxiv.org/pdf/2604.22750v2)
- Agents keep spending on tasks they'll fail. Stopping those runs early saved 28–64% of their tokens for a 1.6–4.2 point drop in success. *Preprint.* [BAGEN, 2606.00198](https://arxiv.org/pdf/2606.00198)
- Anthropic reports multi-agent systems use about 15× the tokens of chat, and that coding parallelizes less well than research. [Anthropic engineering](https://www.anthropic.com/engineering/multi-agent-research-system)

## Size check and 10% growth limit

- GPT-4 judges prefer longer answers more than humans do. [Saito et al., 2310.10076](https://arxiv.org/abs/2310.10076)
- Newer judge models show much less verbosity bias than earlier reports. The rule is kept because it's cheap, not because the effect is large. *Preprints.* [2606.19544](https://arxiv.org/abs/2606.19544), [2604.23178](https://arxiv.org/html/2604.23178)

## Memory off by default

- Memory-poisoning attacks succeeded about 50% of the time on average across the agents tested. *Preprint.* [2606.04329](https://arxiv.org/html/2606.04329)
- Agents that write their own lessons can turn correct experiences into rules that are too general. *Preprint.* [2605.18930](https://arxiv.org/pdf/2605.18930)

## Short main file

- Anthropic's guidance is to keep the SKILL.md body under 500 lines and move detail into reference files that load only when needed. [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

## Not evidence-based yet

These are heuristics from this project, not from the literature: the grounding and precision gates, the mechanism check for docs, the cross-check, and the reviewer roles. Also the independent-tests review for high-stakes code: in this project's 2026-11-21 benchmark, rubric reviewers found nothing in 4 runs, while a reviewer that built its own reference version from the spec and compared 200,000 generated invoices was the strongest check seen. That's one task, so treat it as a lead, not a result. Test them before relying on them at high stakes.

## Removed in v9

- "Choi et al., 2510.07517": not found.
- "Verbosity inflates scores 15–30pp": no source found.
- "ICC 0.58–0.77": couldn't be confirmed from 2606.13685.
- Wu & Aji and Viswanathan et al.: not confirmed.
- Self-Refine (Madaan et al.) was cited for cycle-1 gains. It wasn't re-checked, and the rules it supported now rest on Huang, Zhang, and Song (2603.16244).
