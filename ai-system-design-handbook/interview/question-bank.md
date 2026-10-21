# 60 AI system-design questions with worked answers

Try each answer before reading it. Explain the mechanism, give an example, and name a trade-off. The answers below are intentionally concise enough for revision; follow the linked chapter for the full explanation.

## Foundations and model behavior

### 1. What is the difference between an LLM and an AI application?

An LLM predicts or generates token sequences. The application adds identity, data access, retrieval, tools, validation, user experience, and operations. A strong model can still sit inside an unreliable application. For example, improving its writing cannot repair a missing permission check or a duplicate payment. See [Chapter 1](../chapters/01-ai-without-jargon.md).

### 2. When should you avoid an LLM?

Start with rules or SQL for exact conditions and calculations. A model may help interpret language, but a database should calculate total overdue balance from authoritative rows. Compare with conventional ML for prediction/ranking. Add generation only when it improves the user's task enough to justify uncertainty, evaluation, latency, and cost.

### 3. Why are tokens different from words?

Tokenizers split content into vocabulary-specific units that can include word fragments and punctuation. Counts vary by language, code, formatting, and tokenizer. Estimate using the actual model tooling, including instructions, tools, history, and retrieved evidence. A universal “four characters equals one token” rule is only a rough heuristic for some text.

### 4. What does attention do?

Attention forms weighted combinations of value representations using relationships between queries and keys. It lets representations use information from other positions under the architecture's masking rules. It is a learned numerical mechanism, not a guarantee that the model identifies the right evidence or understands a business rule correctly. See [Chapter 5](../chapters/05-tokens-and-transformers.md).

### 5. Does temperature zero guarantee correct or identical output?

No. Lower sampling randomness does not verify facts, permissions, or calculations. Backend changes, model versions, implementation details, and task ambiguity can also affect reproducibility. Use versioned configuration, deterministic validators, and repeated workload-specific evaluation rather than treating a decoding setting as a correctness mechanism.

### 6. Explain prefill, decode, and KV cache

Prefill processes the input context. Decode generates subsequent tokens. The KV cache stores intermediate attention information used while generating, reducing repeated computation. Longer active sequences and more concurrent requests consume more cache memory. This is why a model fitting in memory at startup does not prove it can handle the target traffic.

### 7. How would you choose between two models?

Run comparable tasks on development and held-out examples, record exact configurations, and measure critical slices, latency, invalid outputs, and cost per accepted task. Include review effort. A cheaper token price may lose if more outputs need correction. Reject a candidate that breaks a critical access or action requirement despite an average quality gain.

### 8. RAG or fine-tuning?

RAG supplies retrieved evidence at request time, useful for current knowledge and citations. Fine-tuning changes learned behavior using training examples. For changing internal policies, start with retrieval; for a persistent specialized behavior failure after a good prompt baseline, investigate adaptation. Neither replaces authorization, exact business state, or data quality. See [Chapter 8](../chapters/08-adaptation-and-training.md).

### 9. What is data leakage in evaluation?

Evaluation information reaches training or tuning, directly or through related examples. Random row splits can leak when rows share a document, customer, or near-duplicate template. Split according to real dependencies and time when appropriate. Preserve a held-out set and do not repeatedly tune on its results while continuing to call it independent.

### 10. What does LoRA change?

LoRA learns low-rank updates to selected model weights rather than broadly training every base parameter. It can reduce training resources, but serving compatibility and quality still need testing. It does not turn a model into a current database or provide per-user access controls. Adapter and base-model versions belong in the release record.

## Data and retrieval

### 11. What must an ingestion pipeline preserve?

The original source, document identity/version, parser version, checksum, ownership, access metadata, and page/section provenance. Parsed content must remain connected to those records through chunking and indexing. Otherwise you cannot reliably update, delete, cite, or authorize it. A parse-success status is insufficient if extracted text is empty or scrambled.

