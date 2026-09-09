# 06 — Agents and Workflow Automation

## Outcome

Build a bounded workflow that uses tools safely, records every decision, and recovers from partial failure.

## Learn

- Deterministic workflows versus model-directed loops
- Tool schemas, permissions, state, memory, and context boundaries
- Plan-act-observe patterns and explicit termination conditions
- Human approval, escalation, compensation, and kill switches
- Idempotent side effects, replay, concurrency, and duplicate events
- n8n, graph-based orchestration, queues, and code-native state machines
- Autonomy as a risk budget, not a product feature

## Build

Create an operations agent that reads a work item, retrieves context, proposes a decision, and can call three tools: one read-only, one reversible write, and one high-impact action. The high-impact action must require policy evaluation and human approval.

Add limits for steps, wall-clock time, tokens, cost, and repeated tool calls. Persist state transitions and tool results. Inject a timeout after the first write, resume the workflow, and prove the side effect does not duplicate.

## Decision drill

Implement the same happy path as a deterministic workflow and as an agent. Compare flexibility, predictability, observability, evaluation burden, and operator confidence.

## Evidence

- State diagram and tool-permission matrix
- Termination and budget policies
- Approval and escalation record
- Replay/partial-failure test
- Agent-versus-workflow ADR

## Proof gate

The system cannot call an unregistered tool, exceed its hard budget, or perform the high-impact action without explicit approval. Every external side effect has an audit record and a recovery path.

## Primary references

- [n8n advanced AI documentation](https://docs.n8n.io/advanced-ai/)
- [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
