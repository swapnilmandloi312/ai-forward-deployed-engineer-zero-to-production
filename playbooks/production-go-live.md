# Production Go-Live Playbook

## Go-live principle

Production starts when real users, real data, or real side effects enter the system—not when the infrastructure is labeled `prod`.

## Readiness

### Outcome and scope

- [ ] Pilot cohort, eligible cases, exclusions, owner, and decision date documented
- [ ] Success, safety, stop, rollback, and expansion thresholds agreed
- [ ] Baseline and measurement source available

### Data and security

- [ ] Data classification, purpose, retention, deletion, and residency reviewed
- [ ] Service accounts use least privilege; tenant boundaries tested
- [ ] Secrets managed and rotated; sensitive logs redacted
- [ ] Vendor/model data-use terms reviewed by the appropriate owner
- [ ] High-impact actions require approved policy/human control

### Quality and reliability

- [ ] Versioned evaluation suite passes by critical slice
- [ ] Load, timeout, rate-limit, duplicate, and partial-failure tests pass
- [ ] Fallback, degraded mode, queue control, replay, and reconciliation tested
- [ ] Backup restoration and deployment rollback demonstrated

### Operations and adoption

- [ ] Dashboard shows service, AI component, safety, cost, and business outcome signals
- [ ] Alerts route to named responders with useful context
- [ ] Kill switch tested by someone other than the builder
- [ ] Runbook, escalation, support hours, and incident communication agreed
- [ ] Users trained on limitations, corrections, and escalation
- [ ] Accessibility and critical user journeys tested

## Launch sequence

1. Record deployed versions and configuration.
2. Enable internal/synthetic traffic and verify traces.
3. Start the smallest approved canary cohort.
4. Review first outcomes manually and compare to thresholds.
5. Expand only after the scheduled decision; do not let silent traffic growth make the decision.
6. Capture unexpected cases in evaluation and product backlogs.

## Stop immediately when

- unauthorized access or data disclosure is suspected;
- irreversible action escapes its policy/approval boundary;
- critical safety threshold fails;
- outcomes cannot be audited or reconciled;
- rollback/kill switch is unavailable;
- the operator does not understand current system state.
