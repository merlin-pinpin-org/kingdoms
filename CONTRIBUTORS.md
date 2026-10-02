# Contributors — roles, teams and responsibilities

> **Source of truth.** This file declares every contributor of the
> organization: their GitHub teams, their platform roles and their
> responsibilities. A GitHub workflow keeps the org in sync with it
> (see the *Sync workflow* section below) — **the doc drives GitHub,
> never the other way around**. It is owned by `@merlin-pinpin-org/maintainers`
> (see CODEOWNERS): no contributor is added or granted a role without a
> maintainer-reviewed change here.

## How to read it

Every contributor entry declares:

- **login** — the GitHub account;
- **name** — the human behind it;
- **cla** — whether the CLA was sent and accepted (`accepted` /
  `pending` / `none`);
- **github-teams** — the org teams the sync workflow ensures on GitHub
  (`maintainers`, `ops`, `devs`, `game-designers`, `vibe-coders`);
- **platform-roles** — what they do on the platform, among:
  - **ops** — infrastructure and deployments: owns the environments,
    secrets, production approvals; reviews infra changes.
  - **dev** — platform developer: owns the core and platform code,
    reviews the core/platform PRs (CODEOWNERS maintainer paths),
    challenges designs; never codes features.
  - **platform** — automated platform machinery (CI/CD, rulesets,
    sync scripts); effectively the maintainers' remit.
  - **mod** — game designer owning one or more mods: writes the game
    rules, drives their mod's PRs with their agent, reviews their
    mod's code (CODEOWNERS names them per mod), validates on the test
    Discord.
  - **vibe** — any human running vibe-coding sessions: their agent does
    the work, they validate and review within their ownership.
- **owns** — concrete ownership: mods (CODEOWNERS paths), infra
  environments, or platform areas;
- **agent-scope** — what a session may do on their behalf (what the
  human delegates vs what stays a human click: production approvals,
  CLA, role changes).

## Process — adding a collaborator (ops/dev/platform/mod/vibe)

1. **The invite** — a maintainer invites the account into the org (web
   UI, one-time bootstrapping action) and into the teams matching
   their contribution.
2. **The CLA** — the contributor signs [CLA.md](CLA.md) and **emails
   it to a maintainer** (no GitHub comment flow); the maintainer files
   the roster PR with `cla: accepted` — the roster entry is the CLA
   record.
3. **This file** — a PR adds the contributor's entry (roles, teams,
   ownership). Maintainers review it — this is the authorization record.
4. **CODEOWNERS** — if the contributor owns a mod, the mod's CODEOWNERS
   lines (kingdoms and kingdoms-services) are added in the same PR, so
   their reviews are required on their mod from day one.
5. **The sync workflow** — once merged, the workflow reconciles GitHub
   with this file: adds missing org memberships/team memberships for
   declared contributors (the roster edit **triggers the team
   additions** — no manual team management), and **flags** (never
   silently removes)
   GitHub members or team memberships absent from the doc — the
   discrepancy lands as a workflow annotation or an issue for the
   maintainers to resolve.
6. **Sessions adapt** — an agent session working with a contributor
   reads this file to know who they are: what they own, what they may
   review, what the session may do for them (a mod owner's session
   drives their mod PRs to ready; an ops human gets deployment
   approval requests; nobody but the declared owners is asked to
   review anything).

## Contributors

Each entry carries an **alias** (the short name sessions and humans use in
conversation and commit/PR references) and a **contact email** (the CLA
address and the session's escalation channel), plus **since** (the date the
contributor joined the roster). Sessions **must materialize these**: address
the human by their alias, use the email for CLA-related exchanges, and check
the roster before assuming who does what.

| Login | Alias | Email | Since | CLA | GitHub teams | Platform roles | Owns | Agent scope |
| ----- | ----- | ----- | ----- | --- | ------------ | -------------- | ---- | ----------- |
| @merlin-pinpin | merlin | merlin@kingdoms.example (to be confirmed by the contributor) | 2024-02-05 | accepted 2026-09 | maintainers, ops, game-designers, vibe-coders | dev, platform, ops, vibe | The whole platform (core, platform, infra); production approvals | Sessions act fully on their behalf except production approvals, CLA and role changes |
| @Drasahaoe | drasah | mabilais.dylan@hotmail.fr | 2025-08-19 | accepted 2026-09 | game-designers, vibe-coders | mod (kingdoms, marriage), vibe | The `kingdoms` and `marriage` mods (CODEOWNERS paths in kingdoms and kingdoms-services); their rules and environments | Sessions build, test, deploy to test and drive to ready; they review their mod's PRs and validate on the test Discord; never asked to merge or run anything |

> **Maintainers**: fill or confirm the email entries via a roster PR — the
> email is the CLA channel and must stay accurate. The `since` date is the
> GitHub account creation date at first entry.

## Sync workflow

`scripts/sync_contributors.py` (kingdoms repo) reads this file and
reconciles the org's teams through the GitHub API, using a
`CONTRIBUTORS_SYNC_TOKEN` org secret (org admin scope):

- **add** — a declared contributor missing from a declared team is
  added;
- **flag** — an org member or team membership with no entry here is
  reported (workflow summary + issue for maintainers), never removed
  automatically: the doc is the truth, but humans resolve the
  discrepancies;
- the workflow runs on every change to this file and weekly
  (scheduled), and fails loudly if the doc and GitHub disagree beyond
  what it could fix.

A new role (a new kind of contributor) is added by extending the
`platform-roles` vocabulary above and the teams in this file — the
workflow picks it up mechanically.
