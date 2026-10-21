# ChatGPT dots: from a vague request to a useful responsibility

**Independent guide by Swapnil AI Labs. Official documentation checked: 21 October 2026.**

OpenAI documents **dots** as agents that can continue work across tools and projects and return with results or decisions. This guide explains how to frame that work, inspect it, and learn the system-design principles behind it. Access, preview limits, and available connections depend on the account and current product. [Official introduction](https://learn.chatgpt.com/docs/dots).

The guide is MIT-licensed original educational material. ChatGPT and its connected services have their own terms. The exercises are proposed recipes; no signed-in account runs or comparative performance results are claimed.

## First setup

Open dots in a supported ChatGPT app or desktop browser and follow its introduction. Name the dot if useful, then choose the connections relevant to your first task. The official setup page documents supported devices and access details. Begin with one responsibility and inspect its result before broadening the scope. [Setup](https://learn.chatgpt.com/docs/dots/getting-started).

Start with this synthetic input:

```text
Project: Example onboarding guide
Confirmed: outline approved; first draft incomplete; launch date undecided.
Source available: a pasted outline and a task table.
Source unavailable: customer feedback from last week's call.
Desired output: a reviewable brief, not an external message.
```

## Assign an outcome with a clear boundary

```text
Help me prepare the onboarding guide from the supplied outline and task table.
First identify the missing information and propose the smallest useful draft.
Separate confirmed decisions, assumptions, and open questions.
Prepare a reviewable artifact and a checklist of what still needs a decision.
Do not contact customers or invent feedback from the unavailable call.
```

**Pass condition:** a useful draft exists, open questions remain visible, and unavailable feedback is not presented as a known fact. If the result is only a plan, ask for the actual artifact and inspect it.

## Understand three different kinds of access

| Access | What to verify | Common misunderstanding |
|---|---|---|
| Connected application | Correct account, scope, and relevant source | A connection does not establish access to every file |
| Dot's cloud computer | The session and files actually available there | Your personal browser's login is not automatically inherited |
| Your connected computer | The required app/access is active and the device is available | Connecting a computer does not supply every past conversation |

OpenAI documents the cloud computer as having its own sessions. A website may therefore require its own secure sign-in or takeover flow. Use that product flow; keep secrets out of ordinary task messages. [Computers and apps](https://learn.chatgpt.com/docs/dots/computers-and-apps).

## Ongoing work and scheduled work

An ongoing project can receive new context and changed priorities. A fixed recurring responsibility needs its timing, time zone, source, output destination, and notification rule specified and saved. Review the saved task rather than relying on an informal promise. Supported event monitoring depends on the connected source. [Tasks and memory](https://learn.chatgpt.com/docs/dots/tasks-and-memory).

Example task design:

```text
For the next four weeks, review the specified project checklist every Monday
at 9 AM Asia/Kolkata. Prepare a short status brief in this conversation.
Notify me about blocked milestones or missing decisions. Do not send messages
to other people. Confirm the source, timing, destination, and what was saved.
```

This text is a learning example; it does not create a schedule by appearing in this repository. Before using it, replace the source with a real permitted one and inspect the resulting saved task.

## Review actions and outcomes

Instructions, app permissions, custom rules, and automatic action review govern what can proceed. Drafting and sending are different authorizations. Inspect work in the documented Activity/Review surfaces; a completed run still needs its output checked. Stopping active work and canceling a recurring schedule are separate decisions. [Controls](https://learn.chatgpt.com/docs/dots/controls).

For an important result, check the source, final artifact, changes made, unresolved errors, and actual delivery destination. A green completion state does not prove every business requirement was met.

## Use dots to practise FDE thinking

Try a requirements brief, stakeholder-question list, research comparison, source-backed project update, and regression-test plan. For each, define observable acceptance criteria and preserve unknowns. If you delegate coding work, provide repository context, allowed scope, and a validation command; review the actual diff and test output.

## Troubleshoot without guessing

- **Missing source:** ask which source could not be read and continue only with identified evidence.
- **Wrong remembered constraint:** supply the correction and have the dot identify its effect on the current task.
- **No recurring output:** inspect the saved schedule, source access, execution result, and delivery destination separately.
- **Login works on your laptop but fails in cloud:** inspect the relevant cloud session; use its supported sign-in flow.
- **Result claims tests passed:** request the actual command/output or clearly state that validation was not run.

Continue: [five worked recipes](PLAYBOOKS.md) · [official sources](SOURCES.md).
