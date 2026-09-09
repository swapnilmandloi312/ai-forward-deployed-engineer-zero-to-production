# Field Project Blueprints

These are customer simulations, not copy-paste applications. Adapt the scope, write your own implementation, use synthetic or permitted data, and preserve evidence of tradeoffs.

## Choose one

| Project | Best for demonstrating | Primary failure risk |
|---|---|---|
| [RCM Denial Intelligence Copilot](./01-rcm-denial-copilot.md) | Document intelligence, regulated workflows, cited decisions | Unsupported recommendation or data disclosure |
| [Collections Voice Agent](./02-collections-voice-agent.md) | Real-time AI, tools, policy, escalation | Unsafe action, consent failure, latency |
| [Recruiting Operations Agent](./03-recruiting-operations-agent.md) | Multi-step automation and human decision ownership | Bias, PII exposure, unauthorized decision |
| [B2B Lead Intelligence System](./04-lead-intelligence-system.md) | Data pipelines, enrichment, scoring, workflow ROI | Bad provenance, suppression failure, spam |
| [Document Operations Pipeline](./05-document-operations-pipeline.md) | Vision/extraction, schemas, confidence routing | Silent extraction error or schema drift |
| [Enterprise AI Control Plane](./06-enterprise-ai-control-plane.md) | Platform architecture, tenancy, policy, FinOps | Cross-tenant access or runaway cost |

## Required project pack

Every project submission must include:

```text
README + problem brief + system/data-flow diagram + code/workflow
+ automated tests + evaluation dataset/report + threat model
+ observability evidence + runbook + outcome review + demo
```

## Scoring

| Area | Weight | What earns full credit |
|---|---:|---|
| Problem and baseline | 15% | Named user, workflow, current metric, constraint, non-goal |
| Architecture and implementation | 20% | Runnable vertical slice; decisions and alternatives documented |
| Evaluation | 20% | Representative slices; regression gate; error analysis |
| Security and governance | 15% | Threats tested; permissions, data use, retention explicit |
| Reliability and operations | 15% | Traces, alerts, failure drill, rollback/replay, runbook |
| Adoption and business evidence | 15% | Pilot design, feedback, unit economics, honest outcome review |

Below 60%: prototype. 60–79%: credible engineering project. 80%+: strong FDE case study. A critical security or unrecoverable side-effect failure caps the total at 59%.
