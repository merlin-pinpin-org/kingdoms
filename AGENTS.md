# AGENTS.md

Kingdoms documentation repo — the **source of truth** for the Kingdoms
Discord bot platform (architecture, ADRs, operating docs, mods
documentation, generated roadmap and dependency graph).

## Read first

- [docs/CONVENTIONS.md](docs/CONVENTIONS.md) — conventions shared by the
  three repositories (language, humans-never-code, secrets, PR lifecycle,
  issues, checks).
- [docs/VIBEWORKFLOW.md](docs/VIBEWORKFLOW.md) — operating model (roles,
  session loop, approvals, deployment flow).
- [docs/DEVELOPER.md](docs/DEVELOPER.md) — this repo's layout, checks,
  ADR process, mods documentation, generated artifacts.

## Repositories

- `kingdoms` (this repo): docs, ADRs, sync/validation scripts
- `kingdoms-services`: all Python code (core, Discord platform, mods)
- `kingdoms-infra`: Docker, CI/CD, GitOps manifests, deploy scripts

## Local rules

- Run `python3 scripts/validate_docs.py --check --source <kingdoms-services>/src/kingdoms --config <kingdoms-services>/config`
  before opening any PR (the `Check Docs` required check re-runs it).
- Never edit `ROADMAP.md` or `docs/DEPENDENCIES.md` by hand — change the
  issue state or its `## Dependencies` section and run the sync scripts
  (`scripts/sync_roadmap.py`, `scripts/sync_dependencies.py`), committing
  the regenerated files to your open PR branch.
- Keep the docs in sync with any change made in `kingdoms-services` or
  `kingdoms-infra` — a code change without its doc update here is
  incomplete.
- Issue templates: `## Summary` / `## Details` (blank issues disabled).
- **No one-off automation:** every recurring operation is a committed
  Makefile target, script or workflow, and every improvised-but-useful
  command is committed ("learned") — see the
  [Automate or learn](.agents/skills/automate-or-learn/SKILL.md) skill and
  [docs/CONVENTIONS.md](docs/CONVENTIONS.md), *Human GitHub scope* and
  *Everything is automation*.
- **Skills** live in [`.agents/skills/`](.agents/skills/) (Agent Skills
  open standard: one directory per skill, `SKILL.md` with YAML
  frontmatter). Read a skill's `SKILL.md` when a task matches its
  description: deploy-and-validate, ci-monitoring, diagnose-deploy,
  release-flow, shape-game-designer-idea, restack-prs, update-roadmap,
  update-dependencies. New procedural knowledge goes there — when you
  learn something new, propose persisting it (see the *Propose to
  memorize new knowledge* rule in CONVENTIONS.md).
