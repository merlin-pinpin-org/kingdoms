# Kingdoms mod — Environment

> Configuration et surfaces déclarées par le mod. Toutes les valeurs
> de saison sont **des données de configuration** (référence §27/§28),
> jamais codées en dur : l'admin les modifie sans toucher au code.

## Configuration (paramètres de saison)

Toutes les valeurs par défaut ci-dessous sont celles de la Saison II.

### Saison

| Key | Type | Default | Description |
| --- | ---- | ------- | ----------- |
| `weeks` | int | 3 | Nombre de semaines (= cycles — 3 en Saison II, essai D55 ; défaut générique 4, D1) |
| `starts_at` | datetime | — | Date/heure de début (lancement manuel admin) |
| `cycle_bistable_at` | datetime | dim. 23h30 | Bascule de cycle + recharge attaque/défense |
| `protection_window` | plage | dim. 23h30 → lun. 10h | Fenêtre de protection (D56) — aucune agression ni Corruption |

### Royaumes

| Key | Type | Default | Description |
| --- | ---- | ------- | ----------- |
| `kingdoms_count` | int | 2 | Nombre de royaumes joueurs |
| `lords_per_kingdom` | int | 4 | Nombre de seigneurs par royaume |
| `kingdoms_preset` | bool | false | Royaumes imposés par l'admin (noms définis) |

### Territoires

| Key | Type | Default | Description |
| --- | ---- | ------- | ----------- |
| `territories_per_kingdom` | int | 5 | Territoires de départ par royaume joueur |
| `gaia_territories` | int | 8 | Territoires de Gaïa au départ |
| `allowed_maps` | list | — | Liste personnalisée de maps autorisées |

### Attaques

| Key | Type | Default | Description |
| --- | ---- | ------- | ----------- |
| `player_attack_delay` | duration | 6h | Délai avant attaque contre un royaume joueur |
| `gaia_attack_delay` | duration | 3h | Délai avant attaque contre Gaïa |
| `attacks_per_week` | int | 1 | Attaques par seigneur et par semaine |
| `defenses_per_week` | int | 1 | Défenses par seigneur et par semaine |
| `gaia_attack_max_per_kingdom` | int | 1 | Seigneurs max par royaume sur une attaque Gaïa |
| `gaia_attack_max_total` | int | 7 | Seigneurs max au total sur une attaque Gaïa |
| `gaia_match_time_limit` | duration | À DÉFINIR | Limite de temps des parties Gaïa (victoire au score) |

### Événements

|
 Key | Type | Default | Description |
| --- | ---- | ------- | ----------- |
| `lords_day_at` | datetime | dim. 23h30 | Jour du Seigneur (cycle + +maps Gaïa + cadastre + alliances) |
| `lords_day_new_maps` | int | 8 | Maps ajoutées à Gaïa au Jour du Seigneur |
| `exploration_at` | datetime | sam. 14h | Exploration hebdomadaire |
| `exploration_rewards` | map | {1er: map+1 tech, 2e: 3, 3e: 2, autres: 1} | Récompenses (points technologiques) |

### Époques

| Key | Type | Default | Description |
| --- | ---- | ------- | ----------- |
| `age_change_at` | datetime | mer. minuit | Changement d'époque |
| `ages` | list | 4 époques | IA Gaïa + bonus par époque (cf. RULES.md §15) |
| `garrison_enabled` | bool | false | Garnison désactivée (décision D4) |

### Paroisse (D64)

| Key | Type | Default | Description |
| --- | ---- | ------- | ----------- |
| `parish_chapel_lock` | duration | 24h | Verrou du mariage classique (Chapelle) |
| `parish_church_cost` | int | 2 | Coût de l'Église |
| `parish_church_lock` | duration | 12h | Verrou à l'Église |
| `parish_cathedral_cost` | int | 3 | Coût de la Cathédrale |
| `parish_cathedral_lock` | duration | 6h | Verrou à la Cathédrale |
| `shrine_duration` | duration | 72h | Durée du chantier Sacrée |
| `marriage_base_stock` | int | 1 | Stock de mariages de base (D59) |
| `corruption_max_per_season` | int | 2 | Corruptions max par saison et royaume (D58) |

### Patrouille (D68)

| Key | Type | Default | Description |
| --- | ---- | ------- | ----------- |
| `patrol_cost` | int | 2 | Coût d'un achat de tranche de Patrouille au Marché (Roi uniquement) |
| `patrol_window_hours` | int | 2 | Durée de la tranche quotidienne protégée |
| `patrol_max_per_season` | int | 2 | Tranches max par royaume et par saison (paramétrable admin avant lancement) |
| `patrol_change_window` | plage | dim. 23h30 → lun. 10h | Fenêtre pendant laquelle le Roi peut modifier la tranche (sinon maintien automatique) |

### Banques d'images (D70)

| Key | Type | Default | Description |
| --- | ---- | ------- | ----------- |
| `map_images` | map | — | Banque d'images des maps (fournies par le game designer, non bloquantes) |
| `blason_images` | map | — | Banque d'images des blasons de civilisation (fournies, non bloquantes) |

## Channels and roles

Mod-declared surfaces (provisioned by the core via ChannelService /
RoleService, addressed by mod-scoped keys) :

- `kingdoms:attack` — `⚔️-attaquer` (déclarations d'attaques)
- `kingdoms:attack_delays` — `🕰️-délais-attaque` (suivi des délais)
- `kingdoms:cadastre` — `🧾-cadastre` (territoires et leurs effets)
- `kingdoms:diplomacy` — `📖-diplomatie` (alliances, civilisations)
- `kingdoms:geopolitics` — `📣-géopolitique` (annonces, traités)
- `kingdoms:market` — `🛒-marché` (boutique technos, réservée au Roi)

Ces salons transversaux vivent dans la catégorie **Scriptorium**
(D70). Les anciens salons globaux Patrouille/Seigneurs/Territoire/
Diplomatie sont **supprimés** : chaque royaume possède sa propre
catégorie `[NomDuRoyaume]` (créée à la validation du nom, visible
des joueurs de la saison + admins) contenant les salons
`kingdom:patrol` (🛡️), `kingdom:lords` (🎖️), `kingdom:overview`
(🏰 Le-Royaume), `kingdom:territories` (🗺️), `kingdom:alliances`
(📜), `kingdom:church` (⛪) et le salon éphémère de rappels
`kingdom:carrier` (🕊️ Pigeon-Voyageur, D69). **Gaïa n'a pas de
catégorie** (entité IA, elle n'attaque jamais).

Roles declared by the mod : `kingdoms_king`, `kingdoms_lord`,
`kingdoms_admin` (Gaïa n'est pas un rôle — c'est une entité IA).

## Persistence boundary

Données de **configuration** (ci-dessus) : conservées entre saisons,
modifiables par l'admin. Données de **saison** (propriétaires des
territoires, alliances, mariages, soldes technologiques, attaques,
défenses, résultats) : entièrement réinitialisées au lancement d'une
nouvelle saison. Le mod ne stocke ni identifiants Discord ni IDs de
jeu dans ses collections ; les IDs de messages persistants vivent dans
le registre de messages de la plateforme.

## Politique de modification (D66)

Chaque paramètre porte une politique : `free` (modifiable à tout
moment, effet sur les événements futurs), `next-cycle` (appliqué au
cycle prochain), `next-season` (prochaine saison). Les chantiers
Sacrée en cours et les Cathédrales validées ne sont jamais
rétro-touchés.
