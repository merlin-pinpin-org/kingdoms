# Kingdoms (documentation repo) — session automation.
#
# The targets mirror the session checklist of docs/CONVENTIONS.md; the agent
# runs `make session-check` before opening any PR and at the end of a session.

KINGDOMS_SERVICES ?= ../kingdoms-services

.PHONY: help session-check sync-artifacts restack-% validate contributors-check contributors-sync

# List the available targets (human entry point).
help:
	@echo "Kingdoms docs repo — available targets:"
	@echo "  make help                        — show this help"
	@echo "  make session-check               — full validation (docs + roadmap + dependencies)"
	@echo "  make validate                    — docs validation only"
	@echo "  make sync-artifacts              — regenerate ROADMAP.md and docs/DEPENDENCIES.md"
	@echo "  make restack-<repo>              — restack the open PRs of a repository"
	@echo "  make contributors-check          — roster dry-run (report org drift, no mutation)"
	@echo "  make contributors-sync           — reconcile the org with CONTRIBUTORS.md (mutates)"
	@echo "  KINGDOMS_SERVICES=<path>          — where the kingdoms-services clone lives (default: ../kingdoms-services)"

# Mechanical session checklist: docs validation, roadmap drift,
# dependency-graph drift. Fails closed with the exact artefacts to fix.
session-check:
	python3 scripts/session_check.py --source $(KINGDOMS_SERVICES)/src/kingdoms --config $(KINGDOMS_SERVICES)/config

# Regenerate the synced artefacts (ROADMAP.md, docs/DEPENDENCIES.md) —
# commit the result to the current PR branch, never edit them by hand.
sync-artifacts:
	python3 scripts/sync_roadmap.py
	python3 scripts/sync_dependencies.py

# Roster sync: the org follows CONTRIBUTORS.md (source of truth).
# `contributors-check` reports without mutating (what the CI runs on roster PRs);
# `contributors-sync` adds/removes memberships, teams and repo grants to match the doc.
contributors-check:
	python3 scripts/sync_contributors.py --check

contributors-sync:
	python3 scripts/sync_contributors.py

# Restack the open PRs of a repository on top of each other (stacking
# convention): make restack-kingdoms-services, make restack-kingdoms-infra...
restack-%:
	./scripts/restack.sh merlin-pinpin-org/$*

validate:
	python3 scripts/validate_docs.py --check --source $(KINGDOMS_SERVICES)/src/kingdoms --config $(KINGDOMS_SERVICES)/config
