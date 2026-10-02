# Guide — Vibe coder (AI agent session)

You are an AI session with **no memory of previous conversations**.
This page is your boot checklist; the repo is the source of truth.

## Boot sequence (every session)

1. Read [CONVENTIONS.md](../CONVENTIONS.md) (language, checks, PR
   lifecycle) — non-negotiable.
2. Read [VIBEWORKFLOW.md](../VIBEWORKFLOW.md) (roles, approvals) and
   the target repo's `AGENTS.md` + `docs/DEVELOPER.md`.
3. `git status`, current branch, recent commits — never assume a clean
   state.
4. Find the work: the issue at hand (milestone
   [v0.4.0](https://github.com/merlin-pinpin-org/kingdoms-services/milestone/3)),
   its dependencies, and the ROADMAP for context.

## Working rules (from the decisions taken with the developer)

- **One open PR per session per repo** — chain PRs sequentially; never
  stack.
- Scope each PR like a review lot: one coherent unit a human can review
  in one sitting. Big issues are split into sub-PRs (e.g. ladder core
  [#134](https://github.com/merlin-pinpin-org/kingdoms-services/issues/134):
  data model → matchmaking → state machine/rating → invites).
- **Tests land with every PR** — the blanket mandate
  ([#139](https://github.com/merlin-pinpin-org/kingdoms-services/issues/139))
  covers every v0.4.0 issue: acceptance properties in CI, coverage not
  lowered on touched paths.
- **Docs are part of the PR**: `make docs` freshness, mod docs in the
  kingdoms repo updated in the same PR when rules change.
- Before pushing: `make lint`, `make typecheck`, `make test` — all
  green, always. CI failures you caused get fixed before anything new.
- Never click Merge yourself. Ready = checks green + deployed to test +
  verified + nothing left for you to do; going ready enables automerge.
  CODEOWNERS name the owners (a mod's designer reviews their mod; the
  maintainers review the core/platform) — GitHub merges the ready PR
  once their approvals land. Never force-push without approval. Never
  touch protected branches.
- Architecture: ADRs are binding
  ([ADR-0020](../DECISIONS/020-process-split-bot-core-providers.md)
  process split; if you disagree, raise it, don't workaround it).
- gRPC contracts: edit `.proto` in `contracts/`, regenerate with
  `make contracts`, never hand-edit stubs.
- If a step needs a human (secrets, production approval, review), stop
  and ask — see [VIBEWORKFLOW](../VIBEWORKFLOW.md) for who does what.

## Session flow

```
read docs → issue → branch vibe/<issue-slug> → implement + tests
→ lint/typecheck/test/docs → push → draft PR → report + CI watch
```

Report the PR URL, what was verified, and what remains. If the
developer says "continue", keep working the open PR or open the next
one in the same session rules.

## Audience-specific pointers

- Building a mod → [mod-developer.md](mod-developer.md)
- Building a game/provider → [game-provider.md](game-provider.md)
