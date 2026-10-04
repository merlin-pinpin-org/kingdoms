---
name: debug-an-env
description: Drive a live environment from a PR thread — /status /start /stop /restart /logs /rollback /dump-db — to validate, debug or recover a stack without SSH. Use whenever an agent session needs to observe or control the running test (or prod) environment during deploy validation, incident triage, or a stuck-stack recovery.
---

# Debug and control a live environment from the PR thread

The `ops-commands` workflow (kingdoms-services) turns a PR comment into
an action on the environment's own runner. Every command follows the
same contract:

1. **One tracking comment** is created on the thread at interception
   (`/cmd <env> — run by @who`) and **updated in place** as the command
   progresses (⏳ checking → 🔵 dispatched, with links). Never expect
   several messages: read the one comment.
2. The **roster authority matrix** gates it (CONTRIBUTORS.md — the
   session's requestor must hold the capability; the agent scope of the
   PR author is checked too, fail-closed).
3. The command dispatches to kingdoms-infra **on the state branch
   `deploy/<env>`** and runs on the environment's runner.

## Command reference (for agents)

| Command | Capability | Use it for |
| --- | --- | --- |
| `/status [env]` | `env-control` | `docker compose ps` dump in the run log: which image runs, since when, healthy or not. Read-only. |
| `/logs [env] [filters]` | `env-logs` | Filtered log dump in the run log + private artifact. Read-only. |
| `/start [env]` / `/stop [env]` | `env-control` | Start/stop the stack in place (containers kept, no pull, no recreate). |
| `/restart [env]` | `env-control` | In-place restart. No pull, no recreate — NOT a redeploy: the same image keeps running. |
| `/rollback [env]` | `rollback` (ops only) | Revert to the previous pinned image; the state push re-triggers the deployment. |
| `/dump-db [env]` | `db-dump` (ops only) | mongodump + Redis snapshot, VPS archive + private artifact. |

`/logs` filters: `--service S` (one compose service), `--since 30m`
(relative), `--from`/`--to` (ISO8601 window), `--tail N` (default 200,
dump capped at 10 MB). `env` defaults to `test`.

## Where to read the result

- `/status`, `/restart`, `/start`, `/stop`: the **run log on
  kingdoms-infra** (link in the tracking comment) — the `docker compose`
  output is in the "Run the control command" step.
- `/logs`: the **run log** (excerpt) + the **private artifact**
  `env-logs-<env>-<run_id>` on the same run.
- The tracking comment links the workflow runs filtered on
  `deploy/<env>`: pick the newest one.

## Agent patterns now possible

- **Validate a deploy**: after a `/deploy` finishes, comment `/status` —
  the compose dump names the exact image tag running and each
  container's health. Then `/logs --service kingdoms-bot --since 15m`:
  `KINGDOMS_BOT_READY` in the log lines is the green flag; a traceback
  names the failing process.
- **Debug a crashed stack**: `/status` first (what runs, what exited),
  then `/logs --since 30m` for all services, then narrow with
  `--service` + `--from`/`--to` once the failing window is known.
- **Recover a stuck stack**: `/restart` (same image). If the image
  itself is bad, tell the ops human — `/rollback` is ops-only.
- **Never**: `/deploy` on top of another PR's validation (CONVENTIONS
  §Test deployment: one image on test at a time); a personal env
  (`envs/<alias>`) frees you from that contention.

## Conventions kept

- Comment as the session's requestor; the gate is fail-closed and the
  verdict lands in the thread.
- Link the run/artifact in any report (CONVENTIONS: reports carry
  GitHub links); quote only the relevant log lines, never the dump.
- `/rollback` and `/dump-db` are ops-only: propose them, do not run
  them unless the human confirms the capability.
