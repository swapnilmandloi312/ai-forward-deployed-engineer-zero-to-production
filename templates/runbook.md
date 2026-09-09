# Operations Runbook: [System]

**Service owner:**<br>
**Business owner:**<br>
**Support/on-call route:**<br>
**Last tested:** [YYYY-MM-DD]

## Service overview

- User outcome:
- Eligible/excluded work:
- Dependencies:
- Environments and deployed versions:
- Dashboards/logs/traces:
- Data sensitivity and logging restrictions:

## Normal checks

| Check | Expected | Frequency | Action on failure |
|---|---|---|---|
| Outcome volume/success |  |  |  |
| Quality/safety slices |  |  |  |
| Queue/reconciliation |  |  |  |
| Latency/errors |  |  |  |
| Cost/budget |  |  |  |

## Immediate controls

- Kill switch:
- Disable external writes:
- Switch to human queue/read-only:
- Provider/model fallback:
- Roll back release/config:
- Pause intake or queue consumption:

## Failure procedures

### Provider/model failure

Detection → impact check → fallback/hold → reconciliation → recovery verification

### Integration or partial write

Detection → stop duplicate risk → identify uncertain records → reconcile destination → replay safely

### Quality/safety regression

Detection → constrain cohort/action → preserve versions/cases → rollback → run critical evals

### Suspected data/security incident

Stop exposure → preserve evidence → contact security/privacy owner → follow approved incident process. Do not paste sensitive data into tickets or chat.

## Recovery verification

- user journey succeeds;
- external side effects reconcile;
- error/quality/safety signals return within threshold;
- backlog drains at a controlled rate;
- stakeholders receive closure and residual-risk note.

## Known limitations and expiry

| Limitation/workaround | Risk | Owner | Review/expiry |
|---|---|---|---|
|  |  |  |  |
