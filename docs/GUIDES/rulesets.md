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
  - `pull_request`: 0 blanket approving reviews, **code-owner review required**,
    review threads must be resolved, **allowed merge methods: `rebase`
    only**
  - `required_status_checks`: Lint (ruff), Typecheck (mypy strict), Unit
    tests (pytest), Validate and boot docker-compose.yml, Smoke test
    (bot image + MongoDB + Redis), Discord smoke (real gateway via the
    CI/CD bot), Build and test the image, Generate and check pydoc
    freshness, Check Docs

### `kingdoms` — `main`

- Target: `~DEFAULT_BRANCH`, enforcement **active**
- Rules: `deletion`, `non_fast_forward`, `required_linear_history`,
  `pull_request` (0 blanket approvals, code-owner review required, **rebase-only**),
  `required_status_checks` (docs validation)

### `kingdoms-infra` — `main`

- Same shape as `kingdoms` `main` (rebase-only, code-owner review).

### `kingdoms-infra` — `Deploy TEST` / `Deploy PROD` (state branches)

- Targets: `refs/heads/deploy/test`, `refs/heads/deploy/prod`
- Rules: `deletion`, `non_fast_forward`, `required_linear_history`,
  `required_status_checks`; `Deploy PROD` additionally requires a pull
  request and `required_deployments` (the `prod` environment approval) —
  **approving a prod deployment is merging that PR** (ADR-0018).
- Bypass actors: `maintainers`, `ops` teams and the `kingdoms-deployer`
  App (the state-branch writer). The **production gate is the GitHub
  environment** (`environment: prod` in deploy-env.yml — required
  reviewers, secrets, `env-prod` runner), not the workflow and not the
  ruleset.
- **Rollback** (`rollback.yml`): a broken deployment reverts the *pinned
  state* (never the code on main). On `test` the revert pushes directly
  (no PR required by the ruleset); on `prod` it opens a revert PR to
  `deploy/prod`. The push re-triggers the Deploy environment workflow,
  which re-applies the previous known-good image. **Known gap**: the
  re-apply is unconditional — when the re-pinned image is already the
  one running, the deploy still runs (tracked in kingdoms-infra — see
  *Drift detection / known gaps* in the repo issues).

### `kingdoms-services` — `release-tags` (target: tag)

- Guards tag creation (`vX.Y.Z`) — only the release pipeline may tag;
  see [../PROCESS.md](../PROCESS.md) *Releases*.

### Rulesets for many environments — one ruleset per env, provisioned

Rulesets target branches by **explicit ref-name conditions** (e.g.
`refs/heads/deploy/test`): there is no wildcard over branches and no
ruleset template in the GitHub UI. With one state branch per environment
(`deploy/<env>`), each new environment therefore needs **its own
`Deploy <ENV>` ruleset** — at 15 environments, that is 15 rulesets, all
identical except the `ref_name` condition and the env name.

The scalable path is provisioning, not manual copying: a ruleset is a
plain API object (`POST /orgs/{org}/repos/{repo}/rulesets`), so a
committed script can create the `Deploy <ENV>` ruleset for a new env from
a single documented template (same rules as `Deploy TEST`, PR
requirement + `required_deployments` for prod-like envs). Until the
platform grows past `test`/`prod`, the two hand-made rulesets suffice;
when a per-contributor environment fleet lands (see the environment
per-user plan), the provisioning script becomes part of the environment
bootstrap — a maintainer runs it once per env (one-time admin action).

Documented expectations for every future `Deploy <ENV>` ruleset: same
rules as `Deploy TEST`, plus the PR rule and `required_deployments` when
the env is prod-like; bypass actors `maintainers`, `ops`,
`kingdoms-deployer`; the gate always lives in the GitHub environment
(required reviewers), never in the workflow.

## Ruleset parameters — exact expected state

For each repository's `main` ruleset (all three are **exactly
identical**), the `pull_request` rule declares: required approving
reviews **0** (the code-owner requirement is what forces the review —
CODEOWNERS names the owner of every touched path, and GitHub requires
that owner's approval; a blanket count would double-review mod PRs),
**require review from code owners**, require conversation resolution,
allowed merge methods **["rebase"]**. **Bypass actors**: the
`maintainers` team (org-wide maintainer on all three repos) — the trust
anchor for bootstrapping and emergencies; nobody else bypasses, the agent
included. The only remaining repository-level settings (Settings →
General → Pull Requests) are the **user preferences**: auto-merge enabled
and automatic head-branch deletion — everything else about merging lives
in the ruleset.

**CODEOWNERS is the review router** — the ruleset only enforces "the
owner(s) of every touched path approved". The default rule
(`* @merlin-pinpin-org/maintainers`) makes everything non-mod
maintainer-reviewed; each mod's paths are delegated to its designer
(one line per mod, added in the mod's own PR — GitHub CODEOWNERS has no
negative/regex patterns, so per-mod lines are the mechanism; a new mod
means adding its line, which is part of the mod's bootstrap).

## Shared checks — factorized once, referenced thrice

Several checks are logically identical across the three repos but exist
as three copies (CLA Check, Auto-triage, Validate issue): GitHub runs
workflows per repository, so the *contexts* cannot be shared, but the
*code* can: a single reusable implementation (a script in `kingdoms` or
a `workflow_call` workflow) with three thin per-repo wrappers keeps the
behavior identical everywhere while the maintenance happens in one
place. Required-check contexts stay per-repo (they match by exact
workflow/job name) — factorization reduces drift, not check count.

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
