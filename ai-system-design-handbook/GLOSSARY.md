# Plain-English glossary

Use this as a quick lookup, then follow [the chapter index](INDEX.md) for examples. Related terms are distinct on purpose: similarity, confidence, correctness, and authorization answer different questions.

| Term | Meaning |
|---|---|
| Ablation | An experiment removing one component to measure its contribution. |
| Active version | The source/index version selected for current serving. |
| Agent | A system in which a model chooses some next steps or tools within application controls. |
| API | A defined interface through which software requests another system's capability. |
| Approximate nearest neighbor | Search that trades some exact ranking recall for speed or scale. |
| Attention | A numerical mechanism that weights information from different positions. |
| Attribution window | The time rule assigning an outcome to an earlier interaction. |
| Authentication | Establishing who a principal is. |
| Authorization | Deciding which actions/resources that principal may access. |
| Backoff | Increasing delay between retry attempts. |
| Backpressure | Slowing or rejecting new work when capacity is constrained. |
| Barge-in | Allowing a voice user to interrupt system playback. |
| Baseline | A reference approach against which improvements are compared. |
| Batch | A group of items processed together, often trading delay for throughput. |
| BM25 | A lexical relevance method using term occurrence, rarity, and length normalization. |
| Bulkhead | A resource boundary that prevents one workload from exhausting another's capacity. |
| Calibration | Agreement between estimated probabilities/scores and observed outcomes under a defined setting. |
| Canary | A limited real-user rollout used to assess a candidate before expansion. |
| Candidate generation | Quickly selecting a manageable set before detailed ranking. |
| Cardinality | The number of distinct values; excessive metric-label cardinality can be costly. |
| Chunk | A source segment used as a retrieval unit. |
| Circuit breaker | A control that temporarily limits calls to an unhealthy dependency and tests recovery. |
| Citation support | Whether the cited evidence actually supports the associated claim. |
| Cold start | A new user/item/system has little history available for prediction or ranking. |
| Compensation | A permitted follow-up action that addresses an earlier external effect. |
| Concurrency | The number of operations in progress at the same time. |
| Context engineering | Choosing and assembling instructions, evidence, tools, history, and state for a request. |
| Context window | The model-specific budget for content processed in an interaction. |
| Cosine similarity | A comparison of vector direction; not a correctness probability. |
| Cost per accepted task | Total workflow cost divided by outcomes meeting the acceptance standard. |
| Cross-encoder | A model that jointly scores a query and candidate, often used for reranking. |
| Data lineage | The record connecting derived data to sources and transformations. |
| Decode | The generation phase that produces new tokens. |
| Deduplication | Identifying repeated records/events; it must match the intended business identity. |
| Denominator | The quantity below a fraction; its definition matters when aggregating ratios. |
| Dense retrieval | Finding items using learned dense vector representations. |
| Distillation | Training a student using a teacher or other learning signals. |
| DPO | A preference-optimization method using preferred/dispreferred examples. |
| Drift | A change in data or behavior relative to the evaluated setting. |
| Durable execution | Resuming work from persisted state across failures/restarts. |
| Embedding | A numerical representation learned to capture relationships useful for a task. |
| Endpointing | Deciding that a speaker's turn has ended. |
| Error budget | Allowed unreliability under a stated service objective and window. |
| Evaluation slice | A labeled subset such as language, document type, or denied-access requests. |
| Evidence grounding | Connecting an answer's claims to the permitted supplied evidence. |
| Exact search | Comparing all eligible candidates rather than using an approximate index. |
| Fallback | A defined alternative path when the primary path cannot complete. |
| Feature | An input variable used by a predictive model. |
| Few-shot example | An example placed in the request to demonstrate desired behavior. |
| Fine-tuning | Updating model parameters with additional training. |
| Freshness | How current the served data is relative to the source. |
| Golden set | A curated evaluation set with trusted labels/rubrics; not automatically comprehensive. |
| Grain | What one row represents, such as a claim event or campaign/day. |
| GraphRAG | Retrieval involving graph relationships, often alongside text evidence. |
| Guardrail | A control intended to constrain behavior; its guarantees depend on implementation. |
| Hallucination | Generated content that is false or unsupported under the task's definition. |
| Held-out set | Evaluation examples kept separate from development choices. |
| HNSW | A graph-based approximate nearest-neighbor indexing approach. |
| Hybrid search | Combining retrieval signals such as keyword and dense similarity. |
| Idempotency | Repeating a logical operation preserves the intended single business effect. |
| Inference | Running a trained model to produce an output. |
| Inter-token latency | Time between generated tokens during output. |
| IVFFlat | An approximate vector index using partitioned lists and uncompressed vector comparisons. |
| Jitter | Randomized retry timing that reduces synchronized bursts. |
| Judge | A human or model scoring output under a rubric. |
| KV cache | Stored key/value attention information used during generation. |
| Latency | Time taken for an operation; specify the start/end and distribution. |
| Leakage | Evaluation contamination or unauthorized data exposure, depending on context. |
| Lexical search | Retrieval based on words/terms rather than learned dense similarity alone. |
| Little's Law | In steady state, average in-flight work equals average arrival rate times mean time in the system. |
| LoRA | Low-rank parameter updates used for efficient adaptation. |
| MCP | A protocol for interactions with servers exposing tools, resources, and prompts. |
| Metadata | Descriptive fields such as source version, tenant, page, and access groups. |
| MRR | Ranking metric based on the reciprocal rank of the first relevant result. |
| Multi-tenancy | Multiple customers share infrastructure with explicit isolation requirements. |
| nDCG | Ranking metric rewarding highly relevant results near the top. |
| OCR | Converting visible text in images into machine-readable text. |
| Outbox | A durable event record committed with business state, then published separately. |
| Overfitting | Strong performance on familiar data with weak generalization. |
| p95 | A value at or below which about 95% of observed measurements fall. |
| Parameter | A learned model value, distinct from a runtime input argument. |
| Precision | The fraction of selected/predicted positives that are relevant/correct under a label definition. |
| Prefill | Processing the input context before subsequent token generation. |
| Prompt injection | Untrusted content attempts to redirect system instructions or authority. |
| Provenance | Evidence about where information came from and when/how it was obtained. |
| QLoRA | Adapter training using a quantized base model in the training approach. |
| Quantization | Using lower-precision representations to reduce some storage/compute needs. |
| RAG | Retrieval-augmented generation: supplying retrieved material to a generative model. |
| Rate limit | A restriction on request, token, or other usage over time. |
| Recall | The fraction of relevant/positive items successfully found. |
| Reconciliation | Checking authoritative external state to resolve mismatches or unknown outcomes. |
| Reranking | Applying a more detailed scorer to an existing candidate set. |
| RRF | Reciprocal rank fusion, combining ordered result lists using reciprocal rank contributions. |
| RLHF | A family of training approaches using human feedback, commonly with reinforcement learning stages. |
| Row-level security | Database policies limiting which rows a role can access under configured conditions. |
| Semantic validity | Whether structured output means the right thing, beyond syntax and types. |
| SFT | Supervised fine-tuning on example inputs and desired outputs. |
| Shadow traffic | Candidate processing without serving its output or allowing its external writes. |
| SLI | A measured service-level indicator. |
| SLO | A target for an indicator over a stated window. |
| Span | One timed operation within a distributed trace. |
| Speculative decoding | Generating token proposals and verifying them with a target model. |
| Tenant | A customer or organizational scope in a shared service. |
| Throughput | Work completed per unit time. |
| Time to first token | Delay before the first generated token appears. |
| Token | A tokenizer-specific unit of model input/output. |
| Trace | A connected record of operations for a request or job. |
| Train/serve skew | A mismatch between training-time and production feature computation. |
| Transaction | A group of database changes committed or rolled back as a unit. |
| TTL | Time to live: an expiry duration, not a complete invalidation/authorization policy. |
| Vector index | A structure supporting efficient vector similarity search. |
| Vertical slice | A small end-to-end implementation spanning the real request path. |
| VAD | Voice activity detection: estimating when speech is present. |
| Watermark | A recorded progress point for incremental ingestion. |
| Workflow | An application-defined route through processing steps. |

Back: [Index](INDEX.md)
