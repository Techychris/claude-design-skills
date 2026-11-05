---
name: diagram-forge
description: "Create clean, professional box-and-arrow diagrams (flowcharts, architecture diagrams, control-spectrum/comparison panels, node graphs) as PNG images via a small matplotlib helper library. Also supports proper ArchiMate enterprise-architecture notation (business/application/technology layer colors, element icons, and the standard relationship arrows: composition, aggregation, assignment, realization, serving, access, flow, triggering, specialization) for Layered Views, Application Structure Views, and similar enterprise-architecture diagrams. Use this INSTEAD of freehand matplotlib/PIL code whenever a diagram, flowchart, architecture sketch, process diagram, node/edge graph, or ArchiMate/enterprise-architecture view is needed for a document, slide, or chat reply. Not for photographs, charts of numeric data (use the data-analysis/plotting skill for that), or hand-drawn/artistic illustration."
compatibility: "Requires matplotlib, numpy, and Pillow (PIL) in the Python environment."
---

# diagram-forge — box-and-arrow diagram kit

A thin matplotlib library (`scripts/diagram_kit.py`) for node/edge diagrams: flowcharts, architecture diagrams, comparison panels, control spectrums. Produces PNGs sized to their content, not to a fixed canvas, so nothing gets clipped.

## Why this exists

Freehand matplotlib diagrams reliably go wrong in the same two ways:
1. **Clipping.** A hardcoded `xlim`/`ylim` that's slightly too small silently cuts off the last box or a label. This is very easy to miss when you generate an image and never re-check its edges.
2. **Wasted or cramped space.** Either huge dead zones because the canvas was guessed too big, or labels/arrows crowding each other because it was guessed too small.

`diagram_kit.py`'s `Canvas` class fixes both by taking the content's width/height as constructor arguments and deriving the figure size and axis limits from that directly, with a fixed margin added on top. There is no separate "canvas size" to get out of sync with the content.

## Workflow

