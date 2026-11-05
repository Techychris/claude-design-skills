---
name: "ux-wireframe"
description: "Turn a UX opportunity or brief into lo-fi wireframes, with 3+ directions to compare, an annotated spec with states, accessibility and responsive rules, and a screen flow, drawn on the Design canvas."
---

# UX wireframe

Work as a senior product designer. A wireframe answers one question ("which structure solves this problem?") before anyone argues about color. Its job is to make a decision easy: which direction, and what the build must handle.

This skill does two things that wireframe tools usually split apart:

- **Explore:** at least three genuinely different directions for the screen that matters most, side by side.
- **Specify:** for the recommended direction, every screen in the flow with content priority, states, interactions, accessibility and responsive rules.

Pictures without a spec leave the build guessing; a spec without pictures never gets compared. Do both, from one JSON file.

If a ux-mapping `map.json` exists, start from it: wireframe one opportunity at a time, and tie every screen to the pains it fixes. For visual craft on higher-fidelity work, use the `design` skill; this skill stays lo-fi on purpose.

## 0. When to use, and when not

Use for: wireframes, lo-fi mockups, screen flows, "show me some options", turning a journey-map fix into screens, and annotated specs before visual design.

Not for: polished UI, brand work or marketing pages (use `design`); a whole site map or IA (use a flow diagram); a single component's visual variants (use `design`).

## 1. Frame

Write a short brief. If the request leaves something open and context allows a responsible assumption, state it in one line and proceed.

- **Problem:** the pain or opportunity in one line, with its ID if it came from a map ("O3: photo rejected weeks after upload; fixes P7").
- **User and moment:** who is on this screen and what they just did.
- **Platform and size:** web 1280–1440 wide, phone 390×844, tablet 768×1024. Pick one primary; others go in the responsive rules.
- **Flow scope:** the screens from the entry point to the outcome (usually 2–5). Mark the **key screen**, the one where the problem is won or lost.
- **Success:** the decision this wireframe should enable ("pick a direction for the photo check and give engineering the states").
- **Fidelity:**
  - *Sketch:* hand-drawn look, for early stakeholder talk where polish would invite the wrong feedback.
  - *Lo-fi* (default): grey boxes, real labels, placeholders.
  - *Mid-fi:* realistic layout and copy, still greyscale.

## 2. Explore: three or more directions

Draw the key screen at least three ways. Each direction varies on a named **axis**:

| Axis | What changes |
|---|---|
| layout | where things sit (stacked, side panel, split) |
| interaction | how the user acts (inline check, separate step, wizard) |
| density | how much at once (one question per screen vs all on one) |
| hierarchy | what leads (warning first vs action first) |
| metaphor | the mental model (checklist, timeline, conversation) |
| flow | where the step sits in the sequence (before upload, after, at payment) |

Rules:

- At least two different axes across the set; directions that differ only in spacing don't count.
- One **conventional** direction (by the book, low risk) and one **novel** one (new territory). The rest can be either.
- Draw every direction at the **same moment** in the flow, with the same content state (for example, all showing a failed check). A direction that quietly shows an earlier step isn't comparable.
- Each gets a one-line **tradeoff** (what it gains, what it costs).
- Then **recommend** one, with a reason tied to the problem, not taste. A blend is fine if you name what comes from where.

## 3. Specify the recommended flow

For every screen in the flow, in the recommended direction:

- **Blocks,** top to bottom, each with an ID, type, label, **priority** (1 = must be seen first; unique per screen), required or optional, and content **source** (static, CMS, computed, user). Use real labels for buttons and navigation; use `[BRACKETED]` placeholders for unknown content; never lorem ipsum.
- **Primary action** with a specific label ("Upload a new photo", not "Submit" or "Continue"), unless the screen is terminal.
- **States** for any screen with an input: empty, loading, error, and success if it differs. Write what the user sees, not the code path. When a state changes what's on screen (an outage hides results, a retry button appears), write it as an object with `text`, `show` (the block IDs still visible) and `add` (blocks only that state has), so it gets drawn correctly instead of as the default screen with a banner on top.
- **Interactions:** what each control does and where it goes.
- **Responsive:** rules for lg, md and sm (what stacks, what collapses, what goes full-width).
- **Accessibility** for any screen with inputs or warnings: labels and fieldsets, where focus goes, errors announced and linked, nothing carried by color alone, touch targets of 44px or more.
- **Fixes:** which pain IDs this screen addresses.

### Facts in copy

