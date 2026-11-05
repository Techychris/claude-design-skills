import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagram_kit import Canvas, PRIMARY, ACCENT, MUTED, INK, WHITE, WARN, HAIRLINE
import numpy as np

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "examples-output")
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------- LEFT PANEL: loop engineering ----------------
c1 = Canvas(4.4, 4.5, margin=0.3)
c1.text(2.2, 4.25, "Loop engineering", size=12.5, color=PRIMARY, weight="bold")

cx, cy, r = 2.2, 2.35, 1.55
c1.dashed_circle(cx, cy, r)
c1.node(cx, cy, 1.7, 0.85, "AGENT", edge=WARN, lw=1.8, title_size=11)

steps = ["discover", "plan", "execute", "verify"]
angles = [90, 0, -90, 180]
label_r = r + 0.42
for step, ang in zip(steps, angles):
    rad = np.radians(ang)
    sx, sy = cx + label_r * np.cos(rad), cy + label_r * np.sin(rad)
    c1.text(sx, sy, step, size=8.6, color=MUTED, boxed=True)

# small curved arrow showing rotation direction, tucked between two labels
c1.arrow((cx + r * 0.62, cy + r * 0.62), (cx + r * 0.85, cy + r * 0.15),
         color=HAIRLINE, rad=-0.5, lw=1.4)

c1.text(cx, 0.35, "context grows every turn until it rots",
        size=8.6, color=WARN, style="italic")

c1.save(os.path.join(OUT_DIR, "loop-panel.png"))

# ---------------- RIGHT PANEL: graph engineering ----------------
c2 = Canvas(6.3, 4.5, margin=0.3)
c2.text(3.15, 4.25, "Graph engineering", size=12.5, color=PRIMARY, weight="bold")

node_w, node_h = 1.5, 0.62

planner = (0.85, 2.35)
workers = [(3.1, 3.5), (3.1, 2.35), (3.1, 1.2)]
reviewer = (5.35, 2.35)
deploy = (5.35, 0.35)

c2.node(*planner, node_w, node_h, "PLANNER", edge=ACCENT, title_size=9.4)
for i, w in enumerate(workers):
    c2.node(*w, node_w, node_h, f"WORKER {chr(65+i)}", edge=ACCENT, title_size=9.4)
c2.node(*reviewer, node_w, node_h, "REVIEWER", edge=PRIMARY, title_size=9.4)

# planner -> workers
for wx, wy in workers:
    rad = 0.18 if wy > planner[1] else (-0.18 if wy < planner[1] else 0)
    c2.arrow((planner[0] + node_w / 2, planner[1]), (wx - node_w / 2, wy), rad=rad)

# workers -> reviewer
for wx, wy in workers:
    rad = -0.18 if wy > reviewer[1] else (0.18 if wy < reviewer[1] else 0)
    c2.arrow((wx + node_w / 2, wy), (reviewer[0] - node_w / 2, reviewer[1]), rad=rad)

# reviewer -> deploy (pass) and reviewer -> worker B (fail), clearly separated
c2.arrow((reviewer[0], reviewer[1] - node_h / 2), (deploy[0], deploy[1] + 0.28),
          color=ACCENT, lw=1.4)
c2.text(reviewer[0] + 0.62, (reviewer[1] + deploy[1]) / 2 + 0.05, "pass",
        size=8, color=ACCENT, style="italic")
c2.node(*deploy, 1.15, 0.5, "DEPLOY", edge=ACCENT, title_size=8.6)

c2.arrow((reviewer[0] - 0.35, reviewer[1] - node_h / 2 - 0.05), (workers[2][0] + 0.2, workers[2][1] - node_h / 2 - 0.15),
          color=WARN, rad=0.32, lw=1.4)
c2.text(4.35, 1.55, "fail", size=8, color=WARN, style="italic")

c2.text(3.15, -0.02 + 0.18, "specialized nodes, shared state, conditional routing",
        size=8.6, color=MUTED, style="italic")

c2.save(os.path.join(OUT_DIR, "graph-panel.png"))

# Composite the two panels side by side, as the SKILL.md design rules describe.
# This is the step that was missing before: the example previously stopped at
# two separate panel files and never produced the actual comparison image.
from PIL import Image

loop_img = Image.open(os.path.join(OUT_DIR, "loop-panel.png"))
graph_img = Image.open(os.path.join(OUT_DIR, "graph-panel.png"))
h = max(loop_img.height, graph_img.height)


def pad_to_height(img, target_h):
    if img.height == target_h:
        return img
    canvas = Image.new("RGB", (img.width, target_h), "white")
    canvas.paste(img, (0, (target_h - img.height) // 2))
    return canvas


loop_img = pad_to_height(loop_img, h)
graph_img = pad_to_height(graph_img, h)
gap = 40
combined = Image.new("RGB", (loop_img.width + gap + graph_img.width, h), "white")
combined.paste(loop_img, (0, 0))
combined.paste(graph_img, (loop_img.width + gap, 0))
combined.save(os.path.join(OUT_DIR, "loop-vs-graph.png"))

print("saved both panels and the composited comparison to", OUT_DIR)
