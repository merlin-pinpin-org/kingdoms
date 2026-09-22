# Skill: Update roadmap

Keep `ROADMAP.md` (repo root) in sync with the actual GitHub issue states
across the three Kingdoms repos.

**Mechanism:** run `scripts/sync_roadmap.py` locally, then commit the updated
`ROADMAP.md` to the PR branch (or open a dedicated PR). The script reads all
three repositories through `gh api`; since they are public, no custom secret
is required. It fails closed when a repository is unreadable — roadmap
statuses for `kingdoms-infra` can never silently go stale.

Statuses that require human judgment (`in-progress`, `blocked`) cannot be
inferred from GitHub state; set them manually — the script preserves them.

## Procedure

1. **Collect issue states** — the script does this itself via `gh api`:
   ```bash
   gh issue list --repo merlin-pinpin-org/<repo> --state all --limit 200 \
     --json number,title,state,stateReason
   ```

2. **Run the sync script** from the repo root:
   ```bash
   python3 scripts/sync_roadmap.py
   ```
   It maps each issue referenced in `ROADMAP.md` to a status:

   | GitHub state | Roadmap status |
   | ------------ | --------------- |
   | open + linked PR | `in-review` |
   | open + assignee actively working | `in-progress` |
   | open + no PR | `todo` |
   | open + blocked dependency | `blocked` |
   | closed as completed | `done` |
   | closed as not planned | `dropped` (move the row to "Out of Scope") |

   Issue references are written as Markdown links:
   `[kingdoms-services#12](https://github.com/merlin-pinpin-org/kingdoms-services/issues/12)`.
   The sync script migrates plain `repo#N` codes automatically, but new rows
   should be written linked from the start.

   `in-review` detection uses closing keywords in open PR bodies, matching
   the script's `CLOSING_REF_RE`. PRs are linked to their issue with a
   closing keyword in the PR description (`Closes #N` same-repo,
   `Closes owner/repo#N` cross-repo): this populates the GitHub
   "Development" section and closes the issue on merge.

3. **Fix what the script reports** — it fails (or warns) on: unreadable
   repository (exit 2), open issue missing from the roadmap, unknown
   repository reference, issue not found on GitHub, Out-of-Scope drift
   (exit 3). Re-run until clean.

4. **Verify "Current Phase"**: the lowest phase that still has non-`done`
   issues. Sub-tasks do not affect the phase calculation. The script updates
   it automatically — check it matches intent.

5. **Check the Change Log**: the script appends a dated row whenever a status
   changed or issues were added/removed.

6. **Commit and open a PR** with the title `docs(roadmap): sync with GitHub
   issues` — or commit to the branch of an existing open PR that needs
   the synced roadmap. Review the diff like any PR change.

## Rules

- A roadmap-only change must **only touch `ROADMAP.md`**.
- Never invent statuses: every row must reflect an actual GitHub issue state.
- New issues discovered during the sync are added to the matching phase table
  (or "Sub-tasks") as linked rows; issues missing from GitHub are removed.
- Do not reorder tables; keep tracks grouped by repo.
- The script prints a warning for open issues missing from the roadmap —
  add them to the matching table.

## Status values

`todo` / `in-progress` / `in-review` / `done` / `blocked` / `dropped`

## See also

- [../../ROADMAP.md](../../ROADMAP.md) — the roadmap this skill maintains
- [../../scripts/sync_roadmap.py](../../scripts/sync_roadmap.py) — the
  automation backing this process (run with `--check` to preview drift)
- [../../AGENTS.md](../../AGENTS.md) — the rule that triggers this skill at
  the end of every session