Lo-fi copy still makes claims. Any figure in a label (a price, a time, a limit) needs a `ref`: a source ID from the map, or "brief" if the user gave it. Otherwise use a placeholder like `[FEE]`. A wireframe that invents "Takes 2 minutes" gets built with it.

## 4. Data model and validator

```json
{
  "title": "", "platform": "web|ios|android", "viewport": {"w": 1280, "h": 800}, "fidelity": "sketch|lofi|midfi",
  "source": {"map": "map.json", "opportunity": "O3", "pains": ["P7"]},
  "brief": "", "user": "", "success": "",
  "key_screen": "SC2",
  "directions": [{"id": "A", "name": "", "axis": "interaction", "kind": "conventional|novel|other", "tradeoff": "",
                  "blocks": [{"id": "B1", "type": "h1", "label": "", "priority": 1}]}],
  "recommend": {"direction": "A", "why": ""},
  "screens": [{"id": "SC1", "name": "", "purpose": "", "fixes": ["P7"], "terminal": false,
    "blocks": [{"id": "B1", "type": "header|steps|h1|text|warning|input|upload|radio|checkbox|select|date|image|list|button|link", "label": "", "priority": 1, "required": true, "source": "static|cms|computed|user", "ref": "", "aspect": "1:1 (images only)", "note": ""}],
    "states": {"empty": "", "loading": "", "error": {"text": "", "show": ["B1"], "add": [{"id": "E1", "type": "button", "label": "", "priority": 1}]}, "success": ""},
    "interactions": [{"on": "B6", "does": "", "to": "SC2"}],
    "responsive": {"lg": "", "md": "", "sm": ""},
    "a11y": [""]}],
  "flow": [{"from": "SC1", "to": "SC2", "label": ""}],
  "open_questions": [""]
}
```

Without a map, drop `source` and fill `brief` instead. Save as `wireframe.json`, write this checker to `check.py`, and run `python3 check.py wireframe.json` (the map path is resolved relative to the JSON file). Fix every FAIL before drawing, and rerun after every revision:

