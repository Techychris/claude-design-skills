---
name: "ux-mapping"
description: "Build or review journey maps, service blueprints, experience maps and empathy maps from evidence, with traceable pains and opportunities and a checked visual output."
---

# UX mapping

Work as a senior service designer and UX researcher. The family here is alignment diagrams: pictures that line up what a person goes through with what an organization does. Treat every map as a decision tool. If it would not change what a team builds, fixes or stops doing, it is not finished.

Three rules run through everything below:

1. **Every entry traces to evidence or is labeled as a guess.** A map built on assumptions is a list of assumptions; that is fine only when it says so.
2. **Every opportunity traces to a pain or a moment of truth.** Opportunities with no pain behind them are feature wishes.
3. **The visual is generated from the data.** Keep the map as JSON, check it, then render from it. Never hand-edit the picture into disagreeing with the data.

For visual craft (type, color, spacing, avoiding a template look) also follow the `design` skill's Direction and Craft rules if it is available. This skill owns structure, content and checks.

## 0. Pick the diagram

| Question the team is asking | Diagram |
|---|---|
| What does this person go through with us, and where does it hurt? | Customer journey map (CJM) |
| Why does it hurt: which internal steps, teams or systems cause it? | Service blueprint (CJM + delivery lanes) |
| How do people do this activity at all, with or without us? | Experience map (product-agnostic) |
| What do we know about this user type right now, fast? | Empathy map |

Redirect instead of forcing a journey map:

- One screen or one task inside a product → a task flow or user flow (decision points = user chooses; conditional branches = system chooses).
- Backlog planning against a workflow → a user story map.
- Internal process with no customer in it → a process map, not this skill.

## 1. Frame

Write a short brief before drawing. If the request leaves something open and context allows a responsible assumption, state it in one line and proceed. Ask only when a wrong guess would waste the whole map. With no scenario given at all, pick a real, researchable one and say so.

- **Actor:** one persona or segment per map. Two actors that interact (buyer and user, patient and nurse) get parallel lanes in a blueprint or two linked maps, never one averaged actor.
- **Scenario:** a concrete goal with a trigger that starts it and an end state ("lapsed passport, trip in 9 weeks → passport in hand"), not "uses our product". A deadline or constraint in the scenario sharpens every lane.
- **Scope:** end-to-end or one phase. Decline two extremes and offer the fix:
  - Too coarse (years of a B2B lifecycle in one map): pick one phase such as pre-purchase, onboarding, renewal or off-boarding.
  - Too narrow (one touchpoint, e.g. "checkout"): widen to the surrounding stages, or switch to a task flow.
- **State:** current (as-is) or future (to-be). Map current first; never mix the two in one lane.
- **Experience type**, because it changes what to look for:
  - *Transactional* (minutes to weeks, one application or purchase): fewest steps; measure time and drop-off.
  - *Continuous* (months or years): include onboarding, routine use, renewal, recovery, leaving; measure retention and trust.
  - *Transformational* (the person changes state: learning, health, fitness): include before and after; measure outcomes, not just satisfaction.
- **Evidence base:** research, assumption (workshop/hypothesis map), or mixed. It goes in the map title.

## 2. Evidence

Gather from three views and compare them:

1. **The person:** interviews about a recent real occurrence, diary studies, reviews, support transcripts, survey verbatims, public forum accounts.
2. **The data:** analytics, funnel drop-off, ticket categories, NPS comments, churn reasons, time-on-task.
3. **The organization:** official policy pages, frontline staff (support, sales, ops), process docs, system inventory.

Where the views disagree, record the disagreement in `disagreements`. It is often the most useful thing on the map. If there are truly none, write `none found: <why>`.

### Tags

Tag every substantive entry:

- **verified**: from supplied material, or a source checked this session that is confirmed and has a link
- **estimated**: inferred from partial or indirect data (say from what)
- **assumed**: hypothesis to validate

Also mark insights as *stated* (the person said it) or *inferred* (deduced from behavior). Never invent a number (a percentage, a score, a count) to fill a cell; leave the gap and list it under `gaps`. A stated gap is a complete answer.

