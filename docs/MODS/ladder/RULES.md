# Ladder mod — Rules

Rules enforced by the ladder mod. Each rule is written so it can be automated
and verified by the bot.

## ELO calculation

1. Starting ELO: 1000 (configurable).
2. K-factor: 32 (configurable).
3. Formula per match:
   `new_elo = old_elo + K * (score - expected_score)` with `score` = 1 win /
   0.5 draw / 0 loss, and
   `expected_score = 1 / (1 + 10^((opponent_elo - own_elo) / 400))`.
4. ELO floors at 100: a loss cannot bring a player below 100.
5. ELO is per game; ratings never transfer between games.

## Match confirmation timeout

1. When a match is created, both players receive a DM and must confirm.
2. If both do not confirm within `LADDER_TIMEOUT` (default 300 s), the match
   is cancelled and both players return to the queue.
3. A player who fails to confirm 3 times in a row is removed from the queue
   (they can rejoin manually).

## Inactivity penalties

1. A player who does not play a match for 30 days is flagged inactive in the
   standings (marker, no ELO loss).
2. After 90 days of inactivity, the player is removed from the ladder
   standings; their ELO is kept and restored on rejoin.

## Dispute resolution

1. Results are recorded from the winner's report (`/ladder report win`); the
   opponent has the configured dispute window (default 24 h) to dispute.
2. A disputed match is flagged for admin review in the `REPORTS` channel
   category; ratings freeze for that match until resolution.
3. Admin decision is final and logged (see the admin mod,
   kingdoms-services#21).

## Fair play

1. One ladder identity per player per game (registration-enforced).
2. Queue manipulation (join/leave spam) is rate-limited; abuse is a
   moderation matter.

## Moderation and penalties

| Infraction | Warning | Temporary Ban | Permanent Ban |
|------------|---------|---------------|---------------|
| Queue manipulation | 1 | 3 | 5 |
| Result falsification | - | 1 | 2 |
| Cheating | - | 1 | 2 |

Enforcement is handled by the moderation workflow (see
[../../WORKFLOWS.md](../../WORKFLOWS.md#3-moderation-workflow)).
