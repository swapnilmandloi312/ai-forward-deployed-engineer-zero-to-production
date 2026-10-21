# Build one system deeply

Choose one project below and deliver a small, reproducible slice. A blueprint is not a completed project. Label every observed result, simulated behavior, and remaining gap honestly.

| Project | Minimum working slice | A difficult behavior to demonstrate |
|---|---|---|
| Policy assistant | Versioned synthetic documents, permitted retrieval, source output | Stale policy and denied-access question |
| Invoice reviewer | Upload fixture, extraction, validation, reviewed local posting | Duplicate delivery and changed-payload conflict |
| Marketing analyst | Synthetic source tables, exact metrics, supported explanation | Zero denominator and incompatible data grain |
| Research workbench | Evidence-backed organization records and reviewed drafts | Missing contact and unsupported pain-point hypothesis |

## Required deliverables

1. [Problem brief](templates/problem-brief.md) with user, baseline, scope, and constraints.
2. Architecture and data contracts explaining sources of truth and permissions.
3. Runnable code with setup, synthetic fixtures, and expected outputs.
4. [Evaluation plan/report](templates/evaluation-plan.md) including failures and held-out cases.
5. [Architecture decision record](templates/architecture-decision-record.md) comparing at least two plausible choices.
6. [Incident/recovery runbook](templates/incident-runbook.md) tested with a deliberate failure.
7. [ROI worksheet](templates/roi-worksheet.md) separating estimates from measured outcomes.
8. A ten-minute demo: user problem, happy path, denied action, dependency failure, evidence, trade-off, and limitation.

## Acceptance questions

Can another person reproduce the slice without private credentials? Can you trace a result to its source/configuration? Does missing information remain missing? Are duplicate or unauthorized actions prevented by trusted code? Can an operator identify and recover failed work? Can you explain why the chosen design is appropriate at this scale?

If a component is simulated, say so beside its output and in the README. Do not present an offline gateway simulation as a working multi-provider LLM service. Add a real integration only with current documentation, authorized data, and appropriate tests.

Use [the interview rubric](interview/rubric.md) to practice defending the finished design.