### 12. Why not embed every PDF as one vector?

One representation may blur several unrelated sections and fail to localize the passage needed for a question. Smaller chunks can match better but lose context. Evaluate structure-aware chunks and parent expansion with labeled questions, including exceptions and tables. Chunk size is a workload-specific choice, not a universal fixed number.

### 13. Is cosine similarity a confidence score?

No. It measures geometric similarity under a particular representation. A value of 0.8 does not mean an 80% chance that the evidence answers the question correctly. If you use scores to gate answers, calibrate the decision against labeled answerability examples and test distribution shifts. See [Chapter 11](../chapters/11-embeddings-and-chunking.md).

### 14. When does keyword search beat dense retrieval?

Exact identifiers, uncommon product names, error codes, and precise terminology can favor lexical search. Dense retrieval can help with semantic paraphrases. Compare both and consider hybrid search if the workload contains both patterns. Do not assume semantic representations always preserve a rare identifier's importance.

### 15. Why combine rankings rather than add raw search scores?

Scores from lexical and vector retrieval may use different scales and distributions. Adding them directly can let one dominate for accidental numerical reasons. Rank fusion combines relative order; reciprocal rank fusion is one example. Its parameters and weights still require evaluation, and it does not produce a probability of relevance.

### 16. What can a reranker fix, and what can it not fix?

A reranker can improve ordering among supplied candidates. It cannot select a relevant document absent from that set. If candidate recall is poor, inspect ingestion, chunking, query representation, filtering, and the first-stage retriever before paying for a stronger reranker. Measure both candidate coverage and final ranking quality.

### 17. Where should tenant filtering happen?

Before unauthorized evidence is exposed to the model, user, logs, or other components outside the allowed boundary. Derive scope from trusted identity and enforce it in the data path. Test actual index/filter behavior because selective approximate search can harm recall. A prompt telling the model to ignore another tenant's data is insufficient.

### 18. How should document updates become visible?

Build and validate a new version, then switch active visibility without exposing partial chunks. Preserve source/version lineage in citations and traces. Retire old retrieval results and invalidate affected caches. Permission revocation needs current enforcement rather than waiting for an eventual reindex. Test both freshness and access behavior.

### 19. What is the difference between retrieval recall and answer correctness?

Recall measures whether relevant evidence was found. Correctness measures the answer under a task rubric. Relevant evidence can be omitted during context assembly, truncated, misunderstood, or combined with a distracting exception. Evaluate stages separately so high recall does not conceal weak generation. See [Chapter 13](../chapters/13-production-rag.md).

### 20. When is GraphRAG justified?

Investigate it when important questions depend on relationships across entities and documents that ordinary retrieval cannot handle adequately. Account for entity resolution, graph extraction errors, updates, access, and cost. Compare against a simpler retrieval baseline first. Adding a graph to ordinary FAQ search can increase maintenance without improving outcomes.

## Context, agents, and tools

### 21. What is context engineering beyond prompting?

It determines which evidence, history, tools, state, and metadata enter the request, in what form and budget. A clear prompt using stale or unauthorized context still fails. Version context sources, preserve citations, remove duplication, and keep durable business state outside conversation prose. See [Chapter 7](../chapters/07-prompting-and-context.md).

### 22. Why is valid JSON not enough?

Parsing establishes syntax; schemas establish some shape/type constraints. Values can still be fabricated, unsupported, inconsistent, or prohibited. Validate domain rules, source evidence, arithmetic, ownership, and action policy. A perfectly shaped invoice with an invented currency must not pass simply because its fields have the expected types.

### 23. Workflow or agent?

Use a predefined workflow when the route and rules are known. Consider an agent when useful next steps depend on intermediate discoveries and cannot be expressed simply as a fixed route. Keep budgets, tools, policy, and completion checks in the application. More autonomy means more trajectories and failure cases to evaluate.

### 24. What should stop an agent loop?

