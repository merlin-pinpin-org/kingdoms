# Skill: Update roadmap

Keep `ROADMAP.md` (repo root) in sync with the actual GitHub issue states
across the three Kingdoms repos.

**Primary mechanism (automatic):** the `/roadmap` PR command (see
[pr-commands.md](pr-commands.md), workflow
`.github/workflows/pr-commands.yml`) runs `scripts/sync_roadmap.py` and
commits the updated `ROADMAP.md` to the PR branch where the command was
commented. Post `/roadmap` as a PR comment (the agent and the developer
both can); the workflow reports the outcome in a PR comment.

**Cross-repo access:** `kingdoms-infra` is a **private** repository, so the
`GITHUB_TOKEN` of `kingdoms` cannot read its issues. `/roadmap` therefore
requires the `DEPS_SYNC_PAT` repository secret: a fine-grained PAT with
**"Issues: read"** on **both** `merlin-pinpin/kingdoms-services` **and**
`merlin-pinpin/kingdoms-infra`. The job fails closed when the secret is
missing or a repository is unreadable — roadmap statuses for
`kingdoms-infra` can never silently go stale.

**This skill (manual fallback):** run it when automation is down, when a
status requires human judgment, or on explicit request ("update the roadmap").
The automation cannot infer `in-progress` or `blocked`; those statuses are
set manually and preserved by the script.

## Procedure

1. **Run `/roadmap` on an open PR** (or post it as the agent): the workflow
   syncs `ROADMAP.md` and commits the result to the PR branch. Review the
   committed diff like any PR change.

2. **Manual fallback only** — collect issue states for `merlin-pinpin/kingdoms`,
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
   "Development" section and closes the issue on merge.

4. **Update "Current Phase"**: the lowest phase that still has non-`done`
   issues. Sub-tasks do not affect the phase calculation.

5. **Append a Change Log row** (dated) if and only if any status changed or
   issues were added/removed.

6. **Open a PR** with the title `docs(roadmap): sync with GitHub issues`
   (or commit to the branch of an existing open PR, e.g. after running
   `/roadmap` on it).

## Rules

- The PR must **only touch `ROADMAP.md`**.
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
- [pr-commands.md](pr-commands.md) — the `/roadmap` PR command automation
- [../../scripts/sync_roadmap.py](../../scripts/sync_roadmap.py) — the
  automation backing this process (run with `--check` to preview drift)
- [../../AGENTS.md](../../AGENTS.md) — the rule that triggers this skill at
  the end of every session
