# ADR-0021: Game services — one per game, the only provider consumer

**Status:** Accepted (developer decision, 2026-10-21 vibe-coding session)

**Date:** 2026-10-21

**Extends:** ADR-0020 (process split), which placed the external
providers (`ext-*`) behind gRPC contracts. This ADR adds the missing
layer between svc-core and the providers.

## Context

ADR-0020 split the bot, the core and the providers into separate
processes, but left svc-core consuming the providers directly
(`GameProviderClient` in `core_process/server.py`). Three requirements
from the developer reshaped this:

1. **One game service per game.** The AoE2 domain (matches, players,
   stats) needs an owner: a service that exploits the raw provider
   data and serves the consolidated state. svc-core is game-agnostic
   plumbing (identity, bindings, dashboard aggregation) — it must not
   own game data.
2. **svc-core never talks to the providers, and vice versa.** The game
   service is the single consumer of its game's providers; svc-core
   and the providers never share a seam.
3. **Providers are not per-game.** ext-liquipedia serves every game;
   ext-librematch serves aoe2-3-4. A provider's identity is its
   upstream API, not a game — the game service arbitrates which
   provider feeds which game.

Table ownership follows: each service owns its tables, no other
service reads them; the data crosses process boundaries only through
gRPC contracts. Per-service DB accounts are deferred (issue
kingdoms-services#281) — the isolation is declared in the code first
(collection constants per service), enforced by the database later.
Redis stays shared: it is cache/hot state, never a source of truth.

## Decision

Add one **game service process per game** (`game-aoe2` today, port
50071), serving the game-generic **`kingdoms.v1.GameData`** contract:

```
bot ──Live/GameData──► svc-core ──UpdateEnrollments──► game-aoe2 ──Game──► ext-librematch (aoe2-3-4)
                        (bindings)                      (aggregator)  ├──Game──► ext-aoe2lobby  (aoe2)
                                                        (owner)      └──Game──► ext-liquipedia (all games)
```

- **GameData contract** (`contracts/kingdoms/v1/gamedata.proto`):
  `GetCoverage`, `WatchDashboard`, `WatchPlayerEvents`,
  `UpdateEnrollments` (game_key-aware — the contract is game-generic,
  a future `game-aoe4` serves it with `game_key = "aoe4"`),
  `GetMatchLinks`. The dashboard and event messages carry the full
  `GameMatchSummary` (map, format, civs, slots, host, aoe2lobby
  join/spectate URLs, `aoe2de://` deep link) so consumers never call
  back for context.
- **Enrollment flow**: svc-core reads the platform's profile bindings,
  pushes the enrolled profile ids to the game service
  (`UpdateEnrollments`); the game service reconciles its realtime
  provider's subscriptions in place (no session teardown). Provider
  subscriptions are the game service's business, never svc-core's.
- **Provider multi-game support**: capabilities stay per-provider; a
  provider that serves several games keys its raw data by `game_key`
  and the game services each consume their slice. (ext-librematch
  today declares aoe2 only; the shape is ready for aoe2-3-4.)
- **Dashboard/events**: the bot reads the enriched dashboard from the
  game service (`GAME_AOE2_URI`) — map, format, civs, join links per
  active player; the plain Live contract (svc-core) remains the
  fallback when the game service is not deployed.

## Consequences

- svc-core's provider clients are gone (`EXT_*_URI` env vars leave
  the core's compose blocks); the game service holds them.
- The game service owns the AoE2 domain tables (matches, players,
  rating_history, profile_stats) — the migration of the existing
  collections into its ownership is tracked in epic
  kingdoms-services#271.
- One more process to deploy (wired in docker-compose and the four
  infra envs; `KINGDOMS_PROCESS=game-aoe2`).
- The providers stay ADR-0020 processes: no database today, their
  raw-data persistence (issue kingdoms-services#279, P6) will land in
  their own logical bases when the code stabilizes.