Observable task completion, maximum steps, elapsed deadline, token/cost budget, cancellation, a denied action, or lack of progress. Persist useful partial results and an outcome reason. A model's claim of completion is insufficient when the requested artifact, verified source, or confirmed transaction is missing.

### 25. What is a tool call?

A structured proposal to invoke a named capability with arguments. The executor still checks syntax, ownership, permissions, state, budget, and approval before performing it. Keep tools narrow. A broad shell or arbitrary SQL tool exposes much more authority than a scoped lookup, so its control requirements differ substantially.

### 26. Does MCP solve tool security?

MCP standardizes interactions with tool/resource/prompt servers. It does not make a server trusted or authorize every operation. Follow the chosen dated specification and retain server identity checks, least privilege, input validation, output limits, and application policy. A tool description is not authority to access every resource. See [Chapter 15](../chapters/15-tools-and-mcp.md).

### 27. When are multiple agents useful?

When independent tasks can benefit from distinct context, parallel execution, or separate authority boundaries. Weigh coordination, repeated context cost, conflicting assumptions, and debugging. A second model is not automatically an independent truth verifier. Start simple and add workers only for a concrete measured need.

### 28. Why separate conversation memory from business state?

History and summaries are context aids and can be incomplete or wrong. Approvals, postings, and job transitions need durable authoritative records. A summary saying “approved” must not permit a transaction if no matching approval exists for the exact action version. See [Chapter 16](../chapters/16-memory-and-state.md).

### 29. How would you handle prompt injection in a document?

Treat its instructions as untrusted content. Restrict exposed tools, minimize data, validate arguments, enforce authorization outside the model, and require defined review for actions. Delimiters and warning prompts can help but are not complete defenses. A read-only document extractor should not have an email or payment tool.

### 30. What makes an n8n workflow production-ready?

Explicit contracts, authenticated triggers, durable job state, atomic deduplication, validated outputs, safe retries, review/reconciliation, protected credentials, controlled execution retention, versioning, and an operator runbook. Node success alone does not establish the business outcome. Queue-mode workers also need downstream quotas and concurrency limits. See [Chapter 17](../chapters/17-n8n-in-production.md).

## Reliability and deployment

### 31. What does a timeout mean for a write?

The caller lacks a complete response; the server may still have committed the action. Mark ambiguous outcomes appropriately and reconcile using a stable destination reference or idempotency key. Blindly repeating the write can duplicate the effect. This is different from a validated rejection that clearly created nothing.

### 32. Why is a local deduplication table insufficient for external exactly-once effects?

The external call can succeed just before the local completion record crashes. Retrying then repeats the external action unless the destination deduplicates or you reconcile first. A local transaction cannot atomically commit an unrelated service's state. State the real guarantees instead of claiming universal exactly-once execution.

### 33. What is the outbox pattern?

Write business state and an event record in the same database transaction. A publisher later forwards the event to a queue. This avoids losing the event between a successful database commit and a failed publish. Publishing can still repeat, so consumers need idempotency. Monitor and recover stuck outbox records.

### 34. How do retries cause outages to grow?

Retries add load to an already failing dependency. Nested policies can multiply attempts, and synchronized clients create bursts. Use an overall deadline, capped attempts, backoff with jitter, appropriate retry guidance, and safe repetition rules. Invalid input and unauthorized requests should not create retry storms.

### 35. What is a circuit breaker?

It temporarily stops ordinary calls to an unhealthy dependency based on a defined failure policy, then allows limited recovery probes. Distinguish dependency failures from request-specific errors. A breaker limits repeated damage; it does not repair the provider or ensure that a fallback meets quality and data-handling requirements.

### 36. What is backpressure?

The system slows, queues within a bound, or rejects new work when capacity is exhausted. Use concurrency limits, queue size/age policies, and tenant fairness. An unlimited queue converts overload into growing delay and storage pressure. Tell users what happened and preserve jobs according to the agreed contract.

