# Start here: learn one system at a time

You do not need a machine learning degree to begin. You need patience, basic Python, and the habit of asking what happens when a component fails. This handbook starts from those foundations and moves toward systems you can explain, test, and operate.

**Everyday intuition:** getting a chatbot to respond is only the beginning. System design also asks where its evidence came from, how correctness is checked, and what happens when an API fails.

## Your first hour

1. Read [what an AI system actually is](chapters/01-ai-without-jargon.md).
2. Read [the Python, API, and SQL bridge](chapters/02-python-api-sql.md). If the code is unfamiliar, spend a few evenings here.
3. Run the local retrieval lab. It uses Python's standard library and synthetic text, so no API key, account, payment, or package installation is required.

```bash
python --version
python -m labs.mini_rag --question "What is the refund window?" --tenant acme
python -m unittest discover -s tests -v
```

Run commands from the handbook folder containing `labs/`. In the parent FDE repository, first run `cd ai-system-design-handbook`. Python 3.11 or newer is the supported baseline. On Windows, use `py` instead of `python` if necessary. On macOS/Linux, `python3` may be the right command. If Git is unfamiliar, use GitHub's **Code → Download ZIP**, extract it, and open a terminal in the extracted folder.

The retrieval lab returns matching source sentences and citations. It deliberately uses lexical search, not an embedding model or a generative LLM. This makes retrieval, access filtering, missing evidence, and evaluation visible before you add paid dependencies.

## How to read a chapter

Use the same cycle every time:

1. **Understand:** read the everyday analogy and concrete example.
2. **Trace:** draw where one request goes and which data crosses each boundary.
3. **Challenge:** ask how the design fails and which metric exposes the failure.
4. **Build:** change a lab or write a small implementation.
5. **Explain:** close the page and teach the idea in two minutes.

Reading without recall feels easier but produces weak interview answers. Writing code without checking its output produces convincing demos that may be wrong. Use both.

## Pick a route

| Your starting point | Route | First useful output |
|---|---|---|
| New to coding | Chapters 1–4; repeat the examples | A script that reads JSON, validates it, and writes a result |
| n8n or automation builder | Chapters 3, 4, 10–13, 17, 20–25 | A workflow with deduplication, review, and an error route |
| Backend/data engineer | Chapters 5–16, then 20–26 | A retrieval system with held-out evaluation |
| Interview in two weeks | [Interview sprint](interview/14-day-sprint.md) | Two timed designs, a trade-off log, and a recorded mock |
| Want structured preparation | [Eight-week plan](ROADMAP.md) | One capstone with tests, evaluation, and an operator runbook |

These are routes through the same material, not separate promises about how fast somebody can become job ready.

## Prerequisite check

Before RAG, be able to explain a Python dictionary, a function, an HTTP request, a SQL `WHERE` clause, and a queue. Before production, be able to explain authentication, authorization, retries, and why repeating a payment request can be dangerous. Before fine-tuning, understand train/validation/test splits and have a baseline to beat.

If any of these are unclear, return to the relevant foundation. There is no penalty for learning the basics carefully.

## What is included and where the boundary is

The handbook covers applied AI system design, core ML concepts, retrieval, agent workflows, adaptation, serving, reliability, security, evaluation, economics, deployment, voice, multimodal systems, and customer delivery. It is not a full Python textbook, a complete deep learning mathematics course, or a certification in a regulated industry.

All case-study numbers are **fictional design assumptions**. All bundled data is synthetic. Labs teach one mechanism at a time; a passing lab is not evidence that a real deployment is secure or compliant. Production gaps are stated next to each lab.

## Your learning notebook

Create a private notebook with four columns: concept, explanation in my words, failed experiment, next change. Keep client documents, credentials, and personal information out of public contributions. Use [the study tracker](templates/study-tracker.md) to record evidence rather than just checked boxes.

Next: [AI without jargon](chapters/01-ai-without-jargon.md) · [Full index](INDEX.md)
