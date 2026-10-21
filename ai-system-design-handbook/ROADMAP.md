# An eight-week study-and-build plan

Plan for roughly 60–90 focused minutes on a study day and a longer build session when needed. The schedule is adjustable; finish the proof of understanding before advancing. Use synthetic data until you have the permissions and controls needed for anything else.

Each week follows the same rhythm: learn, inspect an example, build, break it deliberately, and explain the result. Track the work in [your study tracker](templates/study-tracker.md).

## Week 1 · Data and systems foundations

| Day | Learn or do | Evidence to keep |
|---:|---|---|
| 1 | [AI versus application](chapters/01-ai-without-jargon.md) | Explain five non-model components of a support assistant |
| 2 | [Python and APIs](chapters/02-python-api-sql.md) | Validate a JSON invoice without silently filling missing values |
| 3 | SQL filters and aggregation | Tenant-filtered totals with a zero/missing-data case |
| 4 | [Requirements](chapters/03-requirements-and-capacity.md) | One-page brief for a useful assistant |
| 5 | [Distributed systems](chapters/04-distributed-systems.md) | Draw the external-write crash window |
| 6 | Run all five [labs](labs/README.md) | Save observed outputs and describe each limitation |
| 7 | Explain the week without reading | Two-minute recording or written explanation; review gaps |

## Week 2 · Models and context

| Day | Learn or do | Evidence to keep |
|---:|---|---|
| 8 | [Tokens and transformers](chapters/05-tokens-and-transformers.md) | Account for a complete request's context budget |
| 9 | [Model selection](chapters/06-model-selection.md) | Comparison experiment plan with held-out examples |
| 10 | [Prompt/context design](chapters/07-prompting-and-context.md) | Extraction prompt and layered validators |
| 11 | Missing information and injection examples | Five cases where the system should not guess |
| 12 | [Adaptation](chapters/08-adaptation-and-training.md) | Choose prompting/RAG/training for three scenarios |
| 13 | [Serving](chapters/09-serving-and-inference.md) | Memory estimate with explicit overhead exclusions |
| 14 | Answer bank questions 1–10 aloud | Error log and one corrected explanation |

## Week 3 · Retrieval from source to citation

| Day | Learn or do | Evidence to keep |
|---:|---|---|
| 15 | [Ingestion](chapters/10-document-ingestion.md) | Versioned metadata and deletion checklist |
| 16 | [Embeddings/chunking](chapters/11-embeddings-and-chunking.md) | Compare a general policy and its exception in two chunk layouts |
| 17 | [Search/reranking](chapters/12-search-and-reranking.md) | Labeled exact-ID and paraphrase questions |
| 18 | Inspect the mini retrieval lab | Explain filtering before scoring from actual code |
| 19 | Add ten development questions | Show at least one useful failure, not just successes |
| 20 | [Production RAG](chapters/13-production-rag.md) | Complete request trace and citation contract |
| 21 | Solve [support case](case-studies/01-support-assistant.md) before reading | A diagram plus two rejected alternatives |

## Week 4 · Actions and automation

| Day | Learn or do | Evidence to keep |
|---:|---|---|
| 22 | [Workflow/agent distinction](chapters/14-workflows-and-agents.md) | Justify a fixed workflow for one business task |
| 23 | [Tools/MCP](chapters/15-tools-and-mcp.md) | Narrow tool contract with ownership checks |
| 24 | [Memory/state](chapters/16-memory-and-state.md) | Separate conversation summary from approval record |
| 25 | Run and change the invoice lab | Same key/same payload versus changed payload results |
| 26 | [n8n production](chapters/17-n8n-in-production.md) | Node-by-node plan using [the template](templates/n8n-workflow-design.md) |
| 27 | Solve [invoice case](case-studies/02-invoice-operations.md) | Reconciliation path for an unknown write outcome |
| 28 | Answer questions 21–40 selectively | One 20-minute whiteboard discussion |

## Week 5 · Evaluation and security

| Day | Learn or do | Evidence to keep |
|---:|---|---|
| 29 | [Evaluation](chapters/18-evaluation.md) | Dataset slices, rubric, and release thresholds |
| 30 | Run evaluation and intentionally break a source | A failing report and a diagnosis |
| 31 | Judge calibration and uncertainty | Human/automatic disagreements on ten examples |
| 32 | [Access/security](chapters/19-security-and-access.md) | Threat model with trust boundaries |
| 33 | Add denied-access and stale-version cases | Tests that fail when a control is removed |
| 34 | [Healthcare case](case-studies/05-healthcare-operations.md) | Explain grain and unsupported causal conclusions |
| 35 | Review without reading | Teach syntax validity versus evidence validity |

## Week 6 · Operating the system

| Day | Learn or do | Evidence to keep |
|---:|---|---|
| 36 | [Reliability](chapters/20-reliability.md) | Deadline, retry, fallback, and review policy |
| 37 | Inspect gateway failure/cancellation tests | Explain why queued time belongs inside the deadline |
| 38 | [Observability](chapters/21-observability.md) | Redacted trace fields and three actionable alerts |
| 39 | [Deployment](chapters/22-deployment.md) | Release manifest, canary, and rollback plan |
| 40 | [Economics](chapters/23-cost-and-economics.md) | Base-cost and cost-per-accepted-task model |
| 41 | Run an incident drill | Completed [runbook](templates/incident-runbook.md) with recovery evidence |
| 42 | Explain a failed release | What was reverted, what could not be undone, and why |

## Week 7 · Broaden and deliver

| Day | Learn or do | Evidence to keep |
|---:|---|---|
| 43 | [Voice/multimodal](chapters/24-voice-and-multimodal.md) | Distinguish spoken confirmation from booking state |
| 44 | [Classical ML](chapters/25-ml-recommendations-and-ranking.md) | Precision/recall and threshold example |
| 45 | [FDE discovery](chapters/26-fde-discovery-and-delivery.md) | Discovery questions and scoped vertical slice |
| 46 | [Analytics case](case-studies/03-marketing-analytics.md) | Reproduce the ratio example and define a metric contract |
| 47 | [Lead research case](case-studies/04-lead-research.md) | Provenance record with an explicitly missing contact |
| 48 | [Coding](case-studies/06-coding-assistant.md) or [voice](case-studies/07-voice-assistant.md) case | A full design with difficult failure paths |
| 49 | Choose one [capstone](CAPSTONE.md) | Brief, constraints, and baseline; reject unnecessary scope |

## Week 8 · Build, defend, and share

| Day | Learn or do | Evidence to keep |
|---:|---|---|
| 50 | Implement the smallest end-to-end capstone slice | Runnable path using synthetic fixtures |
| 51 | Add deterministic validation and evaluation | Passed/failed cases with real outputs |
| 52 | Add permissions and recovery | A denied action and a recoverable failure demo |
| 53 | Measure timing/cost and review effort | Clearly separated observations and assumptions |
| 54 | Package README, ADR, and runbook | Another person can reproduce the result |
| 55 | Do two timed mocks | Scores using [the rubric](interview/rubric.md) |
| 56 | Record a ten-minute demo and review gaps | Outcome, evidence, trade-offs, limits, and next experiment |

Finishing the schedule is not the same as mastering every topic. Keep iterating where your explanations or experiments are weakest. For a shorter revision route, use [the interview sprint](interview/14-day-sprint.md).
