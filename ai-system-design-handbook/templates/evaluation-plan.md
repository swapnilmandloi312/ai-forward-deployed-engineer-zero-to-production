# Evaluation plan and report

**Task / owner / date:**
**Candidate and baseline configuration:**
**Dataset version and permitted data source:**

## Expected behavior

Define accepted output, supported refusal/clarification, evidence requirements, and prohibited actions. State important metric definitions and error severity.

## Dataset construction

Record normal/edge/adversarial/denied-access slices, counts, relevance labels, expected citations, grouping, and train/development/test separation. Explain how near-duplicates and temporal leakage are controlled.

## Scorers

List deterministic checks, reference comparisons, human rubric, and any model judge. For a judge, record prompt/model, calibration labels, false-pass/false-fail review, and disagreement procedure.

## Gates chosen before results

| Slice/behavior | Metric | Minimum/maximum | Owner |
|---|---|---|---|
| Answerable | | | |
| Unanswerable | | | |
| Access/actions | | | |
| Latency and cost | | | |

## Results

Report sample sizes, baseline/candidate paired outcomes, important disagreements, severe errors, latency distribution, accepted-task cost, and uncertainty. Link actual outputs rather than only screenshots of a headline score.

## Decision and limits

Ship / limited pilot / revise / reject. Explain the reason, known gaps, monitoring plan, rollback, and who owns the next experiment. Do not convert a small synthetic result into a production guarantee.
