# Evaluation Release Gate

## Trigger

Run this gate when changing a model, prompt, retrieval strategy, corpus, tool, policy, workflow, or deterministic postprocessor.

## 1. Identify change and blast radius

- Link exact code, prompt, model, dataset, index, policy, and tool versions.
- State the intended improvement and affected user journeys.
- Identify high-risk slices and external side effects.
- Confirm rollback target and compatibility assumptions.

## 2. Protect the dataset

- Freeze the release dataset version.
- Check provenance, permission, retention, and leakage risk.
- Confirm coverage of normal, edge, adversarial, abstain, and dependency-failure cases.
- Keep a hidden or delayed set when repeated tuning risks overfitting.

## 3. Run layered tests

| Layer | Question |
|---|---|
| Deterministic | Do schemas, rules, permissions, and integrations pass? |
| Component | Did retrieval, model, or tool behavior improve independently? |
| End-to-end | Does the user task finish correctly? |
| Safety | Are forbidden actions/disclosures blocked? |
| Operations | Do latency, reliability, and cost remain within budget? |
| Human review | Do calibrated reviewers agree on ambiguous cases? |

## 4. Review regressions

- Compare candidate with baseline by slice, not only overall average.
- Inspect every high-impact failure and a random sample of passes.
- Calibrate model-graded metrics against human review.
- Classify root cause: data, retrieval, model, prompt, tool, code, policy, or product.
- Convert accepted regressions into explicit residual risk with an owner.

## 5. Decide

Choose **release**, **limited canary**, **hold**, or **rollback**. Record thresholds, results, known limitations, monitoring, decision-maker, and expiry date for any exception.

## Production follow-through

- [ ] Canary cohort and kill switch verified
- [ ] Online outcome/safety signals visible
- [ ] On-call/operator briefed on new failure modes
- [ ] User correction and escalation paths working
- [ ] Post-release review time scheduled
