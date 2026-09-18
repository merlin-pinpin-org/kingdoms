# ADR-0001: Multi-platform architecture

- **Status**: Proposed
- **Date**: 2026-09-18
- **Deciders**: Developer
- **Reference**: kingdoms#2

## Context

Kingdoms must run on Discord today, but the platform scope may grow later
(Twitch, Telegram, ...). Game rules and workflows should not be rewritten for
each platform, and mods documentation must stay platform-agnostic.

## Decision

Introduce a platform abstraction in the generic core:

- an `IPlatform` interface implemented by each platform (first: `DiscordPlatform`)
- platform-agnostic models (`IMessage`, `IChannel`, `IUser`) and adapters that
  convert between platform objects and core models
- mods and workflows expressed only against the core interfaces

## Consequences

- **Flexibility**: a new platform is a new `IPlatform` implementation plus its
  adapters, without touching game logic.
- **Maintainability**: platform quirks are contained in one layer.
- **Extensibility**: mods developed against the core work on every platform.
- **Cost**: an extra abstraction layer to design and test up front.
