# 09 · Serving, latency, and inference optimization

**Prerequisites:** Chapters 3, 5, and 6. **Goal:** understand where speed and memory go before optimizing them.

## Measure the complete request

Time to first token measures when generated output starts. Inter-token latency measures pacing during generation. End-to-end latency measures when the complete usable result arrives. A system can feel responsive while still taking too long to finish.

**Everyday intuition:** the waiter acknowledging your order quickly is different from the kitchen delivering the meal quickly.

Break down authentication, queue waiting, retrieval, model prefill, model decode, validation, and tool execution. If queue waiting dominates, rewriting the prompt may barely help. If output generation dominates, a shorter justified answer may help more than adding servers.

## Memory and capacity

Model weights occupy memory. A rough lower-bound estimate for raw weight storage is `parameter_count × bits_per_weight / 8`. A 7-billion-parameter model at 16 bits uses roughly 14 billion bytes just for weights. Runtime buffers, activations, KV cache, quantization metadata, framework overhead, and other processes require additional memory.

The KV cache grows with sequence count and sequence length. Long requests can crowd out concurrent short requests. Monitor memory and real throughput on your model, hardware, and serving engine. A model that fits alone may still fail under concurrent traffic.

## Optimization choices

| Technique | Mechanism | Cost or risk |
|---|---|---|
| Shorter context | Remove irrelevant or duplicated input | Removing essential evidence harms quality |
| Shorter output | Ask for a concise useful result | Important qualifications can disappear |
| Quantization | Store/compute with lower-precision representations | Quality and hardware support vary |
| Continuous batching | Schedule active sequences together | Scheduling and tail latency become important |
| Prefix/KV reuse | Reuse eligible prompt computation | Depends on exact prefixes, support, isolation, and eviction |
| Speculative decoding | Propose tokens and verify against a target model | Benefit depends on acceptance and workload |
| Parallel independent calls | Overlap unrelated I/O | Can increase spend and burst pressure |

Paged KV-cache management reduces fragmentation in serving systems that support it. It does not eliminate the underlying memory required by active sequences. Similarly, batching improves throughput under some workloads but can make a lightly loaded interactive request wait longer.

## Response caching versus prompt caching

Response caching reuses a prior answer. Prompt/prefix caching reuses eligible computation or billing treatment for repeated input. They are different mechanisms. Neither should bypass authorization or return a stale policy answer after a revocation.

For an answer cache, include tenant and permission-relevant scope, document version, prompt/model version, normalized request, and other output-changing inputs. Determine invalidation explicitly. For provider prompt caching, verify current rules instead of assuming every repeated token is eligible.

## A practical optimization sequence

1. Fix waste: duplicate retrieval, unnecessarily large tool schemas, unlimited histories, and verbose outputs.
2. Measure with realistic concurrent traffic, including long documents and failure cases.
3. Evaluate a smaller model or a different serving configuration.
4. Apply batching/caching only where correctness and latency requirements allow it.
5. Re-run quality and security checks after every optimization.

Track cost and latency distributions by task type. A single mean hides the occasional huge input that monopolizes capacity.

## Practice and answer

**Question:** A local model fits in GPU memory at startup but fails when several users connect. Why?

**Answer:** the initial fit may account mainly for weights. Concurrent sequences add KV-cache and runtime memory. Restrict in-flight work and context/output budgets, measure peak memory, and select an appropriate serving configuration before increasing traffic.

Further reading: [vLLM documentation](https://docs.vllm.ai/), [PagedAttention paper](https://arxiv.org/abs/2309.06180).

Next: [Document ingestion](10-document-ingestion.md) · [Index](../INDEX.md)
