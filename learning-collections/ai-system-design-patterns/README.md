# AI System Design Patterns: choices, failures, and practice

**Eight original design cards by Swapnil AI Labs.**

Use these cards after learning the fundamentals. Each starts with a concrete constraint, proposes an architecture, shows how it can fail, and ends with an exercise. These are educational designs rather than a claim that one stack fits every deployment.

| Pattern | Main question |
|---|---|
| [01: Authorized retrieval](patterns/01-authorized-retrieval.md) | Which evidence may this caller see right now? |
| [02: Model gateway](patterns/02-model-gateway.md) | How do time, cost, and data rules survive fallback? |
| [03: Reviewed actions](patterns/03-reviewed-actions.md) | Does approval apply to the exact action being executed? |
| [04: Memory and workflow state](patterns/04-memory-and-state.md) | What must remain correct after a retry or correction? |
| [05: Document ingestion](patterns/05-document-ingestion.md) | Can a parser produce a wrong but plausible record? |
| [06: Evaluation as a release gate](patterns/06-evaluation-gates.md) | Which failure blocks release even if averages improve? |
| [07: Voice and human handoff](patterns/07-voice-handoff.md) | Can a conversation stop, correct itself, and transfer context? |
| [08: Tenant budgets and fair service](patterns/08-budgets-and-fairness.md) | Can one expensive job starve everyone else? |

## Study one pattern deeply

Write the invariant in your own words. Draw the data path and identify the enforcement point. Invent one failure that a happy-path demo would miss. Then implement a small slice or a table-driven simulation and record its behavior. Set numeric thresholds from the task's needs; the examples do not prescribe universal production limits.

Use [the architecture review template](REVIEW-TEMPLATE.md). For hands-on discovery, pair a card with the FDE Field Drills in the parent learning collection. For implementation candidates, use the companion Open-source AI Engineering catalog and read each project's current upstream documentation.

## How this connects to personal agents

Muse, ChatGPT dots, and Grok Bot are examples to study through their documented interfaces. These cards explain engineering questions behind persistent responsibilities, connected sources, background work, reviews, and failures. They do not describe the vendors' private implementations or provide an unofficial product API.

Original explanations and diagrams use the [MIT License](LICENSE). Supporting reading points to the owning projects; their code, models, data, and services keep their own terms.
