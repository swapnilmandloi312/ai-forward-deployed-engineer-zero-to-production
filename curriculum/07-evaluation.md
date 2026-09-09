# 07 — Evaluation Engineering

## Outcome

Make AI quality a versioned release decision using representative cases and multiple operational metrics.

## Learn

- Offline, online, deterministic, model-graded, and human evaluation
- Dataset construction, slices, leakage, annotation guidance, and disagreement
- Baselines, thresholds, confidence intervals, and regression gates
- Task success, groundedness, safety, latency, cost, and escalation metrics
- Pairwise comparison, rubric design, and judge calibration
- Production sampling, feedback quality, drift, and edge-case capture
- Separating model failure from retrieval, tool, data, or workflow failure

## Build

Create a 50-case evaluation set for your project. Include frequent cases, high-cost errors, long-tail edge cases, adversarial inputs, unavailable dependencies, and cases that should abstain or escalate.

Version the dataset, rubric, prompt, model, tool definitions, and code. Establish a baseline, propose release thresholds, run a changed system, and publish a short regression report. Manually review a sample of model-graded outputs to estimate judge error.

## Minimum scorecard

| Dimension | Example measure |
|---|---|
| Task success | Correct completed outcomes / eligible cases |
| Safety | Unsafe action or disclosure rate |
| Reliability | Completed without technical failure |
| Escalation | Appropriate and unnecessary escalation rates |
| Latency | p50 and p95 time to outcome |
| Cost | Cost per successful outcome |

## Evidence

- [Evaluation plan](../templates/evaluation-plan.md)
- Dataset/data sheet and slice distribution
- Baseline and candidate run artifacts
- Error taxonomy and five reviewed failures
- Release decision with rationale

## Proof gate

The release decision is reproducible. High-risk slices cannot be hidden by a good average. Evaluation failures are assigned to a component and feed a test, prompt, data, control, or product decision.

## Primary references

- [OpenAI evaluation best practices](https://platform.openai.com/docs/guides/evals)
- [n8n: Test and improve AI workflows](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/)
