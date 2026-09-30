# Kingdoms mod — Décisions validées

> Décisions prises par le game designer **après** la rédaction de la
> référence Season II
> ([../../PLANS/reference/kingdoms-mod-saison2.md](../../PLANS/reference/kingdoms-mod-saison2.md)).
> En cas de désaccord entre la référence et ce document, **ce document
> gagne**. Les points non tranchés restent **À DÉFINIR** (référence §30)
> et ne doivent jamais être inventés par une implémentation.

## D1 — Cycle

- **Un cycle = une semaine.**
- La bascule du cycle a lieu au **Jour du Seigneur (dimanche 23h30)**,
  dernier événement de la semaine ; les attaques/défenses se
  rechargent à la bascule.
- **À confirmer** : publication d'un bilan hebdomadaire du cycle dans
  `📣-géopolitique` (proposé, pas encore validé).

## D2 — Technologies = monnaie

- Les bonus d'époque « +1/+2 technologies » sont des **points
  technologiques** — la même monnaie que celle utilisée pour acheter
  les actions spéciales (référence §20).

## D3 — Mariages d'époque

- « +1 mariage » = un **mariage supplémentaire utilisable** par le
  royaume à chaque passage d'époque.
- **À définir** : les usages non consommés se cumulent-ils d'une époque
  à l'autre ou expirent-ils ?

## D4 — Garnison en pause

- Le bonus « +1 garnison » de l'Âge sombre est **inactif** en Saison II
  (mécanique mise de côté pour équilibrage, référence §24). Il est
  conservé dans la configuration (désactivé), pas supprimé.

## D5 — Exploration = FFA réel, optionnel

- L'exploration du samedi est une **vraie partie AoE2 en FFA** entre
  les seigneurs envoyés.
- La participation est **optionnelle** : chaque royaume *peut* envoyer
  un seigneur (pas d'obligation).
- Le classement 1er/2e/3e correspond au **classement final de la
  partie FFA** ; récompenses inchangées (1er : la map + 1 tech ;
  2e : +3 tech ; 3e : +2 tech ; autres participants : +1 tech).

## D6 — Attaque Gaïa = FFA, chacun pour soi

- Les seigneurs participants ne sont **pas alliés** contre Gaïa :
  chacun joue pour lui-même, contre les autres participants et contre
  l'IA.
- **Un seul gagnant** : le vainqueur de la partie remporte la victoire
  **et le territoire pour son royaume**. Pas de cas multi-gagnants.
- **Limite de temps paramétrable** (admin) : au bout de X, la partie
  s'arrête et le vainqueur est le joueur avec le **plus gros score** à
  cet instant.
- **À définir** : cette limite de temps est-elle une valeur unique
  partagée avec l'exploration (D5) ou deux valeurs séparées ?

## D7 — Défense : n'importe quel seigneur

- Face à une attaque contre son royaume, **n'importe quel seigneur du
  royaume défenseur** peut défendre (pas seulement le propriétaire du
  territoire).

## D8 — Absence de défenseur : paramètre admin

- Si aucun défenseur ne répond dans le délai, le comportement est un
  **paramètre d'administration** à deux valeurs :
  1. **victoire automatique** de l'attaquant (territoire capturé sans
     jouer) ;
  2. **partie contre l'IA** : la rencontre se joue en multijoueur sur
     la map indiquée contre l'IA, selon les paramètres IA du royaume.

## D9 — Technologies : coûts paramétrables

- **Tous les coûts des technologies sont paramétrables** ; les valeurs
  de la référence (Embuscade 2, Traquenard 1, Patrouille 2,
  Contre-espionnage 2, Sabotage 1, Explorateur 2, Jeu d'armes 1,
  Mariage arrangé 3, Corruption 4, Garde Royale 1) sont les
  **valeurs par défaut**.

## D10 — Embuscade

- Un royaume disposant de la technologie Embuscade obtient une
  **attaque supplémentaire** ; le royaume attaqué peut défendre **sans
  dépenser son point de défense** (c'est une attaque d'embuscade).

