# Kingdoms Roadmap

> Current state and next steps of the plan, regenerated from the GitHub
> issues — the past (done issues, change history) lives on GitHub and in
> the git log of the `sync/generated-artifacts` branch. Single writer: the
> [Generated artifacts](../.agents/skills/generated-artifacts/SKILL.md) workflow.

Status values: `todo` / `in-progress` / `in-review` / `done` / `blocked` / `dropped`.

## Current lot

- [Lot 2 — Org & repo rename (before the first client mod lands)](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/2) — **5 open**

### Open issues — what blocks closing the current lot, in work order

Order: dependency wave → priority label → slack → issue number. Details and full graph: [DEPENDENCIES.md](DEPENDENCIES.md).

- [#322 — Tests: the caller-to-remote seams are untested — generalize the signature contract](https://github.com/merlin-pinpin-org/kingdoms-services/issues/322) — `in-review` · P0 · size M · PR [#306](https://github.com/merlin-pinpin-org/kingdoms-services/pull/306)
- [#323 — Catalog: the remote subset is implicit — make it explicit (forbidden vs missing)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/323) — `in-review` · P0 · size M · PR [#306](https://github.com/merlin-pinpin-org/kingdoms-services/pull/306)
- [#330 — HANDOVER: the arch workstream #306 is in flight — posts (civs unresolved, maps/pools to retest), the merge and the test redeploy](https://github.com/merlin-pinpin-org/kingdoms-services/issues/330) — `todo` · P0 · size M · PR [#306](https://github.com/merlin-pinpin-org/kingdoms-services/pull/306)
- [#331 — docs(infra): the no-back-and-forth VPS install guide — ready for the post-rename reinstall](https://github.com/merlin-pinpin-org/kingdoms-services/issues/331) — `todo` · P0 · size M
- [#241 — chore(org): rename the organization and the projects — risky, full pipeline impact (remotes, ghcr images, deploy state branches, docs)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/241) — `todo` · P1 · size L · PR [#306](https://github.com/merlin-pinpin-org/kingdoms-services/pull/306)

## Upcoming lots

- [Lot 3 — Kingdoms mod integration (manual, with Drasah)](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/3) — 5 open
  - The maintainer integrates Drasah's Kingdoms mod BY HAND, with Drasah, on a new branch from his own account (kingdoms-services#316).
- [Lot 4 — Mod SDK & pro docs](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/4) — 9 open
  - The mod development experience goes pro: the SDK and its documentation.
- [Lot 5 — Packaging (PyPI + registries)](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/5) — 1 open
  - Deliverables published: one PyPI package per micro-service and per mod, Docker images on both registries.
- [Lot 6 — Multi-bot, multi-game, multi-mod](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/6) — 17 open
  - Several distinct bots from the same code, each with its own mod set — validated multi-game/multi-mod before 1.0.0.
- [Lot 7 — Externalized storage & disposable VPS](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/7) — 2 open
  - Durable data off the VPS, and a VPS you can throw away and rebuild in minutes.
- [Lot 8 — Pre-1.0.0 review gate (code, DB, architecture, quality)](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/8) — 16 open
  - The final gate before v1.0.0: the full review pass, absorbing the former v0.999.0 scope (kingdoms-services#320, P0).

## Out of scope / no lot

Open issues without a lot:

- [#174 — [Epic] Pre-1.0 content bar — AoE2 full-featured, ladder iso-JeanJack (kingdoms if ready)](https://github.com/merlin-pinpin-org/kingdoms/issues/174) — `todo` · P0 · size XL
- [#179 — [Epic v1.0.0] Modular repo layout — one self-contained directory per mod and per game (code, config, locales, tests)](https://github.com/merlin-pinpin-org/kingdoms/issues/179) — `todo` · P0 · size XL
- [#120 — Implement the automated tournament mod (Epic B, zero-admin tournaments)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/120) — `backlog` · P0 · size L
- [#134 — ci: CLA check does not re-run on /cla comment](https://github.com/merlin-pinpin-org/kingdoms/issues/134) — `todo` · P1 · size S
- [#169 — [Epic] Mod SDK — factorized high-level platform behaviors, the single entry point for mod development](https://github.com/merlin-pinpin-org/kingdoms/issues/169) — `todo` · P1 · size XL
- [#170 — [Epic] Public PyPI packages & service versioning — clean packaging, one image per service, /status or stack-version decision](https://github.com/merlin-pinpin-org/kingdoms/issues/170) — `todo` · P1 · size L
- [#197 — [Docs] Pre-1.0 reconciliation: enforcement claims match reality + the mod target architecture (per-mod dirs, PyPI artifacts, multi-bot)](https://github.com/merlin-pinpin-org/kingdoms/issues/197) — `todo` · P1 · size M
- [#89 — Deploy 4 processes (bot-discord, svc-core, ext-librematch, ext-aoe2lobby) + gRPC networking](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/89) — `todo` · P1 · size L
- [#127 — Externalize MongoDB & Redis to the managed clusters + backup/restore drills off the prod compose](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/127) — `todo` · P1 · size L
- [#156 — [Kingdoms T1] Mod foundations — module, season config, Kingdom/Lord/Gaïa models](https://github.com/merlin-pinpin-org/kingdoms-services/issues/156) — `todo` · P1 · size XL
- [#157 — [Kingdoms T2] Season & enrollment — admin launch, reset, King/Lord registration, queue, swaps](https://github.com/merlin-pinpin-org/kingdoms-services/issues/157) — `todo` · P1 · size XL
- [#158 — [Kingdoms T4] Attacks & defenses — state machine, delays, weekly points, combat technologies](https://github.com/merlin-pinpin-org/kingdoms-services/issues/158) — `todo` · P1 · size XL
- [#159 — [Kingdoms T5] Weekly events — ages, Lord's Day (+Gaïa maps, cadastre), Saturday exploration](https://github.com/merlin-pinpin-org/kingdoms-services/issues/159) — `todo` · P1 · size XL
- [#160 — [Kingdoms T6] Diplomacy & marriages — civilization conditions, alliances, marriages (standard & arranged)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/160) — `todo` · P1 · size XL
- [#161 — [Kingdoms T7] Economic technologies — tech currency, Explorateur, Corruption, Garde Royale](https://github.com/merlin-pinpin-org/kingdoms-services/issues/161) — `todo` · P1 · size XL
- [#162 — [Kingdoms T8] Season end — Conquest victory, tie ShowMatch PA2, closing report](https://github.com/merlin-pinpin-org/kingdoms-services/issues/162) — `todo` · P1 · size XL
- [#163 — [Kingdoms T3] Territories & maps — allowed map catalog, draw without duplicates, ejection/replacement](https://github.com/merlin-pinpin-org/kingdoms-services/issues/163) — `todo` · P1 · size XL
- [#129 — Mod Kingdoms — méta-jeu de conquête AoE2 (Saison II) : documentation & suivi](https://github.com/merlin-pinpin-org/kingdoms/issues/129) — `todo` · P2 · size M
- [#173 — [Epic] Contributor journeys — documented playbooks: bugfix, game connector, platform, mod, test-env ops, prod ops](https://github.com/merlin-pinpin-org/kingdoms/issues/173) — `todo` · P2 · size M
- [#177 — [Epic v1.0.0] Generic platform systems — admin views, registration, seasons, logs, Discord config: centralized code, mod declinations](https://github.com/merlin-pinpin-org/kingdoms/issues/177) — `todo` · P2 · size XL
- [#178 — [Epic v1.0.0] Mod contract — manifest: games, seasonal flag, roles/channels (regex-capable), admin parameters](https://github.com/merlin-pinpin-org/kingdoms/issues/178) — `todo` · P2 · size L
- [#180 — [Epic v1.0.0] Mod development guide — SDK quickstart, component reference, core-evolution protocol, PR boundaries](https://github.com/merlin-pinpin-org/kingdoms/issues/180) — `todo` · P2 · size M
- [#181 — [Epic v1.0.0] Game-connector development guide — plug a new game (CS2, Valorant, Fortnite, Roblox, …) step by step](https://github.com/merlin-pinpin-org/kingdoms/issues/181) — `todo` · P2 · size M
- [#182 — [Epic v1.0.0] OAuth account linking — Steam first (auto AoE2 profile resolution), Twitch later](https://github.com/merlin-pinpin-org/kingdoms/issues/182) — `todo` · P2 · size L
- [#183 — [Epic v1.0.0] Readable pydoc — generated API docs hosted, linked from PyPI packages and the source](https://github.com/merlin-pinpin-org/kingdoms/issues/183) — `todo` · P2 · size M
- [#90 — Cross-process observability — correlation ids, dashboards, degradation alerts](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/90) — `todo` · P2 · size M
- [#19 — [Phase 3] Implement clans mod](https://github.com/merlin-pinpin-org/kingdoms-services/issues/19) — `backlog` · P2 · size M
- [#21 — [Phase 3] Implement admin mod](https://github.com/merlin-pinpin-org/kingdoms-services/issues/21) — `todo` · P2 · size M
- [#109 — [Docs] Product plan — living document (vision, phases 0-4, modules A-J, monetization, sovereignty)](https://github.com/merlin-pinpin-org/kingdoms/issues/109) — `in-progress` · P3 · size M
- [#110 — Epic A: Core domain (players, seasons, matches, scoring, entitlements)](https://github.com/merlin-pinpin-org/kingdoms/issues/110) — `todo` · P3 · size XL
- [#111 — Epic B: Tournament machine (sign-ups, seeding, brackets, disputes)](https://github.com/merlin-pinpin-org/kingdoms/issues/111) — `todo` · P3 · size XL
- [#112 — Epic C: Game data & drafts (maps, mappools, civs, DraftProvider)](https://github.com/merlin-pinpin-org/kingdoms/issues/112) — `todo` · P3 · size L
- [#113 — Epic D: Ratings & stars (Glicko-2, history, badges)](https://github.com/merlin-pinpin-org/kingdoms/issues/113) — `todo` · P3 · size L
- [#114 — Epic E: Presence (real-time availability)](https://github.com/merlin-pinpin-org/kingdoms/issues/114) — `todo` · P3 · size L
- [#115 — Epic F: Team maker (LFG tickets, balanced teams, captain drafts)](https://github.com/merlin-pinpin-org/kingdoms/issues/115) — `todo` · P3 · size XL
- [#118 — Epic J: Social & moderation (friends, private feedback, sanctions)](https://github.com/merlin-pinpin-org/kingdoms/issues/118) — `todo` · P3 · size XL
- [#136 — [Epic K] Vibe-coding mod platform — assisted, UI-based mod co-construction for designers and community](https://github.com/merlin-pinpin-org/kingdoms/issues/136) — `todo` · P3 · size XL
- [#138 — Design: architecture Discord salons-first du mod Kingdoms (Saison 2) — /kingdom unique + panels par salon](https://github.com/merlin-pinpin-org/kingdoms/issues/138) — `todo` · P3 · size M
- [#141 — [Epic L] Contributor spaces — personal branches, personal test environments, personal prod slots](https://github.com/merlin-pinpin-org/kingdoms/issues/141) — `todo` · P3 · size XL
- [#143 — [Task] Factorize the shared check workflows (CLA, auto-triage, validate-issue) into one implementation](https://github.com/merlin-pinpin-org/kingdoms/issues/143) — `todo` · P3 · size M
- [#151 — Assign owners for the orphan mods (ladder, register) — ownership check debt](https://github.com/merlin-pinpin-org/kingdoms/issues/151) — `todo` · P3 · size S
- [#152 — Drifts de session Drasah : mod marriage hors process, branches feat/*, pile de PRs à restacker](https://github.com/merlin-pinpin-org/kingdoms/issues/152) — `todo` · P3 · size S
- [#154 — Mod kingdoms : replier le travail marriage dans le mod kingdoms (décision : feature T6, pas un mod)](https://github.com/merlin-pinpin-org/kingdoms/issues/154) — `todo` · P3 · size S
- [#155 — Hygiène branches/PRs Drasah : renommage vibe/*, restack, doublon salons-first](https://github.com/merlin-pinpin-org/kingdoms/issues/155) — `todo` · P3 · size M
- [#156 — Rétrospective : pourquoi Drasah s'est bloqué (pile de PRs, conventions dérivées) — et ce qu'on change](https://github.com/merlin-pinpin-org/kingdoms/issues/156) — `todo` · P3 · size S
- [#171 — [Epic] Per-service DB accounts — enforced core/games/mods perimeter isolation, trivial provisioning for new services](https://github.com/merlin-pinpin-org/kingdoms/issues/171) — `todo` · P3 · size L
- [#172 — [Epic] Non-Discord data access — exportable guild configs, game stats, per-mod data (GitHub Actions first)](https://github.com/merlin-pinpin-org/kingdoms/issues/172) — `todo` · P3 · size L
- [#187 — Visual engine library — generalize TCG card generation into a reusable JSON+template+art+text visual generator](https://github.com/merlin-pinpin-org/kingdoms/issues/187) — `todo` · P3 · size XL
- [#202 — Branch naming rules — review vibe/<user>/main in favor of per-mod integration branches (vibe/mod-<name>)](https://github.com/merlin-pinpin-org/kingdoms/issues/202) — `todo` · P3 · size S · PR [#190](https://github.com/merlin-pinpin-org/kingdoms/pull/190)
- [#5 — [Phase 2] Configure monitoring](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/5) — `todo` · P3 · size M
- [#94 — TEST: KingdomsService non monté au démarrage du bot (« no service » sur les actions de saison)](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/94) — `todo` · P3 · size S
- [#95 — Multi-tenant GitOps — personal envs (test-<user>), prod slots (per user+mod), provisioning scripts](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/95) — `todo` · P3 · size XL
- [#96 — [Task] Silent rollback — re-pin without re-deploying when the re-pinned image already runs](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/96) — `todo` · P3 · size M
- [#107 — P1: SimCord journeys exit 128 when the pinned deploy_commit is not reachable from main](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/107) — `todo` · P3 · size M
- [#111 — [v0.5.0] Docker Hub rate limits break the builds — mirror the base images on ghcr.io](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/111) — `todo` · P3 · size M
- [#116 — Bot down après reset de token : crash-loop de restart sur LoginFailure + healthcheck aveugle (scaling bot = 1 confirmé)](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/116) — `todo` · P3 · size M
- [#122 — fix(envlogs): the --service filter rejects kingdoms-ext-aoe2lobby (unknown service although listed)](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/122) — `todo` · P3 · size S
- [#124 — chore(deploy): the deploy/logs/seed workflows must not notify the repo owner — attribute the runs to the deployer alias](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/124) — `todo` · P3 · size S
- [#128 — env-console.yml + per-env TEST_GUILD_IDS — the dev console's infra companion](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/128) — `todo` · P3 · size M
- [#20 — [Phase 1] Create deployment scripts](https://github.com/merlin-pinpin-org/kingdoms-services/issues/20) — `todo` · P3 · size S
- [#121 — Full-auto tournament mode (auto rounds, auto seeding, scheduled seasons — after the 80% mode is proven)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/121) — `todo` · P3 · size L
- [#148 — Add /drasah medieval greeting command](https://github.com/merlin-pinpin-org/kingdoms-services/issues/148) — `todo` · P3 · size S
- [#175 — [Task] Fix first designer-session drifts: core-owned provisioning, single source of truth, stack & PR conventions (PR #170 stack)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/175) — `todo` · P3 · size L
- [#199 — [Task] CLI mode awareness — sandbox / pro / cowboy guardrails for humans and agents](https://github.com/merlin-pinpin-org/kingdoms-services/issues/199) — `todo` · P3 · size M
- [#200 — [Task] kingdoms branch — print-only helper for the user branch lifecycle (bootstrap, sync, promote)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/200) — `todo` · P3 · size S
- [#201 — [Task] kingdoms env — personal environment companion (show, deploy, validate)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/201) — `todo` · P3 · size M
- [#214 — [Epic] Gestion-saison — panel admin de gouvernance live (Season II, design validé session Drasah)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/214) — `todo` · P3 · size XL
- [#216 — Tranche ① — Structure Discord : 11 catégories + salons par royaume (D70)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/216) — `todo` · P3 · size L
- [#219 — Tranche ② — panels d'état des salons royaume (hors Salle du Conseil)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/219) — `todo` · P3 · size M
- [#232 — [Kingdoms] Phase 1.1 — salon gestion-saison + tableau de bord épinglé + salon Temps de saison](https://github.com/merlin-pinpin-org/kingdoms-services/issues/232) — `todo` · P3 · size M
- [#286 — chambre-des-comptes: le bouton ne répond plus sur drasah (v4/fix-v1)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/286) — `todo` · P3 · size S

Dropped (closed as not planned):

- [#18 — [Phase 3] Implement report mod](https://github.com/merlin-pinpin-org/kingdoms-services/issues/18)
- [#151 — [Feature] Coaching mod: coach/reviewer pool, booking flow, session workspace, ratings & reputation, commission ledger](https://github.com/merlin-pinpin-org/kingdoms-services/issues/151)
- [#167 — Sub-task: coaching mod — domain core (models, booking state machine, reputation, ledger)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/167)
- [#168 — Sub-task: coaching mod — Discord surface (commands, dynamic views, session workspace)](https://github.com/merlin-pinpin-org/kingdoms-services/issues/168)
