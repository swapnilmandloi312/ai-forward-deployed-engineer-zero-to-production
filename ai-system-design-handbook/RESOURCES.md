# Primary resources and source notes

The core explanations and exercises are written for this handbook. These primary sources support further study and implementation checks. Source pages were consulted during preparation on **21 October 2026**. That date is not a promise that every API or price stays unchanged.

## Research foundations

| Resource | Use it to study | Handbook connection |
|---|---|---|
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | The original transformer architecture | Tokens and attention |
| [LoRA](https://arxiv.org/abs/2106.09685) | Low-rank parameter adaptation | Adaptation choices |
| [QLoRA](https://arxiv.org/abs/2305.14314) | Quantized-base adapter training | Adaptation and memory |
| [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | Learning from preference pairs | Training vocabulary |
| [PagedAttention](https://arxiv.org/abs/2309.06180) | KV-cache memory management for serving | Inference optimization |
| [Reciprocal rank fusion](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf) | Combining ranked result lists | Hybrid retrieval |

Paper-specific experimental results are not reproduced as promises about this handbook's labs or a reader's workload.

## Official implementation references

| Resource | What to verify before implementation |
|---|---|
| [pgvector](https://github.com/pgvector/pgvector) | Supported types/distances, index settings, filtering, and version-specific behavior |
| [vLLM](https://docs.vllm.ai/) | Supported models/hardware, scheduling, memory, and serving configuration |
| [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) | Concurrency behavior and transaction retry requirements |
| [PostgreSQL row-level security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) | Policies, roles, ownership, and bypass behavior |
| [n8n queue mode](https://docs.n8n.io/hosting/scaling/queue-mode/) | Workers, Redis/database roles, storage, and deployment requirements |
| [n8n error handling](https://docs.n8n.io/flow-logic/error-handling/) | Error workflows and failure-routing configuration |
| [MCP specification, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) | The selected dated protocol revision, capabilities, transport, and security guidance |
| [OpenTelemetry traces](https://opentelemetry.io/docs/concepts/signals/traces/) | Spans, context propagation, and observability concepts |
| [OWASP GenAI security project](https://genai.owasp.org/) | Current threat categories and security guidance |

## Architecture perspective

[Anthropic's Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) explains the distinction between predefined workflows and model-directed agents. Its original publication is historical; use current product documentation for actual API and deployment details.

## Inspiration

[Om Bharatiya's AI System Design Guide](https://github.com/ombharatiya/ai-system-design-guide) is credited as inspiration for the learning-reference format. It is not the authority for this handbook's vendor-specific claims. See [acknowledgments](ACKNOWLEDGMENTS.md).

## Maintenance policy

Prefer primary sources. For a new API, capability, protocol revision, pricing claim, benchmark, or legal statement, include the official source and verification date. Avoid undated “best model” tables and guaranteed performance. Label illustrative numbers, identify inferences, and add an executable example only when it was actually checked.
