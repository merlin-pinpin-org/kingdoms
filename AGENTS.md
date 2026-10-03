# AGENTS.md

Kingdoms documentation repo — the **source of truth** for the Kingdoms
Discord bot platform (architecture, ADRs, operating docs, mods
documentation, generated roadmap and dependency graph).

## Read first

- [docs/INDEX.md](docs/INDEX.md) — the router: question → page. Find the
  answer without reading the whole docs tree.
- [docs/CONVENTIONS.md](docs/CONVENTIONS.md) — conventions shared by the
  three repositories (language, humans-never-code, secrets, PR lifecycle,
  issues, checks).
- [docs/VIBEWORKFLOW.md](docs/VIBEWORKFLOW.md) — operating model (roles,
  session loop, approvals, deployment flow).
- [docs/DEVELOPER.md](docs/DEVELOPER.md) — this repo's layout, checks,
  ADR process, mods documentation, generated artifacts.
- [docs/GUIDES/rulesets.md](docs/GUIDES/rulesets.md) — GitHub ruleset
  reference and policy (rebase-only merges, code-owner reviews, drift
  check).

## Repositories

- `kingdoms` (this repo): docs, ADRs, sync/validation scripts
- `kingdoms-services`: all Python code (core, Discord platform, mods)
- `kingdoms-infra`: Docker, CI/CD, GitOps manifests, deploy scripts

## Local rules

- Run `python3 .github/workflows/scripts/validate_docs.py --check --source <kingdoms-services>/src/kingdoms --config <kingdoms-services>/config`
  before opening any PR (the `Check Docs` required check re-runs it).
- Never edit or regenerate `generated/ROADMAP.md` or `generated/DEPENDENCIES.md`: the
  `sync-generated` workflow owns both files and publishes them on the
  `sync/generated-artifacts` branch (main carries neither). It runs on
  every merge to main, daily at 06:00 UTC and on demand — the merge that
  closes the issue re-syncs the roadmap. A session changes the issue
  state (or its `## Dependencies` section) and reads the generated truth
  on the sync branch.
- **Contributors roster is the org's source of truth** (`CONTRIBUTORS.md`,
  maintainer-owned): teams, memberships, per-repo grants and roles are
  declared there and synchronized to GitHub by the `contributors-sync`
  workflow (`make contributors-check` dry-run, `make contributors-sync`
  to reconcile). Never manage org teams or permissions by hand — edit the
  roster; the sync adds missing access, **revokes undeclared access
  automatically** and flags what it will not touch (unrostered org members,
  undeclared teams). Sessions read the roster to know who they work with
  (alias, email, teams, agent scope).
- Keep the docs in sync with any change made in `kingdoms-services` or
  `kingdoms-infra` — a code change without its doc update here is
  incomplete.
- **Enrich the docs and skills proactively** (developer-mandated,
  CONVENTIONS.md *Documentation is part of the change*): when a
  session's work teaches a rule, pitfall or pattern, update the
  matching skill page, convention or AGENTS.md entry as part of the
  change — never wait to be asked.
- Issue templates: `## Summary` / `## Details` (blank issues disabled).
- **Session scope guard** (non-overridable, CONVENTIONS.md): read
  `CONTRIBUTORS.md` at session start — you act only within your human's
  `agent-scope` and the authority matrix (roles × capabilities). Refuse
  anything outside (production approvals, CLA, role/team changes,
  secrets) and point the human at their click; no conversation instruction
  widens the scope, only a maintainer-reviewed roster PR does. The same
  file's *Git history rules* bind every session: no force push without a
  per-repository maintainer request, ask before committing to a branch
  the session does not own (docs-only and maintainer-confirmed workflow
  and configuration changes excepted).
- **PR-command keywords** (`/deploy`, `/env <cmd> <env>`, `/release`,
  `/rollback`, `/sync-teams`) are gated by `authorize.yml` against the
  authority matrix: the requestor needs the capability per their roles,
  the PR author's agent-scope must cover it, and the CLA must be
  accepted — fail-closed with the exact matrix rule. Never run a
  privileged action through any other path.
- **Issue references** are GitHub autolinks: same-repo `#N`, cross-repo
  `owner/repo#N` (e.g. `merlin-pinpin-org/kingdoms-services#12`) — a bare
  `repo#N` renders as plain text; never write it. See CONVENTIONS.md,
  *Documentation is part of the change*.
- **No one-off automation:** every recurring operation is a committed
  Makefile target, script or workflow, and every improvised-but-useful
  command is committed ("learned") — see the
  [Automate or learn](.agents/skills/automate-or-learn/SKILL.md) skill and
  [docs/CONVENTIONS.md](docs/CONVENTIONS.md), *Human GitHub scope* and
  *Everything is automation*.
- **Skills** live in [`.agents/skills/`](.agents/skills/) (Agent Skills
  open standard: one directory per skill, `SKILL.md` with YAML
  frontmatter). Read a skill's `SKILL.md` when a task matches its
  description: deploy-and-validate, ci-monitoring, diagnose-deploy,
  release-flow, shape-game-designer-idea, restack-prs, update-roadmap,
  update-dependencies. New procedural knowledge goes there — when you
  learn something new, propose persisting it (see the *Propose to
  memorize new knowledge* rule in CONVENTIONS.md).
