# Drill 03: The pilot looks successful on average

## The situation

An assistant was evaluated on 100 synthetic cases:

| Segment | Cases | Correct outcomes |
|---|---:|---:|
| Common supported questions | 70 | 68 |
| Missing or outdated evidence | 20 | 12 |
| Permission-boundary cases | 10 | 7 |

The pilot team reports median response time of two seconds, p95 of nine seconds, and three permission failures. Each permission failure exposed text that the caller could not access. The pre-agreed release rule permits **zero permission failures in this suite**. A slide says, “87% correct, ready to launch.”

There are 12 invited pilot users. Nine opened the tool, five completed a task, and three returned in week two. No matched measurement of the old workflow exists. Reviewer time and model costs have not been recorded.

## Your task

Write a release decision for the customer owner. Explain the overall correctness calculation, the weak segments, and the hard gate. Do not convert “zero failures observed” into a claim of zero future risk.

Then prepare:

1. A plan to investigate the three permission failures and add regression cases.
2. A measurement plan for complete task time, reviewer effort, cost per completed task, and abandonment.
3. A small operational handoff: owner, alert, response, rollback, and recovery check.
4. An adoption note with explicit denominators for invited, opened, completed, and returning users.
5. A short next-pilot scope and conditions for reconsidering release.

## Interview extension

The sponsor asks, “Can we just use a stronger model?” Explain which observed problems could plausibly improve through model choice and which require changes in data scope, product workflow, or evaluation. Give one experiment that would help separate those causes.

Check [the answer key](../ANSWER-KEY.md#drill-03).