### Recording sources

Each source records how it was reached (`method`: fetched, search_snippet, supplied, interview, observation, analytics), its URL for web sources, and the date the page shows if any.

- A **search snippet** from the official site can back a verified claim only when the snippet itself contains the exact figure or rule. Say in the source that the full page was not read.
- **Fetch and search disagree** about the same page (different dates or figures): treat it as a possible cached or stale copy. Mark the source `status: unconfirmed`, tag every claim that rests on it `estimated`, and say "unconfirmed" wherever it is cited. Do not build a finding on a page you can't confirm users actually see.
- **Older official pages** at other URLs can be stale. Prefer the current page; cite the older one only as a lead.

### Quotes

Quote marks are only for verbatim words, with a source, in a quote thought. Pains, failures and summaries paraphrase without quote marks. (Proposed UI copy inside an opportunity is fine in quotes; it is your text, not a claim.)

### Changing a tag

When a review or new evidence downgrades a claim, change it **everywhere it appears**: the pain, `disagreements`, `failures`, the summary box, the report-back. Search the map and the rendered text for the source ID and the key phrase before calling it done. A downgrade made in one place and missed in another is the commonest regression.

No research at all: build in hypothesis mode (everything `assumed`), title it "Assumption map", and end with the 3 to 5 research questions that would most change it. A useful minimum to upgrade it: about 5 interviews about recent real occurrences (a rule of thumb; NN/g sets no minimum for journey maps), a pass through analytics or tickets, and a touchpoint inventory.

## 3. Build the journey map

### Stages

3 to 7 stages (a readability rule of thumb, not a research finding). Name them in the actor's words for this scenario ("Realizes it's expired", "Waits without a usable passport"). Stock funnels (Awareness → Consideration → Purchase…) only when the scenario really is that funnel. For each stage record: **goal**, **trigger** (what moves them in), **exit** (what moves them out, including abandoning), and **duration** (minutes, days, weeks; note when perceived wait differs from actual).

### Lanes

| Lane | Write it as | Example |
|---|---|---|
| Actions | verb first, in order, with an ID | "A8 Signs and pays $130 by card" |
| Touchpoints | the noun they touch | "Pay.gov", "Status email" |
| Thoughts | a question in their head; label illustrative unless verbatim | Will it come before my flight? |
| Feelings | an adjective plus the cause | Anxious: heard nothing back in 3 weeks |
| Emotion score | −2 … +2 with basis tag | −2 (estimated, S5) |
| Pain points | gerund, tied to one action | Losing the use of the current passport at submission |
| Opportunities | change verb, tied to pain IDs | Add a confirm step before payment (fixes P5) |

Optional lanes, only if they carry weight: metrics per stage, owning team, channel, expectation vs reality.

Write handoffs, waits and channel switches as actions where they happen ("Calls to add expedite when the wait gets tight"). They are where steps go missing and where the worst pain usually sits.

### Where a pain is caused vs where it is felt

A pain is tied to the action that **causes** it (`at`). If it is **felt** in a later stage, set `felt_in` to that stage. Typical: a decision made at payment that hurts during the wait. Without this, a stage full of causes looks painful on paper while people there feel fine, and the stage where they suffer looks under-explained.

### Emotion and expectation

Score each stage (or key step) and draw one continuous line. Satisfaction follows the gap between expectation and reality more than absolute quality, so for the low points note what the person expected and where that expectation came from (marketing, a competitor, last time). The end of a journey and its single worst moment shape memory most; treat both with extra weight.

The lowest feeling should sit where the most pain is **felt**. When it doesn't, either the scores or the pains are wrong, or there is a real reason (a latent pain, a stage people don't yet know is risky). Fix the data, or write the reason in `latent` for that stage and show it on the visual next to the curve.

### Moments of truth

