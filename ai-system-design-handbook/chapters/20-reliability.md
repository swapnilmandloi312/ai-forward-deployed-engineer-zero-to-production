# 20 · Reliability, fallback, and graceful failure

**Prerequisites:** Chapters 4 and 18. **Goal:** keep failures bounded and recoverable.

## Availability is not usefulness

A service returning HTTP 200 with an unsupported answer is available at the transport layer and failing at the task layer. Track infrastructure availability and accepted task completion separately. A reliable AI system also knows when to abstain or hand work to a person.

**Everyday intuition:** a help desk that always answers the phone but gives incorrect instructions is not providing reliable help.

Define service-level indicators such as successful authorized task completion, p95 latency, queue age, and invalid-output rate. A service-level objective is a target for an indicator over a stated window. The error budget expresses allowed unreliability under that objective; it is not permission to ignore severe incidents.

## Time and attempt budgets

Apply a total request deadline. Allocate smaller budgets to retrieval, model calls, validation, and fallback. When the deadline is nearly exhausted, do not start an expensive second provider call that cannot finish usefully.

Retries help transient problems but amplify load during an outage. Use backoff and jitter, honor provider retry guidance, cap attempts, and avoid nested retry multiplication. For writes, require safe repetition or reconcile before retrying.

## Circuit breakers and bulkheads

A circuit breaker stops sending normal traffic to a dependency after a configured failure pattern. After a cooldown, limited probes test recovery. It should distinguish request-specific failures from dependency-wide problems. One invalid user input should not necessarily trip a global breaker.

Bulkheads isolate resource pools. A large batch extraction job should not consume all capacity reserved for interactive support. Use separate queues or concurrency budgets for task classes and tenants. Fairness prevents one noisy tenant from starving others.

## A fallback ladder

1. Retry a safe transient failure within budget.
2. Use an evaluated, approved alternative model or service.
3. Return a reduced feature, such as current source snippets without generated interpretation.
4. Persist a background job or route to a reviewer.
5. State the limitation and preserve the user's work.

Each step needs explicit eligibility. A stale cached answer may be acceptable for a general help page and unacceptable for a current account balance. Never weaken access controls to improve completion rate.

## Idempotency and recovery

Distinguish retries from reprocessing. A retry repeats the same operation after a failure. Reprocessing may use a new parser, prompt, or business rule and should create a new version with clear lineage. Reusing an old idempotency key with a changed payload should be rejected, not silently treated as the earlier operation.

Dead-letter or review queues need an owner, an investigation interface, and a replay policy. A queue that permanently hides failed jobs is deferred data loss. Record safe reasons and the last known state.

## Practice and answer

**Question:** the primary model times out after 2.8 seconds in a three-second request budget. Should a two-second fallback begin?

**Answer:** ordinarily no. Respect the remaining deadline and return the documented reduced response or persist follow-up work. Starting calls that cannot meet the deadline wastes capacity and makes overload worse.

Build: [gateway simulation](../labs/README.md). Template: [incident runbook](../templates/incident-runbook.md).

Next: [Observability](21-observability.md) · [Index](../INDEX.md)
