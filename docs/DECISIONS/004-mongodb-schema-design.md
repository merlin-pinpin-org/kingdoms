# ADR-0004: MongoDB schema design

**Status:** Accepted
**Date:** 2026-09-18
**Reference:** kingdoms#6

## Context

We need to store:

- Users (profile, preferences, stats)
- Guilds (configuration, channels)
- Workflow states
- Ladder data (matches, rankings)

Game rules evolve with the game designer's iterations, so stored payloads
(mostly workflow data) change shape frequently.

## Decision

Use **MongoDB** with **Pydantic models** for:

- Flexible, schema-less storage
- Easy schema evolution
- Good Python integration (PyMongo, Pydantic)
- Horizontal scalability
- JSON-like query language

### Schema design principles

- Embed related data (user preferences in the user document)
- Reference large/volatile data (messages, logs)
- Use indexes for query performance
- Version schemas for backward compatibility

## Alternatives Considered

1. **PostgreSQL:** more structured, but less flexible for evolving schemas
2. **SQLite:** simple but not scalable, no horizontal scaling
3. **Firebase:** good for realtime, but vendor lock-in

## Consequences

### Positive

- Schema flexibility
- Easy to add new fields
- Good for hierarchical data (users, guilds)
- Horizontal scaling possible

### Negative

- No multi-document transactions
- No joins (need to denormalize)
- Less ACID compliance

## References

- [ARCHITECTURE.md](../ARCHITECTURE.md) — models
- kingdoms-services#4 (DB models)
