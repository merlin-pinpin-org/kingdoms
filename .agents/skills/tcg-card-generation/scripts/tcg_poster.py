#!/usr/bin/env python3
"""Compose a parchment-style rules poster: art texture + real vector text.

Reusability
-----------
The poster is a *background texture* (image model, no text) plus text
drawn by this script with a real vector font — never by the image model
(see the tcg-card-generation skill for the rationale). All content comes
from a JSON file, so the same script renders any two-column rule sheet.

Data format (``--data rules.json``)::

    {
      "texture": "parchemin.jpg",
      "title": "LES RÈGLES DU ROYAUME",
      "subtitle": "Mod Kingdoms — Saison II",
      "footer": "— Tel qu'il est écrit, ainsi soit-il joué —",
      "source_line": "Source : docs/MODS/kingdoms — Mod Kingdoms",
      "columns": 2,
      "sections": [
        {"head": "Les Territoires",
         "body": "Chaque territoire est une map AoE2. ..."}
      ]
    }

Sections are distributed over the columns in order. ``body`` supports
``\\n`` paragraph breaks. The layout auto-fits: font sizes shrink until
both columns end above the footer zone; the script exits non-zero
(fail-closed) when the content cannot fit at the minimum size.

Layout guards (learned from failed attempts — keep them)
--------------------------------------------------------
- Wide inner margins (MARGX = 235 px at 1400 px wide): the generated
  texture has an ornate border; text must stay clear of it.
- Dark ink on light parchment, bold + stroke for the title: plain brown
  on the textured background fails OCR.

Usage
-----
    python tcg_poster.py --data rules.json --out regles_parchemin.jpg

Dependencies: Pillow, DejaVu Serif (same font discovery as tcg_compose).
"""
from __future__ import annotations

import argparse
import json
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageEnhance, ImageFont
except ImportError:
    sys.exit("Pillow is required: pip install pillow")

W, H = 1400, 2050          # poster canvas
MARGX = 235                # inner margin: clear of the ornate border
GUTTER = 70                # gap between columns
YTOP = 310                 # first section baseline
YBOTTOM = 1750             # content must end above this
INK = (62, 42, 22)
INK_DARK = (40, 26, 12)
FADE = (94, 66, 34)
STROKE = (235, 224, 196)

MIN_BODY, MIN_HEAD, MIN_LH = 20, 26, 30  # fail-closed floor


def load_fonts(font_dir: str | None = None) -> dict:
    candidates = []
    if font_dir:
        candidates.append(font_dir)
    try:
        import matplotlib

        candidates.append(
            os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")
        )
    except ImportError:
        pass
    candidates += [
        os.path.expanduser("~/.local/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf"),
        "/usr/share/fonts/truetype/dejavu",
    ]
    for d in candidates:
        if os.path.isfile(os.path.join(d, "DejaVuSerif-Bold.ttf")):
            return {
                "b": os.path.join(d, "DejaVuSerif-Bold.ttf"),
                "r": os.path.join(d, "DejaVuSerif.ttf"),
                "i": os.path.join(d, "DejaVuSerif-Italic.ttf"),
            }
    sys.exit("DejaVu Serif fonts not found")


def wrap(draw, text: str, font, maxw: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def measure_column(draw, sections, fonts, colw):
    """Total height of a column at current sizes; returns per-paragraph
    line lists so the caller does not recompute."""
    body_f, head_f, lh = fonts["body"], fonts["head"], fonts["lh"]
    heights = []
    for sec in sections:
        paragraphs = [wrap(draw, para, body_f, colw) or [""] for para in sec["body"].split("\n")]
        h = 0
        for pl in paragraphs:
            h += len(pl) * lh
        h += len(paragraphs) * 6          # inter-paragraph gap
        h += head_f.size + 16 + 30        # heading + heading gap + section gap
        heights.append((sec, paragraphs, h))
    return heights


def render(data: dict, out: str, font_dir: str | None) -> None:
    f = load_fonts(font_dir)
    tex = Image.open(data["texture"]).convert("RGB")
    img = ImageEnhance.Brightness(tex.resize((W, H))).enhance(1.08)
    # Flatten the ornate texture behind the title and footer zones so the
    # vector text stays high-contrast and OCR-verified (parchment tint,
    # 60% opacity: keeps the aged look, kills the background noise).
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle([W//2 - 560, 60, W//2 + 560, 250], fill=(240, 228, 200, 155))
    od.rounded_rectangle([W//2 - 540, 1860, W//2 + 540, 1995], radius=20, fill=(240, 228, 200, 155))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    d = ImageDraw.Draw(img)

    d.text((W // 2, 130), data["title"], font=ImageFont.truetype(f["b"], 68),
           fill=INK_DARK, anchor="mm", stroke_width=2, stroke_fill=STROKE)
    d.text((W // 2, 205), data["subtitle"], font=ImageFont.truetype(f["b"], 34),
           fill=(45, 30, 14), anchor="mm")
    d.line([(W // 2 - 260, 250), (W // 2 + 260, 250)], fill=FADE, width=3)

    ncols = data.get("columns", 2)
    colw = (W - 2 * MARGX - (ncols - 1) * GUTTER) // ncols
    sections = data["sections"]
    per_col = (len(sections) + ncols - 1) // ncols
    cols = [sections[i * per_col:(i + 1) * per_col] for i in range(ncols)]

    # Auto-fit: shrink until every column fits above YBOTTOM.
    body_size, head_size, lh = 23, 30, 35
    while body_size >= MIN_BODY:
        fonts = {
            "body": ImageFont.truetype(f["r"], body_size),
            "head": ImageFont.truetype(f["b"], head_size),
            "lh": lh,
        }
        laid = [measure_column(d, col, fonts, colw) for col in cols]
        tops = [YTOP + sum(h for _, _, h in c) for c in laid]
        if all(t <= YBOTTOM for t in tops):
            break
        body_size -= 1
        head_size = max(MIN_HEAD, head_size - 1)
        lh = max(MIN_LH, lh - 1)
    else:
        sys.exit("poster: content does not fit at minimum font size — split sections")

    xs = [MARGX + i * (colw + GUTTER) for i in range(ncols)]
    for x, laid in zip(xs, laid):
        y = YTOP
        for sec, paragraphs, _ in laid:
            d.text((x, y), sec["head"], font=fonts["head"], fill=INK)
            y += fonts["head"].size + 16
            for pl in paragraphs:
                for ln in pl:
                    d.text((x, y), ln, font=fonts["body"], fill=INK)
                    y += fonts["lh"]
                y += 6
            y += 30

    d.text((W // 2, 1900), data.get("footer", ""), font=ImageFont.truetype(f["i"], 30),
           fill=INK_DARK, anchor="mm")
    d.text((W // 2, 1960), data.get("source_line", ""), font=ImageFont.truetype(f["r"], 26),
           fill=INK_DARK, anchor="mm")
    img.save(out, quality=93)
    print("ok", out)


def main() -> None:
    p = argparse.ArgumentParser(description="Parchment-style rules poster composer")
    p.add_argument("--data", required=True, help="JSON content file (schema in module docstring)")
    p.add_argument("--out", required=True, help="output JPEG path")
    p.add_argument("--font-dir", default=None, help="DejaVu Serif directory (auto-detected)")
    args = p.parse_args()
    with open(args.data, encoding="utf-8") as fh:
        render(json.load(fh), args.out, args.font_dir)


if __name__ == "__main__":
    main()
