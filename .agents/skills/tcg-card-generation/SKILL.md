---
name: tcg-card-generation
description: Generate collectible card images (TCG) for Kingdoms mods — technologies, territories, civilizations — and parchment-format rule posters, with guaranteed correct French text. Use whenever the game designer asks for card art, printable game cards, or illustrated rules.
---

# TCG card generation

Kingdoms game data (rules, costs, effects) comes from the repo docs and
**must be rendered as text by the composer script, never by the image
model**. Image models produce convincing-looking but misspelled
pseudo-text; the text on a card is therefore always drawn with a real
font by `scripts/tcg_compose.py`.

## Hard rules (learned from failed attempts)

1. **Never ask the image model to write text.** Generate the *art only*,
   with an explicit `NO text, NO letters, NO words anywhere` clause, and
   empty zones reserved for the composer (a blank banner at the top and
   a blank parchment strip at the bottom fifth). Any text found in a
   generated art must be rejected.
2. **Text is drawn by the script**, from data sourced in the repo docs:
   - Technologies → `docs/MODS/kingdoms/RULES.md` (§ Actions spéciales)
     and `docs/PLANS/reference/kingdoms-mod-saison2.md` (§ 20)
   - Territories/effects → `docs/MODS/kingdoms/CADASTRE.md`
   - Civilization conditions → `docs/MODS/kingdoms/CIVILIZATIONS.md`
   Nothing is invented; if a rule is **À DÉFINIR** in the docs, it does
   not go on a card.
3. **Every produced image is validated by OCR** before being delivered:
   the transcript must match the source text word for word (accents and
   apostrophes included). An image whose OCR is gibberish is invalid,
   even if it looks fine. A visual check (legibility, no cropped or
   overlapping text) completes the validation.
4. **Generated art URLs expire (~1 h).** Download each art immediately
   after generation (`urllib.request.urlretrieve`) — never re-share an
   expired link, and never share a sandbox path with the user: deliver
   through a committed file on a branch (raw GitHub URL).

## Pipeline

1. **Data** — collect the card list from the docs (name, cost/type,
   rule text). One row per card.
2. **Art** — one image-generation call per card, prompt template:
   `Medieval fantasy trading card art, portrait orientation, Age of
   Empires II style illustration only, NO text, NO letters, NO words
   anywhere: <scene>. Leave a clear empty parchment-colored strip at
   the bottom fifth of the image and a clear empty banner space at the
   top, both blank and undecorated.`
3. **Download** the art files into a scratch directory immediately.
4. **Compose** — run the composer:

   ```bash
   pip install pillow
   python scripts/tcg_compose.py cards --data <data.json> --outdir <dir>
   python scripts/tcg_compose.py sheet --data <data.json> --outdir <dir>
   ```

   `data.json` format (see `docs/tcg/data/*.json` for examples):

   ```json
   {
     "kind": "technology",
     "cards": [
       {"art": "art_embuscade.jpg", "name": "Embuscade", "cost": 2,
        "rule": "Attaque supplémentaire. Délai minimum : 1 heure."}
     ]
   }
   ```

   Supported `kind`: `technology` (gold/brown frame, red cost badge),
   `territory` (green frame, tower badge, effect + linked-civilization
   box), `civilization` (blue/gold frame, condition text),
   `poster` (parchment rule poster — landscape, flowing columns,
   title flourish, footer seal).
5. **Validate** — OCR every card (or at minimum every card with more
   than two lines of text); compare the transcript to the source text.
   Also run a visual check for layout defects.
6. **Commit** the validated images under `docs/tcg/<kind>/` on
   the working branch (plus the `data.json` used), and share the raw
   GitHub URLs with the user. No PR unless requested.

## Fonts

The composer needs DejaVu Serif faces. If the sandbox has no system
font, install matplotlib and use its bundled fonts
(`.../matplotlib/mpl-data/fonts/ttf/DejaVuSerif*.ttf`) — the script
locates them automatically.

## Existing assets

- Technologies (10 cards + contact sheet): `docs/tcg/`
- Territories (8 cards): `docs/tcg/territories/`
- Rules poster (parchment): `docs/tcg/rules/`
