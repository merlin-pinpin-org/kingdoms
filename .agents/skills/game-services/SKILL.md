---
name: game-services
description: Manage the game services (game-aoe2), their gRPC contracts and the external providers (ext-aoe2lobby, ext-librematch, ext-aoe2techtree, ext-liquipedia). Use when adding or changing a game integration, a provider adapter, the GameData/Game contracts, provider health tests, the profile-sites registry, or diagnosing a provider/game-service outage.
---

# Game services and providers (ADR-0020 + ADR-0021)

The two-layer architecture around the external game data:

```
bot ──GameData──► game-<game_key> ──Game──► ext-<provider> processes ──HTTPS/WS──> external APIs
   │                  │
   └──Live (fallback) │ UpdateEnrollments (inscrits)
        svc-core ─────┘ (bindings — NEVER talks to the providers)
```

**The two invariants (ADR-0021):**

1. The **game service** (`game-aoe2`, port 50071, `kingdoms.game_aoe2`)
   is the ONLY consumer of its game's providers. svc-core never talks to
   the providers; the providers never talk to svc-core.
2. A **provider is not per-game**: ext-liquipedia serves every game,
   ext-librematch serves aoe2-3-4. A multi-game provider keys its raw
   data by `game_key`; each game service consumes its slice.

## Where things live (kingdoms-services)

| Piece | Path | Notes |
|---|---|---|
| GameData contract | `contracts/kingdoms/v1/gamedata.proto` | game-generic (`game_key` param): dashboard, player events, enrollments, provider tests, links |
| Game contract | `contracts/kingdoms/v1/game.proto` | provider-side: capabilities, StreamMatchEvents, UpdateSubscriptions |
| game service | `src/kingdoms/game_aoe2/` | `aggregator.py` (states + `ProviderProber`), `rpc.py` (servicer + wire), `server.py` (entrypoint, port 50071), `client.py` (bot side) |
| Providers | `src/kingdoms/ext_<name>/` | adapter = the protocol translation; server = the Game servicer; NEVER touches Mongo |
| Game module | `src/kingdoms/core/games/aoe2/` | domain identity: grace rules, validation, content |
| Profile sites | `config/games/aoe2/profile_sites.yaml` + `src/kingdoms/core/services/profile_sites.py` | typed URL format/parse per game — a site is config, never code |
| Enrollments | svc-core `_sync_game_enrollments` | reads the bindings, pushes `UpdateEnrollments` to the game service (30 s) |

## Workflows

### Add or change a provider adapter

1. The adapter speaks ONE upstream protocol — validated live first
   (spike: log raw frames, never trust docs blindly; the aoe2lobby
   rewrite taught: the doc said no per-player filter, the service had
   one).
2. One WebSocket/HTTP session per adapter; reconnection is the
   adapter's; subscription reconciliation happens in place (deltas,
   no session teardown) via `Game.UpdateSubscriptions`.
3. Game rules live in the game module, not the adapter: the 15 s
   lobby-closed grace is `core/games/aoe2/grace.LobbyClosedGrace` —
   providers consume it, none re-implements it.
4. Enriched match summaries (map, format, civs, links) ride the event
   metadata — consumers never call back for context.
5. Regenerate the stubs after any proto change: `make contracts`.

### Diagnose a provider outage

1. The admin aoe2 menu → **Providers** button (`panel:game:aoe2:providers`)
   renders the game service's prober results: per provider, the last
   capabilities ping (ok, latency, consecutive failures).
2. The data comes from `GameData.GetProviderTests` — the game service
   probes its providers every 60 s; the bot never pings providers.
3. Logs: each process logs its own; `docker compose logs
   kingdoms-game-aoe2` / `kingdoms-ext-aoe2lobby` on the env.
4. Degradation is nominal: no provider → the dashboard flags
   `degraded`, everything renders offline, nothing crashes.

### Add a profile site (aoe2insights, aoe2.GG, ...)

Config only, no deploy: declare it in
`config/games/<game>/profile_sites.yaml` (`url_template` with
`{relic_id}`, `parse` regex, `id_kind`). The profile view, the
home accounts and the profile-add flow read the registry; users pick
their preferred site (persisted in `user_settings`, key
`profile_site:<game>`).

### Deploy wiring (per env)

`KINGDOMS_PROCESS=game-aoe2` (entrypoint case), port 50071;
`EXT_AOE2LOBBY_URI` + `EXT_LIBREMATCH_URI` point at the ext processes
over the docker network; svc-core and the bot get `GAME_AOE2_URI`.

## Traps learned the hard way

- The ws `schema` frame (civ labels) is only pushed on aoe2lobby's
  contextual endpoint — the adapter opens a short dedicated connection
  to capture it (fallback: raw ids).
- `*_player_remove` lists profile ids; `*_match_remove` lists match ids
  — never confuse them.
- Profile ids compare as `str` everywhere (heterogeneous server types).
- Slots: only `status == 3` is a player (0 Open, 1 Closed, 2 AI) — a
  residual profileid on a closed slot is not a present player.
- Regenerated pb2 stubs need the import rewrite on `*_pb2*.py` (the
  Makefile `contracts` target does it; an import between protos makes
  `*_pb2.py` import a sibling too).
