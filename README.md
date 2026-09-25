[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](LICENSE)

# Kingdoms

Kingdoms is a modular Discord bot platform, built and maintained through a
vibe-coding workflow. It is the successor of JeanJack.

This repository is the **source of truth** for the project: it hosts all
architecture documentation, game workflows, mods documentation (rules and
environment), Architecture Decision Records (ADRs), and auto-generated
development docs. No application code lives here.

## Repositories

| Repository | Purpose |
| ---------- | ------- |
| [kingdoms](https://github.com/merlin-pinpin-org/kingdoms) (this repo) | Documentation: architecture, workflows, ADRs, mods docs, generated dev docs |
| [kingdoms-services](https://github.com/merlin-pinpin-org/kingdoms-services) | All Python code: generic core, Discord platform, mods, YAML configs |
| [kingdoms-infra](https://github.com/merlin-pinpin-org/kingdoms-infra) | Docker, CI/CD, GitOps manifests, deployment scripts |

## Key principles

1. **Platform-agnostic core** — game logic lives in
   `kingdoms-services/src/kingdoms/core/`, behind the `IPlatform`
   interface. Discord is one implementation
   ([ADR-0001](docs/DECISIONS/001-multi-platform-architecture.md))
2. **Modular mods** — each game mode is a self-contained mod declaring its
   channels, roles, and workflows via `ModRegistry`
   ([docs/MODS/](docs/MODS/),
   [docs/architecture/mods.md](docs/architecture/mods.md))
3. **MongoDB only** (no relational database) for durable data, plus
   **Redis** for cache, hot state, and distributed locks
   ([ADR-0004](docs/DECISIONS/004-mongodb-schema-design.md),
   [ADR-0005](docs/DECISIONS/005-redis-state-management.md))
4. **Full-stack testing** — `MockDiscord` provides an in-memory
   `IPlatform` simulation; no test ever touches the real Discord API
   ([docs/architecture/testing.md](docs/architecture/testing.md))
5. **i18n by default** — English is the default locale, French is
   available; every user-facing string comes from YAML locale files
   ([ADR-0008](docs/DECISIONS/008-i18n-system.md))

## Documentation structure

```
kingdoms/
├── README.md                      # This overview
├── AGENTS.md                      # Rules for AI coding agents
├── docs/
│   ├── ARCHITECTURE.md            # Technical architecture (Mermaid diagrams)
│   ├── GAME-DESIGN.md             # The game designer's guide (in French)
│   ├── WORKFLOWS.md               # Game workflows (registration, ladder, ...)
│   ├── MODS/                      # Mods documentation
│   │   ├── register/              # Registration mod (rules, environment)
│   │   ├── ladder/                # Ladder mod (rules, environment)
│   │   └── TEMPLATE/              # Template referenced by new mod docs
│   └── DECISIONS/                 # Architecture Decision Records (ADR)
├── .github/workflows/             # Docs generation and validation workflows
├── scripts/                       # Doc generation and validation scripts
└── templates/                     # Reusable templates (mods, ADRs)
```

## Key documents

- [docs/GAME-DESIGN.md](docs/GAME-DESIGN.md) — **the game designer's guide**:
  how to describe an idea, follow its delivery, test it in Discord, read
  the bot's `/status` — no tooling involved
- [AGENTS.md](AGENTS.md) — rules every AI coding agent must follow in this repo
- [ROADMAP.md](ROADMAP.md) — project phases and issue status (kept in sync
  by `scripts/sync_roadmap.py`; see the
  [Update roadmap](.agents/skills/update-roadmap/SKILL.md) skill)
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — technical architecture
- [docs/WORKFLOWS.md](docs/WORKFLOWS.md) — game workflows
- [docs/DECISIONS/](docs/DECISIONS/) — architecture decision records
- [docs/MODS/](docs/MODS/) — mods documentation

## Automation

Generated artifacts (`ROADMAP.md`, `docs/DEPENDENCIES.md`) are refreshed by
the sync skills ([Update roadmap](.agents/skills/update-roadmap/SKILL.md),
[Update dependencies](.agents/skills/update-dependencies/SKILL.md)): run
`scripts/sync_roadmap.py` / `scripts/sync_dependencies.py` locally and
commit the result to the PR branch — no rolling automation PR, no ghost PR.

Generated technical documentation (pydoc) lives in `kingdoms-services`
([`docs/DEVELOPMENT/pydoc`](https://github.com/merlin-pinpin-org/kingdoms-services/tree/main/docs/DEVELOPMENT/pydoc)),
next to the sources it documents; a dedicated workflow checks its freshness
on every PR of that repo.

The sync scripts read the issues of `kingdoms-services` and
`kingdoms-infra` through `gh api`; all three repositories are public, so no
credentials are needed. They fail closed when a repository is unreadable.
The `Check Docs` workflow (`scripts/validate_docs.py`) runs on every PR.

## Contributing

You do not need an AI agent to contribute to Kingdoms. The human path:

1. Pick or create an issue (templates are mandatory; blank issues are
   disabled).
2. Clone this repo and [`kingdoms-services`](https://github.com/merlin-pinpin-org/kingdoms-services)
   side by side, create a branch from `main`.
3. Edit the documentation, then run `make session-check
   KINGDOMS_SERVICES=../kingdoms-services` — the same validation CI runs
   on every PR.
4. If you created or closed issues, regenerate the synced artifacts with
   `make sync-artifacts` (`ROADMAP.md` and `docs/DEPENDENCIES.md` are
   generated — never edit them by hand).
5. Open a pull request; the maintainer merges.

Documentation must be in **English**; game-related examples may be in
French for i18n purposes.

The project is primarily built through the vibe-coding workflow (an AI
agent implements issues on `vibe/<short-slug>` branches — see
[AGENTS.md](AGENTS.md)), but human contributions follow exactly the same
checks. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide and the
CLA process.

## License

Kingdoms is licensed under the [GNU Affero General Public License v3.0](LICENSE).
AGPL-3.0 was chosen so that any fork operated as a service must publish its
modified source to its users (§13) — a direct deterrent for competitive
privatization, since a bot is inherently a network service. External
contributors sign the [CLA](CLA.md), which preserves a relicensing option for
the project owner.
