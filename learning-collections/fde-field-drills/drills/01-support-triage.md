# Drill 01: A support team asks for an agent

## The situation

A support lead says: “We need an AI agent to solve export problems automatically.” An engineer says most export issues are product bugs. A manager expects a demo next Friday. The only supplied artifact is [this synthetic export](../data/tickets.csv).

Separate the desired outcome from the proposed implementation. Fewer unresolved requests, faster diagnosis, and automatic replies are different goals. Do not assume that sending a reply fixes a product bug.

## Your task

Write five discovery questions. Include the current resolution process, common causes, allowed actions, the owner of product fixes, and the actual success measure. Then inspect the CSV before choosing a model.

Produce these outputs:

1. The count of unique north-tenant tickets and export tickets, with the deduplication rule.
2. A one-page pilot proposal that helps an operator investigate export problems.
3. A boundary describing which actions require further authorization.
4. An evaluation plan with a no-evidence case and an incorrect diagnosis case.
5. A handoff showing when a product engineer must intervene.

## Calculation practice

Assume, for planning only, 40 eligible requests per week and 12 minutes of current human effort per request. Suppose a proposed assisted process needs six minutes of operator work plus two minutes of review per request. Calculate the weekly effort difference before other operating costs. State what must be measured before calling this a saving.

These assumptions are unrelated to the size of the supplied CSV. Do not describe its 11 rows as a week's workload.

## Helpful design constraint

The first pilot may read the supplied synthetic evidence and prepare a triage card. It may not send a customer reply, change an account, or close a ticket. A triage card should include ticket ID, evidence, tentative issue type, missing information, proposed next step, and reviewer decision.

## Stretch exercise

Compare a rule-based category summary with a model-generated narrative. Keep exact counts in deterministic code. Use the model for an explanation only after providing those counts. Record when the narrative adds unsupported causality.

Check your reasoning against [the answer key](../ANSWER-KEY.md#drill-01).
