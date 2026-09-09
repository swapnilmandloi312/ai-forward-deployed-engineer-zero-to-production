# Curriculum

The modules are ordered by dependency, but the readiness scorecard determines your starting point. Each module uses the same evidence loop:

1. **Understand** the operating concept.
2. **Build** a thin end-to-end slice.
3. **Break** it with realistic edge cases.
4. **Operate** it using metrics, controls, and a runbook.
5. **Explain** the decision to a technical and non-technical stakeholder.

## Module index

| Module | Core question |
|---|---|
| [00 — Field mindset](./00-field-mindset.md) | Are we solving the right workflow problem? |
| [01 — Software delivery](./01-software-delivery.md) | Can another engineer run and trust this service? |
| [02 — Data integration](./02-data-integration.md) | Does data move safely and repeatably across real systems? |
| [03 — Cloud delivery](./03-cloud-delivery.md) | Can we deploy, observe, and roll back predictably? |
| [04 — LLM systems](./04-llm-systems.md) | Is the model choice tied to constraints and fallbacks? |
| [05 — RAG and context](./05-rag-context.md) | Can we retrieve the right evidence and show it? |
| [06 — Agents and automation](./06-agents-automation.md) | Are actions bounded, auditable, and recoverable? |
| [07 — Evaluation](./07-evaluation.md) | How do we know a change is actually better? |
| [08 — Security and governance](./08-security-governance.md) | What can go wrong, who is exposed, and which controls apply? |
| [09 — Observability and operations](./09-observability-operations.md) | Can an operator detect and resolve production failure? |
| [10 — Product and adoption](./10-product-adoption.md) | Will users adopt it without creating hidden work? |
| [11 — Commercial execution](./11-commercial-execution.md) | Is value measurable and credible to a decision-maker? |
| [12 — Portfolio and interviews](./12-portfolio-interviews.md) | Can you prove and defend your judgment? |

## Proof gate rubric

- **Pass:** artifact works, failure is tested, decision is explained, and an operator can use it.
- **Conditional:** happy path works but reliability, security, or handoff evidence is incomplete.
- **Fail:** only notes, screenshots, or tutorial reproduction exist.

Record conditional gates in the scorecard; do not hide them with a polished README.
