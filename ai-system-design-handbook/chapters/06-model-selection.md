# 06 · Choose a model with evidence

**Prerequisites:** Chapters 3 and 5. **Goal:** select a model without relying on a leaderboard or a brand preference.

## Start from the task

An invoice extractor, a conversational tutor, and a code-editing assistant have different failure costs. A model that writes engaging prose may struggle with a strict extraction schema. Another may be accurate but too slow for an interactive product. Select against the actual workload.

**Everyday intuition:** hiring the best public speaker does not automatically give you the best accountant. Evaluate the job you need done.

## Build a selection experiment

1. Collect representative examples with explicit expected behavior. Include difficult cases and refusals.
2. Separate development examples from a held-out test set. Do not tune repeatedly on the test set.
3. Keep prompts, tool access, output limits, and scoring conditions comparable.
4. Measure quality by relevant slices, end-to-end latency, cost per completed task, and invalid-output rate.
5. Inspect failures, then choose the simplest candidate that meets the requirements.

Record the exact model identifier or snapshot, configuration, prompt version, evaluation dataset version, date, and provider. Some aliases change over time. A model upgrade is a system change that needs regression testing.

## A decision matrix

| Constraint | What to investigate | Common trap |
|---|---|---|
| Strict JSON | Schema support and semantic validity | Assuming valid JSON means correct values |
| Sensitive data | Contract, retention, access, processing locations | Treating “enterprise” as sufficient evidence |
| High volume | Throughput, token quotas, batching, unit economics | Comparing only the advertised token price |
| Tool actions | Argument correctness and policy compliance | Measuring only chat answer quality |
| Local deployment | Memory, hardware, license, operations | Calling open weights automatically cheaper |
| Multiple languages | Real language-specific examples | Assuming English benchmark performance transfers |

## Hosted versus self-hosted

A hosted API reduces model-serving work but introduces external dependency, quotas, commercial terms, and data-handling decisions. Self-hosting gives more deployment control while requiring hardware, serving expertise, capacity planning, patching, and monitoring. Open-weight availability does not imply unrestricted licensing or transparent training data.

Estimate total cost over the utilization you expect. A continuously running accelerator with little traffic may cost more per task than an API. High utilization, specific control requirements, or a specialized model can change that result. Measure rather than assume.

## Routing and fallback

Routing selects a candidate based on task properties or a measured uncertainty signal. For example, simple classifications use a cheaper model, while difficult extraction cases go to a stronger one or a reviewer. A router adds its own errors, cost, and maintenance.

Fallback handles failures such as a provider timeout. A replacement must support the task, output contract, permissions, and required data terms. Falling back to a provider that is not approved for the data is a security failure even if it improves availability.

## Worked example

On a fictional test, model A costs 1 unit per attempt and succeeds 80% of the time; model B costs 1.5 units and succeeds 97%. If unsuccessful attempts require expensive review, B can be cheaper per accepted outcome. Compare total workflow cost, including retries and human correction, instead of picking A from its lower list price.

## Practice and answer

**Question:** A newer model improves average score but performs worse on cancellation requests. Ship it?

**Answer:** inspect slice size and severity, reproduce the regression, and apply the pre-agreed release gate. An aggregate gain does not justify breaking a critical workflow. Limit rollout or retain the old model until that slice meets the requirement.

Next: [Prompting and context](07-prompting-and-context.md) · [Index](../INDEX.md)
