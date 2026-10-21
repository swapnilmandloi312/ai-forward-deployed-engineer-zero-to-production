# A practical 40-minute design framework

The goal is to make decisions visible. Explain why the design fits the requirements, where it can fail, and how you would know whether it works. Avoid filling the board with every technology you recognize.

## Minutes 0–5: clarify the job

Identify the user, requested outcome, current process, allowed data, and allowed actions. Ask for volume, latency, quality, freshness, cost, and security requirements. State assumptions if information is unavailable. Choose a narrow first scope.

Example: “I will design a read-only employee policy assistant with citations. Refund execution is outside this first version. I assume identity and document access groups are available.”

## Minutes 5–10: estimate and define contracts

Estimate active-period request rate, peak factor, tokens, concurrency, and source volume. Label assumptions and use units. Sketch the main API response and the document/job records. Define what happens when no answer is supported.

Example: “At two requests/second and a four-second mean duration, we expect roughly eight in-flight requests under steady peak load, before measured headroom. Token quotas may bind earlier than request quotas.”

## Minutes 10–20: trace one request

Draw ingestion separately from serving. Walk from user identity to access checks, evidence retrieval, context, model, validation, and final output. Name the source of truth for each important fact or action. Keep the diagram small enough to explain.

For an action workflow, show approval, idempotency, durable state, and reconciliation. For an analytics system, keep exact calculations in SQL or tested code. For voice, include interruptions and the separation between spoken output and transaction state.

## Minutes 20–30: examine the hard boundary

Choose the two or three hardest constraints instead of discussing every component equally. Examples: selective permission filters, duplicate external writes, rapidly changing documents, unsupported claims, token quotas, or tool-loop termination.

Compare alternatives using the requirements. “I choose hybrid retrieval because our dataset mixes exact product codes and paraphrased questions; I will verify it beats lexical search on held-out examples.” This is stronger than calling hybrid retrieval universally best.

## Minutes 30–36: evaluation and operations

Define the evaluation set and slices, critical release gates, latency/cost indicators, alerts, and rollback. Include an unanswerable case, a denied-access case, and a dependency failure. Name who owns review and dead-letter work.

Explain what evidence would make you change the architecture. For example, low candidate recall may justify different chunking, while high recall and weak answers suggest context or generation problems.

## Minutes 36–40: summarize the decisions

Restate the user outcome, primary design, strongest controls, major trade-off, and first pilot milestone. Identify the largest remaining uncertainty and the experiment that resolves it. Do not claim measured performance for an unbuilt design.

## If you get stuck

Return to one concrete input and trace its expected output. Separate unknown requirements from unknown implementation details. It is reasonable to say you would verify a provider-specific feature in current documentation. It is less reasonable to invent that feature or dodge a fundamental authorization question.

Practice: [support case](../case-studies/01-support-assistant.md) · [Rubric](rubric.md)
