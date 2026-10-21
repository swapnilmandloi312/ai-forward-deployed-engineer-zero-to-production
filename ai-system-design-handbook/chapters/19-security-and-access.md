# 19 · Security, privacy, and multi-tenant access

**Prerequisites:** Chapters 4, 13, and 15. **Goal:** identify where an AI feature can reveal data or exceed authority.

## Start with assets and boundaries

List the data, credentials, tools, external writes, users, and administrators. Identify which inputs are trusted and which are merely content. A user's own uploaded file can still contain malicious instructions. A tool server can return dangerous or misleading text.

**Everyday intuition:** a receptionist can read a visitor's letter without accepting the letter as permission to open the safe.

Authentication establishes identity. Authorization determines allowed operations on particular resources. A valid login does not imply access to every document. A model's interpretation of a role description does not replace a policy engine or database check.

## Enforce isolation before exposure

Derive tenant identity from a trusted session or token. Restrict database queries, object storage access, retrieval candidates, source links, caches, and traces. Recheck access when returning sensitive artifacts or executing a write. Permissions can change between a long-running job's start and completion.

PostgreSQL row-level security can add enforcement in the data layer when configured correctly. Understand database roles, table ownership, privileged bypasses, connection-pool context, and testing. Adding a `tenant_id` column alone does not provide isolation.

## Prompt injection and excessive agency

Retrieved documents, websites, email, and tool results can try to redirect behavior. Defense combines least-privilege tools, independent authorization, limited data exposure, argument validation, approval for defined actions, and a bounded execution environment. No single prompt phrase or filter guarantees protection.

For a read-only policy assistant, the strongest protection against sending an unauthorized email is not providing an email-sending capability. For an action assistant, bind approval to the exact draft/action version and verify it at execution time.

## A compact threat model

| Threat | Example | Control to test |
|---|---|---|
| Cross-tenant retrieval | Tenant A asks for Tenant B's policy | Server-derived scope plus negative access tests |
| Cache leakage | Same question reuses another user's answer | Permission-aware keys and invalidation |
| Instruction injection | PDF requests credential disclosure | Restricted tools and external policy enforcement |
| Unsafe output handling | Model text becomes executable SQL/HTML | Parameterization, escaping, and allowlists |
| Secret exposure | API token enters a prompt or trace | Secret storage, minimization, redaction, access limits |
| Resource exhaustion | Huge files or endless tool loops | Size, time, concurrency, step, and cost limits |

## Privacy is a lifecycle

Collect only necessary information. Record why it is processed, who can access it, where it is sent, and how long it is retained. Include raw uploads, extracted text, embeddings, caches, evaluation datasets, logs, and backups in the inventory. Embeddings should not be assumed anonymous.

Verify vendor contracts and data settings for the specific deployment. The words “encrypted” or “enterprise” do not establish that a system meets an organization's requirements. Regulated deployments need their own applicable legal and compliance review; this handbook does not certify one.

## Practice and answer

**Scenario:** the retrieval filter is correct, but full candidate text is logged before the filter. Is the design isolated?

**Answer:** no. Logs are another data-exposure path. Apply access restrictions before content leaves the allowed boundary, minimize logged data, and inspect traces, artifacts, and support tooling as well as the user-facing answer.

Further reading: [OWASP GenAI security project](https://genai.owasp.org/), [PostgreSQL row security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html).

Next: [Reliability](20-reliability.md) · [Index](../INDEX.md)
