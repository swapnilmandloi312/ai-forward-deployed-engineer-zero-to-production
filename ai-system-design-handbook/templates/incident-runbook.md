# Incident and recovery runbook

**Service / primary owner / backup owner:**
**Last drill date and result:**

## Detect and scope

Which alert fires? Identify affected tenants, tasks, source/model/configuration versions, first observed time, and whether data or external actions may be affected. Use safe request/job IDs and controlled evidence.

## Contain

Define how to pause writes, restrict traffic, disable a model path, or fall back to a reduced feature. Do not weaken authorization. Preserve source state and logs under the retention/access policy.

## Diagnose

Check dependency health, recent releases, source freshness, queue age, token/cost changes, permission state, and validation failures. Distinguish confirmed failure from unknown external outcomes.

## Recover

State the approved rollback, restore, replay, reconciliation, and compensation procedures. Identify which operations are safe to repeat and which require destination lookup or manual review. Assign dead-letter ownership.

## Verify

Run a normal request, denied request, missing-data case, and affected failure case. Confirm backlog/reconciliation state and end-to-end indicators before expanding traffic.

## Communicate and learn

Prepare a factual status update with impact, known/unknown scope, mitigation, owner, and next update. Follow the organization's communication authorization process. Record the timeline, root/contributing causes, corrective actions, regression cases, and responsible owners.