### 37. Can you add stage p95 latencies to get request p95?

Not generally. Percentiles are not additive, and stages may have dependent or differently timed slow cases. Trace the end-to-end distribution directly. Use stage measurements to find bottlenecks and approximate budgets, while labeling planning sums as estimates rather than exact percentile calculations.

### 38. What should a release manifest capture?

Application artifact/commit, prompt, exact model/configuration, tool schemas, policy, parser, index/source versions, dependency environment, evaluation report, and rollout/rollback owner. Reverting code may not restore behavior if the model alias or corpus changed. External actions may require compensation rather than a simple rollback.

### 39. Shadow release versus canary?

Shadow runs an eligible copy through the candidate without showing its answer or performing writes. It still costs money and processes data, so approved data handling matters. Canary serves a small real cohort with monitored stop conditions. Both require comparable evaluation and a clear rollback or disable path.

### 40. What makes a fallback acceptable?

It must satisfy the task contract, permissions, approved data terms, and remaining deadline, with evaluated quality. A source-only result or human review may be safer and more useful than an untested second model. Never improve availability by silently sending data to an unapproved provider or weakening access checks.

## Evaluation, security, and economics

### 41. How do you build a useful evaluation set?

Represent real task categories and edge cases, annotate expected behavior and evidence, separate development from held-out testing, and preserve source/configuration versions. Include refusals, conflicts, denied access, and adversarial content. Report important slices and sample sizes rather than only an aggregate score. See [Chapter 18](../chapters/18-evaluation.md).

### 42. How would you use an LLM judge?

Give it an explicit rubric, necessary evidence, and a versioned configuration. Calibrate against independent human labels; inspect false passes, false failures, and slice behavior. A judge can have bias and shared errors with the system it evaluates. Do not let it replace deterministic checks for exact arithmetic or forbidden actions.

### 43. Does zero observed leakage prove security?

No. It establishes that particular tests did not reveal a leak under those conditions. Coverage, correlation, configuration, and unknown attacks limit the inference. Combine architecture controls, negative tests, review, and monitoring. Even statistical bounds require representative independent trials and do not certify an access-control design.

### 44. Authentication versus authorization?

Authentication identifies the principal. Authorization decides what that principal can do with a resource in the current context. A logged-in employee may still be unable to read payroll or another tenant's records. Enforce ownership and policy in trusted code/data systems, not in a prompt. See [Chapter 19](../chapters/19-security-and-access.md).

### 45. What can go wrong with response caching?

An incomplete key can mix tenants, permissions, versions, locales, or prompts. A stale entry can outlive a policy change or access revocation. Define key scope and invalidation, and recheck current access where needed. A TTL limits age but does not by itself solve permission changes or source correctness.

### 46. What should an AI trace contain?

Stage timings, request/job ID, safe error categories, prompt/model/index versions, token usage, and permitted source/artifact references. Include enough to diagnose without defaulting to full sensitive content. Traces complement metrics and logs; they are not the authoritative financial or approval ledger. See [Chapter 21](../chapters/21-observability.md).

### 47. Calculate a simple daily token bill

For 10,000 requests with 2,000 input and 400 output tokens at fictional rates $2 and $8 per million respectively, each request costs $0.0072 and a day costs $72. Add retries, hosting, retrieval, storage, tools, and review separately. Current provider-specific billing rules must be verified before budgeting.

### 48. Why measure cost per accepted task?

Per-token prices ignore failure, retries, and human corrections. Divide the total workflow cost by outcomes accepted under the agreed quality standard. A stronger model can lower that cost if it reduces expensive rework. Segment by task and tenant so a cheap average does not conceal costly document-heavy users.

### 49. When is self-hosting cheaper?

Only a workload-specific total-cost comparison can establish it. Include hardware utilization, memory, redundancy, operations, engineering time, energy/cloud charges, quality, and latency. An idle accelerator can cost more per task than an API. Control, deployment constraints, and licenses may matter independently of cost.

