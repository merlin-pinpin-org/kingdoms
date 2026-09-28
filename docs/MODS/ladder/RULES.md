# Ladder rules (summary)

> Authoritative exhaustive statements live in the JeanJack V2.0 reference
> ([§3 Rating, §4 Maps & pools, §5 Matchmaking & state machine](../../PLANS/reference/ladder-1v1-jeanjack-v2.md)).
> This file summarizes the operative rules for daily use by game
> designers and admins.

## Rating

- Rating system is a per-ladder admin choice: `elo` or `glicko2`
  (extensible). The state machine and correction tools are identical
  for both.
- Elo: `R' = R + K×(S−E)`; K = 60 for the first 10 completed matches
  (provisional), then 32; per-match delta capped at ±40; floor 800;
  initial 1000.
- Glicko-2: rating + RD + volatility (Glickman 2013); provisional state
  is detected by RD threshold, inactivity naturally widens RD.
- Rating is applied exactly once per match, at REPORTED → COMPLETED.
  `rating_history` is the single source of truth (invariant: sum of
  deltas = current rating).
- Admin corrections: manual adjustment (±N, mandatory reason) or match
  cancellation *with compensation* (inverse history entry). All admin
  mutations are audited (`admin_audit`).

## Queue & matchmaking

- Join requires: registered player + at least one linked game profile
  + no active match.
- Two players are compatible when `|Δrating| ≤ threshold` on both
  sides; threshold starts at 60 and grows +20 every 15 s of waiting,
  capped at 400 (all tunable per ladder).
- Matchmaking runs on join (instant) and on a periodic tick, under a
  Redis lock. It pairs players with **maximum matching** (nobody
  pairable is left alone if a full pairing exists).
- Unconfirmed (not-ready) matches expire after `ready_timeout`;
  ready players re-enter the queue.

## Direct invites

- Any registered player can invite another (modal: target, validity
  3/5/15/30 min, optional map from the active pool).
- The invited player accepts/refuses in DM; expiry returns to normal.

## Map pick

- At the moment both players are ready: random admin bans ∪ player
  bans are removed from the active pool, then a map is drawn weighted
  by player favourites. The map is snapshotted on the match.
- Pool switch (season activation) is transactional, notified, audited,
  and cleans orphaned favourites (full reset only on explicit demand).

## Matches

- Lifecycle: `CREATED → READY → STARTED → (LOBBY → GAME) →
  RESULT_PENDING → REPORTED → COMPLETED | CANCELED` — idempotent
  transitions.
- Results: auto-reported by the game provider when reliable
  (auto-completed if `auto_confirm_system_report`), or confirmed
  manually; contradictory player reports cancel out; a mismatch
  between a player report and provider data alerts admins — never a
  silent correction.
- Cancellation: by player (mandatory reason) or system (deadline,
  missing participant); impossible after COMPLETED. No rating impact
  before confirmation.