## D11 — Contre-espionnage

- Disponible si le royaume possède la technologie. Lors de la
  déclaration d'une attaque sur un territoire, une **option
  supplémentaire** permet d'indiquer le nom d'un autre seigneur —
  existant et jouant la partie — de n'importe quel royaume (la
  couverture). **X temps avant le lancement de la partie**
  (paramétrable par l'admin), l'identité du **vrai attaquant** est
  révélée.

## D12 — Sabotage

- Utilisable **en attaque ou en défense**, **avant le début de la
  partie**, uniquement dans les attaques **seigneur contre seigneur**
  (royaume contre royaume) — **indisponible contre Gaïa**.
- Phase de snipe : chaque camp **retire de la liste des civilisations**
  une civilisation que son adversaire ne pourra pas jouer (et
  réciproquement). Maximum **2 par partie**.

## D13 — Explorateur

- Le royaume **reçoit la map gratuitement et immédiatement** (territoire
  de Gaïa, sans déclaration d'attaque, sans partie).

## D14 — Garde Royale

- Protège un territoire **sur une durée** : rend l'attaque du
  territoire impossible.
- La protection est de **24h**, prolongeable : dépenser **1 point de
  technologie ajoute 24h** supplémentaires.

## D15 — Corruption

- Permet d'obtenir un territoire **de n'importe quel royaume ou de
  Gaïa** en dépensant **4 points technologiques** (défaut).
- Le territoire obtient un statut **inattaquable** — et les autres
  joueurs ne peuvent pas non plus le **corrompre** — **jusqu'au cycle
  prochain**.

## D16 — Victoire de saison : Conquête

- Le royaume vainqueur est celui disposant du **plus de territoires** à
  la fin de la saison — type de victoire nommé **« Conquête »**.
- La règle pourra évoluer par la suite (autres types de victoire
  envisageables plus tard).

## D17 — Partie non jouée contre un royaume joueur

- Si l'attaquant ne s'est pas présenté, **l'attaque est consommée**.
- **Exception admin** : selon son appréciation, l'admin peut
  **réattribuer le point d'attaque** si l'absence a une excuse valable.

## D18 — Échelle numérique de l'IA

- Échelle validée : **1=Facile, 2=Standard, 3=Intermédiaire,
  4=Difficile, 5=Extrême** ; les effets se combinent avec plancher 1
  et plafond 5.
- **La progression d'IA liée aux époques ne concerne que Gaïa**
  (Âge sombre=2, Féodal=3, Châteaux=5, Impérial=5) — **pas** les
  royaumes joueurs.
- Pour qu'un royaume dispose d'une IA plus forte (défense contre les
  bots), il faut utiliser **Jeu d'armes** : effet **permanent** (+1
  niveau).
- **Traquenard** réduit le niveau de l'IA **d'un royaume joueur ou de
  Gaïa** — effet **temporaire (une seule fois par utilisation)**,
  contrairement à Jeu d'armes. Traquenard **peut se cumuler** si le
  joueur en dispose plusieurs, à sa guise.

## D19 — Traités : paramètres de vote

- Qui vote : **paramétrable** — uniquement les Rois, ou tous les
  seigneurs.
- Majorité : **paramétrable** — 50%+1, ou unanimité.
- Si le vote est positif, un message annonce que **les Dieux ont
  entendu leurs paroles** ; l'application est **soit au cycle
  prochain, soit à la saison suivante** (selon la demande).
- La **durée dépend de la demande**.
- **Un seul traité par saison**.

## D20 — Validation des résultats

- Les joueurs valident le résultat, qui est **retrouvé
  automatiquement** : AoE2 respecte le **game contract** — le cœur de
  la plateforme gère déjà la récupération des résultats
  (`games/aoe2` + providers ext-librematch / ext-aoe2lobby, ADR-0020).
- En cas de litige, **l'admin tranche**.
