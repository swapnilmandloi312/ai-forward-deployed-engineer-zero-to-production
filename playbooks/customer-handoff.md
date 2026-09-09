# Customer Handoff Playbook

## Goal

Transfer operating capability, decision context, and ownership—not only source code.

## Handoff pack

### Product and scope

- users, eligible cases, exclusions, known limitations, and roadmap;
- baseline, outcome metrics, pilot result, and unresolved assumptions;
- user correction, escalation, feedback, and accessibility guidance.

### System

- architecture, data flows, trust boundaries, dependencies, and systems of record;
- deployed versions, environments, configuration ownership, and change process;
- ADRs explaining important choices and escape paths.

### Quality and safety

- dataset provenance, evaluation procedure, thresholds, results, and weak slices;
- threat model, residual risks, control owners, and exception expiry dates;
- model/prompt/index/tool/policy versioning and release gate.

### Operations

- dashboards, SLOs, alerts, on-call/support boundary, and incident contacts;
- runbooks for frequent failures, rollback, kill switch, replay, and reconciliation;
- backup/restore proof, disaster assumptions, vendor contacts, and budgets.

### Access and governance

- service and human accounts, roles, joiner/mover/leaver process;
- secret rotation, vendor access, data retention/deletion, and audit location;
- named product, technical, security, data, and business owners.

## Transfer method

1. Builder demonstrates normal flow and one failure recovery.
2. Operator performs the same tasks while the builder observes.
3. Operator handles a seeded incident and uses escalation.
4. Owners review open risks, decisions, and next 30-day plan.
5. Access is adjusted to the long-term least-privilege model.
6. Acceptance is recorded with unresolved items and owners.

## Handoff gate

Handoff fails if only the original builder can deploy, diagnose, stop, recover, or explain the system. Schedule a 2–4 week check to review incidents, adoption, drift, cost, and documentation gaps.
