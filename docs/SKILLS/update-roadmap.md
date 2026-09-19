# Skill: Update roadmap

Keep `ROADMAP.md` (repo root) in sync with the actual GitHub issue states
across the three Kingdoms repos.

**Primary mechanism (automatic):** the `Sync roadmap` workflow
(`.github/workflows/sync-roadmap.yml`, kingdoms#27) runs
`scripts/sync_roadmap.py` whenever an issue is opened, reopened or closed —
cross-repo issue events are forwarded from `kingdoms-services` and
`kingdoms-infra` via `repository_dispatch` (`roadmap-ping.yml`, driven by the
`ROADMAP_DISPATCH_PAT` secret). Merged PRs need no dedicated trigger: merging
a PR closes its linked issue, which fires the issue event. When the roadmap
drifts, the workflow updates a single rolling PR (`docs(roadmap): sync with
GitHub issues`) on branch `automation/roadmap-sync`. Nothing to do unless
that PR needs review.

The workflow **fails on purpose** when the GitHub API returns no issue data,
so a broken token can never rewrite the roadmap from incomplete state.

**This skill (manual fallback):** run it when automation is down, when a
status requires human judgment, or on explicit request ("update the roadmap").
The automation cannot infer `in-progress` or `blocked`; those statuses are
set manually and preserved by the script.

## Procedure

1. **Check the rolling sync PR first:**
   `gh pr list --repo merlin-pinpin/kingdoms --head automation/roadmap-sync`
   If it exists and is up to date, review it and ask the developer to merge
   it (the agent environment cannot merge PRs itself). Do not open a new PR
   alongside it.

2. **Collect issue states** for `merlin-pinpin/kingdoms`,
   `merlin-pinpin/kingdoms-services`, and `merlin-pinpin/kingdoms-infra`:

   ```bash
   gh issue list --repo merlin-pinpin/<repo> --state all --limit 200 \
     --json number,title,state,stateReason
   ```

3. **Map each issue** referenced in `ROADMAP.md` to a status:

   | GitHub state | Roadmap status |
   | ------------ | --------------- |
   | open + linked PR | `in-review` |
   | open + assignee actively working | `in-progress` |
   | open + no PR | `todo` |
   | open + blocked dependency | `blocked` |
   | closed as completed | `done` |
   | closed as not planned | `dropped` (move the row to "Out of Scope") |

   Issue references are written as Markdown links:
   `[kingdoms-services#12](https://github.com/merlin-pinpin/kingdoms-services/issues/12)`.
   The sync script migrates plain `repo#N` codes automatically, but new rows
   should be written linked from the start.

   `in-review` detection uses closing keywords in open PR bodies, matching
   the script's `CLOSING_REF_RE`. PRs are linked to their issue with a
   closing keyword in the PR description (`Closes #N` same-repo,
   `Closes owner/repo#N` cross-repo): this populates the GitHub
   "Development" section and closes the issue on merge, which triggers the
   roadmap sync.

4. **Update "Current Phase"**: the lowest phase that still has non-`done`
   issues. Sub-tasks do not affect the phase calculation.

5. **Append a Change Log row** (dated) if and only if any status changed or
   issues were added/removed.

6. **Open a PR** with the title `docs(roadmap): sync with GitHub issues`
   (or update the rolling `automation/roadmap-sync` PR in place if it exists).

## Rules

- The PR must **only touch `ROADMAP.md`**.
- The rolling sync PR is the only roadmap PR: update it in place
  (force-push the branch) instead of opening new PRs. The agent prepares it;
  the developer merges it.
- Never invent statuses: every row must reflect an actual GitHub issue state
  observed in step 2.
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
