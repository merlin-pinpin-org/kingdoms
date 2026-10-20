#!/usr/bin/env python3
"""Render the Kingdoms mod visuals with the visual-generator library.

Source of truth: the JSON files under ``docs/visuals/deck/data/`` and
``docs/visuals/data/`` (names, rules, costs, art paths). Rendering and
validation are delegated to the visual-generator library — installed
in the uv environment (``uv sync --group visuals`` then ``uv run …``,
see pyproject.toml and the library's agent skill for the full
pipeline). This driver only maps the Kingdoms data onto the library's
JSON visual schema and invokes it.

Usage::

    uv run python scripts/visuals_render.py [--only technologies|territoires|regles|match]...

Art lives in ``docs/visuals/deck/assets/``; rendered outputs land in
``docs/visuals/deck/technologies|territoires/``, ``docs/visuals/deck/`` and
``docs/visuals/``.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KIND_PALETTE = {
    "technology": {
        "bg": "#282016", "band": "#342818", "gold": "#b08d4a",
        "gold2": "#786034", "text_light": "#eedca8", "subtitle": "#cdb482",
        "box": "#eee2c4", "ink": "#281e10", "badge": "#b02c20",
        "badge_ring": "#dac179", "badge_txt": "#fff0d2", "footer": "#342818",
        "footer_txt": "#cdb482",
    },
    "territory": {
        "bg": "#1e261a", "band": "#22301e", "gold": "#5c8a4e",
        "gold2": "#42603a", "text_light": "#e0eed2", "subtitle": "#c8d8be",
        "box": "#eee8d0", "ink": "#1e2816", "badge": "#345c2c",
        "badge_ring": "#e0eed2", "badge_txt": "#f0faeb", "footer": "#22301e",
        "footer_txt": "#c8d8be",
    },
    "civilization": {
        "bg": "#1a2234", "band": "#1e2a42", "gold": "#b08d4a",
        "gold2": "#6e6044", "text_light": "#e0e8f8", "subtitle": "#bec8e0",
        "box": "#e8e4d0", "ink": "#1c202c", "badge": "#2c4c84",
        "badge_ring": "#dac179", "badge_txt": "#f0f4ff", "footer": "#1e2a42",
        "footer_txt": "#bec8e0",
    },
}

DEFAULT_SUBTITLE = {
    "technology": "Action spéciale — Technologie",
    "territory": "Territoire",
    "civilization": "Civilisation",
}

OUTDIR = {
    "technology": "technologies",
    "territory": "territoires",
    "civilization": "civilizations",
}


def run(cmd):
    print("+", " ".join(str(c) for c in cmd))
    r = subprocess.run(cmd, cwd=REPO)
    if r.returncode != 0:
        sys.exit(r.returncode)


def card_visual(kind, card, index, total):
    pal = KIND_PALETTE[kind]
    sec = {
        "name": card["name"],
        "cost": card.get("cost", ""),
        "art": os.path.join("docs/visuals/deck/assets", os.path.basename(card["art"])),
        "type_line": card.get("subtitle", DEFAULT_SUBTITLE[kind]),
        "rule": card["rule"],
        "footer_left": f"{index}/{total}",
        "footer_right": "Mod Kingdoms",
    }
    if card.get("extra_label"):
        sec["extra_label"] = card["extra_label"]
        sec["extra_value"] = card["extra_value"]
    return {
        "template": "card_tcg",
        "output": os.path.join("docs/visuals/deck", OUTDIR[kind], card["filename"]),
        "palette": pal,
        "canvas": {"width": 744, "height": 1032},
        "sections": sec,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--only", choices=["technologies", "territoires", "regles", "match"],
                   action="append",
                   help="render only this group (repeatable)")
    args = p.parse_args()
    wanted = args.only or ["technologies", "territoires", "regles", "match"]

    jobs = []

    if "technologies" in wanted or "territoires" in wanted:
        for group in ("technologies", "territoires"):
            if group not in wanted:
                continue
            data = json.load(open(os.path.join(REPO, "docs/visuals/deck/data", f"{group}.json"), encoding="utf-8"))
            kind = data["kind"]
            cards = data["cards"]
            total = len(cards)
            visuals = [card_visual(kind, c, i, total) for i, c in enumerate(cards, 1)]
            sheet = {
                "template": "contact_sheet",
                "output": os.path.join("docs/visuals/deck", OUTDIR[kind], data["sheet_filename"]),
                "sections": {
                    "title": data.get("sheet_title", "KINGDOMS"),
                    "columns": 5,
                    "card_template": "card_tcg",
                    "cards": [dict(canvas=v["canvas"], palette=v["palette"], sections=v["sections"])
                              for v in visuals],
                },
            }
            jobs += [(v, group) for v in visuals]
            jobs.append((sheet, group))

    if "regles" in wanted:
        data = json.load(open(os.path.join(REPO, "docs/visuals/deck/data/regles.json"), encoding="utf-8"))
        poster = {
            "template": "parchment_poster",
            "output": "docs/visuals/deck/regles_parchemin.jpg",
            "art": "docs/visuals/deck/assets/parchemin.jpg",
            "sections": data,
        }
        jobs.append((poster, "regles"))

    if "match" in wanted:
        data = json.load(open(os.path.join(REPO, "docs/visuals/data/match_hen_gaia.json"), encoding="utf-8"))
        jobs.append((data, "match"))

    tmp = os.path.join(REPO, "docs/visuals/deck/data/_render.json")
    n = 0
    for visual, group in jobs:
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(visual, fh, ensure_ascii=False)
        run([sys.executable, "-m", "engine.render", "--data", tmp])
        run([sys.executable, "-m", "tools.ocr_check", "--data", tmp])
        print("ok", visual["output"])
        n += 1
    os.remove(tmp)
    print(f"done: {n} visuals rendered and OCR-checked")


if __name__ == "__main__":
    main()
