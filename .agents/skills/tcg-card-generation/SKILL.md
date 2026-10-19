---
name: tcg-card-generation
description: Generate collectible card images (TCG) and parchment posters for Kingdoms — art by image model, text by the visual-generator library, OCR-validated. Kingdoms content lives under docs/tcg (data, assets, rendered outputs) and docs/visuals; layout and validation come from the visual-generator library. Use whenever a game designer asks for card art, printable cards, decks, or illustrated rules.
---

# TCG card generation (Kingdoms)

Kingdoms visuals are rendered by the **visual-generator** library.
This repo owns only the *content*: the JSON sources of truth under
`docs/tcg/data/` and `docs/visuals/data/`, and the art under
`docs/tcg/assets/` and `docs/visuals/assets/`.

**Canonical skill**: the library ships the reference agent skill —
`.agents/skills/visual-generator/SKILL.md` in
[merlin-pinpin-org/visual-generator](https://github.com/merlin-pinpin-org/visual-generator),
referenced by its README. It documents the install, the CLIs, every
template JSON schema, the OCR validation contract and the known
pitfalls. Read it first; this file only covers what is specific to
Kingdoms.

## The one hard rule

**The image model never renders text.** All text is drawn by the
library from the JSON with a real vector font — provable by OCR.

## Setup (uv)

```bash
uv sync --group visuals     # installs visual-generator (see pyproject.toml)
uv run python scripts/tcg_render.py
```

## Layout

```
docs/tcg/                    ← the Kingdoms deck
├── data/                    ← JSON sources of truth for every image
│   ├── technologies.json    ← 10 technology cards
│   ├── territoires.json     ← 48 territory cards
│   └── regles.json          ← rules poster content
├── assets/                  ← card art + parchment texture + battle backdrop
├── technologies/            ← rendered cards + planche
├── territoires/             ← rendered cards + planche
└── regles_parchemin.jpg     ← rendered poster

docs/visuals/                ← other Kingdoms visuals (match banners…)
├── data/                    ← JSON sources (match_hen_gaia.json…)
├── assets/                  ← crests, civ icons, map thumbnails
└── *.jpg                    ← rendered outputs

scripts/tcg_render.py        ← driver: Kingdoms JSON → library visuals + OCR check
```

**Data is the source of truth.** To change a card, edit the JSON and
re-render; never edit the image.

## Pipeline (per deck)

1. **Data** — edit `docs/tcg/data/<deck>.json`. Extract content from
   the mod docs (`docs/MODS/kingdoms/RULES.md`, `CADASTRE.md`,
   `CIVILIZATIONS.md`); never invent rules, and **À DÉFINIR** content
   does not go on a card.
2. **Art** — one image-generation call per card (or reuse committed
   art in `docs/tcg/assets/`), prompt template: `Medieval fantasy
   trading card art, portrait orientation, Age of Empires II style
   illustration only, NO text, NO letters, NO words anywhere: <scene>.`
3. **Download immediately** — generated URLs expire in ~1 h; deliver
   through committed files (raw GitHub URLs), never sandbox paths.
4. **Render** — `uv run python scripts/tcg_render.py`
   (optionally `--only technologies|territoires|regles|match`).
   The driver maps the Kingdoms JSON onto the library templates
   (`card_tcg`, `contact_sheet`, `parchment_poster`,
   `match_announcement`) with the Kingdoms palettes (defined in
   `scripts/tcg_render.py`), renders and OCR-checks every visual.
5. **Validate — mandatory.** The driver runs the library's OCR check
   on every visual (fail-closed; tesseract + `fra` required — with
   `OCR_CHECK_ALLOW_MISSING_TESSERACT=1` it skips with a warning, and
   every image must then be OCR-checked by another available engine
   before delivery). Complete with a visual check for layout defects.
6. **Commit** the JSON + art + rendered images together on the working
   branch. PR to main only once the library release the branch depends
   on is published.

## Kingdoms specifics

- Card anatomy, palettes and schemas: see the library skill; the
  Kingdoms palettes per `kind` live in `scripts/tcg_render.py`.
- Planches live in `docs/tcg/technologies|territoires/` with their
  deck, never at `docs/tcg/` root.
- Art paths in the JSON are repo-relative (`docs/tcg/assets/…`),
  never sandbox paths.
- Accented slugs in filenames caused art mismatch — generate the
  output filename from the accent-stripped map name.
