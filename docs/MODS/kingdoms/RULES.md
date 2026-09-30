# Kingdoms mod — Règles

> Source fonctionnelle : la référence Season II
> ([../../PLANS/reference/kingdoms-mod-saison2.md](../../PLANS/reference/kingdoms-mod-saison2.md))
> corrigée par [DECISIONS.md](DECISIONS.md). Chaque règle ci-dessous est
> écrite pour être **automatisable** (testable par le bot). Tout point
> **À DÉFINIR** doit être tranché par le game designer avant
> l'implémentation correspondante — jamais inventé.

## Saison et cycle

1. Une saison dure par défaut **4 semaines = 4 cycles** (un cycle =
   une semaine — D1) ; toutes les valeurs sont configurables (D9).
2. La saison est **lancée manuellement** par l'admin (date/heure
   annoncées) ; le passage de saison n'est jamais automatique.
3. Lancer une nouvelle saison **réinitialise toutes les données de
   saison** ; la configuration est conservée et modifiable. Les maps
   sont réutilisables entre saisons.
4. La bascule de cycle a lieu au **Jour du Seigneur (dimanche 23h30)** ;
   les points d'attaque/défense se rechargent à la bascule (1 attaque +
   1 défense par seigneur et par semaine). À chaque bascule, le bot
   publie **la Gazette** dans `📣-géopolitique` : résumé du cycle
   (territoires par royaume, alliances, technologies dépensées) — D1.
5. La saison se termine **le lundi minuit qui suit le Jour du Seigneur
   du 4e cycle** (D38/D52) ; le vainqueur est désigné à ce moment.

## Royaumes et inscription

6. Nombre de royaumes (2 par défaut) et de seigneurs par royaume (4 par
   défaut) : configurables. Gaïa est le royaume IA, ni jouable ni
   inscriptible.
7. Royaumes **imposés** (noms définis par l'admin) ou **non imposés** :
   les joueurs choisissent Roi ou Seigneur ; un Roi suggère le nom de
   son royaume, validé par l'admin (longueur et caractères
   paramétrables — D21) ; les suivants rejoignent un royaume existant.
   Un royaume peut démarrer avec **un Roi seul** (D22).
8. Des joueurs peuvent s'inscrire **en attente** (sans royaume) ;
   un joueur peut **quitter la saison** (option + motif) et l'admin
   affecte un joueur en attente en remplacement ; le remplaçant
   **reprend l'état attaque/défense de la semaine** du sortant
   (anti-abus — D23). Le Roi peut être remplacé par un seigneur du
   même royaume (D26).
9. Des joueurs peuvent être **intervertis entre royaumes uniquement en
   fin de cycle → nouveau cycle** ; les liens de mariages suivent la
   position (D24).

## Territoires et maps

10. Un territoire = une map AoE2, tirée aléatoirement depuis la
    **liste autorisée** définie par l'admin ; **aucun doublon** pendant
    la saison ; défaut : 5 par royaume joueur + 8 pour Gaïa (18 maps).
11. Une map est « utilisée » dès sa première sortie (attribution
    initiale, Jour du Seigneur, exploration, Explorateur) et ne peut
    plus être tirée avant la saison suivante.
12. Si la liste autorisée devient insuffisante, le bot **avertit
    l'admin**. Si Gaïa ne peut plus recevoir ses 8 nouvelles maps au
    Jour du Seigneur, **la saison s'arrête automatiquement** (D31).
13. L'admin peut **éjecter une map** (bug, problème) : le bot la retire
    et tire automatiquement un remplacement non sorti dans la liste
    autorisée ; s'il n'en reste aucune, l'admin est prévenu.

## Attaques et défenses

14. Déclaration dans `⚔️-attaquer` : **n'importe quel seigneur** peut
    déclarer (D27). **Contre un royaume joueur** : délai 6h
    (configurable), l'attaquant fournit le lobby `aoe2de://…` ;
    victoire de l'attaquant = territoire capturé, défaite = le
    défenseur le garde.
