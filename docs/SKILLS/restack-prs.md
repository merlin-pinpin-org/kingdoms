# Skill: Restack stacked PRs

Keep the open PRs of one repository stacked on each other (the stacking
convention of [docs/CONVENTIONS.md](../CONVENTIONS.md)): sequential PRs on
the same repo are rebased on their predecessors so the developer can merge
them in order without conflicts.

**Mechanism:** `scripts/restack.sh` lists the open PRs of the repo (oldest
first), rebases each head branch on the head of the PR below it (or the PR
base for the oldest), and force-pushes each rewritten branch with
`--force-with-lease`. It never merges and never deletes branches.

## Procedure

```bash
# from the kingdoms clone (any repo works — the script clones fresh)
make restack-kingdoms-services     # = scripts/restack.sh merlin-pinpin-org/kingdoms-services
make restack-kingdoms-infra
make restack-kingdoms              # rare: stacked PRs on the docs repo
```

Run it:
- **before opening a new PR** on a repo that already has open PRs (the new
  PR branches off the top of the stack);
- **after a merge** in the stack, so the remaining PRs rebase on the new
  base and stay conflict-free;
- whenever the developer reports a conflict after merging a lower PR.

## Failure mode (fail-closed)

On a rebase conflict the script stops, prints the branch and the worktree
path, and exits non-zero — it never force-pushes a half-resolved stack.
Resolve the conflict in the printed worktree (`git rebase --continue`), then
re-run the script.

## Conventions kept

- `--force-with-lease` only, never `--force`;
- only the PR head branches are rewritten, never a base or protected branch;
- the PR order is the PR number order (oldest at the bottom of the stack).
