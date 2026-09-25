# Guide du game designer — décrire une idée, la voir livrée

Cette page est le point d'entrée du **game designer** : elle explique comment
transformer une idée en fonctionnalité visible dans Discord, sans jamais
toucher à un outil technique. Tout le travail technique est fait par l'agent
(agent sessions) ou par CI — voir [VIBEWORKFLOW.md](VIBEWORKFLOW.md) pour le
modèle complet et [PROCESS.md](PROCESS.md) pour le détail par rôle.

## Ce que vous faites, concrètement

1. **Vous décrivez l'idée dans une session agent** (Discord ou session).
   Pas besoin d'un format précis pour commencer — l'agent vous pose des
   questions et transforme la discussion en **issue GitHub** structurée
   (objectif, contexte, critères d'acceptation) que vous relisez et validez.
2. **L'agent implémente et ouvre une PR.** Vous ne suivez pas la PR elle-même :
   quand l'agent annonce que le déploiement de test est prêt, **vous testez
   dans Discord** sur le serveur de test.
3. **Vous validez le comportement** en jouant. C'est votre unique critère de
   qualité fonctionnelle : est-ce que le bot fait ce que vous aviez en tête ?
4. **Le développeur (ou ops) relit et fusionne la PR.** Vous n'avez pas besoin
   de droits de fusion — c'est volontaire.
5. Pour que la fonctionnalité arrive chez les vrais joueurs, elle doit faire
   partie d'une **version publiée** (`vX.Y.Z`) — demandez simplement à
   l'agent « on publie une version ? » et suivez le fil.

## Comment bien décrire une idée

Une idée bien décrite économise un aller-retour. Les éléments qui aident
l'agent (dans n'importe quel ordre, en langage courant) :

- **Le résultat attendu vu par un joueur** : « quand un joueur tape
  `/royaume`, il voit son château et ses ressources ».
- **Les règles du jeu** : chiffres, durées, limites, ce qui est permis ou
  interdit. Si une règle vous semble floue, dites-le — l'agent vous aidera
  à la rendre précise et automatisable.
- **Un exemple de scénario** : « le joueur A attaque, le joueur B défend,
  voici ce qui devrait se passer ».
- **Ce qui ne doit pas changer** : les interactions existantes à préserver.

L'agent **challenge** systématiquement la conception : il peut proposer une
variante plus simple à automatiser, soulever une contradiction entre deux
règles, ou découper une grosse idée en étapes livrables une par une. C'est
normal et voulu — répondez simplement en langage courant.

## Où tester : le serveur de test

- Les fonctionnalités en cours de développement tournent sur le serveur
  Discord de **test** ; la production (les vrais joueurs) ne reçoit que
  les versions publiées.
- Quand un déploiement de test est en cours, la PR porte un **commentaire
  de suivi** qui affiche sa progression : 🟡 building → 🔵 deploying →
  🟢 deployed (ou ❌ failed). Si vous voyez ❌, signalez-le simplement à
  l'agent — le diagnostic est son travail, pas le vôtre.

## Lire le /status du bot

La commande `/status` est votre tableau de bord en Discord. En langage
courant :

- **Version** — la build en cours d'exécution : un lien vers la PR de test,
  le commit ou la release qui a produit le bot que vous avez sous les yeux.
- **Infra** — le pipeline qui a déployé cette build (lien vers le run) :
  preuve que ce que vous testez est bien la dernière livraison.
- **Admins** — les opérateurs du bot et les admins du serveur : vers qui
  se tourner si quelque chose ne marche pas.
- **Games / Mods** — les jeux configurés et les modules actifs.

## Quand quelque chose coince

- **Une commande ne répond pas** : vérifiez `/status` (le bot est-il à
  jour ?), puis signalez à un admin listé dans le rapport.
- **Un déploiement échoue** (❌ sur la PR) : l'agent diagnostique avec le
  runbook prévu — signalez-le, rien à faire de votre côté.
- **Une idée vous revient** : demandez simplement à l'agent d'ouvrir une
  issue pour ne pas la perdre ; les issues sont le carnet de bord du
  projet.

## Ce que vous ne ferez jamais

- Écrire ou fusionner du code, lancer des commandes, ouvrir un terminal.
- Manipuler des secrets, des environnements ou des permissions GitHub.
- Approuver un déploiement de production (c'est le rôle d'ops).

Si une session agent vous propose une commande à copier dans un terminal,
refusez : c'est un bug de la session, signalez-le.
