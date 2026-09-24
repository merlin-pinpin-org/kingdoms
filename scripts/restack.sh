#!/usr/bin/env bash
# Restack the open PRs of one repository on top of each other.
#
# The stacking convention (docs/CONVENTIONS.md): sequential PRs opened on the
# same repo are rebased on their predecessors so the developer can merge them
# in order without conflicts. This script performs that restack mechanically:
# it lists the open PRs of the repo (oldest first), rebases each head branch
# on its base (base = the base branch of the PR below it in the stack, or the
# PR base), and force-pushes the rewritten branches with --force-with-lease.
#
# Usage:
#   scripts/restack.sh <owner/repo> [--dry-run]
#
# Requires: gh (authenticated), git. The script never merges, never pushes to
# protected branches (only to the PR head branches), and never deletes them.
set -euo pipefail

repo="${1:?usage: restack.sh <owner/repo> [--dry-run]}"
dry_run="${2:-}"
workdir="$(mktemp -d)"
trap 'rm -rf "$workdir"' EXIT

echo "==> Restacking open PRs of $repo"

# List open PRs, oldest first: number, head ref, base ref.
mapfile -t prs < <(gh pr list --repo "$repo" --state open --limit 50 \
  --json number,headRefName,baseRefName \
  --jq 'sort_by(.number)[] | "\(.number) \(.headRefName) \(.baseRefName)"')

if [[ ${#prs[@]} -eq 0 ]]; then
  echo "    no open PR — nothing to restack"
  exit 0
fi

prev_head=""
for pr in "${prs[@]}"; do
  read -r number head base <<< "$pr"
  echo "--> PR #$number: $head (base $base)"
  if [[ "$head" == "$prev_head" ]]; then
    echo "    skipped: same branch as the previous PR"
    continue
  fi
  cd "$workdir"
  gh repo clone "$repo" "repo" -- --quiet 2>/dev/null || true
  cd repo
  git fetch origin "$head" "$base" --quiet
  git checkout -B "$head" "origin/$head" --quiet
  # The base of a stacked PR is the head of the PR below it; otherwise the
  # PR base itself.
  onto="$base"
  [[ -n "$prev_head" ]] && onto="$prev_head"
  git rebase "origin/$onto" --quiet || {
    echo "    CONFLICT while rebasing $head on $onto — resolve manually:"
    echo "    git rebase --continue in $workdir/repo"
    exit 1
  }
  if [[ "$dry_run" == "--dry-run" ]]; then
    echo "    dry-run: $head rebases cleanly on $onto"
  else
    git push --force-with-lease origin "$head" --quiet
    echo "    restacked $head on $onto"
  fi
  prev_head="$head"
done

echo "==> Done"
