# Architecture

> Status: **placeholder** — the full architecture documentation is written in
> kingdoms#2. This skeleton ensures links and the directory structure exist
> from the start.

This document describes the technical architecture of Kingdoms:

- the generic core (platform abstraction, models, services, enums)
- the Discord implementation (platform adapter, bot, UI components)
- the configuration (YAML locales, games, mods)
- the infrastructure (Docker Compose, GitOps, CI/CD)

It will contain at least three Mermaid diagrams (global architecture,
communication flow, channel management) and justify the key technical
decisions. Decisions are recorded as ADRs in [DECISIONS/](DECISIONS/).

See also:

- [WORKFLOWS.md](WORKFLOWS.md) for the game workflow documentation
- [../AGENTS.md](../AGENTS.md) for the repo rules
