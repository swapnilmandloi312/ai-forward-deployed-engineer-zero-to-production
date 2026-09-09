# 05 — Context Engineering and RAG

## Outcome

Build a retrieval system that finds authorized evidence, distinguishes retrieval from generation quality, and produces traceable answers.

## Learn

- Corpus selection, parsing, normalization, metadata, and document lifecycle
- Chunking by semantic and operational boundaries
- Sparse, dense, and hybrid retrieval; filters and reranking
- Query transformation, context packing, citations, and abstention
- Access control before retrieval and after response generation
- Retrieval metrics: hit rate, recall, precision, rank, and coverage
- Answer metrics: faithfulness, completeness, correctness, and usefulness

## Build

Create a small enterprise knowledge assistant over 30–100 synthetic policy or operations documents. Build a question set containing answerable, unanswerable, ambiguous, stale, access-restricted, and conflicting cases.

Evaluate retrieval independently: confirm whether supporting evidence appears in the top results before judging the answer. Require citations that map to source identifiers and versions. Refuse or escalate when evidence is insufficient.

## Decision drill

Compare long-context prompting, search without generation, and RAG. Include corpus size, freshness, access control, explainability, latency, and maintenance cost.

## Evidence

- Corpus/data sheet and update process
- Versioned retrieval test set
- Retrieval and answer scorecard
- Access-control tests
- Failure examples and tuning log

## Proof gate

Restricted documents never appear in unauthorized retrieval. Unanswerable questions do not receive confident fabricated answers. A citation resolves to the exact source version used during generation.

## Primary references

- [OpenAI retrieval guide](https://platform.openai.com/docs/guides/retrieval)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
