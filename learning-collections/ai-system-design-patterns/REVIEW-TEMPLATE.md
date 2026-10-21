# Architecture review template

## Task and constraints

- User outcome and workflow:
- Trusted identity and allowed scope:
- Quality, deadline, and budget requirements:
- Data freshness and retention needs:
- Explicit non-goals:

## Proposed design

- Data path and control path:
- Invariant and enforcement point:
- State, source versions, cache keys, and invalidation:
- Review boundary and execution-time checks:
- Dependencies and allowed fallback routes:
- Rejected alternative and reason:

## Failure table

| Trigger | Expected behavior | Durable state | User-visible result | Verification |
|---|---|---|---|---|
| Missing evidence | Fill in | Fill in | Fill in | Not run |
| Denied scope | Fill in | Fill in | Fill in | Not run |
| Timeout after possible write | Fill in | Fill in | Fill in | Not run |
| Duplicate job | Fill in | Fill in | Fill in | Not run |
| Stale approval or source | Fill in | Fill in | Fill in | Not run |

## Release and operation

- Evaluation segments and hard gates:
- Observed results and sample sizes:
- Logging fields and excluded payloads:
- Alert owner and recovery steps:
- Rollback and verification of fallback:
- Open assumptions and next experiment:
