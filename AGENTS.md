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
- ADR status: a decision shaped and challenged collaboratively with the
  developer during a session is **Accepted** on creation; the ADR body records
  the co-construction. An ADR drafted unilaterally by the agent starts as
  **Proposed** until the developer reviews it.
- Before writing a new ADR file, create its tracking issue and check the numbers
  already reserved by other open issues and in-flight PRs (parallel sessions
  are common); never pick a number already in use.
- Mods documentation lives in `docs/MODS/<mod-name>/` and follows the template in `templates/mod-template/`.
- **Never commit secrets** (tokens, passwords, API keys, private keys,
  `.env` values): real credentials live only in GitHub **environment
  secrets**, injected by the CD runner at deploy time (nothing secret is
  stored on the VPS); repositories carry `.env.example` placeholders only. Before making any repository public, scan the full
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
- **PR draft status is the merge-readiness signal** (see
  `docs/VIBEWORKFLOW.md`): always open PRs as drafts; mark a PR ready for
  review only when, from your point of view, it can be merged (checks
  green, implementation complete, self-review done, docs updated); keep or
  return it to draft (`gh pr ready --undo`) while work remains.
- **Validate a user-facing change in Discord before asking for a merge:**
  deploy the PR to the test environment (the `/deploy` PR comment on
  kingdoms-services) and let the human check the live behavior in Discord
  first; only then ask for the merge. Never present a PR as ready to
  merge while its live validation is still pending.
- **Humans never check out, write code, or run scripts.** This platform is
  a pure vibe-coding test: the AI agent does 100% of the technical work.
  Never propose a solution that requires a human to run a CLI command, a
  script, or any local tooling. The only manual technical actions are
  **clicks in the GitHub web UI** (team, ruleset, environment and secret
  administration, PR approvals, production deployment approvals),
  performed by authorized humans. When a GitHub admin action is needed
  that the agent cannot perform, point the human at the exact web UI page
  — never at a terminal or a command to copy.
- **Never handle secrets.** Secrets are entered only by ops in the GitHub
  web UI (environment secrets); they never transit through an agent
  session, a PR, an issue, or a command line.
- **The merge is one human click.** The agent never merges: it prepares
  PRs to be merge-ready (ready for review, checks green, docs updated,
  issue linked) and reports the PR URL; the developer or ops **clicks
  Merge** in the GitHub web UI. The `main` rulesets enforce the hard
  gate (required checks, squash only). GitHub automerge is intentionally
  not used: it merges as soon as checks and the required approval land,
  ignoring the game designer's Discord validation. An earlier `/merge`
  agent-executed convention was abandoned: the agent opens PRs under the
  developer's identity, GitHub forbids author self-approval, and the
  session platform blocks agent-executed merges.
- **Always include GitHub links in user-facing reports.** Every PR,
  issue, workflow run, or branch mentioned in a session report to a
  human carries its full GitHub URL (e.g.
  `https://github.com/merlin-pinpin-org/<repo>/pull/N`): humans never
  open a terminal, so links are their only way to reach the artifacts.
  A report without links is a bug in the session.

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

- **Issue templates are mandatory in all three repos**: blank issues are
  disabled (`.github/ISSUE_TEMPLATE/config.yml`). Create every issue from the
  template matching its kind (`gh issue create --template <name>`) and keep
  its required sections: `## Objective/Context/Specifications/Acceptance
  criteria/Dependencies` in `kingdoms-services` and `kingdoms-infra`,
  `## Summary/Details` in this repo. A "Validate issue" workflow labels
  non-compliant issues `invalid` — recreate them properly rather than
  editing around the flag.

- Every open issue in `kingdoms-services` and `kingdoms-infra` carries exactly
  one `size/*` label (XS/S/M/L/XL, Fibonacci points, set by judgment), one
  `priority/P0-P3` label (critical-path slack, maintained by
  `scripts/sync_dependencies.py`), and a `phase-N` label.
- Every issue has a `## Dependencies` section: task-list checkboxes pointing
  at the issues it blocks on (fully qualified for cross-repo refs, e.g.
  `merlin-pinpin-org/kingdoms-infra#2`). "Depends on" = cannot start before;
  soft relations stay in `## Related`.
- When creating an issue, add its dependencies and `size/*` label, then run
  `scripts/sync_dependencies.py` and fix the `priority/*` labels it reports
  as drifted. See [docs/SKILLS/update-dependencies.md](docs/SKILLS/update-dependencies.md).

## See also

- [ARCHITECTURE.md](docs/ARCHITECTURE.md) — system overview
- [ROADMAP.md](ROADMAP.md) — project progress, synced with issue states
- [docs/DEPENDENCIES.md](docs/DEPENDENCIES.md) — dependency graph, critical
  path, waves, priorities, synced from issue `## Dependencies` sections
