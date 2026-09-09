# 09 — Observability and AI Operations

## Outcome

Operate the system using service and outcome signals, detect seeded failures, and recover through a tested runbook.

## Learn

- Logs, metrics, traces, events, correlation IDs, and trace context
- Service level indicators, objectives, error budgets, and user journeys
- AI-specific telemetry: model, prompt, retrieval, tool, token, cost, and safety events
- Alert quality, symptom-based alerts, dashboards, and escalation
- Incident command, mitigation, communication, and blameless review
- Rollback, provider fallback, queue control, replay, and degraded modes
- Observability data as sensitive data

## Build

Instrument the complete project path from trigger to business outcome. Capture versions and timing for orchestration, retrieval, model, and tools without storing sensitive payloads.

Seed three failures: provider latency, tool errors, and quality regression. Confirm that each is detected through a useful signal, triaged to the failing component, and mitigated with the runbook. Write a short post-incident review and convert the lesson into a test or control.

## Evidence

- Service and outcome dashboard
- SLI/SLO definitions and alert routes
- Distributed trace for one successful and one failed outcome
- [Operations runbook](../templates/runbook.md)
- Incident timeline and follow-up action

## Proof gate

An operator who did not build the system can identify impact, stop harmful actions, choose a mitigation, and verify recovery. Alerts describe user or business impact rather than raw infrastructure noise alone.

## Primary references

- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- [Google SRE books](https://sre.google/books/)
