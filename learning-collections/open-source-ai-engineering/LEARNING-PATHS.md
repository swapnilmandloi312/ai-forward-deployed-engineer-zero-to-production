# Use the catalog to build understanding

These are suggested experiments, not pretested combinations of every current dependency version. Start from the project's official README and keep a record of your actual environment and result.

## 1. Begin with exact data

Study Pydantic, DuckDB, and a small Streamlit or Gradio interface. Use synthetic CSV records and expose a reviewed total or summary. Test invalid records, a missing field, an empty result, and a tenant filter. Keep arithmetic in the database or deterministic code.

**Evidence:** a runnable example, expected outputs, and one deliberately failing input. **FDE lesson:** a useful application may need validation and integration before it needs a model.

## 2. Learn retrieval with a baseline

Compare lexical retrieval with a selected vector-search path. Candidates include pgvector, Qdrant, Chroma, or FAISS; choose one initially. Use a small labeled corpus containing exceptions and unanswerable questions. Add an embedding model only after documenting its license, input format, and actual resource requirements.

**Evidence:** candidate recall, source versions, filtered access cases, and actual timing. **System-design lesson:** changing three components at once makes it difficult to explain which caused an improvement.

## 3. Add a controlled agent

Choose a code-oriented workflow tool such as LangGraph or PydanticAI and a read-only synthetic lookup. Define a maximum number of steps, output schema, timeout, and completion rule. Test malformed tool arguments, no results, and repeated unsuccessful calls.

**Evidence:** traces and verified final state. **System-design lesson:** a model's suggested tool call is a proposal; execution remains an application-controlled decision.

## 4. Build evaluation before a complicated demonstration

Study promptfoo, DeepEval, or Ragas. Start with deterministic checks and independently labeled examples. If a model judge is used, record its provider, cost, rubric, and human calibration. A library cannot decide the correct acceptance criteria for your business task.

**Evidence:** normal/edge/denied-action slices and inspected false passes. **FDE lesson:** a small honest failure report teaches more than a polished unsupported accuracy claim.

## 5. Understand local inference

Start with the official requirements for Ollama or llama.cpp and a model your machine can support. Learn the difference between application license and weight license. Measure memory, context size, output length, and latency. For GPU-serving study, investigate vLLM or SGLang after the local basics are clear.

**Evidence:** hardware, exact model, configuration, and observed results. **Cost lesson:** a local download may avoid one hosted API bill, but it still uses compute and storage.

## 6. Study documents or voice as a separate pipeline

For documents, compare structured extraction on a synthetic table before adding a language model. For voice, use permitted audio and inspect critical names/numbers, interruptions, and total task success. Follow licensing for OCR/voice models and use the project's actual current setup.

**Evidence:** original fixture, output, error taxonomy, and a correction. **System-design lesson:** perception errors can become downstream reasoning errors.

## Keep a compact experiment record

Write the task, selected source/version, setup, exact command, input, actual output, measurements, failure, and next change. Mark anything unrun as a proposed experiment. Publish only permitted synthetic or otherwise shareable material.

Back: [catalog](README.md).
