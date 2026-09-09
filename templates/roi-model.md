# ROI Model: [Outcome]

Use ranges and label each input as **measured**, **customer-provided**, or **assumption**.

## Outcome unit

Define one successful outcome, for example: reviewed denial routed correctly, compliant promise-to-pay captured, reconciled document posted, or qualified meeting completed.

## Benefits

| Driver | Conservative | Base | Upside | Type/source |
|---|---:|---:|---:|---|
| Eligible volume / month |  |  |  |  |
| Adoption / coverage |  |  |  |  |
| Minutes changed / outcome |  |  |  |  |
| Loaded cost / hour |  |  |  |  |
| Error/rework change |  |  |  |  |
| Revenue/risk impact |  |  |  |  |

Capacity formula:

```text
monthly capacity value = eligible volume × adoption × minutes changed ÷ 60 × loaded hourly cost
```

Do not label capacity as cash savings unless staffing/spend actually changes. Keep revenue influence separate from attributable realized revenue.

## Total cost

| Cost | One-time | Monthly | Source/confidence |
|---|---:|---:|---|
| Discovery/build/integration |  |  |  |
| Model/API/infrastructure |  |  |  |
| Licenses/vendors |  |  |  |
| Human review/exceptions |  |  |  |
| Operations/support/security |  |  |  |
| Training/change management |  |  |  |
| Expected failure/risk cost |  |  |  |

## Results

```text
monthly net benefit = monthly realized benefit - monthly operating cost
payback months = one-time cost / monthly net benefit
annual ROI = (annual benefit - annual total cost) / annual total cost
cost per successful outcome = monthly operating cost / successful outcomes
```

## Sensitivity and decision

- Variables with the largest effect:
- Break-even adoption/volume:
- Unmeasured benefits and risks:
- Measurement plan and owner:
- Decision requested:
