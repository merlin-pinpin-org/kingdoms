# ADR-0002: Workflow engine

- **Status**: Proposed
- **Date**: 2026-09-18
- **Deciders**: Developer
- **Reference**: kingdoms#2

## Context

Most Kingdoms features are multi-step interaction sequences (registration in
DMs, match reporting, moderation). Implementing each sequence ad hoc in commands
leads to duplicated state handling, hard-to-test flows, and poor visibility for
the game designer.

## Decision

Centralize interaction sequences in a `WorkflowEngine` service:

- workflows are declared as steps with entry conditions and transitions
- workflow state is persisted (`WorkflowState` in MongoDB, hot state in Redis)
  so sequences survive restarts and can be resumed
- UI components (buttons, select menus, modals) feed events back into the
  running workflow

## Consequences

- **Robustness**: interrupted flows (bot restart, user idle) can be resumed.
- **Consistency**: all sequences share the same error handling and timeout rules.
- **Testability**: workflows can be replayed without a live platform.
- **Cost**: state must be modeled and versioned carefully when rules evolve.