15. Le combat est **1v1** : un attaquant contre un défenseur, sans
    renforts ni garnison (D41) ; **n'importe quel seigneur du royaume
    défenseur** peut défendre (D7).
16. Si aucun défenseur ne répond dans le délai : comportement
    **paramétrable admin** — victoire automatique de l'attaquant, ou
    partie contre l'IA sur la map (D8).
17. Attaquant absent : **l'attaque est consommée** ; l'admin peut
    réattribuer le point d'attaque sur excuse valable (D17). Résultats
    récupérés **automatiquement via le game contract** ; litige =
    l'admin tranche (D20) ; problème technique = sauvegarde de la
    partie, l'admin tranche (D39).
18. Un territoire avec une attaque **en cours ne peut pas être ciblé**
    à nouveau ; un royaume peut subir plusieurs attaques simultanées
    sur des territoires différents (D42).
19. **Contre Gaïa** : délai 3h (configurable) ; max **1 seigneur par
    royaume**, **7 max** au total ; le premier déclarant réserve le
    territoire et le créneau ; les autres rejoignent la même attaque.
20. Attaque Gaïa = **FFA chacun pour soi** (D6) : un seul gagnant, qui
    remporte le territoire pour son royaume. **Pas de limite de
    temps** (D44). Partie non jouée ou abandon : **l'attaque est
    consommée et Gaïa gagne**.

## Époques (mercredi minuit, configurable)

21. Âge sombre → féodal → châteaux → impérial. L'IA de Gaïa évolue sur
    l'échelle numérique **1=Facile … 5=Extrême** (D18) :
    - **Âge sombre** : IA 2 (Standard) ; +1 mariage
    - **Âge féodal** : IA 3 (Intermédiaire) ; +1 tech, +1 mariage ;
      Ordre Royal attribué (D51)
    - **Âge des châteaux** : IA 5 (Extrême) ; +2 tech, +1 mariage
    - **Âge impérial** : IA 5 (Extrême) ; +2 tech, +1 mariage
22. « +N technologies » = des **points technologiques** (monnaie — D2) ;
    « +1 mariage » = un mariage supplémentaire : la **capacité de
    mariages du royaume** (nombre de seigneurs pouvant être mariés)
    augmente d'une unité à chaque époque (D53).
23. La progression d'IA des époques ne concerne **que Gaïa** ; l'IA
    d'un royaume joueur ne change que par technologies : **Jeu
    d'armes** (+1 permanent jusqu'à la fin de saison) et **Traquenard**
    (−1 par utilisation, expire à la fin du combat, cumulable — D18,
    D35). Plancher 1, plafond 5.

## Événements hebdomadaires

24. **Exploration — samedi 14h** (configurable) : vraie partie AoE2
    **FFA** (D5), participation **optionnelle** (1 seigneur par
    royaume max) ; une map non sortie est tirée ; classement final de
    la partie : 1er remporte la map (territoire de son royaume) + 1
    tech ; 2e : +3 tech ; 3e : +2 tech ; autres participants : +1 tech.
    **Limite de temps paramétrable** : à l'échéance, le plus gros
    score gagne (D44). Égalité : **le gain est attribué aux deux
    joueurs** (D29). Aucun participant : la map va à Gaïa ; un seul
    participant : il obtient la map + le lot du 1er sans jouer (D30).
25. **Jour du Seigneur — dimanche 23h30** (configurable) :
    1) ajout de 8 maps (configurable) à Gaïa tirées parmi les non
    sorties ; 2) application du **cadastre**
    ([CADASTRE.md](CADASTRE.md)) ; 3) actualisation des **alliances**
    selon les territoires possédés et les mariages (D32).

## Diplomatie, mariages, traités

26. Alliances = civilisations (D51), recalculées **à la fin de chaque
    cycle** selon les mariages et les territoires conquis ; en début
    de saison chaque royaume reçoit X civilisations (paramétrable) ;
    on peut obtenir des civilisations puis les perdre (D32). Conditions
    d'obtention : [CIVILIZATIONS.md](CIVILIZATIONS.md).