```python
import json, re, sys, os
w = json.load(open(sys.argv[1])); F = []
scr = {s["id"]: s for s in w.get("screens", [])}
INPUTS = {"input", "upload", "radio", "checkbox", "select", "date"}
GENERIC = {"submit", "ok", "click here", "button", "next", "go", "continue"}
AXES = {"layout", "interaction", "density", "hierarchy", "metaphor", "flow"}
def blocks_of(x): return x.get("blocks", [])
def check_blocks(where, bl, terminal=False):
    pr = [b.get("priority") for b in bl if b.get("priority") is not None]
    if 1 not in pr: F.append(f"{where}: nothing marked priority 1")
    if len(pr) != len(set(pr)): F.append(f"{where}: duplicate priorities")
    ids = [b.get("id") for b in bl]
    if len(ids) != len(set(ids)) or None in ids: F.append(f"{where}: block ids missing or duplicated")
    for b in bl:
        lab = (b.get("label") or "")
        if re.search(r"lorem|ipsum|\bTBD\b|xxx", lab, re.I): F.append(f"{where}/{b.get('id')}: filler text; use a real label or [BRACKETED] placeholder")
        if re.search(r"\d", re.sub(r"(^|\|)\s*\d+\s*[·.)]", "", re.sub(r"\[[^\]]*\]", "", lab))) and b.get("type") not in {"steps"} and not b.get("ref"): F.append(f"{where}/{b.get('id')}: a figure in the copy needs a ref (map source id or 'brief')")
        if b.get("type") == "button" and lab.strip().lower() in GENERIC: F.append(f"{where}/{b.get('id')}: generic button label '{lab}'")
    if not terminal and not any(b.get("type") == "button" for b in bl): F.append(f"{where}: no primary action")
# directions (explore)
d = w.get("directions", [])
if len(d) < 3: F.append(f"{len(d)} directions (want 3+)")
if len({x.get("axis") for x in d}) < 2: F.append("directions all vary on the same axis")
if any(x.get("axis") not in AXES for x in d): F.append(f"direction axis must be one of {sorted(AXES)}")
kinds = [x.get("kind") for x in d]
if "conventional" not in kinds or "novel" not in kinds: F.append("need one conventional and one novel direction")
for x in d:
    if not x.get("tradeoff"): F.append(f"direction {x.get('id')}: no tradeoff")
    check_blocks(f"direction {x.get('id')}", blocks_of(x))
rec = w.get("recommend", {})
if rec.get("direction") not in {x.get("id") for x in d} or not rec.get("why"): F.append("recommend needs a known direction and a why")
# screens (spec)
if w.get("key_screen") not in scr: F.append("key_screen is not a screen")
for s in scr.values():
    sid = s["id"]; bl = blocks_of(s)
    check_blocks(sid, bl, s.get("terminal", False))
    for k, v in s.get("states", {}).items():
        if isinstance(v, dict):
            if not v.get("text"): F.append(f"{sid}: state {k} has no text")
            for x in v.get("show", []):
                if x not in {b.get("id") for b in bl}: F.append(f"{sid}: state {k} shows unknown block {x}")
            for b in v.get("add", []):
                if re.search(r"lorem|ipsum|\bTBD\b", b.get("label", ""), re.I): F.append(f"{sid}: state {k} adds filler text")
                if b.get("type") == "button" and b.get("label", "").strip().lower() in GENERIC: F.append(f"{sid}: state {k} adds a generic button label")
    for b in bl:
        if b.get("type") == "image" and not re.fullmatch(r"\d+:\d+", str(b.get("aspect", ""))): F.append(f"{sid}/{b.get('id')}: image needs an aspect like 1:1 or 16:9")
    if any(b.get("type") in INPUTS for b in bl):
        st = s.get("states", {})
        for k in ("empty", "loading", "error"):
            if not st.get(k): F.append(f"{sid}: has inputs but no {k} state")
    if any(b.get("type") in INPUTS | {"warning"} for b in bl) and not s.get("a11y"): F.append(f"{sid}: no accessibility notes")
    r = s.get("responsive", {})
    for k in ("lg", "md", "sm"):
        if not r.get(k): F.append(f"{sid}: no {k} responsive rule")
    bids = {b.get("id") for b in bl}
    for i in s.get("interactions", []):
        if i.get("on") not in bids: F.append(f"{sid}: interaction on unknown block {i.get('on')}")
        if i.get("to") and i["to"] not in scr and i["to"] not in {"external"}: F.append(f"{sid}: interaction goes to unknown screen {i.get('to')}")
# flow
fl = w.get("flow", [])
for e in fl:
    if e.get("from") not in scr or e.get("to") not in scr: F.append(f"flow edge {e.get('from')}->{e.get('to')} uses an unknown screen")
order = [s["id"] for s in w.get("screens", [])]
if order:
    tos = {e.get("to") for e in fl}; froms = {e.get("from") for e in fl}
    for s in order[1:]:
        if s not in tos: F.append(f"{s}: not reachable in the flow")
    for s in order:
        if s not in froms and not scr[s].get("terminal"): F.append(f"{s}: dead end (no outgoing flow and not terminal)")
# traceability to a ux-mapping map
src = w.get("source", {})
if src.get("map"):
    path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), src["map"])
    try:
        m = json.load(open(path))
        P = {p["id"] for p in m.get("pains", [])}; O = {o["id"]: o for o in m.get("opportunities", [])}
        if src.get("opportunity") not in O: F.append(f"source opportunity {src.get('opportunity')} not in map")
        else:
            want = set(O[src["opportunity"]].get("fixes", []))
            if set(src.get("pains", [])) != want: F.append(f"source pains {src.get('pains')} differ from what {src['opportunity']} fixes {sorted(want)}")
        for x in src.get("pains", []):
            if x not in P: F.append(f"pain {x} not in map")
        fixed = {p for s in scr.values() for p in s.get("fixes", [])}
        for x in src.get("pains", []):
            if x not in fixed: F.append(f"pain {x} not addressed by any screen (screen.fixes)")
        refs = {s["id"] for s in m.get("sources", [])} | {"brief"}
        for s in list(scr.values()) + d:
            for b in blocks_of(s):
                if b.get("ref") and b["ref"] not in refs: F.append(f"{s.get('id')}/{b.get('id')}: ref {b['ref']} not a map source")
    except FileNotFoundError: F.append(f"map file not found: {src['map']}")
elif not w.get("brief"): F.append("no source map and no brief")
if not w.get("open_questions"): F.append("no open questions listed")
print("\n".join("FAIL " + f for f in F) or "PASS"); sys.exit(1 if F else 0)
```

## 5. Draw

### Where

- If the session's artifact tool lists a **Design** type, draw on a Design canvas: the person will compare, comment and edit. Follow the canvas's own format and diagram rules.
- Otherwise, one self-contained HTML page published as an artifact.
- A file format (Figma, draw.io, PNG, PDF) only when the person names one.

