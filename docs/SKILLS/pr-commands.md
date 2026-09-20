# Skill: PR commands

Drive the repo automation from **PR comments**: a collaborator with write
access comments a slash command on a pull request, the `PR commands`
workflow (`.github/workflows/pr-commands.yml`) runs the corresponding
script against the PR branch, commits the generated artifact **to that
PR branch**, and reports the outcome in a PR comment.

This replaces the former event-driven sync workflows (`sync-roadmap.yml`,
`sync-dependencies.yml`, `generate-docs.yml`) and their rolling
`automation/*` PRs: generated artifacts now land in the PR that needs
them — no ghost PR, no accumulated drift. Generated technical docs (pydoc)
live in `kingdoms-services` (PR merlin-pinpin/kingdoms-services#39):
generation and freshness checking moved there.

## Fail-closed validation (all sync/generate scripts)

Every sync/generation script **fails** when its validation fails — none of
them degrades to a partial or best-effort result:

- `/roadmap` (`sync_roadmap.py`): refuses to write `ROADMAP.md` if any of
  the three repositories is unreadable (exit 2) or if any validation
  warning is raised — open issue missing from the roadmap, unknown
  repository reference, issue not found on GitHub, Out-of-Scope drift
  (exit 3). Fix the reported problems and re-run.
- `/dependencies` (`sync_dependencies.py`): fails on missing `size/*` or
  `priority/*` labels, unknown or still-open checked dependencies,
  dependency cycles, and unreadable repositories. It also reports
  `priority/*` label drift (fix with `gh issue edit`, then re-run).
- `/check-docs` (`validate_docs.py`): fails when the `kingdoms-services`
  source or config checkout is absent — partial validation is refused —
  in addition to docstring completeness and mods-documentation checks.
- Generated technical docs are **no longer produced here**: pydoc lives in
  `kingdoms-services` (`scripts/generate_pydoc.py`, `make docs`), where a
  dedicated workflow checks its freshness on every PR of that repo.

## Required checks

The `Check Docs` workflow (`check`) and the `CLA Check` (`cla`) are
**required status checks** on `main` (configured in the repository ruleset —
GitHub admin action, not automatable from the sandbox): a PR cannot merge
while either is red. `Check Docs` runs on **every** PR. In
`kingdoms-services`, the full CI matrix (including the docs freshness
check) is required the same way.
`kingdoms-infra` (private, free plan) has no rulesets: its CI is advisory.
Once `kingdoms-infra` becomes public, its CI can be made required the same
way and the `DEPS_SYNC_PAT` secret becomes unnecessary (see Secrets).

## Commands

| Command | Action | Artifact committed to the PR branch |
| ------- | ------ | ----------------------------------- |
| `/roadmap` | Run `scripts/sync_roadmap.py` | `ROADMAP.md` |
| `/dependencies` | Run `scripts/sync_dependencies.py` | `docs/DEPENDENCIES.md` |
| `/check-docs` | Run `scripts/validate_docs.py --check` (against the current `kingdoms-services` main) | none (report only) |

## Rollout constraint

`issue_comment` workflows only trigger from the workflow file on the
**default branch**. The first `/check-docs` comment posted before this
workflow reached `main` was ignored (expected); after the PR merging
`pr-commands.yml` is merged, the commands work on every PR, including the
one that introduced them (post-merge smoke test).

## Access control

The `parse` job checks the comment author's permission on the repo before
running anything: only `admin`, `maintain` or `write` collaborators can run
PR commands. A PR comment from anyone else fails the run with an explicit
permission error. The permission check uses the `GITHUB_TOKEN`, so it works
for both human collaborators and the agent account.

## Secrets

`/roadmap` and `/dependencies` read the issues of the **private**
`kingdoms-infra` repository, which the `GITHUB_TOKEN` of this repo cannot.
Both jobs fail closed when the `DEPS_SYNC_PAT` repository secret is
missing or a repository is unreadable — they never regenerate from partial
data:

- `DEPS_SYNC_PAT` (repository secret of `kingdoms`): a fine-grained PAT
  with **"Issues: read"** on **both** `merlin-pinpin/kingdoms-services`
  **and** `merlin-pinpin/kingdoms-infra`. Once `kingdoms-infra` becomes
  public, this secret is no longer needed and can be deleted (the default
  `GITHUB_TOKEN` will then read its issues).

The former `ROADMAP_DISPATCH_PAT` secret (in `kingdoms-services` and
`kingdoms-infra`, used by the now-removed `repository_dispatch` pings) is
**no longer needed** and can be deleted.

## When to run which command

- **Every PR touching `docs/` or `scripts/`**: run `/check-docs` before
  requesting review (same check as the `Check Docs` workflow).
- **PRs that change issue states or the dependency graph** (new issue,
  edited `## Dependencies`, size/priority re-decision, merged PR closing
  an issue): run `/roadmap` and `/dependencies` on an open PR — the
  artifacts are committed to its branch, ready for review.
- **PRs that change the `kingdoms-services` source layout or docstrings**:
  pydoc regeneration happens in `kingdoms-services` itself (`make docs`,
  then commit); its `docs` workflow fails on any PR whose committed pydoc
  is stale.

The agent runs these commands itself by posting the comment on the PR
(e.g. `gh pr comment <n> --body "/dependencies"`); the workflow commits
the result and reports back on the PR.

## Commit discipline

- The workflow commits with `github-actions[bot]` identity and conventional
  commit messages (`docs(roadmap): …`, `docs(dependencies): …`).
- Results are committed to the **PR branch** (never `main`, never a
  separate automation branch), so every generated change goes through the
  normal PR review.

## Failure modes

- **Missing `DEPS_SYNC_PAT`**: `/roadmap` and `/dependencies` fail with an
  actionable error message; create the secret (see Secrets) and re-run by
  commenting the command again.
- **Unreadable repository**: same fail-closed behavior as a missing secret.
- **Permission denied on the comment author**: explicit error, nothing runs.
- **Command from a non-collaborator**: fails the `parse` job; no job runs.

## See also

- [update-roadmap.md](update-roadmap.md) — manual fallback for `/roadmap`
- [update-dependencies.md](update-dependencies.md) — manual fallback for `/dependencies`
- [../../AGENTS.md](../../AGENTS.md) — session checklist referencing the commands
