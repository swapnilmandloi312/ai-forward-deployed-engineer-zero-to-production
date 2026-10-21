# Worked answers

These are original solutions to synthetic exercises. Different designs can be valid when their boundaries, measurements, and assumptions are explicit.

## Drill 01

The problem is currently under-specified. Ask which request type consumes time, how operators establish the cause, which data is available, which actions the operator may take, and what successful resolution means. Agree who handles product defects and how users reach that team.

The north tenant has ten export rows and **eight unique ticket IDs**. Keep the most recent timestamp for each ticket within the tenant. The latest categories are export **5**, access **2**, and billing **1**. Thus export tickets are **5/8 = 62.5%** of unique north tickets. The south row must not affect that summary. A category count identifies volume; it does not prove a common underlying bug.

A small pilot prepares evidence-linked triage cards for human review. It starts with known issue categories and records uncertain cases. Read-only evidence access is enough for this first slice. Changing account state, sending customer messages, and closing tickets are outside that scope. If the evidence points to a product defect, create a reviewable engineering handoff with reproduction details; do not label a speculative cause as confirmed.

Planning arithmetic: the current effort is 40 × 12 = **480 minutes**. Proposed effort is 40 × (6 + 2) = **320 minutes**. The hypothetical difference is **160 minutes, or two hours 40 minutes per week**. Verify representative volume, task quality, complete operator/reviewer time, rework, adoption, and operating costs in a pilot before claiming a saving. Time saved is not automatically revenue or headcount reduction.

Useful tests include a duplicate export row, absent evidence, a false diagnosis, another tenant's ticket, and an unavailable downstream service. A model-generated explanation must agree with the deterministic summary and cite the evidence used.

## Drill 02

The answer used a superseded policy and another tenant's rule. Similarity ranking cannot establish policy authority. Derive tenant and user scope from authenticated context. Filter eligible documents before their text reaches the model, enforce version rules, and preserve the source identity/version in the answer. A backend export action must independently check current permissions.

Expected outcomes:

- **North member:** the current North policy requires an administrator; the member is not authorized under the supplied policy. Cite N-policy-3. Do not expose South policy text.
- **North administrator:** the role meets the described policy condition. The assistant still cannot promise that a specific export will succeed; data scope, runtime permissions, and service state need verification.
- **Missing current North policy:** say the available evidence cannot establish the current permission. Route to the policy owner rather than reuse a superseded or foreign policy.
- **Injected scope override:** ignore the request to alter trusted scope. Server enforcement remains effective regardless of generated instructions.
- **Administrator cache entry:** tenant alone is insufficient. Include an effective authorization scope/version, document/index version, and relevant request context, or do not cache the answer.
- **Permission change:** revalidate at sensitive read/action boundaries. Invalidate stale permission-dependent entries; a long-running model call does not freeze authorization.

Observe document IDs, effective scope decisions, version, and the refusal reason under a suitable retention policy. Investigate model inputs and any cache reuse after a suspected leak. Avoid retaining full document text by default. Retrieval quality, freshness, and authorization each need separate tests.

## Drill 03

Overall correctness is **(68 + 12 + 7) / 100 = 87%**. Segment results are approximately 97.1%, 60%, and 70%. The release decision is **no-go** because the agreed permission gate failed three times. Fix access enforcement and the implicated cache/index paths; a stronger model does not replace backend permission checks.

Preserve a minimal reproduction for each failure, identify the enforcement layer that failed, add regression cases, and rerun both the affected segment and the overall suite. Passing the repaired suite is evidence about those cases, not a guarantee about all future inputs. Keep the restricted pilot and rollback decision with an accountable owner.

Adoption: opened is 9/12 invited = **75%**. Completed is 5/12 invited = **41.7%**, or 5/9 opened = **55.6%**. Returning is 3/12 invited = **25%**. A week-two retention claim needs a defined eligible cohort and comparable observation window; those details are absent. Do not choose a denominator just because it makes the result look stronger.

Measure complete task time including review, corrections, failed attempts, and escalation. Compare representative tasks against the existing workflow. Report cost per completed task alongside quality and abandonment. Median latency alone hides slow experiences; inspect the p95 and stage traces.

An operational handoff names who responds to denied-scope anomalies, provider outages, and stale indexes; how to disable risky features; and how to prove the fallback works. A useful next experiment holds the permission enforcement constant while comparing model quality on the missing-evidence segment. Another investigates whether the interface makes uncertainty and escalation understandable.
