---
name: tcg-card-generation
description: Generate collectible card images (TCG) and parchment posters — art by image model, text by the visual-generator library, OCR-validated. Kingdoms content lives under docs/tcg (data, assets, rendered outputs); layout and validation come from the visual-generator library. Use whenever a game designer asks for card art, printable cards, decks, or illustrated rules.
---

# TCG card generation (Kingdoms)

Kingdoms visuals are rendered by the **visual-generator** library
(`merlin-pinpin-org/visual-generator`): JSON data + library templates
+ art. This repo owns only the *content*: the JSON sources of truth
under `docs/tcg/data/` and the art under `docs/tcg/assets/`.

## The one hard rule

**The image model never renders text.** It produces art with
pseudo-text that looks convincing but is misspelled gibberish. All text
on a card or poster is drawn by the library with a real vector font,
from JSON data — which is what makes it possible to *prove*
correctness by OCR. This rule exists because we shipped gibberish
images before; do not "save time" by asking the model for text.

## Layout

```
docs/tcg/                    ← the Kingdoms deck
├── data/                    ← JSON sources of truth for every image
│   ├── technologies.json    ← 10 technology cards
│   ├── territoires.json     ← 48 territory cards
│   └── regles.json          ← rules poster content
├── assets/                  ← card art (extracted or image-model generated)
├── technologies/            ← rendered cards + planche
├── territoires/             ← rendered cards + planche
└── regles_parchemin.jpg     ← rendered poster

docs/visuals/                ← other Kingdoms visuals (match banners…)
├── data/                    ← JSON sources (match_hen_gaia.json…)
├── assets/                  ← crests, civ icons, map thumbnails
└── *.jpg                    ← rendered outputs

scripts/tcg_render.py        ← driver: JSON → library visual schema → render + OCR check
```

**Data is the source of truth.** To change a card, edit the JSON and
re-render; never edit the image.

## Pipeline (per deck)

1. **Data** — edit `docs/tcg/data/<deck>.json`. For Kingdoms, extract
   content from the mod docs (`docs/MODS/kingdoms/RULES.md`,
   `CADASTRE.md`, `CIVILIZATIONS.md`); never invent rules, and
   **À DÉFINIR** content does not go on a card.
2. **Art** — one image-generation call per card (or reuse committed
   art in `docs/tcg/assets/`), prompt template: `Medieval fantasy
   trading card art, portrait orientation, Age of Empires II style
   illustration only, NO text, NO letters, NO words anywhere: <scene>.`
3. **Download immediately** — the generated URLs expire in ~1 h.
   Download each art right away; never re-share an expired link, and
   never share a sandbox path with the user — deliver through a
   committed file on a branch (raw GitHub URL).
4. **Render** —
   `python3 scripts/tcg_render.py --lib <visual-generator clone>`
   (optionally `--only technologies|territoires|regles|match`).
   The driver maps the Kingdoms JSON onto the library templates
   (`card_tcg`, `contact_sheet`, `parchment_poster`,
   `match_announcement`) with the Kingdoms palettes, then runs the
   library's render and OCR check for every visual.
   Dependencies: `pip install pillow matplotlib` in the library.
5. **Validate — mandatory, not optional.** The driver runs
   `tools/ocr_check.py` from the library on every visual (fail-closed;
   tesseract + `fra` required — in sandboxes without tesseract,
   OCR_CHECK_ALLOW_MISSING_TESSERACT=1 skips with a warning, and every
   image must then be OCR-checked by another available engine before
   delivery). Complete with a visual check for layout defects.
6. **Commit** the JSON + art + rendered images together on the working
   branch, share raw URLs. No PR unless requested.

## Card anatomy (library templates)

The library's `card_tcg` template renders the fixed anatomy: name
banner, cost badge (`cost`: int = gear icons, string = badge text,
e.g. "T"), art window (744×1032 canvas), italic type line, rule box
(parchment fill), optional extra box (`extra_label`/`extra_value`),
footer with `n/total` and set signature. Palettes per `kind` are
defined in `scripts/tcg_render.py`. Rule text: one sentence per line —
put `\n` between sentences in the JSON; the template wraps each
paragraph independently.

## Known pitfalls (all learned the hard way)

- Image-model text is unreadable — see the hard rule.
- URLs expire (~1 h) — download immediately.
- Accented slugs in filenames caused art mismatch — generate the
  output filename from the accent-stripped map name.
- Never commit rendered planches at `docs/tcg/` root — they live in
  `docs/tcg/technologies|territoires/` with their deck.
- Sandbox paths in JSON (`/workspace/...`) break re-rendering — art
  paths are always repo-relative (`docs/tcg/assets/...`).
