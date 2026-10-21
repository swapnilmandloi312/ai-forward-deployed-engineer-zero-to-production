# 18 · Evaluation: know whether the system improved

**Prerequisites:** Chapters 3, 7, and 13. **Goal:** turn “looks good” into repeatable evidence.

## Evaluate the behavior that matters

An evaluation is an input, an expected behavior or rubric, a scoring procedure, and recorded results. A dataset alone is not an evaluation system. A single average score is not enough to diagnose failure.

**Everyday intuition:** a driving test needs specific maneuvers and pass criteria. “The car moved” is not a useful passing standard.

For a RAG assistant, separate evidence retrieval, answer correctness, claim support, citation quality, and abstention. For an agent, add tool selection, argument validity, forbidden actions, loop termination, and successful external outcomes.

## Build the dataset deliberately

Start with real task categories using synthetic or appropriately permitted examples. Include normal requests, missing information, unanswerable questions, conflicting sources, exact identifiers, long documents, adversarial text, and denied access. Label important slices so aggregate performance cannot hide a severe weakness.

Maintain development and held-out sets. Group related examples to avoid leakage. Record source/version, expected behavior, annotator instructions, and label disagreements. A small carefully inspected set is useful initially, but avoid presenting a handful of examples as comprehensive validation.

## Different evaluators answer different questions

| Evaluator | Good at | Limitation |
|---|---|---|
| Deterministic checks | JSON shape, IDs, numeric tolerances, denied tool calls | Cannot understand every semantic nuance |
| Reference matching | Exact fields and approved phrases | Can reject valid paraphrases |
| Human rubric | Nuance, evidence support, severity | Cost, consistency, and reviewer training |
| Model judge | Scalable approximate semantic grading | Bias, variability, prompt sensitivity, shared errors |
| Online outcome | Accepted drafts, resolved tasks, user corrections | Confounding and delayed feedback |

A model judge needs calibration against independent human labels. Check false passes and false failures, not just agreement percentage. Keep judge input limited to necessary data, version its prompt/model, and audit difficult slices.

## Basic statistics matter

If 45 of 50 examples pass, the point estimate is 90%, but uncertainty is substantial. Avoid claiming a tiny improvement is meaningful without considering sample size and paired examples. If zero failures occur in `n` independent representative trials, the rough “rule of three” gives an approximate 95% upper bound near `3/n` for a rare failure rate. It is not a guarantee and its assumptions often fail for correlated adversarial cases.

Compare candidates on the same examples. Inspect disagreements and severity. A model winning 92% versus 90% overall while leaking one customer's data is not a reasonable release candidate under a no-leakage gate.

## Make evaluation part of delivery

Run deterministic tests on every code change. Run the appropriate behavioral set when prompts, models, retrieval, tools, or source pipelines change. Establish thresholds before reviewing results. Keep an immutable report with configuration, dataset version, slice results, latency, cost, and known limitations.

Release progressively, monitor real failures, and add newly discovered cases to the development regression set. Preserve a separate held-out set for future decisions. Do not silently relabel failures merely to improve a score.

## Practice and answer

**Question:** users like the writing style more, but answer correctness fell. Is satisfaction sufficient?

**Answer:** no. Satisfaction and correctness measure different things, and a convincing wrong answer may score well with users. Apply the agreed correctness gate, investigate failures, and improve presentation without sacrificing required accuracy.

Build: [evaluation lab](../labs/README.md). Template: [evaluation plan](../templates/evaluation-plan.md).

Next: [Security](19-security-and-access.md) · [Index](../INDEX.md)
