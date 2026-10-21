# 21 · Logs, metrics, traces, and quality monitoring

**Prerequisites:** Chapters 18–20. **Goal:** explain a failure from evidence rather than guessing.

## Three complementary views

Logs record discrete events. Metrics summarize measurements over time. Traces connect operations belonging to a request or job. A trace is made of spans, each representing an operation with timing and metadata. Use a shared request/job ID to connect the views.

**Everyday intuition:** a receipt tells you a purchase happened, a monthly total shows a trend, and a delivery tracking history shows where one package spent its time.

## Trace an AI request

Useful spans include authorization, retrieval, reranking, context assembly, model invocation, validation, and tool execution. Attach prompt/model versions, index version, token usage, safe error categories, and references to permitted artifacts. Do not automatically attach full documents or personal conversations.

For asynchronous jobs, propagate trace context where supported and keep a durable job ID even if a trace is sampled out. A trace is an observation record, not the source of truth for a financial transaction.

## What to measure

| Area | Useful measurements | Why |
|---|---|---|
| Traffic | Requests by task and tenant | Understand workload mix |
| Latency | End-to-end and stage distributions | Locate bottlenecks |
| Reliability | Timeout, invalid-output, fallback, retry rates | Identify degradation |
| Retrieval | Empty results, evidence versions, sampled recall | Find data/relevance issues |
| Cost | Input/output tokens, review effort, accepted tasks | Explain unit economics |
| Workflow | Queue age, review backlog, reconciliation count | Expose stalled work |
| Quality | Sampled correctness, unsupported claims, correction rate | Catch failures beyond status codes |

Keep metric label cardinality bounded. User IDs, document IDs, and full prompts usually belong in controlled logs or traces rather than unbounded metric labels.

## Alerts should lead to an action

An alert needs a threshold, window, owner, and runbook. “Any error occurred” often produces noise. A sustained rise in failed authorized tasks, oldest queue age, or unexpected spend may be actionable. Severe access-control failures may warrant immediate escalation even without a large count.

Monitor both system and business consequences. If accepted invoice drafts suddenly fall while model API calls still succeed, investigate validation, source quality, or model changes. Green infrastructure dashboards cannot establish correct outcomes.

## Quality sampling and drift

Input distributions change: new document templates, languages, product policies, user behavior, and model aliases. Drift is not automatically failure, but it can invalidate earlier evaluation. Compare slices, sample recent outputs, and investigate changes in errors or human correction effort.

Use privacy-aware sampling. Store only the minimum content needed for the review, restrict access, and set retention. Treat evaluation artifacts as potentially sensitive too.

## Practice and answer

**Scenario:** cost doubled while request volume stayed constant.

**Answer:** compare token counts, output length, model routing, tool-loop steps, retries, cache behavior, and workload mix by version. A longer document type or fallback loop can double spend without any traffic growth. Attribute cost to stages and accepted tasks before changing models.

Further reading: [OpenTelemetry traces](https://opentelemetry.io/docs/concepts/signals/traces/).

Next: [Deployment](22-deployment.md) · [Index](../INDEX.md)
