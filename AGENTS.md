# AGENTS.md

## Project
Kingdoms documentation repo — the **source of truth** for the Kingdoms Discord bot platform.

## Repositories
- `kingdoms` (this repo): architecture, workflows, ADRs, mods documentation, generated dev docs
- `kingdoms-services`: all Python code (core, Discord platform, mods, YAML configs)
- `kingdoms-infra`: Docker, CI/CD, GitOps manifests, deployment scripts

## Rules for AI agents
- All documentation is written in **English**, as well as commit messages,
  PR titles and PR descriptions.
- Mermaid diagrams must use **GitHub-compatible syntax** (quote node labels containing special characters like `->` or `{}`; never put colons inside unquoted labels).
- This repo is the source of truth: keep `docs/` in sync with any change made in `kingdoms-services` or `kingdoms-infra`. A code change without its doc update is incomplete.
- Reference issues with full repo-qualified identifiers (e.g., `kingdoms-services#12`) since cross-repo references are common.
- Follow the ADR process in `docs/DECISIONS/` for any major architecture change.
- Mods documentation lives in `docs/MODS/<mod-name>/` and follows the template in `templates/mod-template/`.
- **Never commit secrets** (tokens, passwords, API keys, private keys,
  `.env` values): real credentials live only in GitHub secrets or in
  host-provisioned `.env` files; repositories carry `.env.example`
  placeholders only. Before making any repository public, scan the full
  git history for leaked secrets (`git log -p | grep -E "ghp_|github_pat_|AKIA|PRIVATE KEY"`)
  and get merlin-pinpin's approval.
- The agent **never** merges a PR without an explicit merge approval from
  the developer (a named go-ahead such as "merge #44" — not a review
  comment, a "LGTM", an idea approval, or silence; CI must be green). For
  changes with a critical architecture impact (ADR-level design, data
  model, core interfaces, infrastructure/deployment, security), the
  approval must come from **merlin-pinpin**: he is the sole decision-maker
  for production; other users may at most deploy non-prod environments,
  as he directs.
- At the end of every session, verify the roadmap: post `/roadmap` on your
  open PR — the `PR commands` workflow (`docs/SKILLS/pr-commands.md`) runs
  `scripts/sync_roadmap.py` and commits the synced `ROADMAP.md` to the PR
  branch; only run the "Update roadmap" skill
  (`docs/SKILLS/update-roadmap.md`) manually when automation is down or a
  status needs human judgment.

## Session checklist (do this by default)

At the end of every session, verify consistency across the three repos:

1. **Docs vs code**: a code change in `kingdoms-services` or `kingdoms-infra`
   without its doc update here is incomplete. Check that the docs describing
   what you changed are still accurate.
2. **Issues vs code**: after closing or starting work, confirm the linked
   issues reflect reality (state, acceptance criteria, `## Dependencies`
   checkboxes).
3. **Dependency graph**: post `/dependencies` on your open PR — the
   `PR commands` workflow regenerates `docs/DEPENDENCIES.md` from the
   `## Dependencies` sections of open issues in `kingdoms-services` and
   `kingdoms-infra` and commits it to the PR branch. Only run the
   "Update dependencies" skill (`docs/SKILLS/update-dependencies.md`)
   manually when automation is down or dependencies, sizes or priorities
   were re-decided by a human.
4. **Docs validation**: `python3 scripts/validate_docs.py --check
   --source <kingdoms-services>/src/kingdoms --config
   <kingdoms-services>/config` must pass before opening any PR (fail-closed:
   it refuses to validate without the kingdoms-services source/config).
   The `Check Docs` required check re-runs it on every PR. Generated technical
   docs (pydoc) live in `kingdoms-services` and are freshness-checked there
   (see [docs/SKILLS/pr-commands.md](docs/SKILLS/pr-commands.md)).

## Issue conventions

- Every open issue in `kingdoms-services` and `kingdoms-infra` carries exactly
  one `size/*` label (XS/S/M/L/XL, Fibonacci points, set by judgment), one
  `priority/P0-P3` label (critical-path slack, maintained by
  `scripts/sync_dependencies.py`), and a `phase-N` label.
- Every issue has a `## Dependencies` section: task-list checkboxes pointing
  at the issues it blocks on (fully qualified for cross-repo refs, e.g.
  `merlin-pinpin/kingdoms-infra#2`). "Depends on" = cannot start before;
  soft relations stay in `## Related`.
- When creating an issue, add its dependencies and `size/*` label, then let
  the sync workflow assign `priority/*`; if priorities look off, re-run the
  skill manually. See [docs/SKILLS/update-dependencies.md](docs/SKILLS/update-dependencies.md).

## See also

- [ARCHITECTURE.md](docs/ARCHITECTURE.md) — system overview
- [ROADMAP.md](ROADMAP.md) — project progress, synced with issue states
- [docs/DEPENDENCIES.md](docs/DEPENDENCIES.md) — dependency graph, critical
  path, waves, priorities, synced from issue `## Dependencies` sections
