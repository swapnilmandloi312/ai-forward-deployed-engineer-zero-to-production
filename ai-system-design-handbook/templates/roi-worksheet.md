# ROI and cost worksheet

**Workflow / measurement period / owner:**

| Input | Value | Unit | Observed or assumed? | Evidence |
|---|---|---|---|---|
| Tasks | | tasks/period | | |
| Manual time | | minutes/task | | |
| Assisted time including review | | minutes/task | | |
| Loaded labor rate | | currency/hour | | |
| Accepted outcome rate | | percent | | |
| Model and tool cost | | currency/period | | |
| Hosting/storage/monitoring | | currency/period | | |
| Maintenance and review | | currency/period | | |
| Implementation cost | | one-time currency | | |

Capacity released: `tasks × (manual_minutes − assisted_minutes) / 60`.

Modeled capacity value: `hours_released × loaded_hourly_rate`.

Cost per accepted task: `total_period_workflow_cost / accepted_tasks`, with a defined result for zero accepted tasks.

## Interpretation

Explain adoption, error/rework changes, new risks, and how released capacity will actually be used. Separate capacity value, observed productivity, revenue effects, and actual expense reduction. Avoid double-counting review labor in multiple categories.

## Sensitivity

Recalculate for lower adoption, higher correction effort, and provider/volume changes. State which assumption most affects the decision and how the pilot will measure it.
