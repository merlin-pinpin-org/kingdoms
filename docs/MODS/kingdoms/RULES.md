# Kingdoms mod — Règles

> Source fonctionnelle : la référence Season II
> ([../../PLANS/reference/kingdoms-mod-saison2.md](../../PLANS/reference/kingdoms-mod-saison2.md))
> corrigée par [DECISIONS.md](DECISIONS.md). Chaque règle ci-dessous est
> écrite pour être **automatisable** (testable par le bot). Tout point
> **À DÉFINIR** doit être tranché par le game designer avant
> l'implémentation correspondante — jamais inventé.

## Saison et cycle

1. Une saison dure par défaut **4 semaines = 4 cycles** (un cycle =
   une semaine — décision D1) ; toutes les valeurs sont configurables.
2. La saison est **lancée manuellement** par l'admin (date/heure
   annoncées) ; le passage de saison n'est jamais automatique.
3. Lancer une nouvelle saison **réinitialise toutes les données de
   saison** ; la configuration est conservée et modifiable. Les maps
   sont réutilisables entre saisons.
4. La bascule de cycle a lieu au **Jour du Seigneur (dimanche 23h30)** ;
   les points d'attaque/défense se rechargent à la bascule (1 attaque +
   1 défense par seigneur et par semaine).

## Royaumes et inscription

5. Nombre de royaumes (2 par défaut) et de seigneurs par royaume (4 par
   défaut) : configurables. Gaïa est le royaume IA, ni jouable ni
   inscriptible.
