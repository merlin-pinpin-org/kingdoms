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
| [kingdoms](https://github.com/merlin-pinpin/kingdoms) (this repo) | Documentation: architecture, workflows, ADRs, mods docs, generated dev docs |
| [kingdoms-services](https://github.com/merlin-pinpin/kingdoms-services) | All Python code: generic core, Discord platform, mods, YAML configs |
| [kingdoms-infra](https://github.com/merlin-pinpin/kingdoms-infra) | Docker, CI/CD, GitOps manifests, deployment scripts |

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
│   ├── WORKFLOWS.md               # Game workflows (registration, ladder, ...)
│   ├── MODS/                      # Mods documentation
│   │   ├── register/              # Registration mod (rules, environment)
│   │   ├── ladder/                # Ladder mod (rules, environment)
│   │   └── TEMPLATE/              # Template referenced by new mod docs
│   ├── DEVELOPMENT/               # Auto-generated technical docs
│   │   ├── api/                   # Generated API docs
│   │   └── pydoc/                 # Generated pydoc HTML
│   └── DECISIONS/                 # Architecture Decision Records (ADR)
├── .github/workflows/             # Docs generation and validation workflows
├── scripts/                       # Doc generation and validation scripts
└── templates/                     # Reusable templates (mods, ADRs)
```

## Key documents

- [AGENTS.md](AGENTS.md) — rules every AI coding agent must follow in this repo
- [ROADMAP.md](ROADMAP.md) — project phases and issue status (kept in sync
  automatically by the `Sync roadmap` workflow; the
  [Update roadmap](docs/SKILLS/update-roadmap.md) skill is the manual fallback)
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — technical architecture
- [docs/WORKFLOWS.md](docs/WORKFLOWS.md) — game workflows
- [docs/DECISIONS/](docs/DECISIONS/) — architecture decision records
- [docs/MODS/](docs/MODS/) — mods documentation

## Automation secrets

The cross-repo automation (`Sync roadmap`, `Sync dependencies`) needs to read
the issues of the private `kingdoms-infra` repository, which the default
`GITHUB_TOKEN` cannot. Two repository secrets are required (the workflows fail
closed without them):

| Secret | Where | Fine-grained PAT permission |
| ------ | ----- | --------------------------- |
| `ROADMAP_DISPATCH_PAT` | `kingdoms-services`, `kingdoms-infra` | "Contents: read and write" on `merlin-pinpin/kingdoms` |
| `DEPS_SYNC_PAT` | `kingdoms` | "Issues: read" on `merlin-pinpin/kingdoms-services` AND `merlin-pinpin/kingdoms-infra` |

See the [Update roadmap](docs/SKILLS/update-roadmap.md) and
[Update dependencies](docs/SKILLS/update-dependencies.md) skills for details.

## Contributing

Contributions are made through the vibe-coding workflow:

1. Work is tracked in [GitHub issues](https://github.com/merlin-pinpin/kingdoms/issues).
2. Each issue is developed on a dedicated `vibe/<short-slug>` branch.
3. A draft pull request is opened for every issue and reviewed before merge.
4. Documentation must be in **English**; game-related examples may be in French
   for i18n purposes.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution guide and
the CLA process.

## License

Kingdoms is licensed under the [GNU Affero General Public License v3.0](LICENSE).
AGPL-3.0 was chosen so that any fork operated as a service must publish its
modified source to its users (§13) — a direct deterrent for competitive
privatization, since a bot is inherently a network service. External
contributors sign the [CLA](CLA.md), which preserves a relicensing option for
the project owner.
