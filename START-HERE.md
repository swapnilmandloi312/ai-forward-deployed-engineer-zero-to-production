# Start Here

This repository is designed for evidence, not passive completion. Set up a private learning log if your notes contain employer or customer context; keep only sanitized artifacts public.

## 1. Pick a target role

Collect five current job descriptions for one role: Forward Deployed Engineer, Applied AI Engineer, Solutions Engineer, or AI Automation Engineer. Extract repeated requirements into the [scorecard](./SCORECARD.md). Do not optimize for every AI job at once.

## 2. Run the 45-minute diagnostic

Score every capability from 0 to 3:

- **0 — Unknown:** I cannot explain or demonstrate it.
- **1 — Explain:** I can describe it and follow a tutorial.
- **2 — Build:** I have implemented it independently.
- **3 — Operate:** I have measured, debugged, secured, and handed it over.

Start with the first module where a required skill is below 2. Even experienced builders should complete Module 00 because discovery and outcome framing distinguish FDE work.

## 3. Create your evidence folder

For each project, keep this structure:

```text
project-name/
├── README.md
├── problem-brief.md
├── architecture.md
├── decisions/
├── evals/
├── src-or-workflow/
├── tests/
├── ops/runbook.md
└── outcome-review.md
```

Never upload credentials, real customer data, protected health information, access tokens, or internal documents. Use synthetic data shaped like the real problem.

## 4. Choose a field project

Pick the project closest to a domain you understand. Domain familiarity lets you focus on engineering judgment. If you already build n8n workflows, use n8n for the integration layer and add a small coded service where deterministic control, evaluation, or testability matters.

## 5. Set a weekly operating rhythm

| Session | Work | Output |
|---|---|---|
| Discover | User, workflow, baseline, risks | Updated problem brief |
| Build | Smallest end-to-end slice | Runnable increment |
| Break | Edge cases, attacks, dependency failures | New eval/test cases |
| Operate | Metrics, alerts, runbook, rollback | Operations evidence |
| Communicate | Demo and decision summary | Five-minute field update |

## Week 0 acceptance gate

- [ ] Five target job descriptions analyzed
- [ ] Scorecard baseline completed with evidence links
- [ ] One project and one target user selected
- [ ] Public/private data boundary written down
- [ ] Calendar has at least three build sessions per week
- [ ] First problem interview or workflow observation scheduled

Continue with the [16-week roadmap](./ROADMAP.md).
