# Kingdoms Roadmap

> Single source of truth for project progress. Updated via the
> [Update roadmap](.agents/skills/update-roadmap/SKILL.md) skill.

Status values: `todo` / `in-progress` / `in-review` / `done` / `blocked` / `dropped`.

## Current Phase
Phase 2 — v0.4.0 AoE2 ladder (process split + first game + ladder mod, milestone [v0.4.0](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/3)); ADR-0020 supersedes ADR-0019 for bot/core/providers

Product plan (post-pivot): see the living document [kingdoms#109](https://github.com/merlin-pinpin-org/kingdoms/issues/109) and epics A→J ([#110](https://github.com/merlin-pinpin-org/kingdoms/issues/110)–[#118](https://github.com/merlin-pinpin-org/kingdoms/issues/118)).

## Milestones

### Release milestones (kingdoms-services)
| Milestone | Scope |
|-----------|-------|
| [Lot 1 — Structural](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/1) | Structural lot (changelog #28, exceptions #10 ✱re-raised P0, config #16 ✅, enums #7 ✅, i18n #17 ✅, ChannelService #5, roles #26, UI #13, permission checks #55, DM policy #56, persistent views #122, core tests #22 ✅) — unlocks everything downstream, no player-facing mod. Superseded by the seam pivot: DiscordPlatform #11 ✅ (dead skeleton removed) |
| [v0.4.0 — AoE2 ladder](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/3) | AoE2 ladder vertical slice (JeanJack migration, ADR-0020 process split): gRPC seams #128 → games/aoe2 + providers #129 → identity/message-registry/surfaces #130 → game data (maps/civs/rules/pools/packs) #131 → seasons #132 → registration + profile validation #133 → ladder core #134 (blossom matchmaking, pluggable Elo/Glicko-2) → ladder Discord surface #135 → Discord-first admin surface #136 → E2E acceptance + rollout rehearsal #137. Live test dashboard #147 (providers & game-aoe2 validation tool). Infra: kingdoms-infra#89, #90. Out of scope: clans #19, tournament #120 (Backlog) |
| [Backlog — post-pivot](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/2) | Valid issues awaiting re-qualification into epics A→J |

### Phase 1 — Foundations
| Track | Issue | Status |
|-------|-------|--------|
| kingdoms: repo structure | [kingdoms#1](https://github.com/merlin-pinpin-org/kingdoms/issues/1) | done |
| kingdoms: architecture docs | [kingdoms#2](https://github.com/merlin-pinpin-org/kingdoms/issues/2) | done |
| kingdoms: docs CI | [kingdoms#3](https://github.com/merlin-pinpin-org/kingdoms/issues/3) | done |
| kingdoms: WORKFLOWS.md | [kingdoms#4](https://github.com/merlin-pinpin-org/kingdoms/issues/4) | done |
| kingdoms: MODS docs | [kingdoms#5](https://github.com/merlin-pinpin-org/kingdoms/issues/5) | done |
| kingdoms: ADRs | [kingdoms#6](https://github.com/merlin-pinpin-org/kingdoms/issues/6) | done |
| kingdoms: governance (LICENSE, CLA) | [kingdoms#11](https://github.com/merlin-pinpin-org/kingdoms/issues/11) | done |
| kingdoms: ROADMAP + skill | [kingdoms#9](https://github.com/merlin-pinpin-org/kingdoms/issues/9) | done |
| kingdoms: vibe-coding workflow doc | [kingdoms#10](https://github.com/merlin-pinpin-org/kingdoms/issues/10) | done |
| kingdoms: roadmap automation | [kingdoms#27](https://github.com/merlin-pinpin-org/kingdoms/issues/27) | done |
| services: repo structure | [kingdoms-services#1](https://github.com/merlin-pinpin-org/kingdoms-services/issues/1) | done |
| services: MockDiscord | [kingdoms-services#2](https://github.com/merlin-pinpin-org/kingdoms-services/issues/2) | done |
| infra: repo structure | [kingdoms-infra#1](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/1) | done |

### Phase 2 — Core
| Track | Issue | Status |
|-------|-------|--------|
| services: IPlatform | [kingdoms-services#3](https://github.com/merlin-pinpin-org/kingdoms-services/issues/3) | done |
| services: DB models | [kingdoms-services#4](https://github.com/merlin-pinpin-org/kingdoms-services/issues/4) | done |
| services: ChannelService | [kingdoms-services#5](https://github.com/merlin-pinpin-org/kingdoms-services/issues/5) | done |
| services: WorkflowEngine | [kingdoms-services#6](https://github.com/merlin-pinpin-org/kingdoms-services/issues/6) | done |
| services: enums | [kingdoms-services#7](https://github.com/merlin-pinpin-org/kingdoms-services/issues/7) | done |
| services: adapters | [kingdoms-services#8](https://github.com/merlin-pinpin-org/kingdoms-services/issues/8) | done |
| services: StateService | [kingdoms-services#9](https://github.com/merlin-pinpin-org/kingdoms-services/issues/9) | done |
| services: exceptions | [kingdoms-services#10](https://github.com/merlin-pinpin-org/kingdoms-services/issues/10) | done |
| services: Protocol interfaces | [kingdoms-services#41](https://github.com/merlin-pinpin-org/kingdoms-services/issues/41) | done |
| services: config system | [kingdoms-services#16](https://github.com/merlin-pinpin-org/kingdoms-services/issues/16) | done |
| services: i18n | [kingdoms-services#17](https://github.com/merlin-pinpin-org/kingdoms-services/issues/17) | done |
| infra: CI/CD | [kingdoms-infra#2](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/2) | done |
| infra: infra docs | [kingdoms-infra#3](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/3) | done |
| infra: deployment scripts | [kingdoms-infra#4](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/4) | done |
| infra: monitoring | [kingdoms-infra#5](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/5) | todo |
| infra: post-deploy battery & auto rollback | [kingdoms-infra#78](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/78) | done |
| kingdoms: ADR-0012 taxonomy & repo strategy | [kingdoms#59](https://github.com/merlin-pinpin-org/kingdoms/issues/59) | done |
| kingdoms: ADR-0013 cross-platform identity | [kingdoms#60](https://github.com/merlin-pinpin-org/kingdoms/issues/60) | done |
| kingdoms: ADR-0014 RBAC permissions | [kingdoms#61](https://github.com/merlin-pinpin-org/kingdoms/issues/61) | done |
| kingdoms: ADR-0015 webapp API boundary | [kingdoms#62](https://github.com/merlin-pinpin-org/kingdoms/issues/62) | done |
| kingdoms: ADR-0017 packaging & distribution | [kingdoms#65](https://github.com/merlin-pinpin-org/kingdoms/issues/65) | done |
| kingdoms: issue templates (all repos) | [kingdoms#68](https://github.com/merlin-pinpin-org/kingdoms/issues/68) | done |

### Phase 3 — Mods & Discord
| Track | Issue | Status |
|-------|-------|--------|
| services: DiscordPlatform | [kingdoms-services#11](https://github.com/merlin-pinpin-org/kingdoms-services/issues/11) | done |
| services: Bot structure | [kingdoms-services#12](https://github.com/merlin-pinpin-org/kingdoms-services/issues/12) | done |
| services: UI components | [kingdoms-services#13](https://github.com/merlin-pinpin-org/kingdoms-services/issues/13) | done |
| services: registration + profile validation | [kingdoms-services#133](https://github.com/merlin-pinpin-org/kingdoms-services/issues/133) | done |
| services: ladder mod (core #134 + surface #135) | [kingdoms-services#15](https://github.com/merlin-pinpin-org/kingdoms-services/issues/15) | done |
| services: ladder domain core | [kingdoms-services#134](https://github.com/merlin-pinpin-org/kingdoms-services/issues/134) | done |
| services: ladder Discord surface | [kingdoms-services#135](https://github.com/merlin-pinpin-org/kingdoms-services/issues/135) | done |
| services: OCI image descriptions | [kingdoms-services#144](https://github.com/merlin-pinpin-org/kingdoms-services/issues/144) | done |
| services: process split + gRPC seams (ADR-0020) | [kingdoms-services#128](https://github.com/merlin-pinpin-org/kingdoms-services/issues/128) | done |
| services: games/aoe2 + ext-librematch/ext-aoe2lobby | [kingdoms-services#129](https://github.com/merlin-pinpin-org/kingdoms-services/issues/129) | done |
| services: live test dashboard (channel + /live) | [kingdoms-services#147](https://github.com/merlin-pinpin-org/kingdoms-services/issues/147) | done |
| services: identity, message registry, surfaces | [kingdoms-services#130](https://github.com/merlin-pinpin-org/kingdoms-services/issues/130) | done |
| services: game data catalog (maps/civs/rules/pools/packs) | [kingdoms-services#131](https://github.com/merlin-pinpin-org/kingdoms-services/issues/131) | done |
| services: seasons (rotations, optional reset) | [kingdoms-services#132](https://github.com/merlin-pinpin-org/kingdoms-services/issues/132) | done |
| services: Discord-first admin surface (game data, pools, seasons, rating) | [kingdoms-services#136](https://github.com/merlin-pinpin-org/kingdoms-services/issues/136) | done |
| services: E2E acceptance + AoE2 seeding + rollout rehearsal | [kingdoms-services#137](https://github.com/merlin-pinpin-org/kingdoms-services/issues/137) | todo |
| services: channel access policies (#130/#135 dependency) | [kingdoms-services#57](https://github.com/merlin-pinpin-org/kingdoms-services/issues/57) | done |
| services: Discord delivery backpressure | [kingdoms-services#140](https://github.com/merlin-pinpin-org/kingdoms-services/issues/140) | done |
| services: ladder creation UI (mono-guild) | [kingdoms-services#141](https://github.com/merlin-pinpin-org/kingdoms-services/issues/141) | done |
| services: rating switch via history replay | [kingdoms-services#142](https://github.com/merlin-pinpin-org/kingdoms-services/issues/142) | done |
| services: JeanJack data migration | [kingdoms-services#138](https://github.com/merlin-pinpin-org/kingdoms-services/issues/138) | done |
| services: blanket test mandate (CI properties) | [kingdoms-services#139](https://github.com/merlin-pinpin-org/kingdoms-services/issues/139) | done |
| infra: 4-process deploy + gRPC networking | [kingdoms-infra#89](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/89) | todo |
| infra: cross-process observability | [kingdoms-infra#90](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/90) | todo |
| services: tournament mod (80% operator-assisted) | [kingdoms-services#120](https://github.com/merlin-pinpin-org/kingdoms-services/issues/120) | backlog |
| services: full-auto tournament mode | [kingdoms-services#121](https://github.com/merlin-pinpin-org/kingdoms-services/issues/121) | todo |
| services: clans mod | [kingdoms-services#19](https://github.com/merlin-pinpin-org/kingdoms-services/issues/19) | backlog |
| services: admin mod | [kingdoms-services#21](https://github.com/merlin-pinpin-org/kingdoms-services/issues/21) | todo |
| services: deployment scripts | [kingdoms-services#20](https://github.com/merlin-pinpin-org/kingdoms-services/issues/20) | todo |
| services: semantic release | [kingdoms-services#28](https://github.com/merlin-pinpin-org/kingdoms-services/issues/28) | done |
| services: startup announcement (PR link) | [kingdoms-services#52](https://github.com/merlin-pinpin-org/kingdoms-services/issues/52) | done |
| kingdoms: Mod Kingdoms (Saison II) docs & tracking | [kingdoms#129](https://github.com/merlin-pinpin-org/kingdoms/issues/129) | todo |
| services: Mod Kingdoms T1 — mod foundations | [kingdoms-services#156](https://github.com/merlin-pinpin-org/kingdoms-services/issues/156) | todo |
| services: Mod Kingdoms T2 — season & enrollment | [kingdoms-services#157](https://github.com/merlin-pinpin-org/kingdoms-services/issues/157) | todo |
| services: Mod Kingdoms T3 — territories & maps | [kingdoms-services#163](https://github.com/merlin-pinpin-org/kingdoms-services/issues/163) | todo |
| services: Mod Kingdoms T4 — attacks & defenses | [kingdoms-services#158](https://github.com/merlin-pinpin-org/kingdoms-services/issues/158) | todo |
| services: Mod Kingdoms T5 — weekly events | [kingdoms-services#159](https://github.com/merlin-pinpin-org/kingdoms-services/issues/159) | todo |
| services: Mod Kingdoms T6 — diplomacy & marriages | [kingdoms-services#160](https://github.com/merlin-pinpin-org/kingdoms-services/issues/160) | todo |
| services: Mod Kingdoms T7 — economic technologies | [kingdoms-services#161](https://github.com/merlin-pinpin-org/kingdoms-services/issues/161) | todo |
| services: Mod Kingdoms T8 — season end | [kingdoms-services#162](https://github.com/merlin-pinpin-org/kingdoms-services/issues/162) | todo |
| services: /drasah greeting command | [kingdoms-services#148](https://github.com/merlin-pinpin-org/kingdoms-services/issues/148) | todo |
| services: coaching mod (booking, sessions, reputation) | [kingdoms-services#151](https://github.com/merlin-pinpin-org/kingdoms-services/issues/151) | todo |
| services: app verification readiness (privacy, ToS, identity) | [kingdoms-services#154](https://github.com/merlin-pinpin-org/kingdoms-services/issues/154) | todo |

### Phase 4 — Post-pivot epics (product plan kingdoms#109)

| Track | Issue | Status |
|-------|-------|--------|
| kingdoms: product plan (living doc) | [kingdoms#109](https://github.com/merlin-pinpin-org/kingdoms/issues/109) | in-progress |
| kingdoms: Epic A — Core domain | [kingdoms#110](https://github.com/merlin-pinpin-org/kingdoms/issues/110) | todo |
| kingdoms: Epic B — Tournament machine | [kingdoms#111](https://github.com/merlin-pinpin-org/kingdoms/issues/111) | todo |
| kingdoms: Epic C — Game data & drafts | [kingdoms#112](https://github.com/merlin-pinpin-org/kingdoms/issues/112) | todo |
| kingdoms: Epic D — Ratings & stars | [kingdoms#113](https://github.com/merlin-pinpin-org/kingdoms/issues/113) | todo |
| kingdoms: Epic E — Presence | [kingdoms#114](https://github.com/merlin-pinpin-org/kingdoms/issues/114) | todo |
| kingdoms: Epic F — Team maker | [kingdoms#115](https://github.com/merlin-pinpin-org/kingdoms/issues/115) | todo |
| kingdoms: Epic J — Social & moderation | [kingdoms#118](https://github.com/merlin-pinpin-org/kingdoms/issues/118) | todo |
| kingdoms: Epic K — Vibe-coding mod platform | [kingdoms#136](https://github.com/merlin-pinpin-org/kingdoms/issues/136) | todo |

### Sub-tasks
| Sub-task | Parent | Status |
|----------|--------|--------|
| Unit tests core | [kingdoms-services#22](https://github.com/merlin-pinpin-org/kingdoms-services/issues/22) | done |
| Mongo+Redis caching | [kingdoms-services#23](https://github.com/merlin-pinpin-org/kingdoms-services/issues/23) | done |
| MockDiscord framework | [kingdoms-services#24](https://github.com/merlin-pinpin-org/kingdoms-services/issues/24) | done |
| Registration DM flow | [kingdoms-services#25](https://github.com/merlin-pinpin-org/kingdoms-services/issues/25) | dropped (superseded by #133) |
| Channel/role mgmt | [kingdoms-services#26](https://github.com/merlin-pinpin-org/kingdoms-services/issues/26) | done |
| Bot vs guild admins | [kingdoms-services#35](https://github.com/merlin-pinpin-org/kingdoms-services/issues/35) | done |
| Runtime permission checks | [kingdoms-services#55](https://github.com/merlin-pinpin-org/kingdoms-services/issues/55) | done |
| DM vs channel message policy | [kingdoms-services#56](https://github.com/merlin-pinpin-org/kingdoms-services/issues/56) | done |
| Persistent views & state reconstruction | [kingdoms-services#122](https://github.com/merlin-pinpin-org/kingdoms-services/issues/122) | done |
| Channel access + drift alerting | [kingdoms-services#57](https://github.com/merlin-pinpin-org/kingdoms-services/issues/57) | done |
| On-demand role/channel sync | [kingdoms-services#58](https://github.com/merlin-pinpin-org/kingdoms-services/issues/58) | todo |
| Deploy announcement | [kingdoms-services#52](https://github.com/merlin-pinpin-org/kingdoms-services/issues/52) | done |
| AoE2 game service | [kingdoms-services#27](https://github.com/merlin-pinpin-org/kingdoms-services/issues/27) | dropped (superseded by #129) |
| On-demand test deployments | [kingdoms-services#54](https://github.com/merlin-pinpin-org/kingdoms-services/issues/54) | done |
| Docs architecture | [kingdoms#7](https://github.com/merlin-pinpin-org/kingdoms/issues/7) | done |
| Discord permissions guide | [kingdoms#57](https://github.com/merlin-pinpin-org/kingdoms/issues/57) | done |
| ADR-0012 taxonomy & repo strategy | [kingdoms#59](https://github.com/merlin-pinpin-org/kingdoms/issues/59) | done |
| ADR-0013 cross-platform identity | [kingdoms#60](https://github.com/merlin-pinpin-org/kingdoms/issues/60) | done |
| ADR-0014 RBAC permissions | [kingdoms#61](https://github.com/merlin-pinpin-org/kingdoms/issues/61) | done |
| ADR-0015 webapp frontend & API | [kingdoms#62](https://github.com/merlin-pinpin-org/kingdoms/issues/62) | done |
| discord.py guide | [kingdoms#8](https://github.com/merlin-pinpin-org/kingdoms/issues/8) | done |
| Docs: automation mandate | [kingdoms#92](https://github.com/merlin-pinpin-org/kingdoms/issues/92) | done |
| Docs: human-contributor onboarding | [kingdoms#94](https://github.com/merlin-pinpin-org/kingdoms/issues/94) | done |
| services: human-contributor onboarding | [kingdoms-services#100](https://github.com/merlin-pinpin-org/kingdoms-services/issues/100) | done |
| infra: human-contributor onboarding | [kingdoms-infra#71](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/71) | done |
| kingdoms: CLA check re-run on /cla comment | [kingdoms#134](https://github.com/merlin-pinpin-org/kingdoms/issues/134) | todo |
| Rétrospective : pourquoi Drasah s'est bloqué (pile de PRs, conventions dérivées) — et ce qu'on change | [kingdoms#156](https://github.com/merlin-pinpin-org/kingdoms/issues/156) | todo |
| Hygiène branches/PRs Drasah : renommage vibe/*, restack, doublon salons-first | [kingdoms#155](https://github.com/merlin-pinpin-org/kingdoms/issues/155) | todo |
| Mod kingdoms : replier le travail marriage dans le mod kingdoms (décision : feature T6, pas un mod) | [kingdoms#154](https://github.com/merlin-pinpin-org/kingdoms/issues/154) | todo |
| Drifts de session Drasah : mod marriage hors process, branches feat/*, pile de PRs à restacker | [kingdoms#152](https://github.com/merlin-pinpin-org/kingdoms/issues/152) | todo |
| Assign owners for the orphan mods (ladder, register) — ownership check debt | [kingdoms#151](https://github.com/merlin-pinpin-org/kingdoms/issues/151) | todo |
| [Task] Factorize the shared check workflows (CLA, auto-triage, validate-issue) into one implementation | [kingdoms#143](https://github.com/merlin-pinpin-org/kingdoms/issues/143) | todo |
| [Epic L] Contributor spaces — personal branches, personal test environments, personal prod slots | [kingdoms#141](https://github.com/merlin-pinpin-org/kingdoms/issues/141) | todo |
| Design: architecture Discord salons-first du mod Kingdoms (Saison 2) — /kingdom unique + panels par salon | [kingdoms#138](https://github.com/merlin-pinpin-org/kingdoms/issues/138) | todo |
| chore(org): rename the organization and the projects — risky, full pipeline impact (remotes, ghcr images, deploy state branches, docs) | [kingdoms-services#241](https://github.com/merlin-pinpin-org/kingdoms-services/issues/241) | todo |
| [Kingdoms] Phase 1.1 — salon gestion-saison + tableau de bord épinglé + salon Temps de saison | [kingdoms-services#232](https://github.com/merlin-pinpin-org/kingdoms-services/issues/232) | todo |
| Refactor: déclarer les attributs dynamiques du bot (éliminer getattr/setattr fragiles) | [kingdoms-services#227](https://github.com/merlin-pinpin-org/kingdoms-services/issues/227) | todo |
| Tranche ② — panels d'état des salons royaume (hors Salle du Conseil) | [kingdoms-services#219](https://github.com/merlin-pinpin-org/kingdoms-services/issues/219) | todo |
| Tranche ① — Structure Discord : 11 catégories + salons par royaume (D70) | [kingdoms-services#216](https://github.com/merlin-pinpin-org/kingdoms-services/issues/216) | todo |
| [Epic] Gestion-saison — panel admin de gouvernance live (Season II, design validé session Drasah) | [kingdoms-services#214](https://github.com/merlin-pinpin-org/kingdoms-services/issues/214) | todo |
| [Epic] Mod packaging — un mod = un module UV + un conteneur Docker + sa doc | [kingdoms-services#211](https://github.com/merlin-pinpin-org/kingdoms-services/issues/211) | todo |
| [Epic] /admin data — extensible admin data menu (core, mods, games, providers) with guild-scoped import/export | [kingdoms-services#204](https://github.com/merlin-pinpin-org/kingdoms-services/issues/204) | todo |
| Map versions — game-owned map catalog with version pinning in map pools | [kingdoms-services#203](https://github.com/merlin-pinpin-org/kingdoms-services/issues/203) | todo |
| [Task] CLI triage — prune or repoint commands made stale by the user-sandbox switch | [kingdoms-services#202](https://github.com/merlin-pinpin-org/kingdoms-services/issues/202) | todo |
| [Task] kingdoms env — personal environment companion (show, deploy, validate) | [kingdoms-services#201](https://github.com/merlin-pinpin-org/kingdoms-services/issues/201) | todo |
| [Task] kingdoms branch — print-only helper for the user branch lifecycle (bootstrap, sync, promote) | [kingdoms-services#200](https://github.com/merlin-pinpin-org/kingdoms-services/issues/200) | todo |
| [Task] CLI mode awareness — sandbox / pro / cowboy guardrails for humans and agents | [kingdoms-services#199](https://github.com/merlin-pinpin-org/kingdoms-services/issues/199) | todo |
| [Epic] v1.0.0 Public release | [kingdoms-services#187](https://github.com/merlin-pinpin-org/kingdoms-services/issues/187) | todo |
| [Epic] v0.999.0 Code cleanup — pre-1.0 readiness | [kingdoms-services#186](https://github.com/merlin-pinpin-org/kingdoms-services/issues/186) | todo |
| [Epic] v0.5.0 Scale-out — module split, PyPI packages, micro-services, game APIs & mod dev | [kingdoms-services#185](https://github.com/merlin-pinpin-org/kingdoms-services/issues/185) | todo |
| [Task] Fix first designer-session drifts: core-owned provisioning, single source of truth, stack & PR conventions (PR #170 stack) | [kingdoms-services#175](https://github.com/merlin-pinpin-org/kingdoms-services/issues/175) | todo |
| Sub-task: coaching mod — Discord surface (commands, dynamic views, session workspace) | [kingdoms-services#168](https://github.com/merlin-pinpin-org/kingdoms-services/issues/168) | todo |
| Sub-task: coaching mod — domain core (models, booking state machine, reputation, ledger) | [kingdoms-services#167](https://github.com/merlin-pinpin-org/kingdoms-services/issues/167) | todo |
| P1: SimCord journeys exit 128 when the pinned deploy_commit is not reachable from main | [kingdoms-infra#107](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/107) | todo |
| [Task] Silent rollback — re-pin without re-deploying when the re-pinned image already runs | [kingdoms-infra#96](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/96) | todo |
| [v0.4.0] Multi-tenant GitOps — personal envs (test-<user>), prod slots (per user+mod), provisioning scripts | [kingdoms-infra#95](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/95) | todo |
| TEST: KingdomsService non monté au démarrage du bot (« no service » sur les actions de saison) | [kingdoms-infra#94](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/94) | todo |
| feat(maps): import AoE2 map data (info + images) via the official Liquipedia MediaWiki API | [kingdoms-services#247](https://github.com/merlin-pinpin-org/kingdoms-services/issues/247) | in-review |
| fix(live): le live dashboard édite son message trop souvent — boucle de 429 rate limit Discord | [kingdoms-services#251](https://github.com/merlin-pinpin-org/kingdoms-services/issues/251) | todo |
| [v0.5.0] Docker Hub rate limits break the builds — mirror the base images on ghcr.io | [kingdoms-infra#111](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/111) | todo |

## Out of Scope
- Report mod (`/report` command) — dropped, see [kingdoms-services#18](https://github.com/merlin-pinpin-org/kingdoms-services/issues/18)
  (closed as not planned)
- Twitch platform — architecture-ready (`IPlatform`), not implemented
- Monetization epics (former kingdoms#116 and kingdoms#117, deleted) — parked under glass, see [docs/PLANS/monetization.md](docs/PLANS/monetization.md)

## Change Log
| Date | Change |
|------|--------|
| 2026-09-18 | Initial roadmap (kingdoms#9), synced with GitHub issue states |
| 2026-09-18 | kingdoms#3 in-review (PR #21); session PRs #12-#21 opened for kingdoms#1-#6, #8-#11 |
| 2026-09-19 | auto-sync: kingdoms#1 in-review->done; kingdoms#2 in-review->done; kingdoms#3 in-review->done; kingdoms#4 todo->done; kingdoms#5 todo->done; (+7 more) |
| 2026-09-20 | auto-sync: [kingdoms-services#1](https://github.com/merlin-pinpin-org/kingdoms-services/issues/1) todo->done; [kingdoms-infra#1](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/1) todo->done |
| 2026-09-20 | auto-sync: [kingdoms-services#41](https://github.com/merlin-pinpin-org/kingdoms-services/issues/41) in-review->done |
| 2026-09-20 | auto-sync: [kingdoms-services#2](https://github.com/merlin-pinpin-org/kingdoms-services/issues/2) todo->done; [kingdoms-services#4](https://github.com/merlin-pinpin-org/kingdoms-services/issues/4) todo->done; [kingdoms-services#6](https://github.com/merlin-pinpin-org/kingdoms-services/issues/6) todo->done; [kingdoms-services#9](https://github.com/merlin-pinpin-org/kingdoms-services/issues/9) todo->done; current phase 1->2 |
| 2026-09-20 | auto-sync: [kingdoms-services#12](https://github.com/merlin-pinpin-org/kingdoms-services/issues/12) todo->done |
| 2026-09-20 | auto-sync: [kingdoms-infra#4](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/4) todo->done; [kingdoms-services#12](https://github.com/merlin-pinpin-org/kingdoms-services/issues/12) todo->done |
| 2026-09-20 | auto-sync: [kingdoms-infra#2](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/2) todo->done; [kingdoms-infra#4](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/4) todo->done |
| 2026-09-21 | auto-sync: [kingdoms-services#54](https://github.com/merlin-pinpin-org/kingdoms-services/issues/54) todo->in-review |
| 2026-09-21 | auto-sync: [kingdoms#59](https://github.com/merlin-pinpin-org/kingdoms/issues/59) todo->in-review; [kingdoms#60](https://github.com/merlin-pinpin-org/kingdoms/issues/60) todo->in-review; [kingdoms#61](https://github.com/merlin-pinpin-org/kingdoms/issues/61) todo->in-review; [kingdoms#62](https://github.com/merlin-pinpin-org/kingdoms/issues/62) todo->in-review; [kingdoms#57](https://github.com/merlin-pinpin-org/kingdoms/issues/57) todo->done |
| 2026-09-21 | auto-sync: [kingdoms#65](https://github.com/merlin-pinpin-org/kingdoms/issues/65) todo->in-review; [kingdoms#57](https://github.com/merlin-pinpin-org/kingdoms/issues/57) todo->done; [kingdoms#59](https://github.com/merlin-pinpin-org/kingdoms/issues/59) todo->in-review; [kingdoms#60](https://github.com/merlin-pinpin-org/kingdoms/issues/60) todo->in-review; [kingdoms#61](https://github.com/merlin-pinpin-org/kingdoms/issues/61) todo->in-review; (+1 more) |
| 2026-09-21 | auto-sync: [kingdoms#59](https://github.com/merlin-pinpin-org/kingdoms/issues/59) in-review->done; [kingdoms#60](https://github.com/merlin-pinpin-org/kingdoms/issues/60) in-review->done; [kingdoms#61](https://github.com/merlin-pinpin-org/kingdoms/issues/61) in-review->done; [kingdoms#62](https://github.com/merlin-pinpin-org/kingdoms/issues/62) in-review->done; [kingdoms#65](https://github.com/merlin-pinpin-org/kingdoms/issues/65) in-review->done; (+4 more) |
| 2026-09-21 | auto-sync: [kingdoms#68](https://github.com/merlin-pinpin-org/kingdoms/issues/68) in-review->done |
| 2026-09-22 | auto-sync: [kingdoms-services#54](https://github.com/merlin-pinpin-org/kingdoms-services/issues/54) in-review->done |
| 2026-09-24 | auto-sync: [kingdoms-services#35](https://github.com/merlin-pinpin-org/kingdoms-services/issues/35) todo->done |
| 2026-09-24 | auto-sync: [kingdoms#92](https://github.com/merlin-pinpin-org/kingdoms/issues/92) todo->in-review |
| 2026-09-24 | auto-sync: [kingdoms#94](https://github.com/merlin-pinpin-org/kingdoms/issues/94) todo->in-review; [kingdoms-services#100](https://github.com/merlin-pinpin-org/kingdoms-services/issues/100) todo->in-review; [kingdoms-infra#71](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/71) todo->in-review |
| 2026-09-25 | auto-sync: [kingdoms#92](https://github.com/merlin-pinpin-org/kingdoms/issues/92) in-review->done; [kingdoms-services#100](https://github.com/merlin-pinpin-org/kingdoms-services/issues/100) in-review->done; [kingdoms-infra#71](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/71) in-review->todo |
| 2026-09-25 | auto-sync: [kingdoms-infra#71](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/71) todo->done |
| 2026-09-25 | auto-sync: [kingdoms#94](https://github.com/merlin-pinpin-org/kingdoms/issues/94) in-review->done |
| 2026-09-25 | auto-sync: [kingdoms-infra#3](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/3) todo->done |
| 2026-09-26 | Plan restructure with the game designer: living document kingdoms#109 + epics A→J (#110-#118); milestones v0.3.0 (MVP lot) and Backlog post-pivot created in kingdoms-services; #28 conventional changelog raised to P0 with amended scope (feeds release notes); invalid-labeled issues #3/#5/#7/#8/#11/#22 rehabilitated; current phase 2->3 |
| 2026-09-27 | auto-sync: [kingdoms-services#52](https://github.com/merlin-pinpin-org/kingdoms-services/issues/52) todo->done; current phase 3->2 |
| 2026-09-27 | auto-sync: [kingdoms-services#28](https://github.com/merlin-pinpin-org/kingdoms-services/issues/28) todo->in-review |
| 2026-09-27 | auto-sync: [kingdoms-services#3](https://github.com/merlin-pinpin-org/kingdoms-services/issues/3) todo->done; [kingdoms-services#5](https://github.com/merlin-pinpin-org/kingdoms-services/issues/5) todo->in-review |
| 2026-09-27 | auto-sync: [kingdoms-services#26](https://github.com/merlin-pinpin-org/kingdoms-services/issues/26) todo->in-review |
| 2026-09-27 | auto-sync: [kingdoms-services#55](https://github.com/merlin-pinpin-org/kingdoms-services/issues/55) todo->in-review |
| 2026-09-27 | auto-sync: [kingdoms-services#13](https://github.com/merlin-pinpin-org/kingdoms-services/issues/13) todo->in-review |
| 2026-09-27 | auto-sync: [kingdoms-services#7](https://github.com/merlin-pinpin-org/kingdoms-services/issues/7) todo->done; [kingdoms-services#16](https://github.com/merlin-pinpin-org/kingdoms-services/issues/16) todo->done; [kingdoms-services#17](https://github.com/merlin-pinpin-org/kingdoms-services/issues/17) todo->done; [kingdoms-services#11](https://github.com/merlin-pinpin-org/kingdoms-services/issues/11) todo->done; [kingdoms-services#22](https://github.com/merlin-pinpin-org/kingdoms-services/issues/22) todo->done; (+2 more) |
| 2026-09-27 | auto-sync: [kingdoms-services#56](https://github.com/merlin-pinpin-org/kingdoms-services/issues/56) todo->in-review |
| 2026-09-27 | auto-sync: [kingdoms-services#122](https://github.com/merlin-pinpin-org/kingdoms-services/issues/122) todo->in-review |
| 2026-09-27 | auto-sync: [kingdoms-services#10](https://github.com/merlin-pinpin-org/kingdoms-services/issues/10) todo->in-review |
| 2026-09-27 | auto-sync: [kingdoms-services#5](https://github.com/merlin-pinpin-org/kingdoms-services/issues/5) in-review->done; [kingdoms-services#10](https://github.com/merlin-pinpin-org/kingdoms-services/issues/10) in-review->done; [kingdoms-services#13](https://github.com/merlin-pinpin-org/kingdoms-services/issues/13) in-review->done; [kingdoms-services#28](https://github.com/merlin-pinpin-org/kingdoms-services/issues/28) in-review->done; [kingdoms-services#26](https://github.com/merlin-pinpin-org/kingdoms-services/issues/26) in-review->done; (+3 more) |
| 2026-09-28 | v0.4.0 rework with the game designer: AoE2 ladder slice (JeanJack V2.0 reference archived); ADR-0020 process split (bot-discord/svc-core/ext-*) supersedes ADR-0019, gRPC seams; issues kingdoms-services#128–#137, kingdoms-infra#89–#90; #27/#8/#14/#25 closed as superseded; #19/#120 moved to Backlog; docs/MODS/ladder rewritten; pluggable rating (Elo+Glicko-2), blossom matchmaking, seasons with optional reset |
| 2026-09-28 | v0.4.0 scope challenge: new issues #138–#142 (migration, test mandate, backpressure, ladder creation UI, rating replay switch); #134 split into sub-PRs; #130 replaces #122 mechanism; providers = priority chantier; scoping locked (mono-guild ladders, multi-guild identities, dev-run milestone); anti-abus → post-milestone |
| 2026-09-30 | auto-sync: [kingdoms-services#156](https://github.com/merlin-pinpin-org/kingdoms-services/issues/156) todo->in-review; [kingdoms-services#148](https://github.com/merlin-pinpin-org/kingdoms-services/issues/148) todo->in-review; current phase 3->2 |
| 2026-10-08 | auto-sync: [kingdoms-infra#78](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/78) todo->done; [kingdoms-services#133](https://github.com/merlin-pinpin-org/kingdoms-services/issues/133) todo->in-review; [kingdoms-services#15](https://github.com/merlin-pinpin-org/kingdoms-services/issues/15) todo->done; [kingdoms-services#134](https://github.com/merlin-pinpin-org/kingdoms-services/issues/134) todo->done; [kingdoms-services#135](https://github.com/merlin-pinpin-org/kingdoms-services/issues/135) todo->done; (+48 more) |
| 2026-10-08 | auto-sync: [kingdoms-services#133](https://github.com/merlin-pinpin-org/kingdoms-services/issues/133) in-review->done; [kingdoms-services#147](https://github.com/merlin-pinpin-org/kingdoms-services/issues/147) in-review->done |
| 2026-10-09 | auto-sync: [kingdoms-services#247](https://github.com/merlin-pinpin-org/kingdoms-services/issues/247) added to Sub-tasks (was missing) |
| 2026-10-10 | auto-sync: [kingdoms-services#247](https://github.com/merlin-pinpin-org/kingdoms-services/issues/247) todo->in-review; [kingdoms-services#251](https://github.com/merlin-pinpin-org/kingdoms-services/issues/251) added to Sub-tasks (was missing); [kingdoms-infra#111](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/111) added to Sub-tasks (was missing) |
