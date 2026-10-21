# 12 · Keyword search, vector search, and reranking

**Prerequisites:** Chapter 11. **Goal:** build a retrieval strategy that survives real questions.

## Different searches capture different signals

Keyword search rewards lexical matches. BM25 is a common method that incorporates term frequency, rarity, and document length normalization. Dense vector search uses embedding similarity. A product code such as `ERR-4097` may favor lexical search, while “How do I get my money back?” may match a refund policy better with semantic representations.

**Everyday intuition:** sometimes you know a book's exact title; sometimes you only know what it is about. A good catalog supports both.

## Exact and approximate vector search

Exact search compares against every eligible vector. Approximate nearest-neighbor methods such as HNSW and IVFFlat trade some recall for speed and scale. Their behavior depends on index parameters, distribution, filtering, and database support. Measure recall and latency on your corpus.

Authorization is mandatory regardless of the index. Define the eligible document set before evidence reaches the model or user. Some index implementations apply filters in ways that reduce the returned candidate count or recall. Test selective tenants/groups specifically; do not patch the issue by revealing globally retrieved snippets.

## Hybrid search

Run lexical and vector retrieval over allowed content, then combine candidates. Raw scores from two different search methods are not necessarily on comparable scales. A common alternative is reciprocal rank fusion:

`RRF(document) = Σ 1 / (k + rank_in_each_list)`

Here `k` is a chosen constant, not the number of returned results. A document absent from a list contributes nothing for that list. RRF combines rankings; it is not a probability of correctness.

Suppose one document ranks first in keyword search and fifth in vector search, while another ranks fifth and first. With equal weighting they tie under this simplified scheme. To favor a query type, evaluate explicit weights or a query router; do not assume fusion solves every relevance problem.

## Reranking

The first retrieval stage returns candidates quickly. A reranker more carefully scores query-document pairs, often using a cross-encoder or another model. This can improve the order of a small candidate set but adds latency and cost. It cannot recover a relevant document that the candidate stage never retrieved.

Try a pipeline such as 30 lexical candidates plus 30 vector candidates, deduplicate, rerank the union, then include five useful passages. Those counts are illustrative tuning parameters. Avoid filling the context with five nearly identical chunks from the same page.

## Retrieval metrics

| Metric | Question answered | Caveat |
|---|---|---|
| Recall@k | How much labeled relevant evidence was found in the first k results? | Needs a useful relevance set |
| Precision@k | What fraction of the first k results is relevant? | Penalizes extra results but ignores later ranks |
| MRR | How early is the first relevant result? | Ignores additional relevant evidence |
| nDCG@k | Are highly relevant results ordered early? | Needs graded relevance judgments |

Segment by exact IDs, paraphrases, long questions, languages, stale policies, and permission filters. Measure the effect of empty or unanswerable queries too.

## Practice and answer

**Scenario:** a reranker is accurate on supplied candidates, but the application misses many answers.

**Answer:** inspect candidate recall before modifying the reranker. Possible causes include missing ingestion, unsuitable chunks, embedding mismatch, aggressive filters, or lexical mismatches. Validate one known question all the way from source file to candidate list.

Further reading: [pgvector documentation](https://github.com/pgvector/pgvector), [RRF paper](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf).

Next: [Production RAG](13-production-rag.md) · [Index](../INDEX.md)
