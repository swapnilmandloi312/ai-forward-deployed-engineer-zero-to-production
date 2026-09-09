# 02 — Data and Enterprise Integration

## Outcome

Move data across systems without losing provenance, duplicating actions, or corrupting the system of record.

## Learn

- Source-of-truth ownership and canonical data models
- APIs, webhooks, polling, files, queues, and change-data patterns
- Identity resolution, schema evolution, pagination, and rate limits
- Idempotency, deduplication, checkpoints, replay, and dead-letter handling
- Batch versus event-driven tradeoffs
- Audit records, lineage, retention, deletion, and reconciliation
- n8n as an orchestration layer versus code for high-control components

## Build

Synchronize records from a source CRM-like API into a local operational table, enrich them through a second mock service, and write a status back. Simulate pagination, `429` rate limits, malformed records, repeated webhook delivery, and a write-back failure.

Store the source identifier, source version or timestamp, workflow version, transformation result, destination identifier, and final state. Provide an operator command or workflow branch that safely replays a failed record.

## Decision drill

Compare webhook-first, periodic polling, and nightly batch for the same use case. Include missed-event recovery and total operational cost.

## Evidence

- Data contract and canonical schema
- Field-level provenance table
- Idempotency and retry tests
- Reconciliation report
- Replay runbook with permission boundary

## Proof gate

Replaying the same input produces no unintended duplicate. An operator can explain where each important field came from, identify failed records, and reconcile source and destination counts.

## Primary references

- [n8n workflow documentation](https://docs.n8n.io/workflows/)
- [PostgreSQL transaction processing](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- [CloudEvents specification](https://cloudevents.io/)
