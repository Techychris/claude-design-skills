# PM and Brand/Design Knowledge Base

> Online validation 2026-11-12: corrections from `kb/validation.md` are applied below.

Built 2026-11-12 from read-only local clones. Tags: [verified] = read in the file or confirmed with a count; [inferred] = my reading, not a direct check.
Heads: pm-skills 9b920db4 (clean tree); claude-skills 05905108.

---

## 1. product-on-purpose/pm-skills (`/home/claude/product-on-purpose/pm-skills`)

**Purpose.** Apache-2.0 library of 68 PM skills across the product lifecycle, with workflows, sub-agents and sample outputs. Installable as a Claude Code plugin (`/plugin marketplace add product-on-purpose/agent-plugins`, then `/plugin install pm-skills@product-on-purpose`), via `npx skills add product-on-purpose/pm-skills`, or by cloning. [verified online] [verified: README.md, QUICKSTART.md]

**Structure.** [verified]
- `skills/<name>/SKILL.md`, flat, 68 folders. Focal skills carry `references/TEMPLATE.md` and `references/EXAMPLE.md`.
- `commands/`: 11 files (10 `/workflow-*` plus `/chain`). `_workflows/`: 12 workflow definitions.
- `agents/`: 6 sub-agent definitions plus `_chain-permitted.yaml`. `hooks/`: guardrails and phase router, with tests.
- `library/`: `skill-output-samples` and `sub-agent-samples`. `scripts/`: validators and generators (see `scripts/README_SCRIPTS.md`). `site/`: Astro docs.
- `.claude/` is populated from `skills/` by `scripts/sync-claude.sh`, per QUICKSTART.md (not run here).
- Manifests in `.claude-plugin/` and `.codex-plugin/`. Agent guidance in `AGENTS.md` and `CLAUDE.md`.

**Inventory (68, group level; folder prefixes dropped).**
- Discover (5): interview-synthesis, competitive-analysis, stakeholder-summary, journey-map, market-sizing
- Define (5): problem-statement, hypothesis, opportunity-tree, jtbd-canvas, prioritization-framework
- Develop (4): solution-brief, spike-summary, adr, design-rationale
- Deliver (6): prd, user-stories, acceptance-criteria, edge-cases, launch-checklist, release-notes
- Measure (6): experiment-design, instrumentation-spec, dashboard-requirements, experiment-results, okr-grader, survey-analysis
- Iterate (4): retrospective, lessons-log, refinement-notes, pivot-decision
- Foundation (11): persona, lean-canvas, okr-writer, stakeholder-update, meeting-agenda, meeting-brief, meeting-recap, meeting-synthesize, prioritized-action-plan, stakeholder-briefings, build-risk-review
- Foundation Sprint tool family (7): readiness, basics, differentiation, approach-options, magic-lenses, founding-hypothesis, brief
- Design Sprint tool family (7): readiness, brief, map-and-target, sketch, decide-and-storyboard, prototype-plan, test-and-score
- Standalone tool (1): note-and-vote
- Utility (12): pm-skill-builder, pm-skill-validate, pm-skill-iterate, pm-workflow-builder, mermaid-diagrams, slideshow-creator, update-pm-skills, pm-critic, pm-skill-auditor, pm-changelog-curator, pm-release-conductor, pm-workflow-orchestrator

**The 10 most design-relevant skills.** Rules are paraphrased from each SKILL.md. [verified]

1. `skills/discover-journey-map/SKILL.md`
   - Ground each stage, emotion and pain point in research you can cite. Anything else is a labeled hypothesis with low confidence.
   - Cap moments of truth at the three to five that decide whether a customer stays.
   - Use three to seven named stages, each with a goal, duration, trigger and exit criterion.
   - Tie every opportunity to a named pain point or moment of truth.
   - Decline when persona or scope is missing, and route service-blueprint requests elsewhere.
