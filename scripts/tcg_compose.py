#!/usr/bin/env python3
"""Compose Kingdoms TCG cards and parchment posters.

Cards and posters are drawn from JSON data files; the image model only
ever provides the art (never text — see .agents/skills/tcg-card-generation).

Usage:
  python scripts/tcg_compose.py cards --data data.json --outdir out/
  python scripts/tcg_compose.py sheet --data data.json --outdir out/
"""
import argparse
import json
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Pillow is required: pip install pillow")


def load_fonts():
    candidates = [
        os.path.expanduser(
            "~/.local/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf"
        ),
        "/usr/share/fonts/truetype/dejavu",
    ]
    import matplotlib

    candidates.insert(
        0, os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")
    )
    for d in candidates:
        if os.path.isfile(os.path.join(d, "DejaVuSerif-Bold.ttf")):
            return {
                "b": os.path.join(d, "DejaVuSerif-Bold.ttf"),
                "r": os.path.join(d, "DejaVuSerif.ttf"),
                "i": os.path.join(d, "DejaVuSerif-Italic.ttf"),
            }
    sys.exit("DejaVu Serif fonts not found (see SKILL.md, Fonts section)")


FONTS = load_fonts()
CW, CH = 744, 1032

KINDS = {
    "technology": {
        "bg": (40, 32, 22), "band": (52, 40, 24), "gold": (176, 141, 74),
        "gold2": (120, 96, 52), "text_light": (238, 220, 168),
        "subtitle": (205, 180, 130), "box": (238, 226, 196),
        "ink": (40, 30, 16), "badge": (176, 44, 32), "badge_ring": (218, 193, 121),
        "badge_txt": (255, 240, 210), "footer": (52, 40, 24),
        "footer_txt": (205, 180, 130),
    },
    "territory": {
        "bg": (30, 38, 26), "band": (34, 48, 30), "gold": (92, 138, 78),
        "gold2": (66, 96, 58), "text_light": (224, 238, 210),
        "subtitle": (200, 216, 190), "box": (238, 232, 208),
        "ink": (30, 40, 22), "badge": (52, 92, 44), "badge_ring": (224, 238, 210),
        "badge_txt": (240, 250, 235), "footer": (34, 48, 30),
        "footer_txt": (200, 216, 190),
    },
    "civilization": {
        "bg": (26, 34, 52), "band": (30, 42, 66), "gold": (176, 141, 74),
        "gold2": (110, 96, 60), "text_light": (224, 232, 248),
        "subtitle": (190, 200, 224), "box": (232, 228, 208),
        "ink": (28, 32, 44), "badge": (44, 76, 132), "badge_ring": (218, 193, 121),
        "badge_txt": (240, 244, 255), "footer": (30, 42, 66),
        "footer_txt": (190, 200, 224),
    },
}


def wrap(draw, text, font, maxw):
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


def font(path, size):
    return ImageFont.truetype(path, size)


