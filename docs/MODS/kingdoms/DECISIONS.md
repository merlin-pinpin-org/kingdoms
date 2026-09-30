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
- **Pas de limite de temps** pour les attaques contre Gaïa (la limite
  de temps paramétrable s'applique uniquement à l'exploration —
  décision D44).

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
  réciproquement).
- **Maximum 2 sabotages par seigneur et par rencontre** ; le compteur
  repart à zéro à la rencontre suivante (un seigneur peut détenir
  plusieurs sabotages, sans limite de stock).

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

## D21 — Nom de royaume

- Validé par **l'admin** ; longueur et caractères autorisés
  **paramétrables** par l'admin. L'admin peut aussi **imposer les
  noms** des royaumes (mode royaumes imposés).
- Hors périmètre actuel (version ultérieure) : bonus particuliers
  attribués à chaque royaume.

## D22 — Effectif des royaumes

- Un royaume peut démarrer avec **un Roi seul** ; les limites du
  nombre de seigneurs requis sont **paramétrables** par l'admin.

## D23 — File d'attente, départ et remplacement

- Des joueurs peuvent s'inscrire **sans royaume** (en **attente**),
  pour des raisons d'équilibrage.
- Un joueur peut **quitter la saison en cours** (option avec motif
  indiqué) ; l'admin peut alors affecter un **joueur en attente**.
- Le remplaçant **reprend l'état d'attaque/défense de la semaine** du
  joueur sortant : si celui-ci avait déjà attaqué, le remplaçant ne
  peut pas non plus attaquer (anti-abus).

## D24 — Échange de joueurs entre royaumes

- Uniquement **en fin de cycle → nouveau cycle** : des joueurs peuvent
  être **intervertis** entre royaumes. Les **liens de mariages suivent
  la position** : si A (marié à l'Éthiopie) échange sa place avec B,
  B devient marié à l'Éthiopie.

## D25 — Remplacement d'un seigneur parti

- Un remplaçant ne récupère **que le mariage lié à la personne** ;
  les **territoires et les points sont communs** aux seigneurs du
  même royaume (donc rien à transférer).

## D26 — Remplacement du Roi

- Le Roi peut être **remplacé par un seigneur du même royaume**.

## D27 — Qui déclare une attaque

- **N'importe quel seigneur** peut déclarer une attaque (pas besoin de
  l'accord du Roi).

## D28 — Sabotage & Contre-espionnage : saisie

- **Sabotage** : les joueurs indiquent **sur Discord dans la fenêtre
  d'attaque/défense** s'ils font usage d'un sabotage, **juste avant la
  rencontre**.
- **Contre-espionnage** : proposé **lors de la déclaration
  d'attaque** — le joueur peut déclarer l'attaque **au nom d'un autre
  joueur** (cf. D11).

## D29 — Égalité à l'exploration

- En cas d'égalité, **le gain est attribué aux deux joueurs**.

## D30 — Exploration : aucun ou un seul participant

- **Aucun participant** : la map est ajoutée au royaume de Gaïa.
- **Un seul participant** : il obtient **automatiquement la map avec
  le lot du 1er**, sans nécessité de la jouer.

## D31 — Jour du Seigneur : épuisement des maps

- Improbable en pratique ; règle de repli : **lorsque Gaïa ne peut
  plus disposer de 8 nouvelles maps, la partie (saison) s'arrête
  automatiquement**.

## D32 — Alliances & civilisations

- Correspondance **map → civilisations** fournie par l'admin (le
  game designer fournira la table) ; l'obtention de certaines
  civilisations répond à des **pré-requis fournis par l'admin**.
