# Skill: Update roadmap

Keep `ROADMAP.md` (repo root) in sync with the actual GitHub issue states
across the three Kingdoms repos. The roadmap must never go stale: at the end of
every working session, and on request ("update the roadmap"), execute this
procedure exactly as written.

## Procedure

1. **Collect issue states** for `merlin-pinpin/kingdoms`,
   `merlin-pinpin/kingdoms-services`, and `merlin-pinpin/kingdoms-infra`:

   ```bash
   gh issue list --repo merlin-pinpin/<repo> --state all --limit 200 \
     --json number,title,state,stateReason
   ```

2. **Map each issue** referenced in `ROADMAP.md` to a status:

   | GitHub state | Roadmap status |
   | ------------ | --------------- |
   | open + linked PR | `in-review` |
   | open + assignee actively working | `in-progress` |
   | open + no PR | `todo` |
   | open + blocked dependency | `blocked` |
   | closed as completed | `done` |
   | closed as not planned | `dropped` (move the row to "Out of Scope") |

   Cross-repo links are written fully qualified (`kingdoms-services#12`).

3. **Update "Current Phase"**: the lowest phase that still has non-`done`
   issues. Sub-tasks do not affect the phase calculation.

4. **Append a Change Log row** (dated) if and only if any status changed or
   issues were added/removed.

5. **Open a PR** with the title `docs(roadmap): sync with GitHub issues`.

## Rules

- The PR must **only touch `ROADMAP.md`**.
- Never invent statuses: every row must reflect an actual GitHub issue state
  observed in step 1.
- New issues discovered during the sync are added to the matching phase table
  (or "Sub-tasks"); issues missing from GitHub are removed.
- Do not reorder tables; keep tracks grouped by repo.

## Status values

`todo` / `in-progress` / `in-review` / `done` / `blocked` / `dropped`

## See also

- [../../ROADMAP.md](../../ROADMAP.md) — the roadmap this skill maintains
- [../../AGENTS.md](../../AGENTS.md) — the rule that triggers this skill at
  the end of every session
