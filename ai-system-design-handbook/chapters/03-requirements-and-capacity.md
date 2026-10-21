# 03 · Requirements before architecture

**Prerequisites:** Chapters 1–2. **Goal:** turn “build an AI assistant” into a testable system brief.

## Ask what success means

Functional requirements describe behavior: search policies, extract invoices, draft a reply. Non-functional requirements constrain that behavior: response time, availability, quality, cost, security, freshness, and accessibility. A beautiful architecture cannot rescue a product that solves the wrong problem.

**Everyday intuition:** decide the destination and budget before choosing a vehicle. “Add AI” describes a possible solution, not the user’s underlying need.

For a support assistant, clarify who uses it, which policies it can read, which actions it can take, and when it should escalate. Ask for the present baseline: tickets per day, minutes per ticket, error rate, and user satisfaction. State unknowns instead of hiding them behind a diagram.

## A worked sizing example

Assume a fictional service receives 12,000 requests in a 10-hour active day, with a peak factor of six. Average rate is `12000 / (10 × 3600) = 0.333 requests/second`. Estimated peak is `2 requests/second`. If average in-flight duration during a steady peak is four seconds, Little's Law gives an average of about eight in-flight requests.

This is an estimate under steady-state assumptions, not a production capacity limit. Bursts, slow-tail requests, connection overhead, quotas, retries, and failures need measured headroom. A p95 duration substituted into the formula is a rough planning approximation, not the law's exact average relationship.

Assume each request uses 2,000 input tokens and 400 output tokens. At two requests/second, demand is roughly 240,000 input tokens/minute and 48,000 output tokens/minute before retries. A provider's requests-per-minute quota alone is insufficient; token quotas can be the tighter constraint.

## Budget each stage

| Stage | Fictional planning budget | Why measure separately |
|---|---:|---|
| Identity and policy checks | 50 ms | Access checks cannot be skipped to improve speed |
| Retrieval | 150 ms | Slow database queries hide behind model latency |
| Reranking | 200 ms | Better relevance may consume meaningful latency |
| First generated content | 800 ms | Shapes perceived responsiveness |
| Remaining generation | 2,500 ms | Depends strongly on output length |

Do not add independently measured stage p95 values and call the result the end-to-end p95. Percentiles are not generally additive. Trace the actual end-to-end distribution.

## Quality is a requirement too

“95% accurate” is incomplete. Accurate on which examples? Is an unsupported answer counted as wrong? Does the metric include unanswerable and permission-denied requests? Specify the dataset, rubric, slices, sample size, and threshold.

For example: “On a held-out set of 200 synthetic policy questions, at least 90% of answerable requests must cite the relevant policy span, and all tested cross-tenant queries must reveal no unauthorized content.” The latter is a release test, not a mathematical proof of zero leakage.

## Write the first design brief

Record the user, task, baseline, sources, allowed actions, volume, latency target, quality gate, cost ceiling, and owner. Add a non-goal such as “does not issue refunds automatically.” Non-goals prevent an interview or client engagement from growing without a decision.

## Practice

Use [the capacity lab](../labs/README.md) with 12,000 requests/day, ten hours, peak factor six, and four-second mean latency. Then double output length and explain which constraints might change. Include token throughput, spend, and user waiting time.

Next: [Distributed systems](04-distributed-systems.md) · [Index](../INDEX.md)
