---
name: tcg-card-generation
description: Generate collectible card images (TCG) and parchment posters — art by image model, text by vector composer, OCR-validated. Self-contained skill: data, templates, art and validation live in this directory or docs/tcg. Use whenever a game designer asks for card art, printable cards, decks, or illustrated rules.
---

# TCG card generation (self-contained skill)

This directory is a **standalone toolkit**: it does not depend on Kingdoms
game data — any card game content works. The Kingdoms deck is the
reference example, stored under `docs/tcg/`.

## The one hard rule

**The image model never renders text.** It produces art with
pseudo-text that looks convincing but is misspelled gibberish. All text
on a card or poster is drawn by the composer scripts with a real vector
font, from JSON data — which is what makes it possible to *prove*
correctness by OCR. This rule exists because we shipped gibberish
images before; do not "save time" by asking the model for text.

## Toolkit layout

```
.agents/skills/tcg-card-generation/
├── SKILL.md                 ← this file
└── scripts/
    ├── tcg_compose.py       ← cards + contact sheets (JSON-driven)
    └── tcg_poster.py        ← parchment posters (JSON-driven)

docs/tcg/                    ← the Kingdoms reference deck
├── data/                    ← JSON sources of truth for every image
│   ├── technologies.json    ← 10 technology cards
│   ├── territoires.json     ← 48 territory cards
│   └── regles.json          ← rules poster content
├── technologies/            ← rendered cards + planche
├── territoires/             ← rendered cards + planche
└── regles_parchemin.jpg     ← rendered poster
```

**Data is the source of truth.** To change a card, edit the JSON and
re-render; never edit the image. To add a deck, write a new JSON file
following the schemas documented in the script docstrings.

## Pipeline (per deck)

1. **Data** — write `data.json` (schemas + examples in
   `scripts/tcg_compose.py` and `scripts/tcg_poster.py` docstrings, plus
   the live examples in `docs/tcg/data/`). For Kingdoms, extract content
   from the mod docs (`docs/MODS/kingdoms/RULES.md`, `CADASTRE.md`,
   `CIVILIZATIONS.md`); never invent rules, and **À DÉFINIR** content
   does not go on a card.
2. **Art** — one image-generation call per card, prompt template:
   `Medieval fantasy trading card art, portrait orientation, Age of
   Empires II style illustration only, NO text, NO letters, NO words
   anywhere: <scene>. Leave a clear empty parchment-colored strip at
   the bottom fifth of the image and a clear empty banner space at the
   top, both blank and undecorated.` For posters: `A blank ancient
   parchment background texture, portrait orientation, NO text, ...`
   with an *empty* ornate border (text zones get flattened anyway, but
   the cleaner the texture the better the OCR).
3. **Download immediately** — the generated URLs expire in ~1 h.
   Download each art right away; never re-share an expired link, and
   never share a sandbox path with the user — deliver through a
   committed file on a branch (raw GitHub URL).
4. **Compose** —
   `python scripts/tcg_compose.py cards --data <file> --outdir <dir>`
   (repeat with `sheet` for the contact sheet);
   `python scripts/tcg_poster.py --data <file> --out <file>`.
   Dependencies: `pip install pillow` (fonts auto-located via
   matplotlib's bundled DejaVu Serif; override with `--font-dir`).
5. **Validate — mandatory, not optional.** OCR every rendered image
   (or at minimum every card with ≥ 3 rule lines) and compare the
   transcript to the JSON word for word, accents and apostrophes
   included. A single mismatch = regenerate. Complete with a visual
   check for layout defects (cropped/overlapping text). The poster
   script already applies the known OCR guards: flattened title and
   footer zones, dark ink, wide inner margins (MARGX=235) clear of the
   ornate border, auto-fit font sizing with a fail-closed floor.
6. **Commit** the JSON + rendered images together on the working
   branch, share raw URLs. No PR unless requested.

## Card anatomy (templates)

`tcg_compose.py` has three built-in templates (`kind`), each a full
palette: `technology` (gold/brown frame, red cost badge), `territory`
(green frame, "T" badge, optional linked-civilization box), and
`civilization` (blue/gold frame, condition text). Anatomy: name
banner, cost badge, art window (744×1032 canvas, art 460px), italic
type line, rule box (parchment fill), optional extra box, footer with
`n/total` and set signature. Rule text: one sentence per line — put
`\n` between sentences in the JSON; the composer wraps each paragraph
independently.

## Known pitfalls (all learned the hard way)

- Image-model text is unreadable — see the hard rule.
- URLs expire (~1 h) — download immediately.
- Title on a raw parchment texture fails OCR (brown on brown) — the
  poster script flattens those zones; keep it that way.
- Text too close to the ornate border looks broken and half-occluded —
  keep MARGX ≥ 235.
- Accented slugs in filenames caused art mismatch — generate the
  output filename from the accent-stripped map name.
