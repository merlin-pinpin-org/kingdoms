# Modes — how every contributor works

> **Source of truth for the three working modes.** Every human or AI
> agent picks a mode from this page before touching a repo. The mode
> decides the branch strategy, the review gate and the GitHub powers
> used. When a session is unsure which mode applies, it asks the human
> — it never silently upgrades its own powers.

The mode is a property of **the person + the task**, declared by the
roster ([CONTRIBUTORS.md](../CONTRIBUTORS.md)): maintainers may use all
three, dev/ops use pro mode by default, vibe coders live in sandbox mode.
Nobody downgrades their gate without an explicit human decision.

## The three modes

| | Sandbox (vibe coder) | Pro (dev/ops) | Cowboy (maintainer only) |
|---|---|---|---|
| Who | Any rostered user, default for `vibe` role | `dev` and `ops` roles | `maintainers` only |
| Branch | `vibe/<alias>/main` — everything stacks there | Feature branch per subject → PR to `main` | `main` directly |
| Review gate | Another user validates the PR to `main` (standard path) | CODEOWNERS review, PR per feature | **Explicit human validation per operation** |
| Environment | Personal env only (their bot, their Discord, their runner) | Personal env → shared validation env (`test`) → `prod` | Any |
| Deploy | Own env; `test` via the standard path | Own env, `test`, `prod` (ops check) | Any, including prod |
| Force push / bypass | Never | Never | Yes, after explicit human OK — and you own the fallout |

## Sandbox mode (vibe coder) — the default for vibe roles

One branch, one PR, one environment, zero friction with the rest of
the org:

- **Branch**: everything lands on `vibe/<alias>/main`. No per-feature
  branches, no PRs between own branches — commits stack directly on
  the integration branch for the whole life of a personal mod. The
  sync workflow keeps `main` merged in; the owner resolves conflicts.
- **Mod PR**: while a personal mod is being built, exactly **one PR
  from `vibe/<alias>/main` to `main`** stays open — the *mod PR*. It
  is opened as a draft as soon as work starts, it runs the required
  checks on every push (that is its purpose: continuous validation of
  the stack), and it is never merged until the mod is complete. Do
  not stack additional PRs on top of it — that adds workflow friction
  for no benefit; push to the integration branch instead.
- **Environment**: the personal environment (bot + Discord server +
  runner labeled `env-<alias>`) deploys from the user branch; anything
  can be tested there, it is a sandbox.
- **Promotion**: when the owner judges the mod complete, they mark the
  mod PR ready — validated by another user (the standard path,
  [CONVENTIONS.md](CONVENTIONS.md) — *Integration branches*). Until
  then, nothing leaves the sandbox.
- **Agents do the work**: the human describes, the agent stacks commits
  on the user branch, pushes so the mod PR's checks re-run, deploys on
  the personal env and reports. The human validates in **their**
  Discord.

## Pro mode (dev/ops) — PR per feature

- **Feature branch per subject** (`vibe/<slug>`): one branch per
  coherent scope, collaborative PRs, normal size, CODEOWNERS review.
- **Personal environment** still exists for work in progress (dev in
  progress, risky experiments) — same mapping `vibe/<alias>/main` ↔
  `env-<alias>`.
- **The ladder**: personal env → shared validation env (`test`) →
  `prod` (ops/owner check). A change is never promoted skipping a rung.
- Long evolutions follow this mode even for maintainers; only
  justified urgent/quick fixes may take the cowboy shortcut.

## Cowboy mode (maintainer only) — explicit, per operation

- Direct push to `main`, ruleset bypass, force push, no PR: everything
  GitHub lets a maintainer do.
- **The human validates explicitly for every single operation of this
  kind** — the agent never assumes cowboy mode, never "inherits" it
  from the previous operation, and states what it is about to do
  before doing it.
- **You own the fallout**: no review caught it, so whatever breaks is
  the author's. Use it for justified speed (broken CI fix, hotfix,
  state-branch surgery), not for convenience.
- Default is pro mode: a maintainer works like dev/ops unless the
  situation justifies cowboy and the human has said yes.

## Environment map (all modes)

| Environment | Branch | Runner label | Discord | Who deploys |
|---|---|---|---|---|
| `env-<alias>` (personal) | `vibe/<alias>/main` | `<alias>` (shared VPS ok) | Personal server, personal bot | The owner (any mode) |
| `test` (shared validation) | `deploy/test` | `test` | Shared validation server | Any user, via `/deploy test` |
| `prod` | `deploy/prod` | `prod` (own VPS) | Production server | Release pipeline + ops approval |

Co-located personal environments on one VPS use **per-env debug host
ports** (`kingdoms-infra` docs/ENVIRONMENTS.md); each environment
remains an isolated sandbox (own compose project, own data volumes).

## Agent rules (binding)

1. The session asks the human which mode applies when in doubt.
2. Sandbox mode never touches `main`, never opens PRs to `main`
   uninvited, never deploys outside the personal env.
3. Pro mode never force-pushes, never bypasses a ruleset.
4. Cowboy mode requires a fresh, explicit human validation **per
   operation**; the session reports each cowboy operation in its
   summary so the audit trail exists.
5. The mode applies to the session's GitHub actions only — the human
   can always do more in the web UI than the session may automate.
