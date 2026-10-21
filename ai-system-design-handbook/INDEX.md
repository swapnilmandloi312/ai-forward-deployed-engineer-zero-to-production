# Full learning index

Read in order if you are new. Revisit individual topics as your project reveals gaps. Each chapter links onward; [the glossary](GLOSSARY.md) provides quick definitions.

## Foundations

| # | Chapter | Prerequisite | Practice outcome |
|---:|---|---|---|
| 1 | [AI without jargon](chapters/01-ai-without-jargon.md) | None | Separate the model from the application |
| 2 | [Python, APIs, and SQL](chapters/02-python-api-sql.md) | 1 | Trace and validate a record |
| 3 | [Requirements and capacity](chapters/03-requirements-and-capacity.md) | 2 | Write a measurable brief and estimate throughput |
| 4 | [Distributed systems](chapters/04-distributed-systems.md) | 2–3 | Explain retries, queues, caches, and duplicate effects |

## Model engineering

| # | Chapter | Prerequisite | Practice outcome |
|---:|---|---|---|
| 5 | [Tokens and transformers](chapters/05-tokens-and-transformers.md) | 1–2 | Budget context and explain prefill/decode |
| 6 | [Model selection](chapters/06-model-selection.md) | 3, 5 | Design a workload-specific comparison |
| 7 | [Prompting and context](chapters/07-prompting-and-context.md) | 5–6 | Separate schema, evidence, and policy checks |
| 8 | [Adaptation and training](chapters/08-adaptation-and-training.md) | 5–7 | Choose RAG, prompting, or training appropriately |
| 9 | [Serving and inference](chapters/09-serving-and-inference.md) | 3, 5–6 | Explain memory and latency trade-offs |

## Data and retrieval

| # | Chapter | Prerequisite | Practice outcome |
|---:|---|---|---|
| 10 | [Document ingestion](chapters/10-document-ingestion.md) | 2, 4 | Preserve versions, permissions, tables, and provenance |
| 11 | [Embeddings and chunking](chapters/11-embeddings-and-chunking.md) | 5, 10 | Interpret similarity and test chunk boundaries |
| 12 | [Search and reranking](chapters/12-search-and-reranking.md) | 11 | Evaluate candidates separately from ranking |
| 13 | [Production RAG](chapters/13-production-rag.md) | 7, 10–12 | Design a cited, access-controlled answer path |

## Actions and automation

| # | Chapter | Prerequisite | Practice outcome |
|---:|---|---|---|
| 14 | [Workflows and agents](chapters/14-workflows-and-agents.md) | 4, 7 | Choose bounded autonomy |
| 15 | [Tools and MCP](chapters/15-tools-and-mcp.md) | 2, 7, 14 | Validate and authorize proposed actions |
| 16 | [Memory and state](chapters/16-memory-and-state.md) | 4, 14 | Distinguish conversational notes and business truth |
| 17 | [n8n in production](chapters/17-n8n-in-production.md) | 2, 4, 14–16 | Design a reviewable, recoverable workflow |

## Production engineering

| # | Chapter | Prerequisite | Practice outcome |
|---:|---|---|---|
| 18 | [Evaluation](chapters/18-evaluation.md) | 3, 7, 13 | Build slices, scoring, and release gates |
| 19 | [Security and access](chapters/19-security-and-access.md) | 4, 13, 15 | Draw trust boundaries and test isolation |
| 20 | [Reliability](chapters/20-reliability.md) | 4, 18 | Bound retries, deadlines, and fallback |
| 21 | [Observability](chapters/21-observability.md) | 18–20 | Diagnose from safe logs, metrics, and traces |
| 22 | [Deployment](chapters/22-deployment.md) | 18–21 | Version behavior, release, and recover |
| 23 | [Cost and economics](chapters/23-cost-and-economics.md) | 3, 6, 18 | Measure accepted outcomes and realistic value |

## Applied delivery

| # | Chapter | Prerequisite | Practice outcome |
|---:|---|---|---|
| 24 | [Voice and multimodal](chapters/24-voice-and-multimodal.md) | 5, 18, 20 | Separate perception, conversation, and action state |
| 25 | [ML, recommendations, and ranking](chapters/25-ml-recommendations-and-ranking.md) | 1, 3, 18 | Evaluate predictions and feedback loops |
| 26 | [FDE discovery and delivery](chapters/26-fde-discovery-and-delivery.md) | 3, 18, 23 | Scope a pilot and leave an operable system |

## Practice and reference

[Start here](START-HERE.md) · [Eight-week roadmap](ROADMAP.md) · [Five labs](labs/README.md) · [Seven cases](case-studies/README.md) · [60 interview answers](interview/question-bank.md) · [Fourteen-day sprint](interview/14-day-sprint.md) · [Capstone](CAPSTONE.md) · [Templates](templates/README.md) · [Glossary](GLOSSARY.md) · [Revision sheet](CHEATSHEET.md) · [Sources](RESOURCES.md) · [Troubleshooting](TROUBLESHOOTING.md)
