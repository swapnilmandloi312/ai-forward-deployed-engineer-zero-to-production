# 01 · AI without jargon

**Prerequisites:** none. **Goal:** distinguish the model from the application around it.

## The simple explanation

Artificial intelligence is the broad field of making machines perform tasks associated with intelligence. Machine learning is a family of methods that learns patterns from examples rather than relying entirely on hand-written rules. Deep learning uses neural networks with many layers. A large language model, or LLM, is a model trained on large amounts of data to predict and generate token sequences.

These categories overlap. A fraud classifier, a recommendation system, a speech recognizer, and a chatbot are all AI-related systems, but they do different jobs. Not every business problem needs an LLM.

**Everyday intuition:** the model is the engine; the application is the whole car. A powerful engine still needs brakes, steering, fuel, and a driver who can see the road.

## One running example

A customer asks, “Can I return an item after 20 days?” A plain model may produce a plausible policy from training. A useful support system must identify the store, authenticate the customer when needed, find the current policy, cite it, and avoid inventing exceptions. If a refund action is requested, it must check eligibility and authorization before changing anything.

| Component | Job | Example failure |
|---|---|---|
| Interface | Accept the question and show the result | User loses an answer during a refresh |
| Identity layer | Establish the user and allowed access | Customer sees another company's documents |
| Retrieval/data layer | Find the current evidence | An old return policy is selected |
| Model | Interpret the question and compose a response | It confidently invents a 30-day window |
| Tool executor | Perform permitted actions | The same refund is submitted twice |
| Evaluation/operations | Measure behavior and recover | Wrong answers grow without an alert |

The LLM is one part of this system. Improving only the prompt cannot repair every failure in the other parts.

## Prediction is not verification

A model can be fluent and incorrect. It can also produce an answer that is true in general but unsupported by the documents your application is allowed to use. These are different failures. For a policy assistant, an answer should satisfy both factual correctness and support from the current policy.

Temperature influences sampling behavior; setting it to zero does not make an answer true, safe, or perfectly reproducible across all providers and infrastructure changes. Verification requires external checks, evidence, evaluation, and, for consequential decisions, an appropriate reviewer.

## Choose the smallest useful approach

Use a rule when the condition is explicit: reject an invoice without a currency. Use SQL when the answer is an exact aggregation: total overdue balance by customer. Use conventional ML when a prediction from historical features is needed. Use an LLM when language interpretation, flexible extraction, or generation adds value. Combine them when the task needs several kinds of reasoning.

For example, let an LLM extract invoice fields, validate the total with decimal arithmetic, check vendor identity in a database, and ask a human to approve an external accounting write. This separates language uncertainty from business controls.

## Work it out

For a restaurant booking assistant, list three jobs for deterministic code and two jobs for language understanding. Then explain what happens if the model suggests a time that is unavailable.

**Suggested answer:** code checks availability, enforces party-size limits, and creates the booking with an idempotency key. Language understanding extracts the requested date/time and explains alternatives. The booking API is the source of truth; model output cannot override availability.

**Explain it aloud:** Why can an application using a weaker model sometimes be more reliable than an application using a stronger one?

Next: [Python, APIs, and SQL](02-python-api-sql.md) · [Index](../INDEX.md)
