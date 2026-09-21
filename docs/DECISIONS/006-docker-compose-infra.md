# ADR-0006: Docker Compose infrastructure

**Status:** Accepted
**Date:** 2026-09-18
**Reference:** kingdoms#6

## Context

We need to deploy:

- Bot service
- MongoDB
- Redis
- Potentially other services (monitoring, etc.)

## Decision

Use **Docker Compose** for:

- Local development
- Test environment
- Production environment (with proper orchestration)

### Architecture

- Single `docker-compose.yml` per environment (in `kingdoms-infra/deploy/`)
- Shared Docker images across environments
- Environment-specific configurations
- Health checks for all services

## Alternatives Considered

1. **Kubernetes:** overkill for our scale, complex
2. **Docker Swarm:** middle ground, but Compose is simpler
3. **Bare metal:** not reproducible, hard to maintain

## Consequences

### Positive

- Reproducible environments
- Easy to set up locally
- Consistent across environments
- Good for small-to-medium scale

### Negative

- Limited scaling options
- No automatic scaling
- Manual updates required

## References

- `kingdoms-infra` — deploy manifests
- kingdoms-infra#1 (repo structure), kingdoms-infra#4 (deployment scripts)
