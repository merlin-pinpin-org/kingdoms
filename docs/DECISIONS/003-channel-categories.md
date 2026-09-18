# ADR-0003: Channel categories

- **Status**: Proposed
- **Date**: 2026-09-18
- **Deciders**: Developer
- **Reference**: kingdoms#2

## Context

The bot must send messages to the right place (admin notifications, reports,
ladder announcements) without every mod hard-coding channel names or IDs.
Channel names and IDs vary per Discord server.

## Decision

Route messages through a `ChannelService` driven by a `ChannelCategory` enum
(`ADMIN`, `REPORTS`, `LADDER`, ...):

- mods ask for a channel by category, never by name or ID
- the service resolves the category to a channel via cache, then the database
  (`ChannelModel`), then platform channel creation
- category configuration is stored per server

## Consequences

- **Portability**: the same mod works on any server without code changes.
- **Discoverability**: categories document the intent of every channel the bot
  uses.
- **Self-healing**: missing channels are created on demand and cached.
- **Cost**: channel creation permissions are required for the bot.
