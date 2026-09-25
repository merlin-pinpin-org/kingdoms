# Skill: Automate or learn

Every recurring operation of the platform is a committed artifact — a
Makefile target, a script, or a GitHub Actions workflow. Nothing runs as a
one-off shell command, whether typed by a human (never — see
[docs/CONVENTIONS.md](../CONVENTIONS.md), *Humans never code*) or by an
agent session. This skill decides **where each piece of automation belongs**
and **when a session must persist a command it improvised**.

## Where each automation belongs

| Kind of operation | Artifact | Where |
| ----------------- | -------- | ----- |
| Anything a session runs more than once | Makefile target | `Makefile` of the repo it belongs to (`make lint`, `make session-check`, `make watch-deploy`, `make release`) |
| Reusable implementation, multi-step logic, fail-closed checks | Python or shell script | `scripts/` of the repo it belongs to (`sync_roadmap.py`, `release.sh`, `watch_deploy.sh`) |
| Must run with no session open, or needs permissions the session lacks (releases, deploy pins, scheduled sync), or cannot run in the sandbox | GitHub Actions workflow | `.github/workflows/` of the repo it belongs to |
| How to use the above, plus pitfalls learned | Skill page | `kingdoms/docs/SKILLS/` |

Rules of thumb:

- The Makefile is the **menu**: a new session discovers what exists by
  reading it. A script without its Makefile target (or workflow) is
  half-committed knowledge.
- Scripts are **fail-closed**: explicit error, non-zero exit, no partial
  writes — same standard as the sync scripts (see
  [Generated artifacts sync](../VIBEWORKFLOW.md)).
- Shell scripts pass `bash -n` (and shellcheck when available) before
  pushing; Python scripts run under the repo's checks.
- Anything the sandbox cannot run (compose boots, deploy runs, GitHub
  permissions) is exercised by a CI workflow — never left unverified
  (*Checks must pass everywhere* in [docs/CONVENTIONS.md](../CONVENTIONS.md)).
- A required status check never uses a `paths:` filter (infra developer
  guide, workflow pitfalls).

## Learn it or drop it (the session rule)

Whenever a session types a shell command or writes a helper script for its
own convenience, it must ask: **will this be useful again?**

- **Yes, or plausibly yes → learn it.** Commit it to the repo it belongs
  to: wrap the command in a Makefile target or a script, bake in what the
  session learned (pre-flight checks, pitfalls, failure modes), and
  document it in a skill page if usage is non-obvious. Sessions have no
  conversation memory: **an uncommitted command is knowledge lost**.
- **Genuinely no → keep it ephemeral**, and never present it to a human
  (humans never run commands at all).

Examples of learned commands in this platform: `make restack-<repo>`
(stacked-PR maintenance became a skill + script),
`make session-check` (the end-of-session checklist became a script),
`make release` and `make watch-deploy` (release cutting and deploy
monitoring became scripts with pre-flight checks).

## Procedure

1. Notice you are about to repeat a command, or that a helper script made
   your session easier.
2. Decide the artifact kind with the table above (Makefile target wrapping
   a script; workflow when no session can run it).
3. Commit it to the repo it belongs to, with the pitfalls you hit baked in
   as pre-flight checks or comments in the skill page.
4. Wire it: mention the new target/workflow in the repo's `AGENTS.md` or
   `docs/DEVELOPER.md` if future sessions must discover it, and keep the
   `kingdoms` docs in sync (a code change without its doc update is
   incomplete).
5. Do not ask a human to run it — ever.
