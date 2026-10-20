---
name: mod-intake
description: Guide a novice user (vibe-coder or game-designer) through creating a new mod — intake questionnaire (purpose, seasonal, enrollment criteria, universe/entities), reuse-first check against the core and existing mods, scaffold via `kingdoms mod init`, convention compliance. Use whenever a session starts creating a new mod, whatever the user's skill level.
---

# Mod intake — the guided parcours for a new mod

A session building a mod never improvises: it runs this questionnaire,
checks what already exists before writing anything, scaffolds with the
committed tool, and only then implements. The outcome is uniform — the
same structure, the same seams, the same conventions — whatever the
user's inputs. **The intake is a conversation in plain language; the
implementation is not.**

## 1. The intake questionnaire (ask, in this order)

Ask in the session's working language, one question at a time, in plain
words. Never ask anything technical (no "schema", no "Mongo").

1. **What does the mod do?** One sentence a player would understand.
   → if the idea is unshaped, run
   [shape-game-designer-idea](../shape-game-designer-idea/SKILL.md)
   first, then come back.
2. **Is it seasonal?** Does it run as a season (a period with a start
   and an end, everything reset per season) or is it always on?
   → `seasonal: true|false` — MANDATORY in the declaration.
3. **Who can join?** Free for everyone, or should candidates be checked?
   - nothing to check → no enrollment criteria;
   - checked by a human → `manual: true` (candidates queue, admins
     accept/refuse from the dashboard);
   - checkable automatically → the criteria library
     (see §2) — all-pass auto-accepts, a failure refuses with the reason,
     `manual` on top sends passing candidates to the queue anyway.
4. **What is the universe?** The entities (kingdoms, civs, maps, teams…),
   their names, and their interactions. One entity per row; keep the
   entity list stable (entities become forum posts and Mongo documents —
   renaming later is a migration).
5. **What does the player see?** The surfaces: channels (the mod's
   category), commands, pinned panels. Translate each into declaration
   data (`channels:`, `commands:`) — a channel is a config line, never
   code.

## 2. The enrollment criteria library (automatable checks)

Prefer an automatable criterion over a human gate — the dashboard
remains for the edge cases. Declared in `settings.enrollment`:

| Criterion | Declared as | Checks |
|---|---|---|
| `min_elo` | `min_elo: 1200` | the player's rating ≥ the value |
| `min_matches` | `min_matches: {count: 5, days: 30, game: aoe2}` | X matches in the last Y days on the game |
| `requires_profile` | `requires_profile: true` | a bound, validated game profile |
| `manual` | `manual: true` | every candidate waits for an admin |

Composition rule: all pass → auto-accept (unless `manual`); any failure →
refused with the failing reasons recorded; an unknown stat (unrated
player, missing history) degrades to a refusal reason "manual review" —
never a crash, never a silent accept.

## 3. Reuse-first check (before writing any code)

Run, in order, and tell the user what you found:

1. `uv run kingdoms mod list` — existing mods; an existing mod doing
   the job may answer without new code (depend on it via
   `dependencies:`).
2. The core inventory (see the guide): seasons (one active max,
   rotations), `SeasonRolesService` (per-season roles),
   `EnrollmentService` (apply/criteria/queue), `MembershipService`
   (register/unregister + role sync), `AdminModSection` (admin
   dashboards), `EntityForumSpec` (universe entity forums),
   `build_mod_season_stack` (the whole seasonal stack wired in one call).
3. The mod catalogue
   ([docs/MODS/CATALOGUE.md](../../../docs/MODS/CATALOGUE.md)) —
   something at maturity 2-3 may be extendable instead of rebuilt.

**The core/mods split rule**: duplicated machinery in a mod is a
factorization bug — if two mods need it, it belongs to the core (raise
it, do not copy it).

## 4. Scaffold, then implement

1. `uv run kingdoms mod init <name> --seasonal|--permanent
   [--private --owner <discord-id>]` — the self-contained directory
   (`modules/mods/<name>/`): declaration, package skeleton with the
   three lifecycle hooks, locales, tests.
2. Fill `mod.yaml` from the questionnaire answers (channels, roles,
   commands, `settings.enrollment`).
3. Implement against the core seams only — never import `discord.py`
   directly (the UI SDK builds every surface), never hardcode platform
   ids, never extend core enums.
4. Locale every user-facing string (`locales/en.yaml` + `fr.yaml`).
5. Tests: MockDiscord + in-memory stores, same seams as production.
6. `make lint typecheck test` — green before any push.

Reference: [docs/GUIDES/mod-init.md](../../../docs/GUIDES/mod-init.md)
(the canonical guide), the ladder and kingdoms examples
(`modules/mods/`).

## 5. Conventions — and deliberate deviations

Follow the project conventions by default:
[docs/CONVENTIONS.md](../../../docs/CONVENTIONS.md),
[architecture/mods.md](../../../docs/architecture/mods.md). The
enrollment UX follows the kingdoms precedent (Drasah's apply flow): one
ephemeral bubble per parcours (edited, never stacked), pending ⏳ /
accepted ✅ / refused ❌ states, restart-proof action buttons
(`<mod>:<component>:<payload>` custom ids).

A deviation is acceptable **only when deliberate**: state the reason in
the PR description ("deviates from X because Y"), and link it from the
mod's docs. An undocumented deviation is drift — the session drift
watchdog will find it.

## Anti-patterns

- Writing plumbing the core already owns (season numbering, role sync,
  admin panels, forums) — §3 first, always.
- "The bot decides who joins" → ask for the exact rule; every criterion
  is checkable or it is `manual`.
- A mod with no `seasonal` flag — startup fails loudly (by design).
- Starting the implementation before the questionnaire is complete —
  the intake is what makes mods uniform across users.