Flag 2 to 5, no more. Look for: irreversible decisions (sign, buy, cancel), first real use, the first time something goes wrong and how it is recovered, the ending, and the deepest emotional low. Each gets one line on why it decides whether the person continues or leaves. A well-handled failure can build more loyalty than a smooth path, so recovery moments count.

## 4. Service blueprint

Add five lanes under the journey, top to bottom, with three lines:

1. **Physical evidence:** what the person sees, receives or touches (screens, emails, receipts, signage).
2. **Customer actions** (from the journey).
   — *line of interaction* —
3. **Frontstage:** staff or system actions the person experiences directly.
   — *line of visibility* —
4. **Backstage:** staff or system actions they never see.
   — *line of internal interaction* —
5. **Support processes:** systems, vendors, policies, data.

Every backstage item must support a frontstage or customer action; anything that doesn't is either missing a link or waste.

### Cross-lane failures

Reading a blueprint for failure is the point of drawing one. Record each in `failures` with the lanes involved, the action where it shows, and the pains it explains. Name at least one, or say why there are none. Patterns to look for:

- **Two checks, two standards:** a frontstage check passes what a backstage check later rejects.
- **Hidden cost:** a support-process rule (policy, fraud control, billing) has a consequence nothing frontstage shows.
- **Split channel:** the fix for a limit lives in another channel (phone, branch) than the one the person is in.
- **Promise vs capacity:** a frontstage promise the backstage can't keep.
- **Silent wait:** long stretches with no customer touchpoint while backstage works.
- **Single point of failure:** one frontstage step depending on several support systems.
- **Employee pain becomes customer pain:** the agent can't see history, so the customer repeats the story. When staff are part of the experience, map their side for the same scenario.

Each failure is the "why" behind one or more pains. A high pain with no failure, policy or cause behind it is a symptom; say so in `gaps` if the cause isn't knowable.

Build blueprints with the people who run the backstage (ops, support, engineering) when you can. Without them, say in `gaps` that backstage steps are inferred.

## 5. Experience map and empathy map

**Experience map:** same structure as a CJM, but map the activity rather than your product ("managing household bills", not "using our app"). Record every tool and workaround people use (spreadsheets, sticky notes, calling a friend). Those are the real competitors. The phases with the most effort and emotion are where winning matters.

**Empathy map:** four quadrants (Says, Does, Thinks, Feels) around a center of goals and needs, for one segment, 5 to 10 items each. Says comes from quotes; Does from observation or analytics; Thinks and Feels are inferences and get tagged as such. The gap between Says and Does is where the insight usually is. With no research behind it, title it "Proto-empathy map".

## 6. Opportunities

Each opportunity: what changes, which pains it fixes (IDs), impact, reach and effort (H/M/L each), a proposed owner, and `feasibility` when it depends on something you haven't checked (a policy change, a vendor). Sort into three buckets:

- **Quick wins:** high impact, low effort.
- **Strategic bets:** high impact, high effort.
- **Cross-team disconnects:** fixes that need two or more teams to agree (usually from `failures`).

Mark the top 3, each with `why` (one line) and an owner. Prefer fixes that act on a cross-lane failure or an irreversible moment. Every high-severity pain gets an opportunity or an explicit `no_fix` reason.

## 7. Future state

Only after the current state. Use the same stages and syntax so the two compare line by line. Mark the delta: what changes, what disappears, what is new. For each change, name a small test that would show the future state is better before anyone commits to building it. Present side by side, as an overlay on the current map, or as a separate map when the vision is fundamentally different.

## 8. Data model and validator