The Design type forbids reading back or rendering a canvas unless the user asked. If they asked for testing or review, run the checks in section 6 and say so. If not, run them on your local preview of the generated files and say the published canvas itself wasn't opened.

### Canvas layout

Canvas rules that bite: the first artboard must be named `Main.dc.html` (use the conventional direction); controls are real `<button>`, `<a href>`, `<input>` and `<label>` elements even in lo-fi, never styled spans; rationale and tradeoffs go in canvas sticky notes beside the frames, not inside artboards. Leave room under a sticky (it can grow to 4/3 of its width) before the next row.

One artboard per frame, in three rows with a `title1` note above each:

1. **Directions:** one artboard per direction (key screen, at platform size), labeled "A · Checklist result · conventional · interaction", and so on, with its tradeoff in a sticky note underneath. The recommended one says so in its frame title and sticky.
2. **Flow:** one artboard with every screen of the recommended direction as a mini frame, joined by arrows labeled with the trigger ("Something to fix", "Use anyway"). A straight sequence can be a row with chevrons; branches and loops need placed frames and arrows (follow the canvas's diagram rules). Mark the key screen.
3. **States and spec:** one artboard with the key screen's states as mini frames (empty, loading, error, success), and one spec artboard listing blocks by priority with interactions, responsive rules, accessibility notes, the pains fixed, and open questions.

Annotations: numbered markers on the direction and flow frames, matching block priorities in the spec. Sticky-note style (a tilted note with marker text) is fine at sketch fidelity; plain numbered circles otherwise.

### Lo-fi conventions

- Greyscale only, plus at most one accent for the primary action or the key warning.
- Images are boxes with an X or a `[Photo]` label, drawn at their real aspect ratio (`aspect`: a passport photo is 1:1, a hero is often 16:9); body text is grey bars, except copy that matters to the decision, which is written out. Two images that are meant to be compared sit side by side.
- Real labels on every button, link and nav item, on real controls (buttons at least 44px tall at full size).
- Inputs look like inputs: a label above a box; radios and checkboxes as circles and squares with labels.
- Warnings use a heavier border and a heading, not color.
- At sketch fidelity: graph-paper ground, marker type, hatched fills, slight rotations. Never in lo-fi or mid-fi.

### Generate, don't hand-draw

Write a small script that reads `wireframe.json` and writes the artboards. Map each block type to one lo-fi component, so the same block always looks the same across directions, flow and states. Honor state objects (`show`, `add`) when drawing states. Then revisions are: edit the JSON, rerun the checker, regenerate.

## 6. Render checks

Open your local preview in a headless browser and check by script:

1. **Nothing overflows:** each frame's content fits its size, or the frame grows.
2. **Greyscale:** every color used is grey (saturation under about 10%) except the one declared accent.
3. **Every block ID and screen ID** from the JSON appears in the drawing, and every annotation number matches a block priority.
4. **Phone width:** if the platform is web, the sm rules are drawn or described; a fluid page doesn't scroll sideways at 390px.

Then screenshot each artboard and look at it once.

## 7. Review

Before showing, judge it as if someone else made it:

- [ ] Could someone pick a direction from the Directions row alone, without reading the spec?
- [ ] Is the novel direction actually novel, or the conventional one rearranged?
- [ ] Do all directions show the same moment and the same content state?
- [ ] Does each drawn state match its own words (a state that says "Try again" shows a Try again control)?
- [ ] Does the recommendation follow from the problem and the tradeoffs?
- [ ] Is every pain the opportunity fixes visibly addressed on some screen?
- [ ] Would an engineer know what happens on error, slow network and a small screen?
- [ ] No invented figures or filler copy.

## 8. Report back

In a few lines: the recommended direction and why, what the other directions taught (what to keep from them), the riskiest open question, and what you couldn't check. Next step: test the recommended flow with 3–5 users on the key screen's main task before moving to visual design.

## Credits

Combines ideas (not text) from four open-source skills: bluzir/claude-code-design `wireframe` (three or more directions on varied axes, one conventional and one novel, greyscale and placeholders); Owl-Listener/designer-skills `wireframe-spec` (content priority, interaction notes, states, responsive and accessibility annotations, real labels); nexu-io/open-design `wireframe-sketch` (sketch fidelity and sticky-note annotations); markdown-viewer `wireframe` (platform sizes, consistent component library, navigation flows). Traceability and validation follow the `ux-mapping` skill.