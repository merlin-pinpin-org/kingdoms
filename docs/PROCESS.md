# Process guide: development, test deployment, release, production

This page describes the four processes end to end, from the point of view of
each role: **game designer**, **developer**, and **ops**. It is the
human-readable companion of [ADR-0007](DECISIONS/007-gitops-deployment.md)
and [VIBEWORKFLOW.md](VIBEWORKFLOW.md) — the operating model itself lives
there; this page focuses on *what each person does*.

Two environments exist ([ADR-0007](DECISIONS/007-gitops-deployment.md)):

- **test** — deployed **on demand**, used to validate behavior in Discord;
- **prod** — deployed only from **released versions** (`vX.Y.Z`), the real
  players' environment.

> **Golden rule for every human (game designer, developer, ops):** the
> platform is a pure vibe-coding test — **nobody ever checks out a
> repository, writes code, or runs a command**. Everything technical is
> done by the AI agent (or by CI). The only manual technical actions are
> **clicks in the GitHub web UI**: approving PRs, approving production
> deployments, and the one-time administration (org teams, rulesets,
> environments, secrets). If an agent session proposes a command to copy
> into a terminal, push back — that is a bug in the session.

## Manual actions inventory (complete)

Everything a human may have to click in the GitHub web UI — and nothing
else:

| Action | Who | Frequency |
|--------|-----|-----------|
| Create org teams (`maintainers`, `ops`, `game-designers`) and attach them to the repos | Org owner | once |
| Activate code-owner review + 1 approval in each repo's `main` ruleset; no bypass actors | Org owner | once |
| Set `prod` environment required reviewers (ops) and enter environment secrets | Ops | once, then on rotation |
| Merge a ready PR (review it, then click Merge) | Developer or ops | per PR |
| Approve a production deployment (`prod` environment) | Ops | per prod deploy |

Everything else — issues, branches, code, PRs, CI fixes, `/deploy-test`,
tags, releases, roadmap sync — is executed by the agent.

## 1. Development (feature request → merged code)

| | Game designer | Developer | Ops |
|--|--|--|--|
| Does | Describes the idea to the agent (Discord or session); validates the proposed design; reads the agent's summary; tests in Discord | Challenges the design; reviews the ready PR and **clicks Merge**; never codes | Same as developer, plus reviews infra changes |

**Flow:**

1. The game designer describes the idea in a vibe-coding session. The agent
   challenges it, then creates a **self-contained GitHub issue** in the
   relevant repo.
2. The agent implements it on a `vibe/<slug>` branch and opens a **draft
   PR**; CI runs on the PR (lint, typecheck, tests, image build).
3. The agent monitors CI and fixes failures until green, then marks the PR
   **ready for review**.
4. **Only the developer or ops can merge** (GitHub rulesets + CODEOWNERS
   enforce it; the game designer never needs merge rights). The agent
   prepares the PR to merge-ready and never merges; the human reviews and
   clicks **Merge** (squash) — one click.
5. On merge, the PR closes its issue automatically (`Closes #N`).

The game designer's feedback loop — *I want → the agent builds → I read a
short summary with links → I test in Discord* — never leaves the
vibe-coding session.

## 2. Test deployment (on demand)

Test deployments are **never** tied to a merge: they happen whenever
someone wants to check behavior in the real bot.

| | Game designer | Developer | Ops |
|--|--|--|--|
| Does | Asks the agent (session) to deploy; plays with the bot in Discord | Same, plus the `/deploy-test` PR comment for a specific PR | Guarantees the runner is online, the `test` environment secrets exist; creates the kingdoms-deployer GitHub App and its ruleset once (see kingdoms-infra docs/DEPLOY-TEST-APP.md) |

**Two entry points:**

