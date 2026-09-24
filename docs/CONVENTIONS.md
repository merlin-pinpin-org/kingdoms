# Kingdoms conventions

Shared conventions for the three Kingdoms repositories (`kingdoms`,
`kingdoms-services`, `kingdoms-infra`). These rules apply everywhere; each
repo keeps only its local specifics in its own `AGENTS.md` and
`docs/DEVELOPER.md`.

The operating model (roles, session loop, approvals, deployment flow) is
described in [VIBEWORKFLOW.md](VIBEWORKFLOW.md) — read it first.

## Working language

All code, comments, documentation, commit messages, PR titles and PR
descriptions are written in **English**.

## Humans never code

This platform is a pure vibe-coding test: the agent does 100% of the
technical work. Never propose a solution that requires a human to run a CLI
command, a script, or any local tooling — the only manual technical actions
are **clicks in the GitHub web UI** (approving PRs, production deployment
approvals, one-time admin: teams, rulesets, environments, secrets, VPS
runner install following the infra VPS-SETUP guide), performed by authorized
humans. When a GitHub admin action is needed that the agent cannot perform,
point the human at the exact web UI page — never at a terminal or a command
to copy.

## Never handle secrets

Never commit secrets (tokens, passwords, API keys, private keys, `.env`
values) and never let them transit through an agent session, a PR, an
issue, or a command line. Real credentials live only in GitHub
**environment secrets**, entered by ops in the web UI and injected by the
CD runner at deploy time; repositories carry `.env.example` placeholders
only. Before making any repository public, scan the full git history for
leaked secrets (`git log -p | grep -E "ghp_|github_pat_|AKIA|PRIVATE KEY"`).

## The merge is one human click

The agent never merges: it prepares PRs to be merge-ready (ready for
review, checks green, docs updated, issue linked) and reports the PR URL;
the developer or ops clicks **Merge** in the GitHub web UI. The `main`
rulesets of each repository enforce the hard gate (required checks,
required review, squash only). GitHub automerge is intentionally not used:
it merges as soon as checks land, ignoring the game designer's Discord
validation.

## PR lifecycle (merge-readiness)

1. **Draft status is the merge-readiness signal.** Always open PRs as
   drafts; mark a PR ready for review only when, from your point of view,
   it can be merged (checks green, implementation complete, self-review
   done, docs updated); keep or return it to draft (`gh pr ready --undo`)
   while work remains. Never leave a PR in draft when asking for a merge.
   **Checks are verified on the head commit, completed** — never ask for a
   merge while a check is pending or only the previous commit is green
   (the 2026-09-24 SC2046 incident: the merge landed between the push of
   a doc commit and its lint conclusion). Admins can merge with pending
   checks, so the discipline is the agent's, not GitHub's.
2. **A user-facing change is validated live first.** Deploy the PR to the
   test environment (the `/deploy` PR comment on `kingdoms-services`) and
   let the human check the behavior in Discord — only then mark the PR
   ready and ask for the merge; if fixes are needed, return the PR to
   draft. Doc-only and infrastructure-only changes skip this step.
3. **Stack sequential PRs on the same repository.** When several PRs are
   open on one repo, later ones are rebased on their predecessors so the
   developer can merge them in order without conflicts. Run
   `make restack-<repo>` (the [Restack stacked PRs](SKILLS/restack-prs.md)
   skill) after each merge in a stack and before opening a new PR on a
   repo that already has open ones.
4. **Group related issues into one PR when the scope is coherent.** One
   focused PR per coherent scope beats one PR per sub-issue; the PR body
   lists the covered issues.
5. **Link the PR to its issue** with a closing keyword in the description
   (`Closes <owner>/<repo>#N`): this populates the GitHub "Development"
   section and closes the issue on merge. Omit it when no tracked issue
   exists — never invent an identifier.

## Always include GitHub links in reports

Every PR, issue, workflow run, or branch mentioned in a session report to a
human carries its full GitHub URL (e.g.
`https://github.com/merlin-pinpin-org/<repo>/pull/N`): humans never open a
terminal, so links are their only way to reach the artifacts. A report
without links is a bug in the session.

## Documentation is part of the change

`kingdoms` is the source of truth: a change in `kingdoms-services` or
`kingdoms-infra` without its doc update there is incomplete. Reference
issues with full repo-qualified identifiers (e.g. `kingdoms-services#12`)
since cross-repo references are common.

## Issues

- **Issue templates are mandatory** in all three repos: blank issues are
  disabled. Create every issue from the template matching its kind
  (`gh issue create --template <name>`) and keep its required sections
  (`## Objective`, `## Context`, `## Specifications`,
  `## Acceptance criteria`, `## Dependencies` in `kingdoms-services` and
  `kingdoms-infra`; `## Summary`, `## Details` in `kingdoms`). A
  "Validate issue" workflow labels non-compliant issues `invalid` —
  recreate them properly rather than editing around the flag.
- Every open issue in `kingdoms-services` and `kingdoms-infra` carries
  exactly one `size/*` label (XS/S/M/L/XL), one `priority/P0-P3` label
  (critical-path slack, maintained by
  `kingdoms/scripts/sync_dependencies.py` — do not set by hand unless the
  analysis is wrong) and a `phase-N` label.
- Every issue has a `## Dependencies` section: task-list checkboxes
  pointing at the issues it blocks on (fully qualified for cross-repo
  refs). "Depends on" = cannot start before; soft relations stay in
  `## Related`.
- Keep the issues you touched in sync with reality (state, acceptance
  criteria, `## Dependencies` checkboxes).

## Checks must pass everywhere

Run the repo's checks before pushing (see each repo's
`docs/DEVELOPER.md`): they require public clones only, no credentials —
keep it that way. **A required status check never uses a `paths:` filter**:
it must report on every PR, or GitHub blocks the merge of the PRs it
silently skipped. **Sandbox limits are covered by GitHub Actions**:
anything that cannot run in the dev sandbox must be exercised by a CI
workflow instead — when a check cannot run locally, add or extend the
workflow that validates it; never leave it unverified.

## Diagnose before blaming the infrastructure

When a deployment is stuck, run the diagnosis tooling before reporting a
cause: `make doctor` / `make diagnose-deploy-<env>` in `kingdoms-infra`
([Diagnose a stuck deploy](SKILLS/diagnose-deploy.md) skill). The most
common trap: a run left `waiting` for an environment approval holds the
`deploy-<env>` concurrency group forever, and every newer run stays
`pending` silently — no notification, and the runner is never even asked.
Never report "the runner is the problem" without the diagnose output; a
stuck-deploy report to a human carries the diagnose output and the links
of every stale run to cancel.

## Automate or learn, never one-off

Every recurring operation met during a session becomes a committed script,
Makefile target or workflow in the repo it belongs to ("learn it or drop
it") — never a one-off command that lives only in the session transcript.
Human contributors without an agent and future agent sessions must be able
to replay every operation from the repository alone; document it for both
(the script header for humans, a SKILLS entry when it is a session recipe).
