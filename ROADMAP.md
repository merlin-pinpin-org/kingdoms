# Kingdoms Roadmap

> Single source of truth for project progress. Updated via the
> [Update roadmap](.agents/skills/update-roadmap/SKILL.md) skill.

Status values: `todo` / `in-progress` / `in-review` / `done` / `blocked` / `dropped`.

## Current Phase
Phase 3 — v0.4.0 AoE2 ladder (process split + first game + ladder mod, milestone [v0.4.0](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/3)); ADR-0020 supersedes ADR-0019 for bot/core/providers

Product plan (post-pivot): see the living document [kingdoms#109](https://github.com/merlin-pinpin-org/kingdoms/issues/109) and epics A→J ([#110](https://github.com/merlin-pinpin-org/kingdoms/issues/110)–[#118](https://github.com/merlin-pinpin-org/kingdoms/issues/118)).

## Milestones

### Release milestones (kingdoms-services)
| Milestone | Scope |
|-----------|-------|
| [Lot 1 — Structural](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/1) | Structural lot (changelog #28, exceptions #10 ✱re-raised P0, config #16 ✅, enums #7 ✅, i18n #17 ✅, ChannelService #5, roles #26, UI #13, permission checks #55, DM policy #56, persistent views #122, core tests #22 ✅) — unlocks everything downstream, no player-facing mod. Superseded by the seam pivot: DiscordPlatform #11 ✅ (dead skeleton removed) |
| [v0.4.0 — AoE2 ladder](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/3) | AoE2 ladder vertical slice (JeanJack migration, ADR-0020 process split): gRPC seams #128 → games/aoe2 + providers #129 → identity/message-registry/surfaces #130 → game data (maps/civs/rules/pools/packs) #131 → seasons #132 → registration + profile validation #133 → ladder core #134 (blossom matchmaking, pluggable Elo/Glicko-2) → ladder Discord surface #135 → Discord-first admin surface #136 → E2E acceptance + rollout rehearsal #137. Infra: kingdoms-infra#89, #90. Out of scope: clans #19, tournament #120 (Backlog) |
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
| services: adapters | [kingdoms-services#8](https://github.com/merlin-pinpin-org/kingdoms-services/issues/8) | todo |
| services: StateService | [kingdoms-services#9](https://github.com/merlin-pinpin-org/kingdoms-services/issues/9) | done |
| services: exceptions | [kingdoms-services#10](https://github.com/merlin-pinpin-org/kingdoms-services/issues/10) | done |
| services: Protocol interfaces | [kingdoms-services#41](https://github.com/merlin-pinpin-org/kingdoms-services/issues/41) | done |
| services: config system | [kingdoms-services#16](https://github.com/merlin-pinpin-org/kingdoms-services/issues/16) | done |
| services: i18n | [kingdoms-services#17](https://github.com/merlin-pinpin-org/kingdoms-services/issues/17) | done |
| infra: CI/CD | [kingdoms-infra#2](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/2) | done |
| infra: infra docs | [kingdoms-infra#3](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/3) | done |
| infra: deployment scripts | [kingdoms-infra#4](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/4) | done |
| infra: monitoring | [kingdoms-infra#5](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/5) | todo |
| infra: post-deploy battery & auto rollback | [kingdoms-infra#78](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/78) | todo |
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
| services: registration + profile validation | [kingdoms-services#133](https://github.com/merlin-pinpin-org/kingdoms-services/issues/133) | todo |
| services: ladder mod (core #134 + surface #135) | [kingdoms-services#15](https://github.com/merlin-pinpin-org/kingdoms-services/issues/15) | todo |
| services: process split + gRPC seams (ADR-0020) | [kingdoms-services#128](https://github.com/merlin-pinpin-org/kingdoms-services/issues/128) | todo |
| services: games/aoe2 + ext-librematch/ext-aoe2lobby | [kingdoms-services#129](https://github.com/merlin-pinpin-org/kingdoms-services/issues/129) | todo |
| services: identity, message registry, surfaces | [kingdoms-services#130](https://github.com/merlin-pinpin-org/kingdoms-services/issues/130) | todo |
| services: game data catalog (maps/civs/rules/pools/packs) | [kingdoms-services#131](https://github.com/merlin-pinpin-org/kingdoms-services/issues/131) | todo |
| services: seasons (rotations, optional reset) | [kingdoms-services#132](https://github.com/merlin-pinpin-org/kingdoms-services/issues/132) | todo |
| services: Discord-first admin surface (game data, pools, seasons, rating) | [kingdoms-services#136](https://github.com/merlin-pinpin-org/kingdoms-services/issues/136) | todo |
| services: E2E acceptance + AoE2 seeding + rollout rehearsal | [kingdoms-services#137](https://github.com/merlin-pinpin-org/kingdoms-services/issues/137) | todo |
| services: channel access policies (#130/#135 dependency) | [kingdoms-services#57](https://github.com/merlin-pinpin-org/kingdoms-services/issues/57) | todo |
| services: Discord delivery backpressure | [kingdoms-services#140](https://github.com/merlin-pinpin-org/kingdoms-services/issues/140) | todo |
| services: ladder creation UI (mono-guild) | [kingdoms-services#141](https://github.com/merlin-pinpin-org/kingdoms-services/issues/141) | todo |
| services: rating switch via history replay | [kingdoms-services#142](https://github.com/merlin-pinpin-org/kingdoms-services/issues/142) | todo |
| services: JeanJack data migration | [kingdoms-services#138](https://github.com/merlin-pinpin-org/kingdoms-services/issues/138) | todo |
| services: blanket test mandate (CI properties) | [kingdoms-services#139](https://github.com/merlin-pinpin-org/kingdoms-services/issues/139) | todo |
| infra: 4-process deploy + gRPC networking | [kingdoms-infra#89](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/89) | todo |
| infra: cross-process observability | [kingdoms-infra#90](https://github.com/merlin-pinpin-org/kingdoms-infra/issues/90) | todo |
| services: tournament mod (80% operator-assisted) | [kingdoms-services#120](https://github.com/merlin-pinpin-org/kingdoms-services/issues/120) | backlog |
| services: full-auto tournament mode | [kingdoms-services#121](https://github.com/merlin-pinpin-org/kingdoms-services/issues/121) | todo |
| services: clans mod | [kingdoms-services#19](https://github.com/merlin-pinpin-org/kingdoms-services/issues/19) | backlog |
| services: admin mod | [kingdoms-services#21](https://github.com/merlin-pinpin-org/kingdoms-services/issues/21) | todo |
| services: deployment scripts | [kingdoms-services#20](https://github.com/merlin-pinpin-org/kingdoms-services/issues/20) | todo |
| services: semantic release | [kingdoms-services#28](https://github.com/merlin-pinpin-org/kingdoms-services/issues/28) | done |
| services: startup announcement (PR link) | [kingdoms-services#52](https://github.com/merlin-pinpin-org/kingdoms-services/issues/52) | done |

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
| kingdoms: Epic H — Monetization | [kingdoms#116](https://github.com/merlin-pinpin-org/kingdoms/issues/116) | todo |
| kingdoms: Epic I — Review & coaching marketplace | [kingdoms#117](https://github.com/merlin-pinpin-org/kingdoms/issues/117) | todo |
| kingdoms: Epic J — Social & moderation | [kingdoms#118](https://github.com/merlin-pinpin-org/kingdoms/issues/118) | todo |

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
| Channel access + drift alerting | [kingdoms-services#57](https://github.com/merlin-pinpin-org/kingdoms-services/issues/57) | todo |
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

## Out of Scope
- Report mod (`/report` command) — dropped, see [kingdoms-services#18](https://github.com/merlin-pinpin-org/kingdoms-services/issues/18)
  (closed as not planned)
- Twitch platform — architecture-ready (`IPlatform`), not implemented

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