1. Sketch the diagram on paper/in your head first: what are the nodes, what connects to what, are there groups/bands, is it one panel or a side-by-side comparison. Decide the content width and height in the same made-up unit (inches work well: box sizes like 1.5, gaps like 0.3).
2. Write a small script that imports `diagram_kit` and calls `Canvas(width, height, margin=0.3)`, then `.node()`, `.arrow()`, `.band()`, `.text()` as needed. See `scripts/example_control_spectrum.py` and `scripts/example_two_panel_comparison.py` for full worked examples.
3. `.save(path)` — this always uses `bbox_inches="tight"` with real padding.
4. **Verify before using it anywhere (required):** `.save()` automatically runs an overlap check (see below) and raises rather than writing the file if two node/element boxes land on top of each other — that failure mode sits entirely inside the canvas, so no border check can see it. Separately, check the four image borders aren't pure content-on-edge (a clipping check), then actually look at the image.
   ```python
   from PIL import Image
   import numpy as np
   arr = np.array(Image.open(path).convert("L"))
   b = 3
   for name, region in [("top", arr[:b,:]), ("bottom", arr[-b:,:]), ("left", arr[:,:b]), ("right", arr[:,-b:])]:
       assert region.min() == 255, f"{name} edge has non-white content — something is clipped, widen the canvas"
   ```
   Then `view` the PNG yourself. A diagram you haven't looked at is not done — this mirrors the same rule in the `docforge` skill for documents. **Don't catch and suppress the `ValueError` from `.save()`** — it means two boxes are genuinely stacked on each other (often a loop drawing something that's also drawn separately afterward); fix the positions/loop range, don't paper over it.

## API (`scripts/diagram_kit.py`)

| Method | Use for |
|---|---|
| `Canvas(width, height, margin=0.3)` | Start a diagram. Width/height are content size in arbitrary units (inches is a sane default); margin is added automatically. |
| `.node(cx, cy, w, h, title, subtitle=None, edge=, fill=, badge=)` | A rounded box: title, optional subtitle, optional numbered badge in the corner. |
| `.arrow(p1, p2, color=, rad=0.0)` | An arrow between two points; `rad` bends it (positive/negative curve) — use this instead of straight lines when two arrows would otherwise overlap. |
| `.band(x0, y0, w, h, label=None)` | A soft background rectangle behind a group of nodes, with an optional label above it. |
| `.dashed_circle(cx, cy, r)` | A dashed circle, for loop/cycle diagrams. |
| `.text(x, y, s, boxed=False)` | A standalone label; `boxed=True` puts a light card behind it, useful for labels sitting on top of a dashed circle or crossing lines. |
| `.check_overlaps(tol=0.06)` | Returns any node/element box pairs overlapping by more than `tol` of the smaller box's area. Called automatically by `.save()` — you shouldn't need this directly, but it's available for debugging. |
| `.save(path)` | Runs the overlap check (raises `ValueError` if it fails), then writes the PNG, tight-cropped with padding. |

## Design rules

- Compute width/height from actual content (box counts × box width + gaps), don't guess a round number and hope it fits.
- When two panels are meant to sit side by side (a comparison), generate them as two separate `Canvas` calls at the same `height`, then composite with PIL (`Image.paste`) rather than fighting matplotlib subplot spacing — this gives independent, predictable margins per panel.
- Give curved arrows (`rad=...`) real separation (0.15+ magnitude) whenever more than one arrow touches the same node, or they visually merge.
- Labels near a dashed circle or crossing an arrow should sit outside the circle/line, not on top of it, and use `boxed=True` if there's any chance of overlap with a line underneath.
- Keep one palette per diagram (this kit's default is teal/charcoal); don't mix in colors that don't appear anywhere else in the same document.

## Embedding in a document

This skill only produces PNGs. To put one inside a Word document, hand off to the `docx` skill's `ImageRun` guidance (or a document-template skill if the deliverable uses one) — diagram generation and document assembly are deliberately kept separate here.

## ArchiMate notation

For enterprise-architecture diagrams, use `.archimate_element()` and `.archimate_relationship()` instead of the generic `.node()`/`.arrow()`. These follow the notation conventions distilled in Eero Hosiaisluoma's *ArchiMate Cookbook: Patterns & Examples* (a free, widely-used practical guide to the ArchiMate 3.2 spec, hosiaisluoma.fi) — specifically its recommended ~80%-of-cases subset of elements, plus the layer-color convention the Cookbook calls out explicitly (sec. 8.2.2): yellow for business, light blue/turquoise for application, light green for technology. See `scripts/example_archimate_layered_view.py` for a full worked example (a Layered View, the Cookbook's own top-recommended diagram type).

**`.archimate_element(cx, cy, w, h, label, layer=, kind=)`**

| `layer` | Color |
|---|---|
| `motivation` | lavender |
| `strategy` | orange |
| `business` | yellow |
| `application` | light blue |
| `technology` / `physical` | light green |
| `implementation` | pink |

| `kind` | Shape |
|---|---|
| `active` | plain box, small square icon — actors, roles, devices |
| `behavior` | plain box, small chevron icon — processes, functions, events |
| `service` | pill-shaped (very rounded) — business/application/technology services |
| `object` | plain box, small document icon — business objects, data objects, artifacts |
| `component` | plain box with two small tabs on the left edge (UML-style) — application components |
| `node` | plain box with a small stacked-box icon — technology nodes |

**`.archimate_relationship(p1, p2, kind=)`** — draws the correct line style and endpoint marker for one of: `composition` (filled diamond at the whole/source end), `aggregation` (hollow diamond at source), `assignment` (filled ball at source, open arrow at target), `realization` (dashed line, hollow triangle at target), `serving` (solid line, open arrow at target), `access` (dotted line, small open arrow at target), `flow` (dashed line, filled arrow at target), `triggering` (solid line, filled arrow at target), `specialization` (solid line, hollow triangle at target), `association` (plain line, no arrowhead).

**`.archimate_legend(x, y, layers=(...))`** — a small color-key strip; the Cookbook recommends always including one (sec. 8.2.2) since layer colors carry meaning that isn't obvious without a key.

**Known simplification:** relationship markers (diamonds/triangles) are computed from the straight chord between the two endpoints, even when the connecting line itself is drawn curved (`rad != 0`). For sharply curved relationship lines, the marker angle will be slightly off from the curve's actual tangent at the endpoint — keep `rad` small (under ~0.15) for ArchiMate relationships, or use straight connections, which is how the Cookbook's own diagrams are drawn in practice anyway.

This covers the Cookbook's core element/relationship notation, not its full catalog of diagram *types* (Motivation View, Business Model Canvas, SIPOC, etc.) — those are compositions of these same primitives arranged differently, not additional shapes to implement.
