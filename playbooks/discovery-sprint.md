# Discovery Sprint Playbook

## Goal

Reach a decision about the smallest valuable experiment, not a complete requirements document.

## Before the session

- Identify the workflow owner, 2–3 users, operator, system owner, security/privacy owner, and economic buyer.
- Request sanitized examples of recent work, exceptions, and downstream outcomes.
- Prepare the [problem brief](../templates/problem-brief.md) but leave assumptions visible.
- State that the session will examine workflow and outcomes before selecting technology.

## Session sequence

1. **Recent case:** “Walk me through the last time this happened.”
2. **Trigger and outcome:** What starts and ends the work?
3. **Decision points:** Which decisions use policy, judgment, or external evidence?
4. **Friction:** Where do delay, rework, errors, handoffs, and escalations occur?
5. **Exceptions:** What breaks the normal process? Which errors are most expensive?
6. **Systems/data:** Where does each field originate? Who owns access and corrections?
7. **Baseline:** Volume, handling time, wait time, error, risk, revenue, and current cost.
8. **Constraints:** Security, privacy, compliance, latency, availability, language, adoption.
9. **Decision rights:** What may automation do, recommend, draft, or never touch?
10. **First slice:** Smallest cohort and outcome that can validate the riskiest assumption.

## Challenge the AI request

For each proposed LLM or agent step, ask:

- Can rules, search, templates, or interface design solve it?
- What happens when the output is uncertain or wrong?
- Can the result be evaluated from available evidence?
- Does adding AI change legal, privacy, or approval obligations?
- What data must leave the customer boundary?

## Exit criteria

- [ ] Named user, operator, owner, and decision-maker
- [ ] Current workflow and at least three exceptions mapped
- [ ] Baseline source and confidence recorded
- [ ] Outcome, guardrails, and non-goals agreed
- [ ] Pilot cohort and stop condition proposed
- [ ] Highest-risk assumption assigned an experiment
- [ ] Open access/security dependencies have owners and dates
- [ ] Next decision and decision-maker are explicit

Send a one-page readout within one working day. Separate observed facts, stakeholder claims, assumptions, and decisions.
