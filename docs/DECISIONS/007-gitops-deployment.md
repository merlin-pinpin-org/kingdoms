# ADR-0007: GitOps deployment

**Status:** Accepted
**Date:** 2026-09-18
**Reference:** kingdoms#6

## Context

We need a reliable, auditable deployment process that:

- Is reproducible
- Can be rolled back
- Has a clear audit trail
- Minimizes human error

## Decision

Implement a **GitOps** workflow:

- All infrastructure as code in Git
- Deployment triggered by Git pushes (merge to `main` → test, tags → prod)
- Git history = deployment audit trail
- Manual approval for production
- Automated testing before deployment

Environment policy: `test` auto-deploys on merge, staging deploys
manually, production deploys on tags (see
[VIBEWORKFLOW.md](../VIBEWORKFLOW.md)). The former `dev` environment is
renamed `test`: it is a validation environment on the VPS, not a
developer machine.

**Deployment mechanism (2026 revision, kingdoms-infra#2):** CD jobs run
on a **GitHub Actions self-hosted runner installed on the VPS** (chosen
over SSH-from-Actions and cron-pull: it keeps secrets on the VPS,
attaches deployment to the merge event, and needs no inbound SSH
exposure). The runner carries the labels `self-hosted, kingdoms`. Full
installation procedure:
[kingdoms-infra docs/VPS-SETUP.md](https://github.com/merlin-pinpin/kingdoms-infra/blob/main/docs/VPS-SETUP.md).

## Alternatives Considered

1. **Manual deployment:** error-prone, not auditable
2. **CI/CD only:** no version control for infrastructure
3. **Custom scripts:** hard to maintain, not standardized

## Consequences

### Positive

- Full audit trail
- Reproducible deployments
- Easy rollback (git revert)
- Consistent across environments
- Better collaboration

### Negative

- Learning curve
- More files to maintain
- Need Git access for deployments

## Diagram

```mermaid
flowchart TD
    A["Developer"] -->|"Code Change"| B["Git Commit"]
    B --> C["Git Push"]
    C --> D["GitHub Actions"]
    D --> E["Build Docker Image"]
    E --> F["Push to Registry"]
    F --> G["Deploy to Staging"]
    G --> H["Run Tests"]
    H -->|"Pass"| I["Manual Approval"]
    I --> J["Deploy to Production"]
    H -->|"Fail"| K["Notify Developer"]
    J --> L["Monitor"]
    L -->|"Issue"| M["Rollback"]
    M --> B
```

## References

- [VIBEWORKFLOW.md](../VIBEWORKFLOW.md) — release and environment flow
- kingdoms-infra#2 (CI/CD)