### 50. How do you distinguish capacity released from savings?

Fewer manual minutes create potential capacity. Realized savings require reduced expense or measured beneficial use of that capacity. Include adoption, errors, review, and maintenance. Report modeled value separately from observed cash, throughput, or revenue impact. See [Chapter 23](../chapters/23-cost-and-economics.md).

## Applied judgment and field delivery

### 51. Why should an analytics assistant calculate with SQL?

SQL executes exact defined aggregations over authoritative data, while the model can interpret the question and explain results. Use validated metric definitions and restricted queries. The model must not invent missing dimensions, denominators, or attribution. Check narrative numbers against the result table. See [the analytics case](../case-studies/03-marketing-analytics.md).

### 52. Why is averaging ratios dangerous?

Ratios have different denominators. Spending $100 for one lead and $100 for ten gives daily costs per lead of $100 and $10. Their average is $55, but the combined cost per lead is $200/11, about $18.18. Aggregate numerator and denominator according to the metric contract, then calculate the ratio.

### 53. What does “verified email” mean in a research system?

It must name the actual verification method and date. Syntax, MX records, official publication, confirmation, and delivery history establish different things. An officially published address is not proof of current mailbox deliverability. A guessed naming pattern should remain unconfirmed or absent, with provenance. See [the lead research case](../case-studies/04-lead-research.md).

### 54. Why can denial row count differ from denied claim count?

A claim can have multiple lines, submissions, and events. Define the grain, unique key, date basis, and status rule before counting. Inspect duplicates and source versions instead of assuming one report is wrong. Distinguish counts, amounts, causes, and recoverable value. See [the healthcare operations case](../case-studies/05-healthcare-operations.md).

### 55. What changes when building a voice assistant?

Perception, endpointing, interruption, playback, and critical-entity recognition add failure modes. Evaluate end-to-end task success and latency, not only transcription accuracy. Separate audio state from transaction state: stopping speech does not cancel an already confirmed booking. Include identity checks and a useful escalation path. See [Chapter 24](../chapters/24-voice-and-multimodal.md).

### 56. How would you evaluate a coding assistant?

Use issues with concrete acceptance criteria, relevant tests, hidden checks where useful, and review of scope/security. Inspect actual diffs and test evidence. Measure correctness, regressions, unauthorized tool attempts, review effort, and resource use. A claim that tests passed must correspond to commands that really ran.

### 57. Why can a 99%-accurate fraud classifier be useless?

If only 1% of transactions are fraudulent, predicting “legitimate” for everything gives 99% overall accuracy and zero fraud recall. Evaluate precision/recall, error costs, calibration, and review capacity. Select thresholds using operational consequences, not a default probability or aggregate accuracy. See [Chapter 25](../chapters/25-ml-recommendations-and-ranking.md).

### 58. A customer asks for an AI dashboard. What do you do first?

Map the decision and workflow: user, current task, source data, volume, delays, errors, permissions, and success measure. Investigate a recent difficult case. The right first output might be a reliable data feed or review queue rather than a dashboard. Propose a small measurable vertical slice. See [Chapter 26](../chapters/26-fde-discovery-and-delivery.md).

### 59. What belongs in a customer handoff?

Architecture and data contracts, environment/release record, access model, evaluation results, operational dashboards, alerts, runbook, replay/reconciliation procedure, ownership, support expectations, and known limits. Train the exception owners. The customer should be able to operate and recover the system without relying on the original builder's memory.

### 60. How do you answer an unfamiliar provider-specific question?

State what you know, identify the design principle, and say which current official documentation or experiment would resolve the detail. Record the uncertainty and its consequence. Do not invent an API, pricing rule, capability, or benchmark. Strong engineering judgment includes knowing which claims need verification.

Next: [Practice rubric](rubric.md) · [Full index](../INDEX.md)
