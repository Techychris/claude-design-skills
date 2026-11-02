---
name: design-demo
description: "Use instead of the built-in design skill's Demo mode for faux product UI: hero or feature-card illustrations of an app, bento grids, mocked screens, animated cursor walkthroughs. Loads design-lean for direction, craft rules, tokens and the gate."
---

# Design demo (faux product UI)

**Load `design-lean` first.** Its Direction, Craft rules, Tokens and component gate apply here; this skill adds what a product shot needs. Demo work sits in Build's step 5 when a page needs a product preview, or runs alone when the demo is the whole job.

**Gates for a demo run**

| Gate | Pass condition | Evidence left | Cap | On fail at cap |
| --- | --- | --- | --- | --- |
| D1 Plan | Placement, focal object, action, payoff and what's left out written before code | The plan | — | — |
| D2 Frame | One still at the shown width and at 390 is not empty, flat or boxed | Two stills | 2 reframes | Hand over with the framing fault named |
| D3 Rehearse | Poster frame set; contact sheets at both widths show no fault from the list at the end | Contact sheets | 3 film rounds | Hand over with remaining faults listed |
| D4 Host gate | `gate.js` passes on the host page's own controls, Pause included | Gate totals | 2 fix attempts per check | Report as open issue |

**Setup** (extract, don't retype; the base directory is shown when each skill loads):

```bash
mkdir -p .design && for f in "<design-lean base directory>/SKILL.md" "<design-demo base directory>/SKILL.md"; do python3 - "$f" <<'PY'
import re, sys
for name, code in re.findall(r"`{3}js\n// file: (\S+)\n(.*?)`{3}", open(sys.argv[1]).read(), re.S):
    open(".design/" + name, "w").write("// file: " + name + "\n" + code); print("wrote .design/" + name)
PY
done
```


Miniature product UI: a believable interface, framed in its space, as one still or a short animation in which one thing happens. The viewer recognizes the screen and sees the thing happen. These are authored illustrations, not browser automation: the script draws the cursor pressing and changes the scene. The Craft rules and Tokens from `design-lean` still hold; this section adds what a product shot needs and overrides `design-lean`'s Motion where they differ.

**The one idea:** it reads as a real product, simplified to what the viewer needs, framed with intent, and every motion has a cause.

Five ways it fails:
- **Too much.** Real text in every row, numbers everywhere, everything packed. The more detail, the more it looks generated.
- **Wireframe.** Two gray blobs and a button. Built too small, or stripped of what made it recognizable.
- **Boxed.** A whole window shrunk into a card with even margins: a screenshot pasted in, not a product shot.
- **Flat.** Every object the same weight in the same bordered card. The eye has nowhere to land.
- **Bland.** A gray window with a cursor, whatever the brief said. The brief's look and energy (a blueprint, glass over color, a Dynamic Island, a mascot) are the point; build what it asks for, to these rules.

The fix: a full, structured screen in quiet grays, real words only on what the story is about, placeholder bars for the rest, room to breathe, a crop that puts the eye where the story is. Simplify the words, not the context. An empty corner, a void under a list, rows spread to fill a pane, a window floating on a plate: unfinished, not calm.

**How hard to press.** Build it like a launch page you will be judged on. Then look at the frame as the most exacting designer you know would, the one who screenshots the one wrong thing and sends it back with "what is this?": a dot off its avatar, a unit on its own line, copy touching a card. If you can picture that screenshot, you have found the next fix.

## The Stageshow kit

When it is available, use it: React parts (`Stage`, `Window`, `Phone`, `Row`, `Bar`, `Text`, `Roll`, `Count`, `Collapse`, `Fly`, `Connector` and more, with an `Act` script API), about 70 gold examples and product studies, and `scripts/film.mjs`, which films a contact sheet and flags framing and motion faults. Look for a `stageshow` skill folder or a `kit/` with `stageshow.css` in the project. Otherwise, with network access, install it (`npx skills add benjitaylor/skills --skill stageshow`) or clone `https://github.com/benjitaylor/skills` and work from `stageshow/`. Then its `SKILL.md`, `references/` and the closest gold example are the detailed rules; this section is the summary. Installing it runs that repo's own package scripts, which a sandbox may block. Without the kit, build in plain React or HTML and CSS by the rules below and film with the script under Filming without the kit.

## Run

Most of the quality is decided before any code. Write the plan first: where it sits, the focal object, the action, the payoff, what can be left out.

1. **Medium and place.** Still or animation (loop, once in view, or on hover). The page, its ground, its width. Design at the size it will be seen and show it at 1:1: about 720 × 340 for a hero beside copy, 900 to 1100 wide for a full-width hero, 400 × 300 for a card. Never under about 320 wide for a demo; a bento tile or satellite card may be smaller. Anything that can sit in a phone column gets a compact design at 358 wide: a redesign (closer crop, satellite dropped or stacked), not a squeeze.
2. **Look.** With the product's code or site at hand, take its real tokens, icons, chrome and words. With none, run `design-lean`'s Direction for it. Pick a fidelity: minimal (all bars), standard (words where they carry meaning, bars elsewhere, the default), realistic (real content everywhere; for hero scale, a named real product, or a still whose subject is a list or page). A brief with a style (kawaii, paper, a poster color) gets that style in full, still built to these rules.
3. **The story.** Pick its shape from what the product is valued for: how it feels to use (a cursor does one satisfying thing and the result appears under its hand), a flow (a few screens told as one continuous object, payoff on the last), or what the system does (the consequence lands somewhere else, the link visible, usually no cursor). Three to five beats and a payoff, 10 to 16 seconds. Between a richer story and a calmer frame, choose the frame.
4. **Start from a gold, then frame it.** With the kit, film the closest gold example and copy its folder as the start; keep its stage size, crop, row and type sizes, spacing and beats, then replace its look and content with the brief's product. A copy that only changes the name is not done. Without the kit, pick a layout from the table below and hold yourself to it the same way. Frame before any motion: film one still at both widths; if it is emptier, flatter or more boxed than it should be, fix the frame first.
5. **The screen.** Count the real strings, usually 3 to 7: a budget for words, not elements. Fit every control's text before it moves. Measure what the cursor touches from the DOM; never hard-code positions.
6. **Choreograph.** Keep what appears mounted and toggle it so exits animate. Animate the relationship, not just the object: a new row carries the rows below it; a resizing surface never stretches its text. Beats overlap, groups stagger, the payoff holds, the loop ends where it began or resets with a visible cause.
7. **Rehearse.** Set the poster frame first: the beat that tells the story on its own, never one caught mid-change, the result left on screen. Then film the loop, not only a still: a contact sheet at the shown width and at 390, and step frame by frame through every press, menu, morph and the loop seam. A still can't show a pop. Fix the largest visible fault first (framing, then hierarchy, then motion, then polish) and re-film. Cap: three film rounds; after that, hand over with the remaining faults listed. Ask: what does the eye land on first, and is it the result? Is one window, tile or device clearly leading? Any no is the largest fault. A passing script is necessary, not sufficient. Hand over with a short note: the gold or layout you started from, what you changed, what you did not check.

## Framing

- **One hero object, at most one or two satellites** (a receipt, a phone, a detail card) that carry the point. Keep what identifies the product: a title, the real chrome, the rows that give the action a reason. Logo and nav are optional.
- **Crop only filler.** The payoff, the action, what the cursor touches and every real word stay whole. A placeholder action the crop would slice is removed, not sliced. A button, chip or shadow sliced by the stage edge is the usual fault.
- **Crop 10 to 40% of the hero off stage.** The window or phone fills at least two thirds of the stage's width and runs off an edge. The stage masks everything (`overflow: hidden`).
- **The page is the ground.** On a white or dark page, no plate behind the window and no window whole with air on four sides; that floats. Unframed (whole, centered, an even margin at least as deep as the shadow) only when the developer asks.
- **One gutter,** measured in the final crop: every edge distance matches it, a full gutter or well past. Crossing it by under 24px or stopping a few pixels short is a mistake.
- **Satellites straddle the hero's edge, about half outside,** over chrome (a sidebar, header or margin), never over content. Two satellites are two kinds and sizes (a card and a notification at true size), never two equal cards stacked. Anchored UI (popover, menu, toast) is not a satellite: it sits where the product puts it.
- **A window keeps its device's shape:** whole at 1.25:1 or wider; bled, what shows is at least square. Fix by crop, never by squashing.
- **What the story opens stays in frame,** a gutter from every edge on every frame; place the trigger so the overlay has room. No dead corners at rest or anywhere in the loop.
- **Start flat and frontal.** Depth from shadow, z-order, scale and opacity; tilt only where it earns its keep (a loose pile of paper), perspective only when asked.
- **Phones:** a satellite phone starts at 40% of the window's visible width and at least 220px; let it run off the bottom rather than shrink. Notifications stay at true iOS proportion and are never cut. A phone cropped at the top loses its status bar and nav bar together. Never draw a status bar or home indicator by hand; take the frame from the kit or a real reference.

| Layout | Hero | Use for |
| --- | --- | --- |
| Pinned, bottom bleed | Inset 8–12% left, right and top; 15–35% past the bottom | Feature cards and bento tiles |
| Corner bleed | Inset 10% top and left; 15–35% past right and bottom; satellite on the left or bottom edge | Heroes beside copy |
| Stage with gutters | Inset 8–20% each side on a colored stage, off the bottom | Brand moments |
| Satellite focus | Hero cropped hard; a large satellite (30–40% of hero width) carries the story | One small thing: a notification, a receipt, a diff |
| Wide hero | A 900–1100px window at 1:1, off the bottom; realistic fidelity | Homepage heroes at full width |
| Device pair | Desktop 75–80% wide, off the bottom; phone straddling the right edge, a third outside | Cross-device stories |
| Many of one | A grid of one thing off every edge; one tile in focus by depth, the only one with words | Scale shown as repetition |
| Fade crop | Window inset top and sides, masked out over its last third, filler only under the fade | When an edge would cut the window at an arbitrary line |
| Close-up | The whole window at 1.3–1.6x, chrome and all, the subject row whole | A card about one control |
| Panel over product | A settings panel over the product's margin, one neutral leader to what it changed | A setting and its effect |
| Opposite corners | Copy bottom-left; the product hung from the top-right corner | Bento tiles with a line of copy |

A bento grid is one set: one hero tile, then a window, a stat, an object and a diagram, each a different kind; plan the grid before any tile.

## The still frame

- **Restraint.** Real strings on the title, the thing acted on, what is typed, the result; the rest is bars. Bars are filler at the edges; bars where the eye lands read unfinished. Where the story touches a list, two or three real rows. In a small surface a row is one line: avatar, name, value. Placeholder widths vary row to row (60, 45, 70, 52). Label and value match: both words or both bars. One number gets to be big. Say the feature's signal once, not in header, satellite and every row.
- **Keep the domain's signature content:** album art, thumbnails, avatars (each named avatar its own color). Swapped out, it is a generic list.
- **No masthead for a fictional name** and no product name on screen unless the brief leans on it and the real product would show it there. A faux app's title is a `div`, never `h1` to `h6`: the demo lives inside someone's page outline.
- **Type:** real 11 to 15px UI sizes, scaled by the stage, never 7px. Small text line height at least 1.3. Monospace only for code, identifiers and aligned numbers.
- **Spacing:** words keep a 12px inset from any window, card, panel or hovered-row edge (never under 8); bars may bleed, words do not. Row padding 12px, 8 for a dense list. A title over its subtitle sits 4 to 6px apart. A button keeps 8px or more from the field above it. No near-tangents: edges 1 to 3px apart read as accidents; align exactly or part by at least 8.
- **Optical centering:** center a label on its letters (`text-box: trim-both cap alphabetic`) in pills, buttons and avatars. A centered amount centers its digits, with the currency sign hung outside at `right: 100%`.
- **Icons come from a set, never your hand:** the product's own pack first, else one set chosen on purpose (SF-style for Apple chrome, Material Symbols for Android, else Phosphor, Iconoir, Radix, Tabler, Heroicons or Lucide), one size (14–16px) and stroke per scene, filled at 14px and under. Emoji are content, never icons. Other products' logos are their real marks in original proportions, never a look-alike.
- **AI features:** no sparkle, wand or star and no purple as the AI color; show what the AI does (the question sent, thinking, the answer streaming in with its height, sources last). The product's own icon is fine even if it is a sparkle.
- **No invented logo:** a letter in a colored square is not a mark. Use the real mark or a plain text wordmark.
- **Color:** one neutral family for window, sidebar and cards; five inks and one accent to start. Don't outline the hero with an accent ring to point at it; lift it the way the product would. Nothing translucent overlaps. On dark, depth comes from a lighter surface, not shadow.
- **Chrome:** a desktop app gets its real chrome; browser chrome only when the browser is part of the picture. Never draw platform chrome from memory; look at the real app or a screenshot. Sidebar columns run the full height of their window. A messaging app on an iPhone keeps Messages' conventions unless the brief gives it a look.

## Demo motion

Storytelling motion (the cursor, rolls, flights, staggered dependents) follows these rules instead of the Motion section and web-motion's 300ms component budget, 50ms shared-trigger rule, 30–80ms stagger and 500ms cascade cap. UI feedback inside the demo (hover, press, a toggle, a toast) keeps those rules and the product's own timing.

- **Two curves.** Travel `cubic-bezier(0.45, 0, 0.1, 1)`, timed by distance: a longer trip takes longer, and a move reads by its overlap with the next beat. Arrival from nowhere `cubic-bezier(0.25, 0.8, 0.25, 1)` over 0.8 to 1s. Stagger groups in reading order 40 to 80ms apart, 80 to 120ms between grid tiles.
- **Open on a finished screen that works as a still.** The cursor rests on empty surface between beats, near its next move, never on an unused control. No cursor move you can't explain; with no cursor, no stand-in (no wandering focus ring or spotlight). The elements decide the cursor's kind: I-beam over text, hand over links, arrow on native app buttons, resize on edges.
- **Every change moves.** Change only what changed: roll the changed span of text and slide what follows by its measured width; numbers roll last digit first. A button keeps one slot for all its states. Typed text becomes a chip in place.
- **Nothing pops.** Everything has an entrance and stays mounted until its exit finishes. Solid things (windows, phones, cards) arrive by moving, never fading through. Cards and pills arrive whole from just above; a toast enters and leaves through the screen edge it is anchored to. Content arrives after its container. A popup is sized before its first frame and holds the edge it opened from.
- **One object, one trip, ending in its final place:** open the room, measure the slot, then fly. Landings decelerate over the last third, no bounce. After motion nothing moves: the handoff frame matches in size, place and look.
- **Drags:** keep the grab offset, the others make room continuously, the drop snaps to a measured slot. A text selection sits under the I-beam.
- **The payoff is visible at the shown size and arrives full,** never a blank surface for a quarter second. It holds about 2s before the exit; nothing sits still more than three seconds.
- **Loops:** a reset removes what the loop added as one thing, with a seen cause (undo, clear, close), as a reverse stagger around an anchor, or snapped while hidden. Data never rewinds in view. A loop never plays a navigation backwards. No dead air at the seam: the next action begins within about a second of the exit.
- **Playback:** any demo that plays on its own for more than 5s in total, a loop of any cycle length or a once-in-view story, gets a visible, keyboard-operable Pause control beside it (WCAG 2.2.2). Pause when the demo is off screen or the tab is hidden. Pausing stops the script's clock and freezes only the animations on the stage (`document.getAnimations().filter((a) => stage.contains(a.effect?.target))`); freezing every animation in the document also freezes the host page's controls mid-press.
- **Reduced motion** shows the poster frame, with Play as an opt-in.

The `design-lean` component gate applies to real, interactive UI. A demo's stage is an illustration: put `data-stage` on its root and the gate skips it and every component inside it (its easing and decorative controls would fail on purpose). Gate the host page's own controls, Pause included.

## Faults that come back every round

Check these before handing over:
- Content that swaps instead of moving
- Gray bars where the eye lands
- A plate behind the window, or a window floating with air on four sides
- Empty bands, and controls or shadows cut by the stage
- Stock AI and made-up logos: sparkles, purple, a letter in a colored square
- Busy rows and uneven insets
- Long holds, and a reset with no cause
- A selection that isn't under the I-beam
- A status bar or home indicator drawn by hand
- A centered amount centered together with its sign

## Filming without the kit

Extract `film.js` the same way as the gate (command under Setup); don't retype it. It shoots one element at a fixed interval and lays the frames out at 2x as one contact sheet, so a loop reads as one image. It films the first `.frame`, the wrapper that holds the stage; put that class on it or pass `--select`. Read every sheet you make. Frames run left to right: compare neighbors in a row, and the last of a row with the first of the next, before calling a change a jump.

```bash
node .design/film.js page.html --width 1440 --every 600 --count 20 --out loop.png   # the whole loop
node .design/film.js page.html --width 390 --every 700 --count 16 --out phone.png   # the compact design
node .design/film.js page.html --start 1600 --every 100 --count 10 --out beat.png   # one beat; a shot takes 100 to 200ms, so read the timestamps
node .design/film.js page.html --reduce --still --out poster.png                    # what reduced motion shows
```

```js
// file: film.js
// Film a demo: shoot one element at a fixed interval and lay the frames out as one contact sheet.
// Usage: node film.js <url-or-html-path> [--select .frame] [--width 1440] [--every 500] [--count 20]
//                     [--start 0] [--still] [--reduce] [--out sheet.png]
// Prints page errors and console warnings. Requires Playwright (require('playwright')).
const { chromium } = require('playwright');
const path = require('path');
const args = process.argv.slice(2);
const USAGE = 'Usage: node film.js <url-or-html-path> [--select .frame] [--width 1440] [--every 500] [--count 20] [--start 0] [--still] [--reduce] [--out sheet.png]';
const opt = (k, d) => { const i = args.indexOf('--' + k); if (i < 0) return d; const v = args[i + 1]; if (v === undefined || v.startsWith('--')) { console.error(USAGE); process.exit(2); } return v; };
const has = (k) => args.includes('--' + k);
const target = args[0];
if (!target) { console.error(USAGE); process.exit(2); }
const url = /^https?:|^file:/.test(target) ? target : 'file://' + path.resolve(target);
const sel = opt('select', '.frame'), width = +opt('width', 1440), every = +opt('every', 500);
const count = has('still') ? 1 : +opt('count', 20), start = +opt('start', 0), out = opt('out', 'sheet.png');

(async () => {
  let browser;
  try {
  browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width, height: 900 }, deviceScaleFactor: 2, reducedMotion: has('reduce') ? 'reduce' : 'no-preference' });
  const logs = [];
  page.on('pageerror', (e) => logs.push('pageerror: ' + e.message));
  page.on('console', (m) => { if (['error', 'warning'].includes(m.type())) logs.push(m.type() + ': ' + m.text()); });
  await page.goto(url);
  const el = page.locator(sel).first();
  if (!(await el.count())) { console.error(`No element matches ${sel}; pass --select`); if (logs.length) console.error(logs.join('\n')); process.exitCode = 1; return; }
  await el.scrollIntoViewIfNeeded();
  await page.waitForTimeout(start);
  const shots = []; const t0 = Date.now();
  for (let i = 0; i < count; i++) {
    const wait = t0 + i * every - Date.now(); if (wait > 0) await page.waitForTimeout(wait);
    shots.push({ t: Date.now() - t0 + start, png: (await el.screenshot()).toString('base64') });
  }
  // Lay the frames out at true size (2x) in a grid sized to fit, then screenshot the grid.
  const box = await el.boundingBox();
  const cols = count === 1 ? 1 : box.width >= 600 ? 2 : 3;
  const sheet = await browser.newPage({ deviceScaleFactor: 2, viewport: { width: Math.ceil(cols * (box.width + 16) + 16), height: 600 } });
  await sheet.setContent(`<body style="margin:0"><div id="s" style="display:inline-grid;padding:16px;background:#e4e6ea;font:12px system-ui;gap:16px;grid-template-columns:repeat(${cols},${box.width}px)">` +
    shots.map((s) => `<figure style="margin:0"><figcaption style="color:#3c3c46;margin-bottom:6px">${s.t} ms</figcaption><img style="display:block;width:${box.width}px" src="data:image/png;base64,${s.png}"></figure>`).join('') + '</div></body>');
  await sheet.locator('#s').screenshot({ path: out });
  console.log(`${out}: ${shots.length} frame(s) of ${sel} at ${width}px${has('reduce') ? ', reduced motion' : ''}`);
  if (logs.length) { console.log(logs.join('\n')); process.exitCode = 1; }
  } catch (e) { console.error('film.js: ' + e.message.split('\n')[0]); process.exitCode = 1; }
  finally { await browser?.close(); }
})();
```

---

Built from: Demo mode condensed and adapted from Stageshow by Benji Taylor (https://github.com/benjitaylor/skills, MIT), as adapted in the Anthropic design skill; restructured with gates. Keep this credit in any copy or adaptation.

Stageshow notice: Copyright (c) 2026 Benji Taylor. Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