- En début de saison, chaque royaume reçoit **X civilisations**
  (paramétrable par l'admin). **À la fin de chaque cycle**, les
  alliances s'actualisent **en fonction des mariages et des
  territoires conquis** ; on peut obtenir des civilisations au début
  puis **les perdre ensuite**.

## D33 — Choix des civilisations en partie

- Le bot **actualise automatiquement** la liste des civilisations
  jouables par royaume ; chaque seigneur choisit sa civilisation à sa
  convenance, à condition d'y **avoir accès** et qu'elle ne soit pas
  **sabotée** (un seigneur ne peut pas empêcher l'autre d'obtenir sa
  civilisation).

## D34 — Mariages

- Chaque seigneur peut se marier **une fois** ; la promise est une
  reine, princesse ou autre personnalité **ayant réellement existé**
  par civilisation (liste fournie par le game designer) — rôle **RP
  uniquement**, sans importance mécanique.
- Si le seigneur **perd un combat**, il perd le mariage : **au cycle
  prochain** il perdra l'effet du mariage.

## D35 — Traquenard / Jeu d'armes : durée des effets

- **Traquenard** expire **à la fin du combat**.
- **Jeu d'armes** s'active **automatiquement** à l'obtention et reste
  **jusqu'à la fin de la saison**.

## D36 — Achat multiple de technologies

- Un royaume peut acheter **plusieurs fois la même technologie** si
  les conditions sont respectées ; chaque technologie a un
  **paramètre de limite d'obtention**.

## D37 — Corruption : fin de protection

- La protection tombe **lundi minuit** (après le dimanche du cycle).

## D38 — Fin de saison

- La saison se termine **le lundi qui suit le dimanche du 4e cycle**
  (après les 4 cycles), à minuit — précisé par D52.

## D39 — Litiges techniques en partie

- Le joueur utilise une **sauvegarde du jeu** pour continuer la
  partie ; **l'admin se réserve le droit de trancher**. La règle sera
  ajoutée au règlement.

## D40 — Fair-play & sanctions

- Gestion **humaine** (admin) ; des règles de comportement seront
  ajoutées au règlement (document à part).

## D41 — Garnison : confirmée en pause

- Renforts et garnisons sont **mis de côté** ; réintroduits plus
  tard. Le combat d'attaque contre un royaume joueur est donc
  **1 attaquant vs 1 défenseur**, sans renforts.

## D42 — Attaques simultanées

- Un territoire avec une déclaration d'attaque **en cours ne peut pas
  être ciblé** par une nouvelle attaque.
- Un royaume peut **subir plusieurs attaques simultanées** sur des
  territoires différents.

## D43 — Patrouille

- Permet à un royaume de **refuser un créneau horaire d'agression**
  (ex. minuit–2h) : impossible pour les autres royaumes d'attaquer
  dans cette tranche. Application **immédiate** ; une attaque déclarée
  **avant** l'application dans cette tranche **n'est pas annulée**,
  mais aucune nouvelle attaque n'y sera possible ensuite.
- Un royaume peut **modifier sa tranche**, applicable **au cycle
  prochain**.
- **Maximum 2 patrouilles par royaume et par saison**, donc 4h de
  tranquillité au total si les deux sont possédées.

## D44 — Limite de temps : uniquement l'exploration

- **Pas de limite de temps** pour les attaques contre Gaïa.
- La **limite de temps paramétrable** s'applique **uniquement au FFA
  du samedi (exploration)** : au bout de X, le vainqueur est le
  joueur au plus gros score.

## D45 — Mariage arrangé vs mariage standard

- Le mariage arrangé donne **l'exclusivité** d'une civilisation,
  **appliquée instantanément**.
- Le mariage standard s'obtient **gratuitement via les âges/époques** ;
  la règle **d'un mariage par seigneur ne peut pas être contournée**
  (même par le mariage arrangé).
- « Si le seigneur meurt » = **perd un combat**, même logique que D34.

## D46 — Cadastre et conditions de civilisations

- Fournis par le game designer (Saison II) : effet de chaque map au
  Jour du Seigneur ([CADASTRE.md](CADASTRE.md)) et conditions
  d'obtention de chaque civilisation
  ([CIVILIZATIONS.md](CIVILIZATIONS.md)).
- Types d'effets de cadastre observés : offrir une technologie
  ponctuelle (par jour/semaine/dimanche), un point de technologie,
  une civilisation, un mariage, une embuscade, un sabotage, un
  contre-espionnage, une exploration, réduire/augmenter des délais
  d'agression, augmenter la capacité de patrouille, offrir une
  garnison (garnisons en pause — D41), ou une map désignée /
  points de technologie au choix.
- **À valider/traduire en grammaire** : certaines conditions de
  civilisations sont référentielles (Hongrois = « appartenir au
  Royaume des HeN », Shu/Wei/Wu = posséder « Chinois ») et plusieurs
  comportent des seuils paramétrables (nombre de maps, types
  d'environnement) ; les types de maps (eaux, ouverte, nomade,
  désert/sable, montagne/colline, marais, lacs, dorée/or, start
  wall) doivent être saisis dans le catalogue de maps de l'admin.

## D47 — Garde Royale : compléments

- **Pas de cumul** : impossible de poser plusieurs Gardes Royales sur
  le même territoire.
- Achat : **24h de protection** sans autre dépense ; **prolongation :
  1 point de technologie pour 3h** (et non 24h).

## D48 — Explorateur : correction

- Le royaume reçoit une **map aléatoire qui n'est pas encore sortie**
  (pas une map possédée par Gaïa) — tirée parmi la **liste des maps
  possibles** (autorisées), donc jamais protégée par Corruption ou
  Garde Royale.
- **Consommable** : après usage, l'effet ne peut plus être réactivé —
  il faut relancer une nouvelle acquisition (expédition).
- La map reçue devient un **territoire du royaume immédiatement**.

## D49 — Ordre Royal = traité (une seule mécanique)

- Avec l'âge requis (Âge féodal), le royaume ayant le plus
  d'**alliances** obtient l'**Ordre Royal**, qui lui donne le droit de
  **proposer le traité** de la saison (un seul traité par saison —
  D19). Ordre Royal et traité ne sont donc **qu'une seule et même
  mécanique** : le porteur de l'Ordre Royal propose, les participants
  votent (paramètres D19), et si voté, l'application suit la demande
  (cycle prochain ou saison suivante).
- Si le porteur ne propose rien dans son délai (D51), **l'opportunité
  est perdue** : il n'existe qu'un Ordre Royal par saison, sans
  réévaluation.

## D50 — ShowMatch PA2 (égalité finale)

- **PA2 = Play All 2** : les joueurs doivent jouer **les deux
  matchs obligatoirement** (contrairement au Best-Of) — le vainqueur
  d'une manche PA2 est désigné **au score sur l'ensemble des deux
  matchs**.
- **Format : 1v1 PA2 successifs**. Premier duel entre un joueur de
  chaque royaume : si **2-0**, son royaume remporte la manche ; si
  **1-1**, un **autre seigneur** de chaque royaume enchaîne un
  nouveau PA2, et ainsi de suite jusqu'à un **2-0**.
- **Choix des maps et civilisations** : chaque royaume choisit ses
  maps **parmi ses propres territoires** et ses civilisations
  disponibles ; **aucune map ni civilisation ne peut être
  réutilisée** au cours du ShowMatch.
- **Repli** : si un royaume n'a plus de civilisations ou de
  territoires disponibles, la suite se joue sur **Megarandom en
  civilisation aléatoire**.
- **Suite du ShowMatch** : on continue jusqu'à une victoire ; si tous
  les 1v1 ont eu lieu, le format passe en **2v2, puis 3v3**, et ainsi
  de suite.

## D51 — Ordre Royal : attribution et délai

- **Alliance = civilisation** (le royaume ayant le plus de
  civilisations).
- Attribué **au passage d'Âge féodal (mercredi minuit)** ; il n'en
  existe **qu'un seul** par saison, manifesté au féodal.
- Le Roi porteur de l'Ordre Royal dispose de **24h pour faire sa
  proposition de traité** (délai paramétrable par l'admin) ; passé ce
  délai, **l'opportunité est perdue**.
- Le vote suit les paramètres D19 (Rois ou tous les seigneurs ;
  50%+1 ou unanimité).

## D52 — Heure de fin de saison

- La saison se termine **lundi minuit**, après le Jour du Seigneur du
  4e cycle (en cohérence avec D37, fin de la protection Corruption).

## D53 — Mariages : durée et budget

- Un mariage est **permanent** jusqu'à ce que le seigneur marié
  **perde un combat** (il perd alors le mariage, effet retiré au
  cycle prochain — D34).
- **Chaque seigneur peut se marier une seule fois** ; les « +1
  mariage » d'époque augmentent la **capacité de mariages du
  royaume** (nombre de seigneurs pouvant être mariés au total).

## D54 — Liste des promises

- La liste des personnalités historiques (promises par civilisation)
  est déposée dans [PROMISES.md](PROMISES.md) — **RP uniquement**.
- Elle couvre plus de civilisations que les 50 conditions documentées
  (Danois, Magyars, Mapuche, Muisca, Saxons, Tupi, Varègues…) :
  promises disponibles dès qu'une civilisation est obtenue.
