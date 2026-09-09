# AI Incident Response Playbook

## Incident types

AI incidents may involve availability, incorrect output, unsafe action, privacy/security, runaway cost, model/provider drift, retrieval corruption, or systematic user harm. Treat outcome degradation as an incident even when every service returns HTTP 200.

## First 15 minutes

1. Name an incident lead and communication owner.
2. State user/business impact, affected cohort, first-known time, and confidence.
3. Stop or constrain harmful side effects using kill switch, approvals, rate limits, or cohort disablement.
4. Preserve versions, traces, policy decisions, and relevant evidence without copying sensitive data into chat or tickets.
5. Choose safe degraded mode: deterministic fallback, read-only, human queue, previous version, or full stop.
6. Notify the required security/privacy/customer owner for suspected disclosure or regulated impact.

## Triage by layer

| Layer | Checks |
|---|---|
| Input/data | Schema, freshness, distribution, permissions, corrupted source |
| Retrieval | Index version, filters, access control, recall, stale evidence |
| Model/prompt | Model alias, provider change, prompt version, structured output |
| Tools/workflow | Permission, timeout, duplicate action, state transition, queue |
| Policy | Rule version, missing approval, threshold, exception |
| Infrastructure | Capacity, dependency, secret, network, deployment |
| Product | Misleading UI, hidden review work, misunderstood limitation |

## Communication cadence

Each update should contain: impact, current mitigation, evidence/confidence, next action, owner, and next update time. Avoid claiming root cause before evidence supports it.

## Recovery

- Reproduce the failure on sanitized input.
- Add a regression case before applying the final fix when practical.
- Re-run critical safety and outcome slices.
- Reconcile external side effects and uncertain states.
- Restore gradually through a canary and verify user outcomes.
- Communicate residual risk and any manual follow-up.

## Review

Within the agreed window, document timeline, impact, contributing conditions, detection gap, mitigation, root cause, and actions. Assign each action an owner and date. Prefer system changes over “be more careful.”
