# GitHub rulesets — reference and policy

This guide documents **every ruleset of the three Kingdoms repositories**,
the platform's policy on them, and the workflow that keeps them honest.
Rulesets are the enforcement layer of the conventions: what the session
discipline handles softly (draft status, self-review), GitHub enforces
hard (required checks, required reviews, merge methods).

> **Humans never code — and barely click.** Rulesets are one-time
> bootstrapping: an org admin creates them once in the GitHub web UI
> (Settings → Rules → Rulesets), and the agent maintains the
> documentation you are reading. The agent never edits rulesets through
> the API (org permissions live with the maintainers); it documents the
> expected state and flags drift.

## Policy — merge method: rebase, never squash

**Every `main` ruleset allows only the `rebase` merge method** — this is
a parameter of the `pull_request` **rule inside the ruleset** (Require a
pull request before merging → Allowed merge methods: **Rebase and
merge** only). There is no repository-level merge-method setting to
touch: squash, merge commits and the method choices all live in the
ruleset's `pull_request` rule.

Why rebase-only:

1. **Stacked PRs are the norm** (CONVENTIONS.md, *PR lifecycle*): sessions
   grow one PR per repo with clean, sequential, logical commits. A squash
   would collapse that story into one opaque commit and rewrite the SHA,
   breaking every PR stacked on top of it (forcing `--force-with-lease`
   cascades and stale reviews).
2. **Linear history is already a rule**: every `main` ruleset enforces
   `required_linear_history` + `non_fast_forward` + `deletion`. Rebase is
   the only merge method consistent with that shape.
3. **The session commits like it merges** (5-bis): each commit is a
   self-contained logical unit that passes the checks on its own —
   rebasing preserves exactly those units, squash destroys them.
4. **Automerge needs no question asked**: with a single allowed method,
   GitHub's automerge picks rebase mechanically; there is no squash-or-
   rebase decision left to anyone, and the auto-commit never guesses.

Consequence for sessions: never merge locally, never create merge commits,
keep the branch rebased (`make restack-<repo>` for stacks), and expect the
PR to land as its exact commit list, one commit per logical unit.

## Rulesets per repository

The authoritative live state is the GitHub API
(`gh api repos/merlin-pinpin-org/<repo>/rulesets`); this section is the
**documented expectation** the check workflow compares against.

### `kingdoms-services` — `main`

- Target: `~DEFAULT_BRANCH`, enforcement **active**
- Rules:
  - `deletion`, `non_fast_forward`, `required_linear_history`
  - `pull_request`: 1 approving review, **code-owner review required**,
    review threads must be resolved, **allowed merge methods: `rebase`
    only**
  - `required_status_checks`: Lint (ruff), Typecheck (mypy strict), Unit
    tests (pytest), Validate and boot docker-compose.yml, Smoke test
    (bot image + MongoDB + Redis), Discord smoke (real gateway via the
    CI/CD bot), Build and test the image, Generate and check pydoc
    freshness, Check Docs

### `kingdoms-services` — `release-tags` (target: tag)

- Guards tag creation (`vX.Y.Z`) — only the release pipeline may tag;
  see [../PROCESS.md](../PROCESS.md) *Releases*.

### `kingdoms` — `main`

- Target: `~DEFAULT_BRANCH`, enforcement **active**
- Rules: `deletion`, `non_fast_forward`, `required_linear_history`,
  `pull_request` (1 approval, code-owner review, **rebase-only**),
  `required_status_checks` (docs validation)

### `kingdoms-infra` — `main`

- Same shape as `kingdoms` `main` (rebase-only, code-owner review).

### `kingdoms-infra` — `Deploy TEST` / `Deploy PROD` (state branches)

- Targets: `refs/heads/deploy/test`, `refs/heads/deploy/prod`
- Rules: `deletion`, `non_fast_forward`, `required_linear_history`,
  `required_status_checks`; `Deploy PROD` additionally requires a pull
  request and `required_deployments` (the `prod` environment approval) —
  **approving a prod deployment is merging that PR** (ADR-0018).

## Ruleset parameters — exact expected state

For each repository's `main` ruleset, the `pull_request` rule must
declare: required approving reviews **1**, **require review from
code owners**, require conversation resolution, allowed merge methods
**["rebase"]**. Anything else in the tables above (targets, linear
history, checks) is part of the same ruleset. The only remaining
repository-level settings (Settings → General → Pull Requests) are the
**user preferences**: auto-merge enabled and automatic head-branch
deletion — everything else about merging lives in the ruleset.

## Drift detection — the ruleset check workflow

Documentation is the expectation; GitHub is the reality. A scheduled
workflow (kingdoms-services #183, *Ruleset conformance*) compares the
live rulesets of the three repos against this guide's expected state:

- **fail**: a `main` ruleset whose `allowed_merge_methods` is not
  `["rebase"]`, a missing code-owner review requirement, a missing or
  renamed required status check, a ruleset flipped to `evaluate` or
  disabled;
- the failure opens an issue flagged for maintainers with the exact
  drift — humans resolve it in the web UI (the doc drives GitHub, never
  the other way around, same as [CONTRIBUTORS.md](../../CONTRIBUTORS.md)).

## Bootstrapping checklist (one-time, org admin)

1. On each repo: `main` ruleset — linear history + PR rule (1 approval,
   code-owner review, conversation resolution, **rebase only**) +
   required checks (names must match the CI job names exactly).
2. `release-tags` (kingdoms-services) and the deploy state-branch
   rulesets (kingdoms-infra).
3. Repository-level user preferences: **Allow auto-merge** on,
   automatic head-branch deletion on (Settings → General → Pull
   Requests — the only settings outside the rulesets).
4. No bypass actors on any ruleset — the agent included.
