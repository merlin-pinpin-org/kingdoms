# Ladder mod

The ladder mod manages competitive rankings: players join a matchmaking
queue, get paired into matches, and their results drive ELO ratings and
ladder standings.

## Purpose

- Provide a competitive ranking system per game (ELO)
- Automate matchmaking from a join queue
- Record match results and maintain rankings
- Publish results and standings in the `LADDER` channel

## ELO rating system

- Every player starts at the configured starting ELO (default 1000)
- Match results adjust both players' ratings using the standard ELO formula:
  `new_elo = old_elo + K * (result - expected_score)` where `K` is the
  configured K-factor (default 32) and `expected_score` derives from the
  rating difference
- The exact rules (K-factor, starting ELO, floors) are defined in
  [RULES.md](RULES.md)

## Matchmaking algorithm

1. Players join the queue with `/ladder join` (registration required)
2. The queue is matched first-in-first-out
3. When 2+ players are queued, a match is created between the two
   longest-waiting players of the same game
4. Both players receive a DM and must confirm availability

See the ladder workflow in
[../../WORKFLOWS.md](../../WORKFLOWS.md#2-ladder-workflow) for the
authoritative sequence and diagram.

## Queue system

- One queue per game, capped at the configured `MAX_QUEUE_SIZE`
- Leaving is possible until the match is confirmed (`/ladder leave`)
- Unconfirmed matches return both players to the queue after the confirmation
  timeout

## Ranking calculation

- Rankings are derived from ELO (descending), with tie-breaks by number of
  matches played, then earliest registration
- Rankings are recomputed after every recorded match
- Standings are published to the `LADDER` channel category

## Data stored

| Collection | Content |
| ---------- | ------- |
| `users` | Player ELO per game (on UserModel) |
| `matches` | Match records: players, game, status, result, timestamps |
| `ladder` | Snapshot of current rankings per game |

## Rules

See [RULES.md](RULES.md) for ELO calculation, confirmation timeout,
inactivity penalties, and dispute resolution.

## Environment

See [ENVIRONMENT.md](ENVIRONMENT.md) for permissions, channel categories,
and database requirements.
