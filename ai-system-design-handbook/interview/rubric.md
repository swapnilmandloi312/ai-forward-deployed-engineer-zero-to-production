# Score a design discussion

Use 0–3 for each dimension: **0** absent/incorrect, **1** named without a workable explanation, **2** coherent with an example, **3** coherent with trade-offs and verification. The maximum is 24. This is a practice rubric, not an employer's hiring standard.

| Dimension | What a strong answer demonstrates |
|---|---|
| Problem framing | User, outcome, baseline, scope, and assumptions |
| Capacity/contracts | Units, traffic/tokens, state records, and API behavior |
| End-to-end architecture | One traceable path, sources of truth, and boundaries |
| AI judgment | Model/retrieval/agent choices backed by an experiment |
| Security | Identity, authorization, data lifecycle, and tool limits |
| Reliability | Deadlines, safe retries, idempotency, fallback, and recovery |
| Evaluation/operations | Slices, gates, traces, alerts, rollout, and rollback |
| Communication | Clear explanation, honest uncertainty, and focused trade-offs |

## Critical errors to revisit regardless of score

- Authorization exists only in a prompt.
- A timeout is treated as proof that an external write did nothing.
- Generated confidence is presented as a calibrated probability without evidence.
- A benchmark or tiny smoke set is used to promise production accuracy.
- A case-study assumption is reported as a measured client outcome.

## What to do with the score

Choose the two weakest dimensions and create a concrete exercise for each. For example, if reliability scored one, add an external-success/local-crash scenario to the invoice design. If communication scored one, explain the same system using six boxes and one request before adding detail.

Repeat the case after a few days. Improvement should appear in reasoning and evidence, not just smoother memorization.

Back: [Question bank](question-bank.md) · [Cases](../case-studies/README.md)
