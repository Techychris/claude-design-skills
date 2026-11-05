import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagram_kit import Canvas, PRIMARY, ACCENT, MUTED, INK, WHITE, FAINT

labels = ["Prompt\nchaining", "Routing", "Parallel-\nization", "Orchestrator-\nworkers",
          "Evaluator-\noptimizer", "Autonomous\nagent"]
tags = ["sequential", "dispatch", "fan-out", "runtime", "eval loop", "self-run"]

box_w, box_h, gap, pad = 1.62, 1.05, 0.32, 0.2
n_workflow = 5
band_h = box_h + 0.5

workflow_w = n_workflow * box_w + (n_workflow - 1) * gap + 2 * pad
band_gap = 0.4
agent_w = box_w + 2 * pad

total_w = workflow_w + band_gap + agent_w
label_h = 0.3
handoff_h = 0.5
tagline_h = 0.45
total_h = band_h + label_h + handoff_h + tagline_h + 0.15

c = Canvas(total_w, total_h, margin=0.3)

band_y = tagline_h + 0.15
c.band(0, band_y, workflow_w, band_h, label=None, edge=HAIRLINE if False else "#D6D9DC")
agent_x0 = workflow_w + band_gap
c.band(agent_x0, band_y, agent_w, band_h, edge=ACCENT, fill="#E6F4F2")

c.text(workflow_w / 2, band_y + band_h + 0.16, "WORKFLOWS 1\u20135   \u00b7   you design the path",
       size=9.6, color=PRIMARY, weight="bold", va="bottom")
c.text(agent_x0 + agent_w / 2, band_y + band_h + 0.16, "AGENT 6   \u00b7   it designs its own",
       size=9.6, color=ACCENT, weight="bold", va="bottom")

box_cy = band_y + band_h / 2
x = pad + box_w / 2
for i, (label, tag) in enumerate(zip(labels[:n_workflow], tags[:n_workflow])):
    cx = x + i * (box_w + gap)
    c.node(cx, box_cy, box_w, box_h, label, tag, edge=PRIMARY, badge=i + 1, badge_color=PRIMARY,
           title_size=9.6, sub_size=7.9)
    if i < n_workflow - 1:
        c.arrow((cx + box_w / 2, box_cy), (cx + box_w / 2 + gap, box_cy))

# final arrow from last workflow box into the agent band
last_cx = x + (n_workflow - 1) * (box_w + gap)
agent_cx = agent_x0 + agent_w / 2
c.arrow((last_cx + box_w / 2, box_cy), (agent_x0 + pad - 0.05, box_cy), color=MUTED)
c.node(agent_cx, box_cy, box_w, box_h, labels[5], tags[5], edge=ACCENT, lw=1.9,
       badge=6, badge_color=ACCENT, title_size=9.6, sub_size=7.9)

# hand-over-control arrow, above both bands, clearly inside the canvas
handoff_y = band_y + band_h + label_h + 0.28
c.arrow((workflow_w * 0.55, handoff_y), (agent_x0 + agent_w * 0.5, handoff_y),
        color=ACCENT, lw=1.5)
c.text((workflow_w * 0.55 + agent_x0 + agent_w * 0.5) / 2, handoff_y + 0.14,
       "hand over control", size=8.2, color=ACCENT, style="italic", va="bottom")

c.text(total_w / 2, tagline_h / 2 + 0.05, "you write the path  \u2192  it writes its own",
       size=9, color=MUTED, style="italic")

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "examples-output")
os.makedirs(OUT_DIR, exist_ok=True)
c.save(os.path.join(OUT_DIR, "six-patterns.png"))
print("saved", total_w, total_h)
