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

**Human GitHub scope (developer-mandated, exhaustive):** on GitHub, humans
accept to do exactly two recurring things — **merge PRs** and **approve
production deployments** — plus the one-time bootstrapping (org teams,
rulesets, environments, secrets, runner install). Anything else (issues,
branches, releases, tags, workflow dispatches the agent cannot perform,
cherry-picks, backports) is the agent's job, executed through automation.
If a session concludes that another manual step is unavoidable, that is a
bug in the automation: fix the automation, not the process.

## Everything is automation — no one-off commands

Nothing in this platform is done by a one-off shell command, by humans *or*
by agent sessions. Every recurring operation exists as a committed,
reusable artifact:

- **Makefile target** — the entry point of anything a session runs more
  than once (`make lint`, `make test`, `make session-check`,
  `make watch-deploy`, `make release`…). Long or multi-step logic lives
  under it, not inline in a session.
- **Committed script** (`scripts/*.py`, `scripts/*.sh`) — the reusable
  implementation, fail-closed, no partial writes; shell scripts pass
  `bash -n` (and shellcheck when available) before pushing.
- **GitHub Actions workflow** — anything that must run even when no
  session is open, or that needs permissions a session lacks (releases,
  deploy pins, scheduled sync); sandbox-limited checks are exercised by
  CI workflows, never left unverified.

**Learn it or drop it (developer-mandated).** Whenever a session types a
shell command or writes a helper script for its own convenience, it must
ask: *will this be useful again?* If yes — even plausibly — **commit it**:
wrap the command in a Makefile target or a script in the repo it belongs
to, with the session's learning (pitfalls, pre-flight checks) baked in.
Sessions have no conversation memory: a command that is not committed is
knowledge lost. If the answer is genuinely no, the command stays ephemeral
and is never presented to a human. See the
[Automate or learn](../.agents/skills/automate-or-learn/SKILL.md) skill
for the procedure.

**Propose to memorize new knowledge (developer-mandated).** When a session
learns to do something new — a procedure, a workaround, a pitfall, a
command it improvised — it must **propose to the human** to persist it for
future sessions, stating the destination: a Makefile target or script in
the repo it belongs to (executable knowledge), a GitHub Actions workflow
(runs without a session or needs permissions the session lacks), a skill
page in `.agents/skills/<name>/SKILL.md` (procedural know-how and
pitfalls), or a rule in `docs/CONVENTIONS.md` / `docs/VIBEWORKFLOW.md`
(binding convention). On approval (or by default at the end of a session,
committed to a PR), the knowledge is committed and wired into the docs so
future sessions discover it. Learning something new and staying silent
about it is a bug in the session.

A session must never ask a human to run anything, and must never leave a
recurring operation existing only in a past session's transcript — both
are bugs in the session.

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
the developer or ops clicks **Merge** in the GitHub web UI — one of the two
recurring human actions (see *Human GitHub scope* above). The `main`
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
   test environment (the `/deploy` PR comment on `kingdoms-services`),
   **verify the deployment yourself** (healthchecks green, stack
   healthy, no crash loop), **then** mark the PR ready and ask the human
   to test and merge — the human's Discord check is the final acceptance,
   not a precondition for ready. If fixes are needed, return the PR to
   draft. Doc-only and infrastructure-only changes skip the live
   deployment (nothing to redeploy) but not the rest of the lifecycle.
3. **Never overwrite another PR's test deployment.** The test environment
   runs one image at a time: before deploying a PR, check the `deploy/test`
   pinned image; if a **different** PR is currently under validation
   there, do not deploy on top of it — wait for its cycle to finish. And
   after merging, only re-align the test environment to `main` if the
   merged PR is the one that was deployed there.
4. **Stack sequential PRs on the same repository.** When several PRs are
   open on one repo, later ones are rebased on their predecessors so the
   developer can merge them in order without conflicts. Run
   `make restack-<repo>` (the [Restack stacked PRs](../.agents/skills/restack-prs/SKILL.md)
   skill) after each merge in a stack and before opening a new PR on a
   repo that already has open ones.
5. **Group related issues into one PR when the scope is coherent.** One
   focused PR per coherent scope beats one PR per sub-issue; the PR body
   lists the covered issues.
6. **Link the PR to its issue** with a closing keyword in the description
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
([Diagnose a stuck deploy](../.agents/skills/diagnose-deploy/SKILL.md) skill). The most
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
