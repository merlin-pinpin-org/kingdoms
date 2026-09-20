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
  git history for leaked secrets (`git log -p | grep -E "ghp_|github_pat_|AKIA|PRIVATE KEY"`).
- Merge approvals and required checks are enforced by the `main` ruleset
  of each repository; do not document person-based permissions here.
- Anyone can run the local checks (`python3 scripts/validate_docs.py` with
  the `kingdoms-services` clone next to this repo); they require public
  clones only, no credentials.
- At the end of every session, verify the roadmap: run
  `scripts/sync_roadmap.py` (the "Update roadmap" skill,
  `docs/SKILLS/update-roadmap.md`) and commit the synced `ROADMAP.md` to
  your open PR branch. Statuses needing human judgment (`in-progress`,
  `blocked`) are set manually and preserved by the script.

## Testing strategy (summary)

Full strategy: [docs/architecture/testing.md](docs/architecture/testing.md).
Two complementary Discord test doubles — pick the right depth:

- **MockDiscord** (mock objects, `kingdoms-services` `tests/mocks/`) for
  adapter and UI-builder unit tests; permissive by design, never validates
  the discord.py glue.
- **SimCord** (behavioral simulator, dev-dependency `simcord[pytest]` in
  `kingdoms-services`) for journeys through the real discord.py dispatch:
  slash commands, buttons, selects, modals, permissions, timeouts,
  Components V2. Drive the bot as a user; never call a command callback
  directly; no token, no network, no sleeps.

A doc change describing testing must keep this page and
`docs/architecture/testing.md` consistent.

## Session checklist (do this by default)

At the end of every session, verify consistency across the three repos:

1. **Docs vs code**: a code change in `kingdoms-services` or `kingdoms-infra`
   without its doc update here is incomplete. Check that the docs describing
   what you changed are still accurate.
2. **Issues vs code**: after closing or starting work, confirm the linked
   issues reflect reality (state, acceptance criteria, `## Dependencies`
   checkboxes).
3. **Dependency graph**: run `scripts/sync_dependencies.py` (the
   "Update dependencies" skill, `docs/SKILLS/update-dependencies.md`) and
   commit the regenerated `docs/DEPENDENCIES.md` to your open PR branch.
   Fix any priority-label drift it reports (`gh issue edit`), then re-run.
4. **Docs validation**: `python3 scripts/validate_docs.py --check
   --source <kingdoms-services>/src/kingdoms --config
   <kingdoms-services>/config` must pass before opening any PR (fail-closed:
   it refuses to validate without the kingdoms-services source/config).
   The `Check Docs` required check re-runs it on every PR. Generated technical
   docs (pydoc) live in `kingdoms-services` and are freshness-checked there.

## Issue conventions

- Every open issue in `kingdoms-services` and `kingdoms-infra` carries exactly
  one `size/*` label (XS/S/M/L/XL, Fibonacci points, set by judgment), one
  `priority/P0-P3` label (critical-path slack, maintained by
  `scripts/sync_dependencies.py`), and a `phase-N` label.
- Every issue has a `## Dependencies` section: task-list checkboxes pointing
  at the issues it blocks on (fully qualified for cross-repo refs, e.g.
  `merlin-pinpin/kingdoms-infra#2`). "Depends on" = cannot start before;
  soft relations stay in `## Related`.
- When creating an issue, add its dependencies and `size/*` label, then run
  `scripts/sync_dependencies.py` and fix the `priority/*` labels it reports
  as drifted. See [docs/SKILLS/update-dependencies.md](docs/SKILLS/update-dependencies.md).

## See also

- [ARCHITECTURE.md](docs/ARCHITECTURE.md) — system overview
- [ROADMAP.md](ROADMAP.md) — project progress, synced with issue states
- [docs/DEPENDENCIES.md](docs/DEPENDENCIES.md) — dependency graph, critical
  path, waves, priorities, synced from issue `## Dependencies` sections