27. Le bot **actualise automatiquement** la liste des civilisations
    jouables par royaume ; chaque seigneur choisit sa civilisation à
    sa convenance, à condition d'y avoir accès et qu'elle ne soit pas
    **sabotée** (D33).
28. Mariage : chaque seigneur peut se marier **une fois** (D34) ; il
    sécurise une civilisation pour le royaume ; la promise est une
    personnalité historique (RP uniquement — D54,
    [PROMISES.md](PROMISES.md)). Le mariage est **permanent jusqu'à
    ce que le seigneur perde un combat** (effet retiré au cycle
    prochain — D34/D53). Le **mariage arrangé** (3 techs) donne
    l'**exclusivité** instantanée d'une civilisation sans contourner
    la limite d'un mariage par seigneur (D45).
29. **Ordre Royal = traité** (une seule mécanique — D49/D51) : à
    l'entrée à l'Âge féodal, le royaume ayant le **plus de
    civilisations** l'obtient ; son Roi dispose de **24h**
    (paramétrable) pour proposer le traité de la saison — un seul
    traité par saison (D19) ; vote POUR/CONTRE paramétrable (Rois ou
    tous les seigneurs ; 50%+1 ou unanimité — D19) ; si voté :
    annonce « les Dieux ont entendu leurs paroles » et application au
    cycle prochain ou à la saison suivante selon la demande ; sans
    proposition dans le délai, l'opportunité est perdue.

## Technologies (monnaie — D2/D9)

30. Points technologiques gagnés aux époques, à l'exploration, par le
    cadastre et par effet (Corruption : +1 tech à l'ennemi) ;
    dépensés en actions spéciales. **Coûts et limites paramétrables**
    (D9/D36) ; un royaume peut acheter plusieurs fois la même
    technologie dans la limite d'obtention de chacune. Les dix
    actions :
    - **Embuscade** (2) : attaque supplémentaire ; le défenseur
      volontaire ne dépense pas son point de défense (D10)
    - **Traquenard** (1) : −1 niveau IA (royaume joueur ou Gaïa) par
      utilisation, expire fin de combat, cumulable (D18/D35)
    - **Patrouille** (2) : crée un créneau horaire de 2h où toute
      attaque est refusée ; application immédiate, modification au
      cycle prochain ; **2 patrouilles max par royaume et par
      saison** (D43)
    - **Contre-espionnage** (2) : déclarer l'attaque au nom d'un autre
      seigneur (la couverture) ; révélation du vrai attaquant X temps
      avant la partie, paramétrable (D11/D28)
    - **Sabotage** (1) : snipe de civilisations en attaque ou défense,
      uniquement royaume contre royaume ; **2 max par seigneur et par
      rencontre**, compteur remis à zéro à la rencontre suivante (D12)
    - **Explorateur** (2) : map aléatoire **non sortie** reçue
      gratuitement et immédiatement, devient territoire du royaume ;
      consommable (D48)
    - **Jeu d'armes** (1) : +1 niveau IA permanent jusqu'à la fin de
      saison (D18/D35)
    - **Mariage arrangé** (3) : exclusivité instantanée d'une
      civilisation (D45)
    - **Corruption** (4) : achète un territoire de n'importe quel
      royaume ou de Gaïa sans confrontation ; l'ennemi reçoit +1
      tech ; territoire inattaquable et incorruptible **jusqu'à
      lundi minuit** (D15/D37)
    - **Garde Royale** (1) : 24h de protection d'un territoire ;
      prolongation 1 tech = **3h** ; pas de cumul sur un même
      territoire (D47)

## Garnison

31. **Mise de côté** pour équilibrage (Saison II — D4/D41) : aucune
    règle active ; les règles envisagées (transformation de points,
    renforts, max 3 garnisons / 3 renforts) sont **en travaux, non
    définitives**. Les effets « garnison » du cadastre sont conservés
    mais **inactifs**.
