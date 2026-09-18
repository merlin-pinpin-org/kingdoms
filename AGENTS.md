# AGENTS.md

## Project
Kingdoms documentation repo — the **source of truth** for the Kingdoms Discord bot platform.

## Repositories
- `kingdoms` (this repo): architecture, workflows, ADRs, mods documentation, generated dev docs
- `kingdoms-services`: all Python code (core, Discord platform, mods, YAML configs)
- `kingdoms-infra`: Docker, CI/CD, GitOps manifests, deployment scripts

## Rules for AI agents
- All documentation is written in **English**.
- Mermaid diagrams must use **GitHub-compatible syntax** (quote node labels containing special characters like `->` or `{}`; never put colons inside unquoted labels).
- This repo is the source of truth: keep `docs/` in sync with any change made in `kingdoms-services` or `kingdoms-infra`. A code change without its doc update is incomplete.
- Reference issues with full repo-qualified identifiers (e.g., `kingdoms-services#12`) since cross-repo references are common.
- Follow the ADR process in `docs/DECISIONS/` for any major architecture change.
- Mods documentation lives in `docs/MODS/<mod-name>/` and follows the template in `templates/mod-template/`.
- At the end of every session, run the "Update roadmap" skill (`docs/SKILLS/update-roadmap.md`) to sync `ROADMAP.md` with GitHub issue states.
