"""
diagram_kit.py — small matplotlib helper library for clean box-and-arrow diagrams
(flowcharts, architecture diagrams, comparison panels).

Design rules this kit enforces so diagrams don't come out looking amateurish:
  - The canvas is sized FROM the content (you tell it how much space content needs;
    it does not use a fixed xlim/ylim you have to guess and can clip against).
  - Every save goes through bbox_inches="tight" with real padding, so there's never
    a box or label flush against (or past) the image edge.
  - One shared palette + spacing scale, so multiple diagrams in the same document
    look like they belong together.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# ---- shared palette (teal/charcoal, works on white) ----
INK = "#1F2328"
PRIMARY = "#2B2F33"
ACCENT = "#0F766E"
WARN = "#B45309"
MUTED = "#6B7280"
FAINT = "#F3F4F6"
HAIRLINE = "#D6D9DC"
WHITE = "#FFFFFF"

FONT_TITLE = 10.5
FONT_SUB = 8.4
FONT_LABEL = 8.6

# ---- ArchiMate notation (per The Open Group ArchiMate 3.2 spec, as distilled in
# Eero Hosiaisluoma's "ArchiMate Cookbook: Patterns & Examples", hosiaisluoma.fi) ----
#
# Layer colors follow the established ArchiMate convention the cookbook calls out
# explicitly (sec. 8.2.2): yellow=business, light blue/turquoise=application,
# light green=technology. Motivation and Strategy use the same lavender/orange
# convention most ArchiMate tooling (e.g. Archi) defaults to. These are close
# approximations of that convention, not an official hex palette, since the
# spec itself doesn't mandate exact hex values.
ARCHIMATE_LAYERS = {
    "motivation":  {"fill": "#E6D9F2", "edge": "#8E6FB0"},
    "strategy":    {"fill": "#FFE1C2", "edge": "#C97A2E"},
    "business":    {"fill": "#FFFDB0", "edge": "#B8A600"},
    "application": {"fill": "#CFE8FA", "edge": "#2E7DA6"},
    "technology":  {"fill": "#D3F2D0", "edge": "#4C9A4C"},
    "physical":    {"fill": "#D3F2D0", "edge": "#4C9A4C"},
    "implementation": {"fill": "#FBD7DA", "edge": "#B23A4A"},
}

# Relationship notation (Cookbook sec. 4 / ArchiMate spec fig. 61):
#   composition   - filled diamond at the "whole" end, solid line
#   aggregation   - hollow diamond at the "whole" end, solid line
#   assignment    - filled ball at the "doer" end, solid line, arrowhead at target
#   realization   - hollow triangle at target, DASHED line
#   serving       - open (line-only) arrowhead at target, solid line
#   access        - small open arrowhead at target, DOTTED line
#   flow          - filled arrowhead at target, DASHED line
#   triggering    - filled arrowhead at target, solid line
#   specialization- hollow triangle at target, solid line
#   association   - plain line, no arrowhead
ARCHIMATE_RELATIONSHIPS = {
    "composition":    {"line": "solid",  "start": "diamond_filled", "end": None},
    "aggregation":    {"line": "solid",  "start": "diamond_hollow", "end": None},
    "assignment":     {"line": "solid",  "start": "ball_filled",    "end": "arrow_open"},
    "realization":    {"line": "dashed", "start": None, "end": "triangle_hollow"},
    "serving":        {"line": "solid",  "start": None, "end": "arrow_open"},
    "access":         {"line": "dotted", "start": None, "end": "arrow_small_open"},
    "flow":           {"line": "dashed", "start": None, "end": "arrow_filled"},
    "triggering":     {"line": "solid",  "start": None, "end": "arrow_filled"},
    "specialization": {"line": "solid",  "start": None, "end": "triangle_hollow"},
    "association":    {"line": "solid",  "start": None, "end": None},
}


def _unit(p1, p2):
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    d = (dx ** 2 + dy ** 2) ** 0.5 or 1.0
    return dx / d, dy / d


class Canvas:
    """A matplotlib axes sized exactly to your content, with a fixed margin."""

    def __init__(self, width, height, margin=0.35, dpi=200):
        self.width, self.height, self.margin = width, height, margin
        self.fig, self.ax = plt.subplots(
            figsize=(width + margin * 2, height + margin * 2), dpi=dpi
        )
        self.ax.set_xlim(-margin, width + margin)
        self.ax.set_ylim(-margin, height + margin)
        self.ax.set_aspect("equal")
        self.ax.axis("off")
        # (x0, y0, x1, y1, label) for every node()/archimate_element() box, used by
        # check_overlaps() to catch two boxes silently landing on top of each other
        # (e.g. a loop that draws a box the caller also draws separately) — a defect
        # that sits entirely inside the canvas, so the edge-clipping check can't see it.
        self._boxes = []

    def _text_width(self, s, fontsize, weight="bold"):
        """Actual rendered width of `s` at `fontsize`, in data units (== inches here)."""
        txt = self.ax.text(0, 0, s, fontsize=fontsize, fontweight=weight, alpha=0)
        self.fig.canvas.draw()
        bbox = txt.get_window_extent(renderer=self.fig.canvas.get_renderer())
        inv = self.ax.transData.inverted()
        (x0, _), (x1, _) = inv.transform(bbox)
        txt.remove()
        return x1 - x0

    def _break_long_word(self, word, width, size, weight):
        """Hard-break a single token that's too wide to fit even alone,
        one character at a time. Rare in practice (short labels are the norm
        for this kit), but without this a single long unbroken word — no
        spaces to wrap on — silently overflows the box just like the
        original bug this method exists to prevent."""
        chunks, cur = [], ""
        for ch in word:
            trial = cur + ch
            if not cur or self._text_width(trial, size, weight) <= width:
                cur = trial
            else:
                chunks.append(cur)
                cur = ch
        if cur:
            chunks.append(cur)
        return chunks

    def _fit_label(self, text, width, height, fontsize, min_fontsize=6.5, weight="bold"):
        """
        Wrap `text` to fit within `width`, shrinking fontsize if it still doesn't
        fit `height` after wrapping. Returns (wrapped_text, fontsize). Uses actual
        renderer measurements rather than a character-count estimate, so it's
        exact regardless of font/weight — no calibration to keep in sync.

        This exists because matplotlib's `wrap=True` text kwarg only wraps at the
        *figure* boundary, not at any given width — it does nothing useful for text
        inside a specific box, and long labels will silently render past their box
        edges with no warning otherwise.

        Existing manual line breaks in `text` are preserved rather than re-flowed:
        each pre-existing line is greedily word-wrapped independently (only
        splitting a line further if it doesn't already fit), so a caller-supplied
        break like "Orchestrator-\\nworkers" is left alone if both halves already fit.

        A single word with no spaces (so nothing to wrap on) is hard-broken at
        the character level if it's still too wide alone — this is the same
        overflow failure mode in miniature, and skipping it here would just
        reintroduce the bug for that one case.
        """
        size = fontsize
        for _ in range(12):
            out_lines = []
            for line in text.split("\n"):
                if self._text_width(line, size, weight) <= width:
                    out_lines.append(line)
                    continue
                cur = ""
                for word in line.split(" "):
                    tokens = ([word] if self._text_width(word, size, weight) <= width
                              else self._break_long_word(word, width, size, weight))
                    for tok in tokens:
                        trial = f"{cur} {tok}".strip()
                        if not cur or self._text_width(trial, size, weight) <= width:
                            cur = trial
                        else:
                            out_lines.append(cur)
                            cur = tok
                if cur:
                    out_lines.append(cur)
            wrapped = "\n".join(out_lines)
            n_lines = len(out_lines)
            line_height = size / 72 * 1.25
            if n_lines * line_height <= height * 0.82 or size <= min_fontsize:
                return wrapped, size
            size = max(min_fontsize, size - 0.5)
        return wrapped, size

    def node(self, cx, cy, w, h, title, subtitle=None, edge=PRIMARY, fill=WHITE,
             lw=1.5, badge=None, badge_color=None, title_size=FONT_TITLE, sub_size=FONT_SUB):
        box = FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                              boxstyle="round,pad=0.02,rounding_size=0.055",
                              linewidth=lw, edgecolor=edge, facecolor=fill, zorder=3)
        self.ax.add_patch(box)
        avail_h = h * (0.62 if subtitle else 0.8)
        wrapped_title, fitted_size = self._fit_label(title, w * 0.88, avail_h, title_size)
        ty = cy + (h * 0.16 if subtitle else 0)
        self.ax.text(cx, ty, wrapped_title, ha="center", va="center", fontsize=fitted_size,
                     color=INK, fontweight="bold", zorder=4)
        if subtitle:
            wrapped_sub, sub_fitted = self._fit_label(subtitle, w * 0.88, h * 0.28, sub_size)
            self.ax.text(cx, cy - h * 0.24, wrapped_sub, ha="center", va="center",
                         fontsize=sub_fitted, color=MUTED, style="italic", zorder=4)
        if badge is not None:
            bc = badge_color or edge
            self.ax.text(cx - w / 2 + 0.14, cy + h / 2 - 0.14, str(badge),
                         ha="center", va="center", fontsize=7.6, color=WHITE,
                         fontweight="bold", zorder=5,
                         bbox=dict(boxstyle="circle,pad=0.22", facecolor=bc, edgecolor="none"))
        self._boxes.append((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, title))
        return box

    def band(self, x0, y0, w, h, label=None, edge=HAIRLINE, fill=FAINT, label_color=None, lw=1.2):
        b = FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.09",
                            linewidth=lw, edgecolor=edge, facecolor=fill, zorder=1)
        self.ax.add_patch(b)
        if label:
            self.ax.text(x0 + w / 2, y0 + h + 0.14, label, ha="center", va="bottom",
                         fontsize=FONT_SUB + 0.4, color=label_color or PRIMARY, fontweight="bold")
        return b

    def arrow(self, p1, p2, color=MUTED, rad=0.0, lw=1.2, style="-|>", zorder=2):
        self.ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=10,
                                           color=color, linewidth=lw, zorder=zorder,
                                           connectionstyle=f"arc3,rad={rad}"))

    def dashed_circle(self, cx, cy, r, color=HAIRLINE, lw=1.3):
        c = Circle((cx, cy), r, facecolor="none", edgecolor=color, linewidth=lw,
                   linestyle=(0, (5, 3)), zorder=1)
        self.ax.add_patch(c)
        return c

    def text(self, x, y, s, size=FONT_LABEL, color=MUTED, weight="normal", style="normal",
             ha="center", va="center", boxed=False, zorder=4):
        kwargs = dict(ha=ha, va=va, fontsize=size, color=color, fontweight=weight,
                      style=style, zorder=zorder)
        if boxed:
            kwargs["bbox"] = dict(boxstyle="round,pad=0.28", facecolor=WHITE,
                                   edgecolor=HAIRLINE, linewidth=0.8)
        self.ax.text(x, y, s, **kwargs)

    # ---------------- ArchiMate notation ----------------

    def archimate_element(self, cx, cy, w, h, label, layer="application", kind="active",
                           title_size=9.0, lw=1.4):
        """
        An ArchiMate element box, colored by layer and shaped/iconed by kind.
        layer: motivation | strategy | business | application | technology | physical | implementation
        kind:  active | behavior | service | object | component | node
          - active:    plain box, small square icon (actor/role/device/etc.)
          - behavior:  plain box, small chevron icon (process/function/event)
          - service:   pill/very-rounded box (business/application/technology service)
          - object:    plain box, small "document" icon (business object/data object/artifact)
          - component: plain box with two small tabs on the left edge (UML-style component)
          - node:      plain box with a small stacked-box icon (technology node)
        """
        if layer not in ARCHIMATE_LAYERS:
            raise ValueError(f'Unknown ArchiMate layer "{layer}". '
                              f'Valid: {", ".join(ARCHIMATE_LAYERS)}')
        valid_kinds = ("active", "behavior", "service", "object", "component", "node")
        if kind not in valid_kinds:
            raise ValueError(f'Unknown ArchiMate kind "{kind}". Valid: {", ".join(valid_kinds)}')
        colors = ARCHIMATE_LAYERS[layer]
        fill, edge = colors["fill"], colors["edge"]
        rounding = 0.5 if kind == "service" else 0.05
        box = FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                              boxstyle=f"round,pad=0.02,rounding_size={rounding}",
                              linewidth=lw, edgecolor=edge, facecolor=fill, zorder=3)
        self.ax.add_patch(box)
        wrapped_label, fitted_size = self._fit_label(label, w * 0.86, h * 0.7, title_size)
        self.ax.text(cx, cy, wrapped_label, ha="center", va="center", fontsize=fitted_size,
                     color=INK, fontweight="bold", zorder=4)

        ix, iy = cx + w / 2 - 0.16, cy + h / 2 - 0.13  # icon anchor, top-right corner
        if kind == "active":
            self.ax.add_patch(plt.Rectangle((ix - 0.09, iy - 0.07), 0.18, 0.14,
                               fill=False, edgecolor=edge, linewidth=1.0, zorder=5))
        elif kind == "behavior":
            self.ax.annotate("", xy=(ix + 0.09, iy), xytext=(ix - 0.09, iy),
                             arrowprops=dict(arrowstyle="-|>", color=edge, lw=1.1,
                                             shrinkA=0, shrinkB=0), zorder=5)
        elif kind == "object":
            self.ax.add_patch(plt.Rectangle((ix - 0.09, iy - 0.07), 0.18, 0.14,
                               fill=False, edgecolor=edge, linewidth=1.0, zorder=5))
            self.ax.plot([ix - 0.09, ix + 0.09], [iy, iy], color=edge, linewidth=0.9, zorder=5)
        elif kind == "component":
            for off in (0.16, -0.02):
                self.ax.add_patch(plt.Rectangle((cx - w / 2 - 0.05, cy + off), 0.1, 0.09,
                                   facecolor=WHITE, edgecolor=edge, linewidth=1.0, zorder=5))
        elif kind == "node":
            self.ax.add_patch(plt.Rectangle((ix - 0.1, iy - 0.09), 0.16, 0.13,
                               fill=True, facecolor=fill, edgecolor=edge, linewidth=1.0, zorder=5))
            self.ax.add_patch(plt.Rectangle((ix - 0.06, iy - 0.05), 0.16, 0.13,
                               fill=True, facecolor=fill, edgecolor=edge, linewidth=1.0, zorder=6))
        self._boxes.append((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, label))
        return box

    def archimate_relationship(self, p1, p2, kind="association", rad=0.0, color=None, lw=1.3):
        """
        One of the ArchiMate relationship types (see ARCHIMATE_RELATIONSHIPS):
        composition, aggregation, assignment, realization, serving, access,
        flow, triggering, specialization, association.
        """
        if kind not in ARCHIMATE_RELATIONSHIPS:
            raise ValueError(f'Unknown ArchiMate relationship "{kind}". '
                              f'Valid: {", ".join(ARCHIMATE_RELATIONSHIPS)}')
        spec = ARCHIMATE_RELATIONSHIPS[kind]
        c = color or PRIMARY
        linestyle = {"solid": "-", "dashed": (0, (5, 3)), "dotted": (0, (1, 2.2))}[spec["line"]]

        # main line (curved via a bezier-ish quadratic through a control point if rad != 0)
        if rad == 0:
            self.ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=c, linewidth=lw,
                        linestyle=linestyle, zorder=2, solid_capstyle="round")
            line_p1, line_p2 = p1, p2
        else:
            self.ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-", linewidth=lw,
                               color=c, linestyle=linestyle, zorder=2,
                               connectionstyle=f"arc3,rad={rad}"))
            line_p1, line_p2 = p1, p2  # marker orientation approximated on the straight chord

        ux, uy = _unit(line_p1, line_p2)
        size = 0.13
        if spec["end"] == "arrow_open":
            self.ax.annotate("", xy=p2, xytext=(p2[0] - ux * 0.22, p2[1] - uy * 0.22),
                             arrowprops=dict(arrowstyle="-|>", color=c, lw=lw,
                                             mutation_scale=12, shrinkA=0, shrinkB=0), zorder=3)
        elif spec["end"] == "arrow_small_open":
            self.ax.annotate("", xy=p2, xytext=(p2[0] - ux * 0.16, p2[1] - uy * 0.16),
                             arrowprops=dict(arrowstyle="->", color=c, lw=lw,
                                             mutation_scale=8, shrinkA=0, shrinkB=0), zorder=3)
        elif spec["end"] == "arrow_filled":
            self.ax.annotate("", xy=p2, xytext=(p2[0] - ux * 0.22, p2[1] - uy * 0.22),
                             arrowprops=dict(arrowstyle="-|>", color=c, lw=lw,
                                             mutation_scale=12, shrinkA=0, shrinkB=0), zorder=3)
        elif spec["end"] in ("triangle_hollow",):
            self._triangle(p2, (ux, uy), size, filled=False, color=c)

        if spec["start"] == "diamond_filled":
            self._diamond(p1, (ux, uy), size, filled=True, color=c)
        elif spec["start"] == "diamond_hollow":
            self._diamond(p1, (ux, uy), size, filled=False, color=c)
        elif spec["start"] == "ball_filled":
            self.ax.add_patch(Circle(p1, size * 0.32, facecolor=c, edgecolor=c, zorder=4))

    def _diamond(self, tip, direction, size, filled, color):
        ux, uy = direction
        px, py = -uy, ux  # perpendicular
        back = (tip[0] + ux * size * 1.6, tip[1] + uy * size * 1.6)
        mid = (tip[0] + ux * size * 0.8, tip[1] + uy * size * 0.8)
        pts = [tip,
               (mid[0] + px * size * 0.5, mid[1] + py * size * 0.5),
               back,
               (mid[0] - px * size * 0.5, mid[1] - py * size * 0.5)]
        poly = plt.Polygon(pts, closed=True, facecolor=(color if filled else WHITE),
                           edgecolor=color, linewidth=1.2, zorder=4)
        self.ax.add_patch(poly)

    def _triangle(self, tip, direction, size, filled, color):
        ux, uy = direction
        px, py = -uy, ux
        back = (tip[0] + ux * size * 1.7, tip[1] + uy * size * 1.7)
        pts = [tip,
               (back[0] + px * size * 0.55, back[1] + py * size * 0.55),
               (back[0] - px * size * 0.55, back[1] - py * size * 0.55)]
        poly = plt.Polygon(pts, closed=True, facecolor=(color if filled else WHITE),
                           edgecolor=color, linewidth=1.2, zorder=4)
        self.ax.add_patch(poly)

    def archimate_legend(self, x, y, layers=("business", "application", "technology"), size=0.22):
        """A small color-key strip for the layers used, per the Cookbook's own
        recommendation (sec. 8.2.2) to make layer-color meaning explicit."""
        for i, layer in enumerate(layers):
            if layer not in ARCHIMATE_LAYERS:
                raise ValueError(f'Unknown ArchiMate layer "{layer}". '
                                  f'Valid: {", ".join(ARCHIMATE_LAYERS)}')
            colors = ARCHIMATE_LAYERS[layer]
            lx = x + i * 1.5
            self.ax.add_patch(plt.Rectangle((lx, y), size, size, facecolor=colors["fill"],
                               edgecolor=colors["edge"], linewidth=1.1, zorder=4))
            self.ax.text(lx + size + 0.08, y + size / 2, layer.capitalize(), ha="left",
                        va="center", fontsize=FONT_SUB, color=MUTED, zorder=4)

    def check_overlaps(self, tol=0.06):
        """Return [(label_a, label_b, overlap_fraction), ...] for any two node/element
        boxes that overlap by more than `tol` of the smaller box's area. `tol` is a
        small nonzero default so two boxes that merely share a hairline edge (by design)
        don't false-positive — this is for genuine overlap, like two boxes stacked on
        top of each other."""
        problems = []
        boxes = self._boxes
        for i in range(len(boxes)):
            ax0, ay0, ax1, ay1, al = boxes[i]
            for j in range(i + 1, len(boxes)):
                bx0, by0, bx1, by1, bl = boxes[j]
                iw = max(0.0, min(ax1, bx1) - max(ax0, bx0))
                ih = max(0.0, min(ay1, by1) - max(ay0, by0))
                if iw <= 0 or ih <= 0:
                    continue
                area_a = (ax1 - ax0) * (ay1 - ay0)
                area_b = (bx1 - bx0) * (by1 - by0)
                frac = (iw * ih) / max(1e-9, min(area_a, area_b))
                if frac > tol:
                    problems.append((al, bl, frac))
        return problems

    def save(self, path, pad_inches=0.12):
        overlaps = self.check_overlaps()
        if overlaps:
            detail = "; ".join(f'"{a}" \u00d7 "{b}" ({f:.0%} overlap)' for a, b, f in overlaps)
            raise ValueError(
                f"diagram_kit: refusing to save \u2014 overlapping boxes detected: {detail}. "
                "This is usually a loop drawing a box that's also drawn separately elsewhere "
                "(the same bug class as the original six-patterns example: a loop iterated "
                "over all items instead of stopping before the one drawn on its own). Fix the "
                "node positions or loop range \u2014 don't suppress this check, it exists because "
                "the edge-clipping check alone missed exactly this defect in production."
            )
        plt.figure(self.fig.number)
        plt.savefig(path, dpi=self.fig.dpi, facecolor="white", bbox_inches="tight",
                    pad_inches=pad_inches)
        plt.close(self.fig)
