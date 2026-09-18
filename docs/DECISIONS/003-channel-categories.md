# ADR-0003: Channel categories

**Status:** Accepted
**Date:** 2026-09-18
**Reference:** kingdoms#2, kingdoms#6

## Context

Different types of messages need to go to different channels:

- Registration confirmations → `ADMIN` channel
- Reports → `REPORTS` channel
- Ladder updates → `LADDER` channel
- General messages → default channel

Without a system, we'd have:

- Hardcoded channel IDs
- No flexibility for different guilds
- Difficulties adding new channel types

## Decision

Implement a **`ChannelCategory` enum** and a **`ChannelService`** that:

- Defines channel categories (`ADMIN`, `REPORTS`, `LADDER`, `GENERAL`, ...)
- Maps `guild_id + category → channel_id`
- Creates channels automatically if missing (via `IPlatform`)
- Caches mappings in Redis for performance
- Falls back to MongoDB (`ChannelModel`) for persistence

## Alternatives Considered

1. **Hardcoded channel IDs:** simple but inflexible
2. **Config file only:** no automatic channel creation
3. **User-configured per guild:** too complex for the initial version

## Consequences

### Positive

- Flexible channel routing
- Automatic channel creation
- Works across multiple guilds
- Easy to add new categories
- Good performance (cached)

### Negative

- Slight complexity in `ChannelService`
- Need to handle channel creation errors (permissions)

## References

- [ARCHITECTURE.md](../ARCHITECTURE.md) — channel management diagram
- [WORKFLOWS.md](../WORKFLOWS.md) — channel category management and message
  routing
- kingdoms-services#5 (ChannelService), kingdoms-services#7 (enums)
