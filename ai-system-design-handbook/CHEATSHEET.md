# Revision sheet: mechanisms, equations, and decisions

Use this after reading the chapters. It is a memory aid, not a replacement for a worked explanation.

## Core calculations

| Quantity | Calculation | Limitation |
|---|---|---|
| Active-period request rate | `requests / active_seconds` | Daily average can hide busy hours |
| Estimated peak rate | `average_rate × peak_factor` | Validate bursts with measurements |
| Mean in-flight work | `arrival_rate × mean_duration` | Little's Law assumes steady state |
| Token cost | `(input × input_rate + output × output_rate) / 1e6` | Real billing may have extra categories |
| Raw vector bytes | `count × dimensions × bytes_per_value` | Excludes text, indexes, replicas, overhead |
| Capacity released | `tasks × minutes_saved / 60` | Not automatically realized savings |
| Cost per accepted task | `total_workflow_cost / accepted_tasks` | Define accepted task and zero denominator |
| Precision@k | `relevant_in_top_k / k` | Needs relevance labels and defined handling of fewer results |
| Recall@k | `relevant_in_top_k / all_labeled_relevant` | Incomplete labels limit interpretation |

## Choose the intervention from the failure

| Observation | Investigate first |
|---|---|
| Source is not indexed | Ingestion/parser/state/freshness |
| Relevant source not in candidates | Chunking, query representation, retrieval/filtering |
| Candidate found but absent from final context | Reranking, deduplication, context budget |
| Correct evidence present but answer wrong | Prompt, model, exception handling, verification |
| Correct JSON but invented values | Source/evidence and semantic validation |
| Same action occurs twice | Atomic claims, destination idempotency, reconciliation |
| Queue delay rises | Capacity, downstream quota, fairness, retry amplification |
| Cost rises without more requests | Tokens, output length, loops, retries, routing, cache changes |

## Before a model call

Establish the task and identity. Fetch allowed current evidence. Bound context and tools. Define missing-information behavior. Record prompt/model/source versions. Apply time and cost limits.

## Before a tool write

Validate arguments and ownership. Check current permissions, exact-version approval, business constraints, and operation identity. Know the destination's deduplication behavior. Persist confirmed or unknown outcome and a reconciliation path.

## Before a release

Run meaningful deterministic checks and relevant held-out evaluations. Inspect critical slices. Verify data terms/access, recovery, observability, cost, owner, rollout, and rollback. Label every simulated component and unmeasured assumption.

## Five statements to explain precisely

Similarity is not probability. Valid syntax is not correct content. Retrieved evidence is not automatically a grounded answer. A timeout is not proof that a write failed. Potential capacity value is not automatically cash saved.

Back: [Index](INDEX.md) · [Interview questions](interview/question-bank.md)