```json
{
  "title": "", "diagram": "cjm|blueprint|experience|empathy",
  "actor": "", "scenario": "", "state": "current|future", "experience_type": "",
  "evidence": "research|assumption|mixed",
  "sources": [{"id": "S1", "what": "", "url": "", "method": "fetched|search_snippet|supplied|interview|observation|analytics", "date": "", "status": "ok|unconfirmed"}],
  "stages": [{
    "id": "ST1", "name": "", "goal": "", "trigger": "", "exit": "", "duration": "",
    "actions": [{"id": "A1", "text": "", "touchpoint": ""}],
    "thoughts": [{"text": "", "kind": "quote|illustrative", "source": "S1"}],
    "emotion": {"score": 0, "basis": "verified|estimated|assumed", "source": "S1"},
    "evidence_phys": [], "frontstage": [], "backstage": [], "support": []
  }],
  "moments": [{"at": "A1", "why": ""}],
  "pains": [{"id": "P1", "at": "A1", "felt_in": "ST3", "text": "", "severity": "high|med|low", "basis": "verified|estimated|assumed", "source": "S1"}],
  "failures": [{"id": "F1", "at": "A1", "lanes": "frontstage vs backstage", "pains": ["P1"], "text": ""}],
  "latent": [{"stage": "ST2", "text": ""}],
  "opportunities": [{"id": "O1", "fixes": ["P1"], "text": "", "impact": "H|M|L", "reach": "H|M|L", "effort": "H|M|L", "bucket": "quick-win|bet|disconnect", "owner": "", "top": false, "why": "", "feasibility": ""}],
  "no_fix": [{"pain": "P2", "reason": ""}],
  "disagreements": [""],
  "gaps": [""]
}
```

`felt_in`, `latent`, `feasibility` and `date` are optional; `failures` is required for blueprints.

Save the map as `map.json`, write this checker to `check.py` and run `python3 check.py map.json`. Fix every FAIL before building the visual, and run it again after every revision:

```python
import json, re, sys
m = json.load(open(sys.argv[1])); F = []
st = m.get("stages", []); sid = [s["id"] for s in st]
acts = {a["id"]: s["id"] for s in st for a in s.get("actions", [])}
src = {s["id"]: s for s in m.get("sources", [])}
pains = {p["id"]: p for p in m.get("pains", [])}
B = {"verified", "estimated", "assumed"}; SEV = {"high": 3, "med": 2, "low": 1}
bp = m.get("diagram") == "blueprint"
def ok_src(i): s = src.get(i); return bool(s and s.get("url") and s.get("status", "ok") != "unconfirmed")
def tagged(where, b, s):
    if b not in B: F.append(f"{where}: no basis tag")
    elif b == "verified" and not ok_src(s): F.append(f"{where}: verified needs a confirmed source with a url")
# sources
for s in src.values():
    if s.get("method") not in {"fetched", "search_snippet", "supplied", "interview", "observation", "analytics"}: F.append(f"{s['id']}: method missing or unknown")
    if s.get("method") in {"fetched", "search_snippet"} and not s.get("url"): F.append(f"{s['id']}: web source without url")
# stages
if not 3 <= len(st) <= 7: F.append(f"{len(st)} stages (want 3-7)")
for s in st:
    for k in ("goal", "trigger", "exit"):
        if not s.get(k): F.append(f"{s['id']}: missing {k}")
    e = s.get("emotion", {}); tagged(f"{s['id']} emotion", e.get("basis"), e.get("source"))
    for t in s.get("thoughts", []):
        if t.get("kind") == "quote" and t.get("source") not in src: F.append(f"{s['id']}: quote without a known source")
    if bp and s.get("backstage") and not s.get("frontstage"): F.append(f"{s['id']}: backstage with nothing frontstage")
# pains
quoted = re.compile(r"[\"“”]|(^|[\s(])'[^']+'(?=[\s.,;:)]|$)")
for p in pains.values():
    if p.get("at") not in acts: F.append(f"{p['id']}: not tied to an action")
    if p.get("felt_in") and p["felt_in"] not in sid: F.append(f"{p['id']}: felt_in is not a stage")
    tagged(p["id"], p.get("basis"), p.get("source"))
    if quoted.search(p.get("text", "")): F.append(f"{p['id']}: quote marks in a pain; use them only in a quote thought")
# opportunities
fixed = set(); tops = []
for o in m.get("opportunities", []):
    if not o.get("fixes"): F.append(f"{o['id']}: fixes no pain")
    for f in o.get("fixes", []):
        if f not in pains: F.append(f"{o['id']}: unknown pain {f}")
        fixed.add(f)
    if o.get("top"):
        tops.append(o)
        if not o.get("why") or not o.get("owner"): F.append(f"{o['id']}: top opportunity needs why and owner")
nofix = {n["pain"] for n in m.get("no_fix", []) if n.get("reason")}
for p in pains.values():
    if p.get("severity") == "high" and p["id"] not in fixed | nofix: F.append(f"{p['id']}: high pain with no opportunity or reason")
if m.get("opportunities") and not 1 <= len(tops) <= 3: F.append(f"{len(tops)} top opportunities (want 1-3)")
# moments
mo = m.get("moments", [])
if not 2 <= len(mo) <= 5: F.append(f"{len(mo)} moments of truth (want 2-5)")
for x in mo:
    if x.get("at") not in acts: F.append("moment not tied to an action")
# cross-lane failures (blueprint)
fl = m.get("failures", [])
if bp and not fl: F.append("blueprint lists no cross-lane failures")
for f in fl:
    if f.get("at") not in acts: F.append(f"{f.get('id')}: failure not tied to an action")
    if not f.get("lanes") or not f.get("pains") or any(x not in pains for x in f.get("pains", [])): F.append(f"{f.get('id')}: failure needs lanes and known pains")
# emotion vs pain density, using where pain is felt
dens = {i: 0 for i in sid}
for p in pains.values():
    where = p.get("felt_in") or acts.get(p.get("at"))
    if where in dens: dens[where] += SEV.get(p.get("severity"), 0)
latent = {l.get("stage") for l in m.get("latent", []) if l.get("text")}
if st and pains:
    top2 = sorted(sid, key=lambda i: -dens[i])[:2]
    score = {s["id"]: s.get("emotion", {}).get("score", 0) for s in st}
    low = min(sid, key=lambda i: score[i])
    if low not in top2 and low not in latent: F.append(f"lowest feeling at {low} but most pain felt at {top2}: fix one, or explain in latent")
    for i in top2:
        if score[i] > 0 and i not in latent: F.append(f"{i}: dense pain but positive feeling: fix one, or explain in latent")
# disagreements, gaps, unconfirmed propagation
if m.get("evidence") != "assumption" and not m.get("disagreements"): F.append("no disagreements listed (write 'none found: <why>' if truly none)")
unconf = [i for i, s in src.items() if s.get("status") == "unconfirmed"]
texts = [("disagreement", d) for d in m.get("disagreements", [])] + [(f.get("id", "failure"), f.get("text", "")) for f in fl] + [("gap", g) for g in m.get("gaps", [])]
for where, t in texts:
    for i in unconf:
        if re.search(rf"\b{i}\b", t) and "unconfirmed" not in t.lower(): F.append(f"{where} cites {i} (unconfirmed) without saying so")
if m.get("evidence") == "assumption" and "assum" not in m.get("title", "").lower(): F.append("assumption map not labeled in title")
if not m.get("gaps"): F.append("no research gaps listed")
print("\n".join("FAIL " + f for f in F) or "PASS"); sys.exit(1 if F else 0)
```

## 9. Output

### Where it goes

- If the session's artifact tool lists a **Design** type, build the map there: it is a design the person will revise and share. If it is for a team to rearrange live in a workshop, a **Whiteboard** type fits better; when unsure, Design.
- Otherwise, one self-contained HTML page published as an artifact.
- A file format (PNG, PDF, PPTX, Miro or FigJam import, Mermaid) only when the person names one. A markdown table version is a fine extra for pasting into docs.

**Design canvas and render checks.** The Design type forbids reading back or rendering a canvas unless the user asked. This skill's render checks (below) need that. Resolve it once, up front:

- The user asked for checking or review (a QA pass, a review pipeline, "make sure it's right"): run the checks and say so.
- They didn't: run the checks on your local preview of the generated file before publishing (that reads your own output, not the canvas), and say in the reply that the published canvas itself wasn't opened.
- A hand-built HTML artifact has no such limit.

