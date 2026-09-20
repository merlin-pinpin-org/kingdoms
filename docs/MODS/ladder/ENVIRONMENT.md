# Ladder mod — Environment

## Discord requirements

- Bot permissions: send messages, send DMs, view channels, manage messages
  (refresh standings posts)
- Channels declared by the mod (provisioned automatically by the core via
  `ModRegistry`, kingdoms-services#26):
  - `ladder:ladder_admin` — admin notifications (disputes, moderation)
  - `ladder:ladder_rankings` — standings and match results
  - `ladder:ladder_info` — rules, matchmaking info, announcements
- Platform-level categories used: `REPORTS` (disputes)
- Roles declared by the mod (logical keys, resolved by `RoleService`):
  - `ladder_participant` — registered players only (the register mod's game roles)
  - `ladder_admin`

## Database requirements

- Collections:
  - `users` (ELO per game stored on UserModel)
  - `matches` (match records and status)
  - `ladder` (ranking snapshots per game)
  - `workflow_states` (match confirmation workflows)
- Indexes:
  - `matches.game + matches.status` — queue and pending match lookups
  - `users.games + users.elo` — ranking computation

## Redis keys

- `ladder:queue:{game}` — matchmaking queue (list, FIFO)
- `ladder:lock:{match_id}` — match result write lock
- `workflow:{user_id}:ladder-confirm` — confirmation hot state, TTL =
  `LADDER_TIMEOUT`

## Configuration options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| enabled | bool | true | Enable/disable the mod |
| starting_elo | int | 1000 | Initial ELO for new ladder players |
| k_factor | int | 32 | ELO K-factor |
| min_elo | int | 100 | ELO floor |
| max_queue_size | int | 10 | Maximum players per game queue |
| dispute_window_hours | int | 24 | Result dispute window |

## Environment variables

```ini
# Required (shared with the platform)
DISCORD_TOKEN=your_token
MONGO_URI=mongodb://localhost:27017
REDIS_URI=redis://localhost:6379

# Optional (ladder mod)
LADDER_TIMEOUT=300
MAX_QUEUE_SIZE=10
```
