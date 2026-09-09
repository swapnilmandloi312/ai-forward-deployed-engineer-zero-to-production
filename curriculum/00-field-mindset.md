# 00 — Field Mindset and Discovery

## Outcome

Turn “we need AI” into a bounded workflow problem, measurable baseline, and decision-ready first slice.

## Learn

- Observe the current workflow before proposing architecture.
- Separate the buyer, user, operator, security owner, and person affected by errors.
- Quantify volume, time, delay, error, rework, risk, and revenue impact.
- Distinguish a stated request from the underlying job to be done.
- Define success, guardrails, non-goals, stop conditions, and an adoption owner.
- Use ambiguity logs and assumption tests instead of silently guessing.

## Field drill

Interview or role-play with three people around one workflow. Ask for a recent real example, not a hypothetical ideal process. Map:

```text
trigger → inputs → decisions → actions → handoffs → exceptions → outcome
```

Mark systems of record, manual copies, waiting time, irreversible actions, and people who can override a decision. Calculate a baseline such as minutes per case, cases per week, error rate, or recovery rate.

Then write two solution candidates:

1. a deterministic automation without an LLM;
2. an AI-assisted version with a human decision point.

Explain when the simpler option wins.

## Evidence

- [Problem brief](../templates/problem-brief.md)
- Current-state workflow map
- Stakeholder and decision-rights map
- Baseline calculation with data source
- Assumption log and first experiment

## Proof gate

Another person can explain who experiences the problem, how often, what it costs, the smallest useful outcome, and why AI is or is not necessary. No architecture is approved until this gate passes.

## Primary references

- [OpenAI Forward Deployed Software Engineer role](https://openai.com/careers/forward-deployed-software-engineer-seattle-seattle/)
- [Palantir: A day in the life of an FDSE](https://blog.palantir.com/a-day-in-the-life-of-a-palantir-forward-deployed-software-engineer-45ef2de257b1)
