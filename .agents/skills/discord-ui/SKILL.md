---
name: discord-ui
description: Build any Discord message, view, embed or Components V2 layout through the kingdoms-services UI SDK, never discord.ui directly. Use whenever a session builds, reviews or refactors a bot message, button, select menu, ranking, config panel or any user-facing Discord UI.
---

# Discord UI (the SDK rules)

Every user-facing Discord message of the platform is built through the
UI SDK in `kingdoms-services` — `src/kingdoms/discord/ui/`
(`factory.py` for the bricks and builders, `screens.py` for the
archetypes). No feature instantiates `discord.ui` / `discord.Embed`
classes directly: the SDK is the single place where the Discord layout
rules are enforced, at build time, with a clear `UILayoutError` —
before anything is sent.

## The bricks

Two builders cover the ADR-0009 dual system:

- `UIEmbed` — light informational output (`.field()`, `.footer()`,
  `.build()`), where markdown links and line breaks **do** render
  (classic embed fields).
- `UILayout` — rich Components V2 output, composed of `Container`,
  `Section`, `Text`, `Row`, `Button`, `Separator`, `Thumbnail`,
  `Action` (interactive button), `SelectMenu` (interactive select).

```python
from kingdoms.discord.ui import UILayout, Container, Section, Text, Row, Button, Separator

view = (
    UILayout()
    .add(
        Container(accent=BLURPLE)
        .add(Text("# 🚀 Title\n-# `badge`"))
        .add(Section(Text("**Services**"), button=Button("PR", url)))
        .add(Separator())
        .add(Row(Button("Pipeline", run_url), Button("Image", pkg_url)))
    )
    .build()
)
```

## Navigation is buttons, not links (the V2 text rule)

In Components V2 text blocks — and **worst in sub-texts / footers
(`-# …`) — links and line breaks do not render reliably**. The rule:

- text blocks carry **plain labels, code spans and timestamps only**
  (`<t:…:R>`);
- **every link is a link button in an action row**
  (`Row(Button(label, url), …)`);
- a section layout follows the announcement pattern:

  ```
  **Services**
  [Branch] [Pull-request]        ← action row
  PR title                       ← plain text
  `sha7`                         ← plain text
  [Commit] [Files]               ← action row
  <t:…:R>                        ← timestamp
  [🚦 Pipeline] [📦 Image]       ← action row
  ```

- embeds (`UIEmbed`) are the exception: markdown links render there
  (e.g. the `/status` embed keeps its `[label](url)` lines).

## Interactive items

- `Action(label, custom_id, on_click, style=…)` — button with an async
  callback. The custom_id **must** follow
  `<mod>:<component>:<payload>` (e.g. `admin:ping:`, `ranking:page:next`);
  the convention is enforced at build time.
- `SelectMenu(custom_id, options, on_choose, …)` — the callback
  receives `(interaction, chosen_values)`; no digging through
  `interaction.data` in feature code.
- `Row` holds 1–5 items; a `SelectMenu` sits alone in its row.

## Screen archetypes (`screens.py`)

Prefer a ready-made shape over raw composition:

- `render_ranking(Ranking(title, entries))` — paged leader board
  (podium on page 1); the Prev/Next actions **edit the message in
  place** (UPDATE_MESSAGE), never repost.
- `build_config_panel(title, settings, mod=…, on_apply=…, on_reset=…)` —
  one `SelectMenu` per setting + Apply/Reset actions.
- `build_match_report(title, summary, details, mod=…)` — structured
  report with optional links and thumbnail.
- `PaginatedScreen(pages, mod=…, title=…)` — generic pagination when
  an archetype does not fit.

## Build-time guarantees (why the SDK exists)

The SDK rejects, with a clear `UILayoutError` before anything is sent:

- the 4000-character shared TextDisplay budget (V2) and the embed
  character budget;
- the 40-component cap;
- a `Section` without exactly one accessory (`button=` or
  `thumbnail=`), or with more than 3 text blocks;
- a `Row` with more than 5 items, or a misplaced `SelectMenu`;
- a `custom_id` that breaks the `<mod>:<component>:<payload>`
  convention.

## Testing

- Unit: assert on the serialized wire (`view.to_components()`), with
  `simcord.components.validate_components` for full validation.
- Behavioral: SimCord journeys drive the real dispatch — click the
  buttons (`alice.click(message, custom_id=…)`), read the message back
  (`channel.last_message`) and assert on observable state; pagination
  must edit the message in place (same message id).

## Procedure

1. Reach for an archetype first (`screens.py`); compose factory bricks
   only when no archetype fits — and if the composition recurs,
   propose a new archetype.
2. Build through `UILayout` / `UIEmbed` only; never touch
   `discord.ui` classes in feature code.
3. Keep text blocks navigation-free (labels, code spans, timestamps);
   links ride in action rows.
4. Localize labels through the i18n catalogs (`config/locales/`),
   never hardcoded.
5. Assert the wire structure in tests (`to_components()`), and the
   click journey in SimCord for anything interactive.
