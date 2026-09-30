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
