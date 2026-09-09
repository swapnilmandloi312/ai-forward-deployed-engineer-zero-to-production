# 04 — LLM Systems and Model Routing

## Outcome

Design an LLM component whose model choice, output contract, fallback, cost, and risk are explicit.

## Learn

- Tokens, context windows, sampling, latency, and cost drivers
- Prompt roles, structured outputs, tool calls, and validation
- Task decomposition and deterministic preprocessing/postprocessing
- Model selection by quality, latency, price, privacy, and regional availability
- Provider abstraction, retry policy, fallback, caching, and budget controls
- Versioning prompts, models, tools, and datasets together
- When classification, rules, search, or traditional ML is a better fit

## Build

Create a workflow that classifies an operational item and extracts a typed record. Use at least two model configurations and a deterministic baseline. Reject or route invalid output instead of silently repairing every error.

Track model, prompt version, tokens, latency, estimated cost, validation result, and final disposition. Simulate provider timeout, rate limiting, malformed output, and a budget threshold.

## Decision drill

Write an ADR that chooses a model configuration for the pilot and defines when the routing policy should change. Include data-use constraints and an exit plan for provider dependency.

## Evidence

- Versioned prompt and output schema
- Comparison against deterministic baseline
- Model-routing ADR
- Provider-failure test
- Cost per successfully processed item

## Proof gate

The component never treats unvalidated model text as a trusted command. Provider failure has a visible, bounded outcome. Model selection is supported by task-specific evidence, not leaderboard rank.

## Primary references

- [OpenAI API documentation](https://platform.openai.com/docs/)
- [Anthropic API documentation](https://docs.anthropic.com/)
- [Google AI for Developers](https://ai.google.dev/)
