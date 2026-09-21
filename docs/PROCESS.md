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

> **Golden rule for the game designer:** everything goes through the AI
> agent (Mistral vibe-coding). You never run a git or shell command
> yourself: you describe what you want, the agent does it and reports back
> with links. Your only manual actions are **clicking** in GitHub
> (approve/merge when granted) and **testing in Discord**.

## 1. Development (feature request → merged code)

| | Game designer | Developer | Ops |
|--|--|--|--|
| Does | Describes the idea to the agent (Discord or session); validates the proposed design; reads the agent's summary | Reviews the PR, requests changes or approves | Maintains the runner, VPS, secrets (GitHub environment secrets) |

**Flow:**

1. The game designer describes the idea in a vibe-coding session. The agent
   challenges it, then creates a **self-contained GitHub issue** in the
   relevant repo.
2. The agent implements it on a `vibe/<slug>` branch and opens a **draft
   PR**; CI runs on the PR (lint, typecheck, tests, image build).
3. The agent monitors CI and fixes failures until green, then marks the PR
   **ready for review**.
4. **Only the developer can approve and merge** (GitHub rulesets enforce
   required reviews; the game designer never needs merge rights).
5. On merge, the PR closes its issue automatically (`Closes #N`).

The game designer's feedback loop — *I want → the agent builds → I read a
short summary with links → I test in Discord* — never leaves the
vibe-coding session.

## 2. Test deployment (on demand)

Test deployments are **never** tied to a merge: they happen whenever
someone wants to check behavior in the real bot.

| | Game designer | Developer | Ops |
|--|--|--|--|
| Does | Asks the agent (session) to deploy; plays with the bot in Discord | Same, plus the `/deploy-test` PR comment for a specific PR | Guarantees the runner is online, the `test` environment secrets exist |

**Two entry points:**

- **Vibe-coding session** (the normal path for the game designer): "deploy
  this on test" — the agent dispatches the **Deploy test** workflow on
  `kingdoms-infra` with the commit-SHA-tagged image and reports the result.
- **PR comment `/deploy-test`** (any PR on `kingdoms-services`): builds the
  PR image (tag `pr-<n>-sha-<sha>`) and deploys it. The PR gets a ✅/❌
  comment with the run links. Only the PR author or a write-access user
  may use it.

Test-config changes on `main` also retrigger the deployment automatically.

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
   the **released image** `ghcr.io/merlin-pinpin/kingdoms-services:vX.Y.Z`.
   Production will only ever run such released images — a commit-SHA image
   is never promoted to prod by re-tagging; a release is cut instead.

## 4. Production deployment (released code → prod VPS)

Production is the most protected environment. Three gates stack:

1. **Released image only** — the prod manifest **fails closed** unless
   `KINGDOMS_BOT_IMAGE` is set to a released `vX.Y.Z` image.
2. **GitHub environment `prod`** — required reviewers (deployment waits for
   a human approval in the GitHub UI).
3. **Repository ruleset on the Deploy prod workflow** — only identified
   **production deployers** (the developer) may trigger it; everyone else
   is refused by GitHub before anything runs.

| | Game designer | Developer | Ops |
|--|--|--|--|
| Does | Nothing on prod (except validating in Discord once deployed) | Is the production deployer: triggers Deploy prod (on a released tag or manually) and approves the environment protection | Provisions the prod VPS + `env-prod` runner; sets the `prod` environment secrets; creates and maintains the ruleset |

**Current status:** the **Deploy prod** workflow intentionally fails with
a log listing everything to create (the `prod` GitHub environment with its
variables, the ruleset, the `env-prod` runner). It becomes functional once
those exist; nothing else changes.

## The game designer's feedback loop (summary)

```
idea ──▶ vibe session (Mistral agent)
          │ issue → branch → PR → CI green → ready for review
          │
          ▼ "deploy on test"        Developer approves & merges
        test bot in Discord  ◀──── deployment on demand (SHA image)
          │
          ▼ "it works, release it"
        tag vX.Y.Z ──▶ released image ──▶ prod deploy (developer, gated)
```

- One interface: **the vibe-coding session** (plus Discord to test).
- One reviewer: **the developer** (GitHub enforces it).
- One production gate: **released tags + protected workflow + protected
  environment**.
