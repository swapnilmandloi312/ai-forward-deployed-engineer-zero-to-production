# AI release manifest

**Release ID / date / owner:**

| Component | Exact reference | Verification evidence |
|---|---|---|
| Code/container | | |
| Runtime/dependencies | | |
| Model identifier/configuration | | |
| Prompt | | |
| Tool schemas/adapters | | |
| Policy/approval configuration | | |
| Parser and source versions | | |
| Embedding model and index | | |
| Evaluation dataset/report | | |
| Database migration | | |

Record secret names/references only, never values. If a provider alias cannot be pinned, state the reproducibility limitation and monitoring/re-evaluation plan.

## Rollout

Define environment, cohort, traffic share, observation window, success/stop thresholds, cost ceiling, and reviewer/incident owner.

## Rollback and external effects

State the previous compatible configuration and index/schema dependencies. Explain which external effects cannot be undone by reverting code, how unknown outcomes are reconciled, and which compensating actions are allowed.
