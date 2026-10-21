# 26 · FDE discovery, delivery, and customer trust

**Prerequisites:** Chapters 3, 18, and 23. **Goal:** connect technical design to a real operational outcome.

## Begin with the work, not the requested tool

A customer says, “We need an AI dashboard.” Ask who uses it, which decision it supports, what happens today, where time is lost, and what evidence would justify changing the process. A dashboard may be useful; a missing data integration or review queue may be the more urgent problem.

**Everyday intuition:** if someone asks for a faster printer, first check whether printing is the step causing the delay.

Map the process with the people doing it. Identify source systems, manual handoffs, exception types, data owners, security constraints, and the person accountable for the final decision. Separate observed facts from assumptions.

## A useful discovery conversation

- “Walk me through the last difficult case.” Concrete examples reveal exceptions.
- “How many cases look like this each week?” Volume establishes scale.
- “Where do mistakes appear, and how are they corrected?” Recovery reveals hidden work.
- “Which systems and permissions would a pilot need?” Access can determine feasibility.
- “What result would make you keep using this?” Adoption needs a measurable standard.

Do not promise a delivery date before the access, data, integration, and validation risks are understood. Offer a small scoped milestone with an explicit proof point.

## Build a vertical slice

Choose one user, one workflow, one source, and one reviewable output. For invoice operations, the first slice might create a validated draft for a reviewer using synthetic data. Add the external write after the controls and reconciliation path are understood.

A vertical slice exercises the whole path in a small scope. Building all databases first and all user interfaces later delays discovery of integration problems. Keep a decision log explaining rejected alternatives and the evidence that would change your choice.

## Trust comes from inspectable work

Show source evidence, known limitations, and failure behavior. Demonstrate an unanswerable question, a denied-access request, and a dependency outage as well as the happy path. Explain costs and measured value in the customer's units: minutes, accepted records, cycle time, backlog, or quality.

For a pilot, agree on baseline measurement, success criteria, review ownership, rollout cohort, and a stop condition. An impressive demo is not the same as adoption. Observe whether users return, accept outputs, and correct errors.

## Handoff and feedback

Deliver an operator runbook, ownership map, environment/configuration record, evaluation report, permission model, recovery procedure, and support expectations. Train the people responsible for exceptions. A system that only its original builder can run is not fully handed over.

Return repeated field needs to the product or platform team. Distinguish reusable capability from a customer's one-off customization. Avoid adding bespoke branches indefinitely without revisiting the design.

## Practice and answer

**Question:** a customer asks for fully automatic invoice posting immediately. What should you propose first?

**Answer:** map the current approval and exception process, measure the baseline, and demonstrate extraction plus validation in a reviewable draft. Define when a write can be authorized and how duplicates/unknown outcomes are reconciled. Expand automation only when measured behavior and ownership support it.

Use: [problem brief](../templates/problem-brief.md), [ROI worksheet](../templates/roi-worksheet.md), [capstone rubric](../CAPSTONE.md).

Next: [Case studies](../case-studies/README.md) · [Interview preparation](../interview/README.md) · [Index](../INDEX.md)