def make_card(pal, art_path, name, subtitle, body, extra, cost_label, index, total):
    c = Image.new("RGB", (CW, CH), pal["bg"])
    d = ImageDraw.Draw(c)
    d.rectangle([0, 0, CW - 1, CH - 1], outline=pal["gold"], width=10)
    d.rectangle([16, 16, CW - 17, CH - 17], outline=pal["gold2"], width=3)
    d.rectangle([26, 26, CW - 27, 100], fill=pal["band"], outline=pal["gold"], width=3)
    nf = font(FONTS["b"], 48 if len(name) <= 12 else 40)
    d.text((60, 63), name, font=nf, fill=pal["text_light"], anchor="lm")

    r = 40
    cx, cy = CW - 76, 63
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=pal["badge"], outline=pal["badge_ring"], width=4)
    cf = font(FONTS["b"], 48 if len(cost_label) <= 2 else 30)
    d.text((cx, cy), cost_label, font=cf, fill=pal["badge_txt"], anchor="mm")

    art = Image.open(art_path).convert("RGB")
    aw, ah = CW - 88, 460
    c.paste(art.resize((aw, ah)), (44, 112))
    d.rectangle([44, 112, 44 + aw - 1, 112 + ah - 1], outline=pal["gold2"], width=3)

    tl = font(FONTS["i"], 28)
    d.text((CW // 2, 600), subtitle, font=tl, fill=pal["subtitle"], anchor="mm")
    d.line([60, 624, CW - 60, 624], fill=pal["gold2"], width=2)

    box_top, box_bottom = 640, CH - 80
    if extra:
        box_bottom = 830
    d.rounded_rectangle([36, box_top, CW - 37, box_bottom], radius=14, fill=pal["box"], outline=pal["gold2"], width=3)
    rf = font(FONTS["r"], 30 if len(body) <= 120 else 27)
    line_h = 44 if rf.size == 30 else 40
    lines = wrap(d, body, rf, CW - 160)
    y = (box_top + box_bottom) // 2 - (len(lines) * line_h) // 2
    for ln in lines:
        d.text((60, y), ln, font=rf, fill=pal["ink"])
        y += line_h

    if extra:
        d.rounded_rectangle([36, 846, CW - 37, CH - 80], radius=14, fill=pal["band"], outline=pal["gold"], width=3)
        lab = font(FONTS["r"], 26)
        d.text((CW // 2, 876), extra["label"], font=lab, fill=pal["subtitle"], anchor="mm")
        val = font(FONTS["b"], 32)
        d.text((CW // 2, 922), extra["value"], font=val, fill=pal["text_light"], anchor="mm")

    d.rectangle([26, CH - 66, CW - 27, CH - 27], fill=pal["footer"], outline=pal["gold"], width=3)
    ff = font(FONTS["r"], 24)
    d.text((48, CH - 46), f"{index}/{total}", font=ff, fill=pal["footer_txt"], anchor="lm")
    d.text((CW - 48, CH - 46), "Mod Kingdoms", font=ff, fill=pal["footer_txt"], anchor="rm")
    return c


def compose_cards(data, outdir):
    kind = data.get("kind", "technology")
    if kind not in KINDS:
        sys.exit(f"unknown kind: {kind}")
    pal = KINDS[kind]
    cards = data["cards"]
    total = len(cards)
    os.makedirs(outdir, exist_ok=True)
    for i, card in enumerate(cards, 1):
        extra = None
        if card.get("extra_label"):
            extra = {"label": card["extra_label"], "value": card["extra_value"]}
        img = make_card(
            pal,
            card["art"],
            card["name"],
            card.get("subtitle", "Action spéciale — Technologie"),
            card["rule"],
            extra,
            str(card.get("cost", "")),
            i,
            total,
        )
        slug = card['name'].lower().replace(' ', '-').replace('\u2019', '')
        path = os.path.join(outdir, card.get("filename", f"{i:02d}_{slug}.jpg"))
        img.save(path, quality=95)
        print("ok", path)


def compose_sheet(data, outdir):
    kind = data.get("kind", "technology")
    pal = KINDS[kind]
    cards = data["cards"]
    cols = 5
    rows = (len(cards) + cols - 1) // cols
    margin, gapx, gapy = 28, 24, 24
    small_w, small_h = 488, int(488 * CH / CW)  # keep card aspect ratio
    W = margin * 2 + cols * small_w + (cols - 1) * gapx
    H = 60 + margin * 2 + rows * small_h + (rows - 1) * gapy
    sheet = Image.new("RGB", (W, H), (24, 20, 16))
    d = ImageDraw.Draw(sheet)
    title = font(FONTS["b"], 44)
    d.text((W // 2, 30), data.get("sheet_title", "KINGDOMS"), font=title, fill=(218, 193, 121), anchor="mm")
    for i, card in enumerate(cards):
        full = make_card(
            pal, card["art"], card["name"],
            card.get("subtitle", "Action spéciale — Technologie"),
            card["rule"], None, str(card.get("cost", "")), i + 1, len(cards),
        )
        small = full.resize((small_w, small_h))
        r, col = divmod(i, cols)
        x = margin + col * (small_w + gapx)
        y = 60 + margin + r * (small_h + gapy)
        sheet.paste(small, (x, y))
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, data.get("sheet_filename", "planche.jpg"))
    sheet.save(path, quality=92)
    print("ok", path)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("command", choices=["cards", "sheet"])
    p.add_argument("--data", required=True)
    p.add_argument("--outdir", required=True)
    args = p.parse_args()
    with open(args.data, encoding="utf-8") as f:
        data = json.load(f)
    if args.command == "cards":
        compose_cards(data, args.outdir)
    else:
        compose_sheet(data, args.outdir)


if __name__ == "__main__":
    main()
