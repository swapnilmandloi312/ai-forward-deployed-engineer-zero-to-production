# 11 · Embeddings, similarity, and chunking

**Prerequisites:** Chapters 5 and 10. **Goal:** understand what a vector search actually compares.

## An embedding is a numerical representation

An embedding model turns content into a vector: an ordered list of numbers. Training encourages vectors to capture useful relationships for particular tasks. Related meaning may be close in that space, but closeness is not truth, permission, or a calibrated confidence score.

**Everyday intuition:** a map puts nearby places close together. It does not tell you whether a building is open or whether you are allowed inside.

For vectors `a` and `b`, cosine similarity is `dot(a,b) / (norm(a) × norm(b))`, provided both norms are nonzero. Dot product and Euclidean distance are other common comparisons. The selected embedding model and index must agree on representation and distance conventions.

## A tiny numerical example

Let `a = [1,0]`, `b = [0.8,0.6]`, and `c = [0,1]`. Each has norm one. Cosine similarity between `a` and `b` is 0.8; between `a` and `c` it is 0. This shows a geometric ranking, not an 80% probability that `b` answers a question correctly.

Real embeddings have many more dimensions and less interpretable individual coordinates. Do not treat a coordinate as a universal feature such as “medical relevance.”

## Why chunking matters

An entire handbook may be too broad for one vector. A single sentence may omit a necessary exception. Chunking divides a source into retrieval units while preserving enough context to answer useful questions.

| Strategy | Useful when | Failure to test |
|---|---|---|
| Fixed token windows | Documents have weak structure | A rule and its exception get separated |
| Heading/section chunks | Documents have meaningful sections | Oversized sections or inherited headings |
| Sentence-aware chunks | Prose needs readable boundaries | Critical references point outside the chunk |
| Table/record chunks | Relationships are structured | Header context or units disappear |
| Parent-child retrieval | Small units match, larger context explains | Parent text overwhelms the context budget |

Overlap can preserve boundary context but creates duplicate content and storage. A 20% overlap is an experiment setting, not a universal best practice. Tune chunk size, overlap, and metadata on retrieval evaluation rather than copying a popular number.

## Keep the evidence attached

Every chunk should retain a stable ID, document version, page/section, tenant/access information, and source relationship. Put explanatory titles or table headers into the indexed text when useful, but distinguish source text from generated contextual additions. Otherwise a generated summary may accidentally become a fabricated citation.

If the embedding model changes, re-embed the corpus or maintain explicitly separated versions. Matching vector dimensionality is not enough to make two embedding spaces compatible. Test a new index in parallel and switch only after quality and access checks pass.

## Storage sizing

For one million vectors of 1,536 dimensions stored as float32, raw vector values use `1,000,000 × 1,536 × 4 = 6,144,000,000 bytes`, approximately 6.14 GB in decimal units. Text, metadata, indexes, replicas, and operational headroom add more. Do not quote raw vector size as total database size.

## Practice and answer

**Question:** increasing chunk size improves recall but answers get worse. How can both be true?

**Answer:** the larger unit may contain the relevant sentence but also more distracting text. Retrieval recall, evidence precision, and answer quality are separate measurements. Try more precise matching plus controlled parent expansion, then evaluate again.

Next: [Search and reranking](12-search-and-reranking.md) · [Index](../INDEX.md)
