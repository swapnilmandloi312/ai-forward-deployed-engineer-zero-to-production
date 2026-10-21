# Four Grok Bot practice jobs

These are original proposed exercises. Use fictional records first, and verify account capabilities before depending on a particular integration.

## 1. Review a vague FDE request

**Customer input:** "Make our support team more efficient with AI."

Ask the Bot to identify the user, current workflow, task volume, resolution definition, exception types, data owners, review process, and baseline. Require a one-page pilot brief with a small first scope and a reason to choose rules, retrieval, or a model.

**Review:** missing facts remain questions; no promised automation percentage appears. **Follow-up challenge:** reveal that the source system has no usable API and ask which assumptions must change.

## 2. Compare a retrieval design

Supply three public project sources and ten synthetic questions. Ask for a comparison plan that keeps the same questions, labels, environment, and access filters across candidates. Have it distinguish retrieval hit rate, answer support, latency, and cost.

**Review:** there is a reproducible baseline and a list of actual artifacts to collect. **Failure example:** claiming dense retrieval wins without running it. **Correction:** record the recommendation as a hypothesis and specify the experiment.

## 3. Triage synthetic support tickets

```text
T1: 09:00; export button fails; workspace A
T2: 09:04; CSV export gives an error; workspace B
T3: 09:10; password reset delayed; workspace C
T4: 09:12; export fails after choosing a date; workspace A
```

Ask for possible clusters, evidence IDs, uncertainty, investigation questions, and a reviewable incident update. Do not ask it to close tickets or contact customers in this practice task.

**Expected:** three export-related observations, one separate password-reset report, and no invented root cause. T1 and T4 may refer to the same workspace; four reports are not necessarily four affected customers. **FDE lesson:** define the grain before interpreting counts.

## 4. Prepare a repository learning release

Provide a completed exercise, the actual test log, and a list of known gaps. Ask for a concise release note and a proposed next issue. Require that observed results, simulations, and planned integrations stay distinct.

**Review:** a synthetic offline lab is not described as a deployed customer system. A test command not present in the log is marked unrun. **Follow-up:** ask for a short demo script that shows a failure and its recovery, as well as the happy path.

## A reusable review rubric

For each job, check source support, missing-information handling, requested output, scope, external-action boundary, and outcome evidence. Record pass/fail and a concrete failure example for each criterion. Use repeated runs when you are evaluating variable model behavior. A six-item checklist is a useful smoke test, not a general reliability guarantee.

Back: [guide](README.md).
