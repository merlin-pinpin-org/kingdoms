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
while either is red. `Check Docs` runs on **every** PR. `kingdoms-services`
and `kingdoms-infra` enforce their full CI matrix the same way (all three
repositories are public with an active `main` ruleset).

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

No custom secret is needed anymore: all three repositories are public, so
the default `GITHUB_TOKEN` reads the issues of `kingdoms-services` and
`kingdoms-infra` directly. The jobs still fail closed when a repository is
unreadable — they never regenerate from partial data.

Former secrets that can be deleted:

- `DEPS_SYNC_PAT` (repository secret of `kingdoms`): obsolete since all
  repositories became public — the default `GITHUB_TOKEN` reads the issues.
- `ROADMAP_DISPATCH_PAT` (in `kingdoms-services` and `kingdoms-infra`, used
  by the now-removed `repository_dispatch` pings).

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

- **Unreadable repository**: the job fails with an actionable error message
  and refuses to write anything — fix the access and re-run by commenting
  the command again.
- **Permission denied on the comment author**: explicit error, nothing runs.
- **Command from a non-collaborator**: fails the `parse` job; no job runs.

## See also

- [update-roadmap.md](update-roadmap.md) — manual fallback for `/roadmap`
- [update-dependencies.md](update-dependencies.md) — manual fallback for `/dependencies`
- [../../AGENTS.md](../../AGENTS.md) — session checklist referencing the commands