If the person has design systems but none is set as default, ask whether to use one when they're around to answer. When none fits the subject (a retail brand for a government service), use your own look and say why in one line.

### Generate, don't hand-draw

Write a small script that reads `map.json` and writes the visual (a `.dc.html` artboard, or the HTML page). Then IDs, text and tags can't drift from the data, and every revision is: edit the JSON, rerun the checker, regenerate. On a Design canvas, follow its diagram rules: one host with absolutely placed elements, each card its own element, bands first, then lines, then cards, then labels; the emotion curve may be one SVG because it is a chart plot, with its score labels as separate elements.

### Layout

- Stages are columns and time runs left to right. Lane labels sit in a left column. On narrow screens scroll or pan sideways; never stack lanes vertically (it destroys the timeline). A canvas gives pan and zoom for free.
- The emotion line is the strongest graphic element: aligned to column centers, with a zero baseline. Put the `latent` note next to the curve, clear of the line.
- One accent for pain, one for opportunity, a third for moments of truth, neutrals for everything else; pick colors that differ in lightness, not hue alone. Moments of truth are the most visible markers. No emoji.
- Evidence tags visible but quiet. Cross-reference pains, failures and opportunities by ID.
- A "Top 3 fixes" box near the title so they're findable in under five seconds. A footer with sources (linked), disagreements and research gaps.
- Size cards for their text; over-tall beats clipped, but trim dead space a review points out.

### Render checks

Open the local preview in a headless browser and check, by script rather than by eye:

1. **No text overflows its card:** each card's content height ≤ its inner height.
2. **No label crosses the curve:** sample points along the emotion polyline and test them against every label's box. When placing score labels, try several spots per point (above-right, above-left, below-right, below-left) and keep the first clear one.
3. **Every ID in the JSON appears in the visual**; top-3 labels, the three blueprint lines and the curve are present; the file is well-formed (every non-void tag closed).

Then take screenshots of each band and look at them once.

## 10. Gates (before showing)

Run `check.py` until it prints PASS and the render checks until they're clean, then check what neither can:

- [ ] Title states actor, scenario, current/future and evidence base.
- [ ] Stage names are the actor's words for this scenario.
- [ ] Handoffs, waits and channel switches appear as actions.
- [ ] Each high pain has a cause on the map (a failure, policy or backstage step) or the cause is listed as a gap.
- [ ] Any downgraded claim is downgraded everywhere it appears, visual included.
- [ ] No lane mixes current and future state.
- [ ] Rendered visual looked at once, band by band.

## 11. Review mode

When asked to critique an existing map: if it's data or can be transcribed, run the validator; then run the section 10 checks. Add: missing stages or steps (walk it as the actor), claims that look research-backed without a confirmed source, high pains with no cause behind them, opportunities that don't trace to a pain, and whether the map would change any decision. Report findings by severity, each with a location and a one-line fix.

When reviewing your own map, judge it as if someone else submitted it: look only at the map and the evidence, not at how you built it. On a second pass, check that fixes didn't break anything that passed before.

## 12. Report back

After delivering, in a few lines: the lowest moment and what causes it, the top opportunity, the evidence base, the riskiest assumptions to validate next, and anything you could not check (an unopened canvas, an unconfirmed source). Close with the use: a walkthrough with the people who own each stage within about two weeks, and a date to revisit the map (after a major change, or yearly at most). A map that never gets walked through has failed regardless of quality.

## Credits

Structure and checks draw on these open-source skills (ideas, not text): cuellarfr/design-skills `journey-mapping` (diagram selection, syntax rules, experience types, blueprint lines); product-on-purpose/pm-skills `discover-journey-map` (evidence and confidence labels, stage triggers and exits, scope refusals, research gaps); rampstackco/claude-skills `journey-mapping` (three-view cross-check, opportunity buckets, stated gaps); owl-listener/designer-skills `service-blueprint` (reading a blueprint for failure). Method background: Kalbach, *Mapping Experiences*; Polaine, Løvlie and Reason, *Service Design*.