---
name: release-flow
description: Cut a release of the Kingdoms bot (tag vX.Y.Z, GitHub release, deploy to prod) when the game designer has validated the features in Discord and asks for it. Use when the human says to tag, release, or ship to production.
---

# Release flow

Releasing is a human-requested, agent-executed pipeline: the agent runs
`make release` on kingdoms-services, which tags `vX.Y.Z`, and the Docker
workflow publishes the image, creates the GitHub release and pins it on
`deploy/prod` (prod-like environments deploy released images only — never
a PR image).

## Preconditions

- The game designer has **validated the features in Discord** (every
  feature is validated before a release is tagged — CONVENTIONS).
- All checks are green on `main`; the roadmap is synced.
- The release notes are drafted (the workflow creates the GitHub release
  page from them).

## Procedure

1. **Draft the release notes** (`scripts/release_notes.sh` on
   kingdoms-services assembles the change log since the last tag).
2. **Tag and push** from the kingdoms-services clone:
   ```bash
   make release VERSION=vX.Y.Z
   ```
   The Makefile target runs the pre-flight checks (clean tree, on main,
   up to date, notes present) before anything is pushed.
3. **The workflows do the rest**: build and push
   `ghcr.io/merlin-pinpin-org/kingdoms-services:vX.Y.Z` (plus `sha-<sha>`
   and `main` tags), create the GitHub release, pin the released image on
   `deploy/prod` (the pin push triggers the prod deploy on the prod
   runner, gated by the prod environment's required reviewers).
4. **Watch the prod deploy** with `make watch-deploy` (kingdoms-services)
   — or the kingdoms-infra `make doctor` if anything stays pending (see
   the [diagnose-deploy](../diagnose-deploy/SKILL.md) skill). Prod
   deploys need the required reviewers' approval: link the run to the
   human, who clicks *Approve and deploy*.
5. **Post-release**: the game designer validates the release in Discord;
   `/status` shows the release link. Keep the roadmap and dependency
   artifacts in sync (the closed issues change the graph).

## Rules

- The agent never tags on its own initiative — a release is explicitly
  requested by the human.
- Versioning: semver-ish `vX.Y.Z`; breaking rule changes bump the major,
  new features the minor, fixes the patch.
- Never release with a red check or an unsynced roadmap; the Makefile
  pre-flight fails closed.