6. Royaumes **imposés** (définis par l'admin) ou **non imposés** : les
   joueurs choisissent Roi ou Seigneur ; un Roi suggère le nom de son
   royaume ; les suivants rejoignent un royaume existant.
   **À DÉFINIR** : validation du nom de royaume ; nombre minimum de
   joueurs par royaume ; départ/changement/remplacement d'un joueur.

## Territoires et maps

7. Un territoire = une map AoE2, tirée aléatoirement depuis la
   **liste autorisée** définie par l'admin ; **aucun doublon** pendant
   la saison ; défaut : 5 par royaume joueur + 8 pour Gaïa (18 maps).
8. Une map est « utilisée » dès sa première sortie (attribution
   initiale, Jour du Seigneur, exploration) et ne peut plus être tirée
   avant la saison suivante.
9. Si la liste autorisée devient insuffisante, le bot **avertit
   l'admin**.
10. L'admin peut **éjecter une map** (bug, problème) : le bot la retire
    et tire automatiquement un remplacement non sorti dans la liste
    autorisée ; s'il n'en reste aucune, l'admin est prévenu.

## Attaques et défenses

11. Déclaration dans `⚔️-attaquer`. **Contre un royaume joueur** :
    délai 6h (configurable), l'attaquant fournit le lobby
    `aoe2de://…` ; victoire de l'attaquant = territoire capturé,
    défaite = le défenseur le garde. **À définir** : format exact
    (1v1 ?), qui défend (propriétaire ou n'importe quel seigneur ?),
    non-réponse du défenseur dans le délai, partie non jouée,
    validation des résultats.
12. **Contre Gaïa** : délai 3h (configurable) ; max **1 seigneur par
    royaume**, **7 max** au total ; le premier déclarant réserve le
    territoire et le créneau ; les autres rejoignent la même attaque.
13. Attaque Gaïa = **FFA chacun pour soi** (décision D6) : un seul
    gagnant, qui remporte le territoire pour son royaume. Limite de
    temps paramétrable : à l'échéance, le plus gros score gagne.
14. Partie non jouée ou abandon (Gaïa) : **l'attaque est consommée et
    Gaïa gagne**. **À définir** : équivalent contre royaume joueur ;
    déconnexions et problèmes techniques.

## Époques (mercredi minuit, configurable)

15. Âge sombre → féodal → châteaux → impérial. L'IA de Gaïa et les
    bonus royaume évoluent par époque :
    - **Âge sombre** : IA Standard ; +1 mariage (+1 garnison inactif — D4)
    - **Âge féodal** : IA Intermédiaire ; +1 tech, +1 mariage ;
      Ordre Royal et traités débloqués
    - **Âge des châteaux** : IA Extrême ; +2 tech, +1 mariage
    - **Âge impérial** : IA Extrême ; +2 tech, +1 mariage
16. « +N technologies » = des **points technologiques** (monnaie — D2) ;
    « +1 mariage » = un mariage **utilisable** supplémentaire (D3,
    cumul à définir).
17. **À définir** : échelle numérique commune des niveaux IA
    (proposé : 1=Facile … 5=Extrême) pour combiner époques +
    Traquenard (−2) + Jeu d'armes (+1).

## Événements hebdomadaires

18. **Exploration — samedi 14h** (configurable) : vraie partie AoE2
    **FFA** (D5), participation **optionnelle** (1 seigneur par
    royaume max) ; une map non sortie est tirée ; classement final de
    la partie : 1er remporte la map (territoire de son royaume) + 1
    tech ; 2e : +3 tech ; 3e : +2 tech ; autres participants : +1 tech.
    **À définir** : égalités, absences, problèmes techniques ; limite de
    temps (proposé : partagée avec les attaques Gaïa, D6).
19. **Jour du Seigneur — dimanche 23h30** (configurable) :
    1) ajout de 8 maps (configurable) à Gaïa tirées parmi les non
    sorties ; 2) application du **cadastre** (effets de maps définis
    par l'admin — **à définir** : grammaire des effets) ; 3)
    actualisation des **alliances** selon les territoires possédés.

## Diplomatie, mariages, traités

20. Alliances liées aux civilisations, recalculées au Jour du
    Seigneur selon les territoires. **À définir** : règles complètes de
    calcul, draft civilisationnel, choix des civilisations.
21. Mariage : lie un seigneur au Roi/à la Reine d'une civilisation ;
    sécurise la civilisation pour le royaume ; si le seigneur marié
    perd un combat, l'alliance tombe. **À définir** : fonctionnement
    administratif détaillé.
22. Traités (dès l'Âge féodal) : proposés par le royaume possédant le
    plus de civilisations, votés POUR/CONTRE, annoncés dans
    `📣-géopolitique`. **À définir** : qui vote exactement, majorité,
    durée, annulation.
23. Ordre Royal (Âge féodal) : royaume avec le plus d'alliances ; son
    Roi propose une règle supplémentaire soumise au vote ; si votée,
    les développeurs tentent de l'implémenter à l'Âge des châteaux
    (sinon reportée à une saison suivante).
24. **Égalité finale** : ShowMatch PA2 ; chaque royaume choisit une
    map parmi ses territoires ; en cas d'égalité persistante, on
    ajoute des joueurs et une nouvelle map jusqu'à départage.
    **À définir** : format exact.

## Technologies (monnaie — D2)

25. Points technologiques gagnés aux époques, à l'exploration (D5) et
    par effets (Garde Royale, Corruption vers l'ennemi), dépensés en
    actions spéciales. **À définir** : fonctionnement détaillé de chaque
    action (répétabilité, cibles, créneaux) :
    - Embuscade (2) : attaque supplémentaire, délai mini 1h, défense
      volontaire sans consommer de point de défense
    - Traquenard (1) : −2 niveaux IA Gaïa
    - Patrouille (2) : refuse un créneau d'agression de 2h ; 2
      utilisations permanentes
    - Contre-espionnage (2) : attaque via un autre membre (vrai
      attaquant caché)
    - Sabotage (1) : snipe, max 2 par partie
    - Explorateur (2) : obtient une map de Gaïa sans déclaration
      d'attaque
    - Jeu d'armes (1) : +1 niveau de difficulté IA en défense contre
      les bots
    - Mariage arrangé (3) : exclusivité d'une civilisation via
      mariage ; perdue si le seigneur meurt
    - Corruption (4) : achète un territoire sans confrontation ;
      l'ennemi reçoit +1 tech ; **à définir** : durée de protection
    - Garde Royale (1) : protège un territoire ; +1 tech / 24h ;
      **à définir** : portée de la protection

## Garnison

26. **Mise de côté** pour équilibrage (Saison II) : aucune règle
    active ; les règles envisagées (transformation de points, renforts,
    max 3 garnisons / 3 renforts) sont **en travaux, non définitives**.
