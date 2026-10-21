# A fourteen-day interview sprint

Use this when you already have basic programming experience. It is revision and practice, not a substitute for learning foundations. Spend about an hour on recall and an hour on design/build practice where your schedule allows.

| Day | Read/practice | Required output |
|---:|---|---|
| 1 | [Answer framework](answer-framework.md), requirements, capacity | Scope and size a fictional support assistant |
| 2 | Tokens, transformers, selection; questions 1–10 | Explain prefill/KV cache and justify a model experiment |
| 3 | Ingestion, embeddings, chunks; questions 11–15 | Design versioned source/chunk records |
| 4 | Search and RAG; questions 16–20 | Run the retrieval lab and diagnose a paraphrase miss |
| 5 | Prompt/context and structured output; questions 21–22 | Validate an extracted field against evidence |
| 6 | Agents/tools/memory; questions 23–30 | Draw a bounded action loop and approval boundary |
| 7 | Timed [support case](../case-studies/01-support-assistant.md) | Score it before reading the solution |
| 8 | Distributed/reliability; questions 31–40 | Explain duplicate writes, outbox, deadlines, and fallback |
| 9 | Evaluation/security; questions 41–46 | Dataset slices and a trust-boundary diagram |
| 10 | Cost/analytics; questions 47–52 | Reproduce token costs and weighted ratio calculations |
| 11 | Field/voice/ML; questions 53–60 | Give three examples of limitations you would verify |
| 12 | Timed [invoice case](../case-studies/02-invoice-operations.md) | Explicit unknown-outcome reconciliation and reviewer flow |
| 13 | Portfolio demo plus difficult questions | Ten-minute demo with a deliberate failure |
| 14 | Repeat the weakest case without notes | Compare rubric scores and write the next learning priority |

After each session, write one statement you previously believed and now explain more precisely. Example: replace “RAG prevents hallucinations” with “RAG supplies evidence, while retrieval, context assembly, generation, and claim support need separate evaluation.”

Back: [Interview home](README.md)
