# 17 · n8n workflows that can be operated

**Prerequisites:** Chapters 2, 4, and 14–16. **Goal:** apply system-design principles to visual automation.

## Nodes are not the whole architecture

n8n makes integrations and workflow logic visible. Reliability still depends on the surrounding contracts: input validation, durable state, credential access, idempotency, review, retries, monitoring, and ownership. A green execution does not prove the business outcome is correct.

**Everyday intuition:** drawing a clear assembly line helps, but the line still needs quality checks, inventory records, and a way to handle a defective part.

## A practical invoice workflow

1. **Trigger:** receive an upload reference or webhook event. Verify its authenticity and ownership before processing.
2. **Normalize:** assign a stable document/event ID, validate the payload, and retrieve the permitted object.
3. **Deduplicate:** atomically claim the operation in a database using a unique key. A separate “check then insert” can race.
4. **Extract:** parse the document and request structured fields from the model if needed.
5. **Validate:** check decimal totals, currency, vendor identity, duplicates, and required evidence.
6. **Review:** prepare a draft; obtain a decision tied to its exact version.
7. **Write:** call the accounting API with a stable idempotency reference when supported.
8. **Reconcile:** record the confirmed external ID or mark an ambiguous outcome for investigation.
9. **Report:** emit operational metrics and a useful error/review route.

Use code for complicated validation when it improves clarity. Do not hide important business rules inside a long prompt or an undocumented expression.

## Worker scaling

In n8n queue mode, a main instance handles workflow triggers and jobs are distributed to workers through Redis, with execution state in the configured database. Scale workers to increase processing capacity, subject to downstream quotas and database/storage capacity. Keep supported storage and deployment configuration aligned with the official documentation; binary-file handling needs particular attention.

Adding workers without limits may produce provider rate-limit failures faster. Separate concurrency limits by destination and tenant where needed. Monitor queue age as well as queue length: one old unprocessed job may matter more than many new short jobs.

## Error handling and execution data

Create a deliberate error workflow that records the job ID, stage, safe error category, attempt count, and owner. Distinguish temporary API failures from invalid data and denied access. Configure retries around an overall policy instead of enabling them everywhere.

Execution logs can contain documents, personal data, prompts, and API responses. Decide what to retain, redact, restrict, and prune. Credentials should remain in approved credential storage, not exported workflow JSON or a Code node. Scrub environment-specific IDs before sharing workflow exports.

## Development to production

Use separate test credentials and synthetic data. Export and version workflows, document required credentials and environment variables, and review changes. A workflow template is incomplete unless a reader knows the expected input, output, required configuration, error behavior, and validation procedure.

This repository includes a [node-by-node blueprint](../templates/n8n-workflow-design.md), rather than an untested workflow export pretending to be universally import-ready. Node versions and application schemas vary; validate against your actual n8n installation before activation.

## Practice and answer

**Question:** two webhook deliveries arrive together and both pass a duplicate-check node. How do you prevent two invoices?

**Answer:** use an atomic database uniqueness constraint or equivalent claim, then destination-side idempotency/reconciliation. A visual branch that first reads and later writes does not prevent a concurrency race.

Further reading: [official queue mode documentation](https://docs.n8n.io/hosting/scaling/queue-mode/), [official error handling documentation](https://docs.n8n.io/flow-logic/error-handling/).

Next: [Evaluation](18-evaluation.md) · [Index](../INDEX.md)