2. `skills/develop-design-rationale/SKILL.md`
   - State the decision in one sentence; that sentence becomes the title.
   - Document at least two or three alternatives fairly, without strawmen.
   - Write evaluation criteria before reasoning, then name the trade-offs accepted.
   - Record whether the decision is reversible.
   - Skip the document for trivially reversible choices, and send architecture choices to `develop-adr`.
3. `skills/tool-design-sprint-readiness/SKILL.md`
   - Score eight canonical checks. All met is Go; one or two yellow flags is Conditional Go; three or more fails, or a hard fail on checks 1, 3 or 6, is Wait.
   - Treat Friday customer access as a gate. Recruiting takes 7 to 10 days, so it starts at Go. (unsourced; GV says recruiting starts Tuesday) [repo rule, not Sprint book]
   - Require a team of up to seven (Sprint book; the repo's floor of four is its own), and a Decider present for Monday framing, Wednesday supervote and Friday review.
   - Require a prototype medium that two people can build in one day.
   - Confirm the team will act on the Friday result.
4. `skills/tool-design-sprint-brief/SKILL.md`
   - Keep the brief to two pages. If it grows, sharpen the sprint questions and the prototype-medium decision instead.
   - Limit the challenge statement to four sentences.
   - Use two to four sprint questions, one sentence each.
   - Give three to five success criteria.
   - Include a customer recruiting table and a one-paragraph prototype medium rationale.
5. `skills/tool-design-sprint-map-and-target/SKILL.md`
   - Set the long-term goal on a six-month to five-year horizon (Sprint book). A roadmap goal fails this test.
   - Phrase three to seven sprint questions as testable "Can we / Will / How" risks, not solutions.
   - Keep the customer map to 5 to 15 steps, from key player to outcome.
   - Heat-map the How-Might-We notes with `tool-note-and-vote`, then cluster into four to eight themes.
   - Let the Decider pick the target moment. If it was pre-decided, the day is ratification theater.
6. `skills/tool-design-sprint-sketch/SKILL.md`
   - Keep sketching silent and individual. Group brainstorming is the main failure mode.
   - Reduce each lightning demo to one reusable pattern, not the whole product.
   - Run the four steps in order: Notes, Ideas, Crazy 8s, Solution Sketch.
   - Make each sketch readable without its author present. Sketches are concepts, not the prototype.
   - Strip sketcher names before the blind Wednesday heat map.
7. `skills/tool-design-sprint-decide-and-storyboard/SKILL.md`
   - Run heat-map dots, then a straw poll, then the Decider's supervote. Do not average the votes.
   - Storyboard one sketch by default. Run a rumble only when two distinct approaches split the supervotes and the team can build both.
   - Write 5 to 15 storyboard panels, each stating what the customer sees and does. [repo rule, not Sprint book; unsourced]
   - Run critique with the sketcher silent.
   - Treat the supervote as final. Reopening it on Thursday counts as sprint failure.
8. `skills/tool-design-sprint-prototype-plan/SKILL.md`
   - Assign five roles: Maker, Stitcher, Writer, Asset Collector, Interviewer. Always assign the Asset Collector.
   - Set the fidelity bar as "would a customer believe this is real for the interview".
   - Use the fixed five-act interview (Welcome, Context, Intro, Tasks, Debrief). Keep Tasks open-ended.
   - Run a trial with a stand-in customer on Thursday afternoon.
   - Re-confirm all five Friday participants on Thursday morning, while buffer slots can still be activated.
9. `skills/tool-design-sprint-test-and-score/SKILL.md`
   - Recruit five target-profile customers. Three to four or six to seven draws a documented warning; below three or above seven means re-deciding. [repo rule, not Sprint book]; the Sprint book says five.
   - Close Friday with a Decider call: build, iterate, pivot, stop or reframe.
   - Score the sprint questions against each customer on a grid.
   - Route the outcome: build to `deliver-prd`, iterate to `measure-experiment-design`, pivot to `iterate-pivot-decision`.
   - The family validator does not enforce the customer-count thresholds, per the file's own note.
10. `skills/tool-note-and-vote/SKILL.md`
   - Run five steps: frame the question, silent ideation, silent voting, short discussion of the distribution, Decider supervote.
   - Budget 12 to 25 minutes; the default is 25.
   - Time-box the discussion so five minutes does not become twenty.
   - Keep ideation silent. A "let's just discuss it" shortcut reproduces what the team would have produced anyway.
   - Record the Decider's call. The session cannot end without a recorded decision.

**License.** Apache-2.0: `LICENSE`, `.claude-plugin/plugin.json`, and the `license` field in each of the 68 SKILL.md files. The LICENSE appendix (line 177) names "Copyright 2026 Jonathan Prisant"; there is no NOTICE file. [verified online]

**Gotchas.**
- The README foundation table has 10 rows under a heading that says 11. `foundation-build-risk-review` is absent from the table and appears only in prose (README.md line 346). [verified]
- `tool-design-sprint-sketch/SKILL.md` says sketches are due Tuesday end-of-day (line 51) and also Tuesday morning (line 58). [verified]
- `discover-journey-map` puts service blueprints out of scope. `journey-mapping` in claude-skills includes one. The two repos disagree on scope. [verified]
- The "68" count matches across README, QUICKSTART, CLAUDE.md and the folder count. [verified]
- README says "200+ real-world sample outputs". `library/` holds 223 files in total, not all of them outputs. [inferred; 223 not rechecked, unsourced]

---

## 2. rampstackco/claude-skills (`/home/claude/rampstackco/claude-skills`)

**Purpose.** MIT catalog of 109 stack-agnostic skills covering brand, design, content, SEO, dev, ops, growth and research, plus a workflows tier of multi-skill runbooks. Its one stated exception is the SEO audit suite, which assumes the Ahrefs MCP. [verified: README.md]

**Structure.** [verified]
- `skills/<name>/SKILL.md` for 109 folders. Each has `references/` holding 527 files in total.
- `workflows/`: 15 runbooks, plus README, GETTING-STARTED, CONNECTORS, AGREEMENT-LOG and `run-records/`.
- `.claude-plugin/`: `plugin.json` (rampstack-skills 1.2.0) and `marketplace.json`. `.github/scripts/lint_skills.py` is the lint check.
- `scripts/`: `generate_readme_catalog.py`, `build-codex.mjs`, `build-pi.mjs`, `build-tested-on.mjs` and others. Also `dist/`, `tools/`, `assets/`, `docs/`.
- Top-level docs: `README.md`, `SKILL_AUTHORING.md` (conventions), `MAPPING.md` (v1 history), `STARTER-KIT.md`. Lock files: `SKILL.lock`, `WORKFLOWS.lock`.

**Inventory (109; 16 README groups; folder names).** [verified: README catalog rows match the 109 folders]
- Strategy and discovery (5): brand-discovery, creative-brief, creative-direction, information-architecture, content-strategy
- Brand (7): brand-ideation, brand-identity, brand-style-guide, brand-voice, brand-archetype-system, logo-design, creative-brief-selector
- Design (4): design-system, design-standards, art-direction, vertical-site-conventions
- Content (13): pillar-content-architecture, content-brief-authoring, content-and-copy, landing-page-copy, email-sequences, programmatic-seo, editorial-qa, ai-content-collaboration, long-form-content-frameworks, content-refresh-system, content-repurposing, content-distribution, evidence-based-reviews
- SEO foundation (7): seo-onpage, seo-technical, seo-keyword, seo-competitor, seo-offpage, seo-content-audit, seo-aeo-geo
- SEO audit suite (7): seo-audit-orchestration, seo-backlink-audit, seo-keyword-gap-audit, seo-content-gap-audit, seo-traffic-diagnosis, seo-site-health-audit, seo-rank-tracking
- Product (15): backlog-triage, pm-spec-writing, ticket-authoring, roadmap-planning, integration-orchestrator, experiment-design, feature-flagging, experimentation-analytics, experimentation-platform-orchestrator, product-analytics-setup, data-warehouse-experimentation, feature-launch-playbook, jtbd-framing, okr-design, beta-program-management
- Development (5): code-review-web, frontend-component-build, accessibility-audit, performance-optimization, oss-contribution-research
- Quality assurance (2): qa-testing, test-case-authoring
- Operations (9): launch-runbook, incident-response, after-action-report, domain-strategy, monitoring-and-alerting, backup-and-disaster-recovery, security-baseline, email-deliverability, media-asset-management
- Growth (2): analytics-strategy, cro-optimization
- Growth tooling (12): lead-magnet-design, calculator-design, quiz-and-assessment-design, multi-step-form-design, chatbot-flow-design, funnel-flow-architecture, onboarding-wizard-design, interactive-product-tour, upgrade-flow-design, scheduler-and-booking-design, comparison-tool-design, product-configurator-design
- Marketing (3): paid-media-strategy, ads-creative-development, ads-performance-analytics
- Research (6): ux-research, usability-testing, journey-mapping, discovery-research-synthesis, user-feedback-aggregation, competitor-experience-audit
- Cross-cutting workflows (5): form-strategy, content-migration, internationalization, dependency-management, cost-optimization
- Process and team (7): stakeholder-communication, documentation-strategy, vendor-evaluation, team-onboarding-playbook, skill-creation-walkthrough, sprint-operations, dispatch-authoring

**The 10 most design-relevant skills.** Rules are paraphrased from each SKILL.md. [verified]

1. `skills/design-system/SKILL.md`
   - Build five layers in order: foundations (tokens), elements, components, patterns, governance.
   - Use two token tiers: raw base values, plus semantic names that components reference.
   - Set the brand before tokens, because tokens depend on it.
   - Ship the 10 to 15 most-used components before refining tokens or atoms.
   - Name an owner and a deprecation path before rollout.
2. `skills/design-standards/SKILL.md`
   - Define color, spacing, type and radius tokens before building any UI. Hardcoded values are debt.
   - Meet WCAG AA: 4.5:1 for body text, 3:1 for large text and UI elements (a failing brand color is a problem only for text and UI use, not decoration).
   - Build mobile-first, then test at 375, 768, 1024 and 1440 px.
   - Run the pre-ship checklist in `references/preship-checklist.md` before release.
   - Avoid several competing primary elements; they flatten the scan order.
3. `skills/brand-identity/SKILL.md`
   - Design a logo system (primary mark, wordmark, symbol, lockups, monogram), not a single mark.
   - Test the logo at 16 px and in single color before approval.
   - Check the brand color for contrast before committing; a color that fails AA on white makes brand-based UI inaccessible by default.
   - Keep the palette to roughly five to eight colors, since neutrals carry most of the surface.
   - Stress-test identity on three to five mock applications before sign-off.
4. `skills/brand-style-guide/SKILL.md`
   - Include "what we are not" rules. Without rejection rules, anything becomes acceptable.
   - Pair each rule with a real application example.
   - Date and version the guide, noting what changed.
   - Publish in the format the team opens daily, such as a web page or Figma, not a static PDF.
   - Document actual practice, not aspirational rules.
5. `skills/creative-direction/SKILL.md`
   - Take a position on four axes: tone register, aesthetic philosophy, audience relationship, sensory ambition.
   - Walk one axis at a time and record the reasoning behind each pick.
   - Flag hard combinations, such as functional plus provocative, before committing to them.
   - Write a one-paragraph synthesis, then the brief, and have downstream skills read it first.
   - Check that the brief changes downstream output. If it does not, it is decoration.
6. `skills/art-direction/SKILL.md`
   - Write the story (premise, emotional through-line, brand role, takeaway) before the look.
   - Settle usage and licensing rights before the shoot or first sketch.
   - Use specific references and never a direct competitor's work.
   - Schedule treatment, halfway and final reviews. Late fixes cost more.
   - Plan crops and variants for each distribution context up front.
7. `skills/logo-design/SKILL.md`
   - Choose the mark architecture first (wordmark, lockup, letterform, symbol, monogram). Everything else follows from it.
   - Explore three to four wordmark variants across typographic registers before adding symbols.
   - Test each candidate at 16 px favicon size, in embroidery, single color and stacked layouts. Drop the failures.
   - Present six to twelve visually distinct finalists, each documented.
   - Keep a symbol to one idea. Three ideas reads as committee work.
8. `skills/journey-mapping/SKILL.md`
   - Scope to one persona, one journey and one timeframe.
   - Budget two to four weeks for inputs from interviews and operational data.
   - Draft phases and touchpoints first, then add goals, thoughts, emotions and pain points.
   - Add a service blueprint (front-stage, back-stage, supporting processes) to expose causes, not just symptoms.
   - Validate with real users before the stakeholder workshop. A map built on assumptions reflects assumptions.
9. `skills/usability-testing/SKILL.md`
   - Define three to five goal-framed tasks tied to specific decisions.
   - Run one or two pilot sessions before the main batch.
   - Cluster issues by root cause, then rate severity before recommending fixes.
   - Synthesize during the study; patterns usually appear by session four or five.
   - Report in written form plus highlight clips.
10. `skills/brand-archetype-system/SKILL.md`
   - Choose one of 12 core archetypes first. Each supplies palette, type, voice and imagery starters.
   - Place the choice on the four creative-direction axes so it matches the brief.
   - Pick one of the 18 vertical applications only after the core choice is settled.
   - Treat palette and type values as starters, then map them to your own tokens.
   - Read the trademark and attribution section (around line 116) before reusing archetype material.

**License.** MIT: `LICENSE` (line 3: "Copyright (c) 2026 RampStack Co."), `.claude-plugin/plugin.json`. [verified]

**Gotchas.**
- Category drift: 15 SKILL.md files use categories missing from the enum in `SKILL_AUTHORING.md`: `marketing` (3) and `growth-tooling` (12). [verified]
- Required-section drift: each of the eight required H2 headings is absent in 36 to 39 files (for example `## When to use` in 36). `lint_skills.py` has no check for these headings, so a green CI does not mean drift-free. [verified: lint_skills.py]
- 62 of 109 files add a non-canonical `## If required data is unavailable` section, which the authoring guide does not permit. [verified]
- 60 of 109 files exceed the 250-line aim. None exceed the 500-line cap. `journey-mapping` keeps template placeholders in its body. [verified]
- `SKILL_AUTHORING.md` has two `## Reference files` headings (lines 95 and 196). [verified]
- `MAPPING.md` is v1 history covering 11 skills. It maps to `seo-foundations`, which no longer exists. [verified]
- README marks 103 of 109 catalog rows "set up for testing, not yet run". Only 6 have a recorded run. [verified]
- `.github/workflows/lint.yml` runs `lint_skills.py` on push and pull_request to main. Pass status on Actions was not readable (blocked). The job fails on push if the `LINT_CONFIG_TOKEN` secret is missing. [verified: workflow file, online]
- Re-check the rendered github.com page before quoting the skill count: one fetch read 107, while the pinned README at 059051082ab0 says 109. [verified online]
- pm-skills: `plugin.json` version is 2.35.0 on main, but the latest GitHub release is v2.34.0 (2026-10-17). Cite the release, not 2.35.0. [verified online]
- Style rule: zero em dashes across the 109 SKILL.md files. [verified]

---

## 3. Cross-repo notes

- No cross-references: a grep of both repos' `.md` files finds no mention of the other. [verified]
- Scope disagreement: `discover-journey-map` (pm-skills) refuses service blueprints; `journey-mapping` (claude-skills) includes one. [verified]
- Shared research rule: both journey skills refuse or warn against maps without research evidence. [verified]
- Design-sprint family (pm-skills) is a workshop method; the brand and design skills (claude-skills) cover craft outputs. No file reconciles the two. [inferred]

_Validated 2026-11-12 against primary sources; see ../validation-reports/._
