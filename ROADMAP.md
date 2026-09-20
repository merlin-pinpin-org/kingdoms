# Kingdoms Roadmap

> Single source of truth for project progress. Updated via the
> [Update roadmap](docs/SKILLS/update-roadmap.md) skill.

Status values: `todo` / `in-progress` / `in-review` / `done` / `blocked` / `dropped`.

## Current Phase
Phase 1 — Foundations (repos structure, architecture docs)

## Milestones

### Phase 1 — Foundations
| Track | Issue | Status |
|-------|-------|--------|
| kingdoms: repo structure | [kingdoms#1](https://github.com/merlin-pinpin/kingdoms/issues/1) | done |
| kingdoms: architecture docs | [kingdoms#2](https://github.com/merlin-pinpin/kingdoms/issues/2) | done |
| kingdoms: docs CI | [kingdoms#3](https://github.com/merlin-pinpin/kingdoms/issues/3) | done |
| kingdoms: WORKFLOWS.md | [kingdoms#4](https://github.com/merlin-pinpin/kingdoms/issues/4) | done |
| kingdoms: MODS docs | [kingdoms#5](https://github.com/merlin-pinpin/kingdoms/issues/5) | done |
| kingdoms: ADRs | [kingdoms#6](https://github.com/merlin-pinpin/kingdoms/issues/6) | done |
| kingdoms: governance (LICENSE, CLA) | [kingdoms#11](https://github.com/merlin-pinpin/kingdoms/issues/11) | done |
| kingdoms: ROADMAP + skill | [kingdoms#9](https://github.com/merlin-pinpin/kingdoms/issues/9) | done |
| kingdoms: vibe-coding workflow doc | [kingdoms#10](https://github.com/merlin-pinpin/kingdoms/issues/10) | done |
| kingdoms: roadmap automation | [kingdoms#27](https://github.com/merlin-pinpin/kingdoms/issues/27) | done |
| services: repo structure | [kingdoms-services#1](https://github.com/merlin-pinpin/kingdoms-services/issues/1) | done |
| services: MockDiscord | [kingdoms-services#2](https://github.com/merlin-pinpin/kingdoms-services/issues/2) | todo |
| infra: repo structure | [kingdoms-infra#1](https://github.com/merlin-pinpin/kingdoms-infra/issues/1) | done |

### Phase 2 — Core
| Track | Issue | Status |
|-------|-------|--------|
| services: IPlatform | [kingdoms-services#3](https://github.com/merlin-pinpin/kingdoms-services/issues/3) | todo |
| services: DB models | [kingdoms-services#4](https://github.com/merlin-pinpin/kingdoms-services/issues/4) | todo |
| services: ChannelService | [kingdoms-services#5](https://github.com/merlin-pinpin/kingdoms-services/issues/5) | todo |
| services: WorkflowEngine | [kingdoms-services#6](https://github.com/merlin-pinpin/kingdoms-services/issues/6) | todo |
| services: enums | [kingdoms-services#7](https://github.com/merlin-pinpin/kingdoms-services/issues/7) | todo |
| services: adapters | [kingdoms-services#8](https://github.com/merlin-pinpin/kingdoms-services/issues/8) | todo |
| services: StateService | [kingdoms-services#9](https://github.com/merlin-pinpin/kingdoms-services/issues/9) | todo |
| services: exceptions | [kingdoms-services#10](https://github.com/merlin-pinpin/kingdoms-services/issues/10) | todo |
| services: Protocol interfaces | [kingdoms-services#41](https://github.com/merlin-pinpin/kingdoms-services/issues/41) | done |
| services: config system | [kingdoms-services#16](https://github.com/merlin-pinpin/kingdoms-services/issues/16) | todo |
| services: i18n | [kingdoms-services#17](https://github.com/merlin-pinpin/kingdoms-services/issues/17) | todo |
| infra: CI/CD | [kingdoms-infra#2](https://github.com/merlin-pinpin/kingdoms-infra/issues/2) | todo |
| infra: infra docs | [kingdoms-infra#3](https://github.com/merlin-pinpin/kingdoms-infra/issues/3) | todo |
| infra: deployment scripts | [kingdoms-infra#4](https://github.com/merlin-pinpin/kingdoms-infra/issues/4) | todo |
| infra: monitoring | [kingdoms-infra#5](https://github.com/merlin-pinpin/kingdoms-infra/issues/5) | todo |

### Phase 3 — Mods & Discord
| Track | Issue | Status |
|-------|-------|--------|
| services: DiscordPlatform | [kingdoms-services#11](https://github.com/merlin-pinpin/kingdoms-services/issues/11) | todo |
| services: Bot structure | [kingdoms-services#12](https://github.com/merlin-pinpin/kingdoms-services/issues/12) | todo |
| services: UI components | [kingdoms-services#13](https://github.com/merlin-pinpin/kingdoms-services/issues/13) | todo |
| services: registration mod | [kingdoms-services#14](https://github.com/merlin-pinpin/kingdoms-services/issues/14) | todo |
| services: ladder mod | [kingdoms-services#15](https://github.com/merlin-pinpin/kingdoms-services/issues/15) | todo |
| services: clans mod | [kingdoms-services#19](https://github.com/merlin-pinpin/kingdoms-services/issues/19) | todo |
| services: admin mod | [kingdoms-services#21](https://github.com/merlin-pinpin/kingdoms-services/issues/21) | todo |
| services: deployment scripts | [kingdoms-services#20](https://github.com/merlin-pinpin/kingdoms-services/issues/20) | todo |
| services: semantic release | [kingdoms-services#28](https://github.com/merlin-pinpin/kingdoms-services/issues/28) | todo |

### Sub-tasks
| Sub-task | Parent | Status |
|----------|--------|--------|
| Unit tests core | [kingdoms-services#22](https://github.com/merlin-pinpin/kingdoms-services/issues/22) | todo |
| Mongo+Redis caching | [kingdoms-services#23](https://github.com/merlin-pinpin/kingdoms-services/issues/23) | todo |
| MockDiscord framework | [kingdoms-services#24](https://github.com/merlin-pinpin/kingdoms-services/issues/24) | todo |
| Registration DM flow | [kingdoms-services#25](https://github.com/merlin-pinpin/kingdoms-services/issues/25) | todo |
| Channel/role mgmt | [kingdoms-services#26](https://github.com/merlin-pinpin/kingdoms-services/issues/26) | todo |
| Bot vs guild admins | [kingdoms-services#35](https://github.com/merlin-pinpin/kingdoms-services/issues/35) | todo |
| AoE2 game service | [kingdoms-services#27](https://github.com/merlin-pinpin/kingdoms-services/issues/27) | todo |
| Docs architecture | [kingdoms#7](https://github.com/merlin-pinpin/kingdoms/issues/7) | done |
| discord.py guide | [kingdoms#8](https://github.com/merlin-pinpin/kingdoms/issues/8) | done |

## Out of Scope
- Report mod (`/report` command) — dropped, see [kingdoms-services#18](https://github.com/merlin-pinpin/kingdoms-services/issues/18)
  (closed as not planned)
- Twitch platform — architecture-ready (`IPlatform`), not implemented

## Change Log
| Date | Change |
|------|--------|
| 2026-09-18 | Initial roadmap (kingdoms#9), synced with GitHub issue states |
| 2026-09-18 | kingdoms#3 in-review (PR #21); session PRs #12-#21 opened for kingdoms#1-#6, #8-#11 |
| 2026-09-19 | auto-sync: kingdoms#1 in-review->done; kingdoms#2 in-review->done; kingdoms#3 in-review->done; kingdoms#4 todo->done; kingdoms#5 todo->done; (+7 more) |
| 2026-09-20 | auto-sync: [kingdoms-services#1](https://github.com/merlin-pinpin/kingdoms-services/issues/1) todo->done; [kingdoms-infra#1](https://github.com/merlin-pinpin/kingdoms-infra/issues/1) todo->done |
| 2026-09-20 | auto-sync: [kingdoms-services#41](https://github.com/merlin-pinpin/kingdoms-services/issues/41) in-review->done |
| 2026-09-20 | post-merge smoke test: PR comment commands verified on main (GITHUB_TOKEN cross-repo reads) |
