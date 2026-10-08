# Kingdoms mod (conquête de territoires AoE2)

> Rewritten from the game designer's Season II reference
> ([../../PLANS/reference/kingdoms-mod-saison2.md](../../PLANS/reference/kingdoms-mod-saison2.md))
> — the reference is the **functional source of truth**. This directory
> adapts it to the Kingdoms stack. Where the reference and
> [DECISIONS.md](DECISIONS.md) disagree, the decisions win. Anything
> marked **À DÉFINIR** must not be invented by an implementation.

## Purpose

A territory-conquest meta-game on top of Age of Empires II: player
Kingdoms (Roi + Seigneurs) fight each other and Gaïa (the AI kingdom)
to conquer maps, week after week, across seasons. The bot is the
**world-state manager**: it owns territories, schedules weekly events,
enforces attack/defense budgets, and applies diplomacy.

## Concepts

- **Saison** — 4 semaines / 4 cycles par défaut (configurable), lancée
  manuellement par l'admin ; réinitialisation complète des données de
  saison au lancement d'une nouvelle saison.
- **Royaume** — player kingdom (2 par défaut en Saison II) : un Roi,
  des Seigneurs (4 par défaut). Gaïa est le royaume IA.
- **Territoire** — une map AoE2 ; tirée depuis la liste autorisée,
  jamais en doublon pendant la saison.
- **Attaques / défenses** — 1 attaque et 1 défense par Seigneur et par
  semaine ; délai de 6h (royaume joueur) / 3h (Gaïa) ; les attaques
  Gaïa sont des FFA « chacun pour soi » (gagnant unique).
- **Événements hebdomadaires** — Exploration (samedi 14h, FFA
  optionnel), Jour du Seigneur (dimanche 23h30 : +maps Gaïa, cadastre,
  alliances), changement d'époque (mercredi minuit).
- **Technologies** — la monnaie du jeu ; achète des actions spéciales
  (Embuscade, Traquenard, Patrouille, Contre-espionnage, Sabotage,
  Explorateur, Jeu d'armes, Mariage arrangé, Corruption, Garde Royale).
- **Diplomatie** — alliances liées aux civilisations, actualisées selon
  les territoires ; mariages ; traités ; Ordre Royal.

## Core integration

The mod is **game-bound** (AoE2 only, see [../README.md](../README.md) — game-bound mods):
hard-coded AoE2 options are intentional. Everything shared is owned by the core:

- **Seasons** — registered in the core season registry with the visible id
  `kingdoms-aoe2-<guild id>-<index>` (index incremental from 1, per guild).
  The legacy internal `s-<timestamp>` ids are a fallback only.
- **Maps & map pools** — sourced from the core game catalog
  (`GameDataService`); the mod grafts onto the existing
  `aoe2-maps` and `aoe2-map-pools` forum topics (in the `games` category)
  and never creates or duplicates them.
- **Players** — Discord users come from the core identity/user service;
  the mod never manages accounts itself.
- **Territories** — distinct from maps: a territory is backed by one
  AoE2 map but carries the mod's own function (ownership, protection).
  Its visible id is `territory:<season id>:<map key>`; the
  `kingdoms-territories` forum (in the `games` category, built by the
  core entity-forum engine) carries one post per territory, linked to
  its map's `aoe2-maps` post, ids shown in a footer.
- **Map pool rotations** — the season's pool reference lives on the
  core season document (`map_pool_id`); the core's `map_pool_history`
  activations are the rotations, referenced from the season.

## Seeding (deploy time)

The mod's season data seeds with its own CLI, by visible ids (the
panels' footers):

```
python -m kingdoms.mods.kingdoms.kingdoms_seed_cli <seed_yaml> <guild_id>
```

The YAML file (see the ladder/core seeds for the deploy-time pattern):

```yaml
season_id: kingdoms-aoe2-<guild id>-<index>   # required — the footer id
kingdoms: [Aquitaine]                        # imposed kingdom names
territories:                                 # optional initial draw
  - { map_key: arabia, owner: gaia }
  - { map_key: kawasan, owner: Aquitaine }
lords:                                       # enrolled players
  - { player_id: "<discord id>", kingdom: Aquitaine, role: lord, display_name: Rollon }
```

Idempotent (re-run skips existing ids). The maps and pools themselves
come from the core AoE2 seed — the mod seed only references map keys.
The territory ids are `territory:<season id>:<map key>`.

## Usage

```text
/kingdoms …      — jo
ueur : inscription, royaume, actions
/kingdoms-admin … — admin : saison, paramètres, maps, interventions
```

Les salons déclarés par le mod incluent `⚔️-attaquer`,
`🕰️-délais-attaque`, `🧾-cadastre`, `📖-diplomatie`,
`📣-géopolitique`.

## See also

- [RULES.md](RULES.md) — règles du mod
- [ENVIRONMENT.md](ENVIRONMENT.md) — configuration et surfaces
- [DECISIONS.md](DECISIONS.md) — décisions validées après la référence
- [../../PLANS/reference/kingdoms-mod-saison2.md](../../PLANS/reference/kingdoms-mod-saison2.md) — référence fonctionnelle