- **Vibe-coding session** (the normal path for the game designer): "deploy
  this on test" — the agent posts the **`/deploy-test` comment** on the
  feature PR (the comment is the trigger; the agent does not need workflow
  permissions), the workflow builds the PR image and dispatches the
  kingdoms-infra Deploy test workflow through the **kingdoms-deployer
  GitHub App** (ephemeral token, Actions: write only), and the agent
  **monitors the run** and reports the result with the logs analyzed on
  failure. No human click is needed.
- **PR comment `/deploy-test`** (any PR on `kingdoms-services`): same
  mechanism, usable by anyone authorized — the PR image (tag
  `pr-<n>-sha-<sha>`) is built and deployed automatically, and the PR gets a
  ✅/❌ comment with the run links. Only repository collaborators with
  `admin`, `maintain` or `write` permission may use it; fork PRs are
  rejected (kingdoms-services#67).

  Note: the agent sandbox cannot dispatch workflows directly — deploying
  **`main` with no open PR** is the one case that needs a human click on
  **Run workflow** (the agent gives the exact link and the image tag to
  use).

Test-config changes on `main` also retrigger the deployment automatically,
with no human action at all.

Every deployment runs the same safety chain: **mandatory pre-deploy
backup → compose up → health gate → automatic rollback on failure**.

## 3. Release (merged code → `vX.Y.Z`)

| | Game designer | Developer | Ops |
|--|--|--|--|
| Does | Asks the agent to tag a release; reads the release notes in GitHub | Approves that a version may be released | Nothing (the release is a git tag + the Docker workflow publishes the `vX.Y.Z` image) |

**Flow:**

1. The game designer says "release this" in a session; the agent prepares
   the version (changelog summary, tag `vX.Y.Z`, GitHub release).
2. Tag and release permissions are **enforced by GitHub** (rulesets); the
   agent executes, it is not granted by convention.
3. Pushing the tag makes the `kingdoms-services` Docker workflow publish
   the **released image** `ghcr.io/merlin-pinpin-org/kingdoms-services:vX.Y.Z`.
   Production will only ever run such released images — a commit-SHA image
   is never promoted to prod by re-tagging; a release is cut instead.

## 4. Production deployment (released code → prod VPS)

Production is the most protected environment. Three gates stack:

1. **Released image only** — the prod manifest **fails closed** unless
   `KINGDOMS_BOT_IMAGE` is set to a released `vX.Y.Z` image.
2. **GitHub environment `prod`** — required reviewers (deployment waits for
   a human approval in the GitHub UI).
3. **Actions policy on the Deploy prod workflow** — only **ops** team actors
   may trigger it; everyone else is refused by GitHub before anything runs.
   The workflow pauses on the `prod` environment protection until an ops
   member approves the deployment in the UI.

| | Game designer | Developer | Ops |
|--|--|--|--|
| Does | Nothing on prod (except validating in Discord once deployed) | Nothing on prod (cannot deploy) | Is the production deployer: ops triggers or lets the released tag trigger Deploy prod, and **clicks Approve** on the `prod` environment protection; provisions the prod VPS + `env-prod` runner; sets the `prod` environment secrets in the UI |

**Current status:** the **Deploy prod** workflow intentionally fails with
a log listing everything to create (the `prod` GitHub environment with its
variables, the ruleset, the `env-prod` runner). It becomes functional once
those exist; nothing else changes.

## The game designer's feedback loop (summary)

```
idea ──▶ vibe session (Mistral agent)
          │ issue → branch → PR → CI green → ready for review
          │
          ▼ "deploy on test"
        agent comments /deploy-test on the PR → automatic build + deploy
          │
          ▼ agent monitors → result;      Developer/ops clicks Merge
        test bot in Discord  ◀──── deployment on demand (SHA image)
          │
          ▼ "it works, release it"
        tag vX.Y.Z ──▶ released image ──▶ prod deploy (ops, gated)
```

- One interface: **the vibe-coding session** (plus Discord to test).
- One human click per PR: **Merge** (developer or ops — GitHub rulesets
  enforce required checks and squash-only merges; the agent never merges).
- One production gate: **released tags + ops-only workflow policy + ops
  environment approval**.
