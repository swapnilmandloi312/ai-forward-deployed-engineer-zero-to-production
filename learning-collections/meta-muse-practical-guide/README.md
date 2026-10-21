# Meta Muse: a practical learning guide

**A plain-English guide by Swapnil AI Labs. Documentation checked: 21 October 2026.**

Learn to give Muse a clear job, inspect its work, and connect the experience to AI system-design concepts. This is an independent educational guide. Its original text is MIT-licensed; Meta's product, models, and services keep their own terms. The practice tasks below have not been run against a signed-in Muse account.

## Understand the names

**Muse is the personal agent. Muse Spark is a model family behind Meta's AI work.** An agent combines a model with tools, state, and an interface; the model name alone does not describe the whole product. Meta's launch material describes Muse working through its app or WhatsApp, using a dedicated cloud environment, and returning when it needs a decision. [Sources](SOURCES.md).

## Begin with a small, observable task

1. Open Muse from an official Meta entry point in the sources page. Check access in your account and region; the launch announcement described a US rollout, not universal availability.
2. Start with text you can safely paste, such as the synthetic project table below.
3. State the outcome, sources, output format, constraints, and how you will judge success.
4. Review the result against the supplied facts. Correct a mistake explicitly and ask for a revised version.
5. Connect an additional service only when a task actually needs it. Review the access being requested in the current product interface.

Do not assume that downloading an app, connecting a service, or mentioning a recurring task proves that a particular capability is active. Confirm the relevant access or saved task in the interface.

```text
Project: Synthetic website refresh
Task A: write homepage outline; owner Sam; due 2026-11-03; status blocked
Task B: review accessibility; owner Lee; due 2026-11-05; status pending
Known dependency: Task A needs an approved positioning statement.
Unknown: whether the positioning statement has been approved.
```

## Your first useful prompt

```text
Use only the synthetic project information above.
Prepare a status brief with: confirmed facts, blockers, missing information,
and the next three actions. Keep an unknown value marked unknown.
Do not contact anybody or change another application.
For each action, state the input or decision needed before it can proceed.
```

**Expected result:** the brief identifies the missing positioning approval. It does not claim Sam has finished the homepage or invent a meeting with Lee. A plausible-looking paragraph is not sufficient; compare every statement with the input.

## Five ways to practise

| Practice | Give Muse | Ask it to produce | Check yourself |
|---|---|---|---|
| Meeting preparation | A synthetic agenda and prior decisions | Decisions needed, questions, source references | No invented attendees or commitments |
| Research comparison | Three permitted public product pages | Comparison table and unresolved claims | Sources support each feature claim |
| Learning plan | Current skill level, target, weekly time | Sequenced exercises and completion evidence | Time and prerequisites are realistic |
| Project coordination | The synthetic task table | Dependency-aware next steps | Missing approval stays missing |
| Draft review | A fictional customer update | Clearer draft and factual corrections | No new promises, dates, or measured results |

For a real task, choose sources you are allowed to use. Model fluency and the presence of a source link do not independently establish factual support.

## Connect this to FDE work

You are practising requirements discovery when you specify a useful outcome. You are practising context engineering when you select the relevant input. You are practising evaluation when you define a pass/fail check. You are practising operational delivery when you inspect a blocked task and identify its owner.

The same habits transfer to systems you build with Python or n8n. The hosted product handles implementation details, but your responsibility for clear scope and verified outcomes remains.

## Read results before expanding authority

Meta describes action review, user-controlled connections, and an audit trail. Its security explanation describes a dedicated VM and separate controls around credentials and external actions. Treat those as vendor-described mechanisms, not a security certification for your own workflow. Use the actual product's review and access screens when you choose to perform an external action. [Sources](SOURCES.md).

For practice, keep the first task draft-only. If you later want a message sent, specify the exact recipient, approved content, and destination under the product's applicable controls. A request to write a draft is a different instruction from a request to send it.

## Troubleshooting by evidence

| Symptom | Investigate | Useful next instruction |
|---|---|---|
| Output guesses a missing detail | Input ambiguity | "List missing facts before proposing the plan." |
| Agent cannot reach a source | Connection, login, or source permissions | "Identify the unavailable source and preserve the partial result." |
| Research feels generic | Undefined decision or comparison criteria | "Compare these three options against these four criteria." |
| Work seems finished but no artifact exists | Completion was not observable | "Show the actual artifact and explain which checks passed." |
| An old preference affects the answer | Stale remembered context | "Use this updated constraint for this task; identify conflicting assumptions." |

## A fair product experiment

Use the same synthetic project task in Muse, dots, and Grok Bot. Record the date, available tools, instructions, source access, actual outputs, corrections, and elapsed time. Mark a blocked or unavailable run explicitly. This guide makes no claim that one product wins that comparison.

Continue: [worked recipes](PLAYBOOKS.md) · [official sources](SOURCES.md).
