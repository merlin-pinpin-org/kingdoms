---
name: deploy-and-validate
description: Deploy a pull request to the test environment and validate it yourself (healthchecks, stack healthy, no crash loop) before marking the PR ready. Use for any PR with something to deploy on kingdoms-services (the /deploy flow), and to decide whether the test environment may be re-aligned to main after a merge.
---

# Deploy to test and validate before ready

The developer-mandated PR lifecycle (see *PR lifecycle* in
[docs/CONVENTIONS.md](../../../docs/CONVENTIONS.md)): a PR the agent asks
a human to merge has been **deployed to test and validated by the agent
itself** first. The human's Discord check is the final acceptance, not a
precondition for ready.

## Preconditions (all required before deploying)

- All CI checks green **on the head commit, completed** (never deploy on a
  pending check).
- The branch is up to date with its base (`gh pr view` shows
  `mergeable: MERGEABLE`; restack first if not — see the
  [restack-prs](../restack-prs/SKILL.md) skill).
- Nothing to redeploy (doc-only, workflow-only PRs) → skip the deployment,
  keep the rest of the lifecycle.

## Procedure (kingdoms-services PRs)

1. **Check the test environment is free**: read the pinned image on the
   `deploy/test` state branch —
   `git show origin/deploy/test:envs/test/state/kingdoms-bot.yml`.
   If a **different** PR is pinned there and still under validation, do
   not deploy on top of it: wait for its cycle to finish (never overwrite
   another PR's test deployment).
2. **Deploy**: comment `/deploy` on the PR
   (`gh pr comment <n> --repo merlin-pinpin-org/kingdoms-services --body "/deploy"`).
   Only collaborators with write+ may trigger it; forks are rejected.
3. **Follow the pipeline**: the `Deploy PR (comment)` workflow builds the
   image (`pr-<id>-<timestamp>-<sha>`), pushes it to GHCR, then dispatches
   the `Pin state` workflow on kingdoms-infra which pins it on
   `deploy/test`; the pin push triggers `Deploy environment`, which runs on
   the env's self-hosted runner.
4. **Validate the deployment yourself** — all of:
   - `Deploy PR (comment)` run: conclusion `success`;
   - `Pin state` + `Deploy environment` runs: `success`;
   - Deploy environment logs end with `deployment to 'test' applied and
     healthy` — kingdoms-bot, kingdoms-mongo and kingdoms-redis all
     report healthy (the bot healthcheck probes `/healthz`);
   - the pinned image on `deploy/test` matches the PR head sha.
   A crash loop, an exited container or a failed healthcheck → the PR
   stays in draft, diagnose (see the
   [diagnose-deploy](../diagnose-deploy/SKILL.md) skill), fix, redeploy.
5. **Mark ready and hand over**: `gh pr ready <n>`, then report the PR URL
   and the deployed image and ask the human to test in Discord and merge.

## After a merge: re-align test to main?

Only if the merged PR is the one deployed on test. Merging to `main` never
re-pins test automatically (test is pinned by `/deploy` comments and by
tag releases); re-aligning is a deliberate action, done by deploying the
`main` state or the next release — never on top of another PR's
validation run.

## Infra PRs (kingdoms-infra)

Infra PRs have no `/deploy`: their CI **boots the real stack** from the
branch (compose validation, smoke test, backup/restore round-trip). The
agent validates the CI evidence the same way (all green on head) before
marking ready; the infra changes reach the test environment at the next
re-pin after merge.
