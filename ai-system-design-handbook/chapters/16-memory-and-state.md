# 16 · Conversation memory, business state, and durable execution

**Prerequisites:** Chapters 4 and 14. **Goal:** know what should be remembered, where, and for how long.

## Memory is not one storage bucket

Conversation history helps interpret a dialogue. A user preference can personalize future responses. Retrieved organizational knowledge supports facts. Business state records what actually happened. These have different owners, lifetimes, and correctness requirements.

**Everyday intuition:** a conversation note, an address book, a reference manual, and a bank ledger are all records, but you would not use them interchangeably.

| Record type | Example | Appropriate treatment |
|---|---|---|
| Session history | “I meant last month” | Bounded context with a session identity |
| Summary | Condensed previous discussion | Lossy aid; preserve source links for critical facts |
| Preference | Preferred response language | Editable, scoped, and deletable |
| Knowledge | Current reimbursement policy | Versioned retrieval with access checks |
| Business state | Invoice approval and posting ID | Durable database and audit trail |

## Summaries lose information

A summary reduces tokens but may drop an exception or misstate a decision. Do not treat “the user approved it” in a generated summary as proof that a write was authorized. Store approval identity, action payload/version, time, and relevant policy state independently.

Keep links to original messages or artifacts where retention allows. Evaluate summary quality on decisions, constraints, names, dates, and corrections rather than only readability. A fluent summary that reverses a negation can cause expensive mistakes.

## Memory retrieval needs permissions

A long-term vector memory can accidentally retrieve another user's personal information or an outdated preference. Scope every retrieval, store provenance, allow correction, and define deletion propagation. Avoid retaining sensitive information simply because it appeared in a conversation.

Memory can be poisoned: untrusted content might claim the user always permits transfers. Only trusted sources and deliberate application rules should update authorization-related records. General preferences must never expand tool permissions.

## Durable execution

Long-running tasks can outlive an HTTP request or process. Store a job ID, state, attempts, deadlines, intermediate artifacts, and side-effect references. A worker restarting should continue from a known safe boundary instead of asking a model to reconstruct reality from prose.

For an external write, distinguish `proposed`, `approved`, `submitted`, `confirmed`, `failed`, and `unknown`. “Unknown” is a useful state: it means reconciliation is needed. Pretending every timeout is a failure can create duplicates.

Replay is also subtle. Re-running a model call may produce different output. Replaying an external tool call may repeat an effect. Persist accepted outputs and use activity-level idempotency/reconciliation. Durable workflow engines provide useful mechanisms, but the business semantics still need to be designed.

## Practice and answer

**Scenario:** a conversation summary says an invoice was approved, while the approval table has no matching record.

**Answer:** the table and approval policy control the write. Treat the summary as unverified context, ask for or obtain the required approval through the authorized workflow, and investigate why the summary invented or overgeneralized a decision.

Next: [n8n](17-n8n-in-production.md) · [Index](../INDEX.md)
