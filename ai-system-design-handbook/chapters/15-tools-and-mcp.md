# 15 · Tool calling, MCP, and permission boundaries

**Prerequisites:** Chapters 2, 7, and 14. **Goal:** separate a model's proposed action from an authorized action.

## A tool call is a proposal

A tool is an application capability with a name, input contract, implementation, and output contract. A model may produce a tool name and arguments. Your application must decide whether that call is valid and permitted before executing it.

**Everyday intuition:** filling in a transfer form is not the same as being authorized to move the money.

Prefer narrow tools such as `get_invoice(invoice_id)` over broad tools such as `run_any_sql(query)`. Derive the tenant and user scope in the server. A schema that permits `tenant_id` in arguments does not mean the model should choose it freely.

## A safe tool contract

```json
{
  "name": "prepare_invoice_draft",
  "description": "Prepare a reviewable draft; does not post to accounting.",
  "arguments": {
    "source_document_id": "doc-123",
    "vendor_id": "vendor-7",
    "amount_minor_units": 125050,
    "currency": "USD"
  }
}
```

The executor checks the document belongs to the authenticated tenant, the vendor is allowed, the amount and currency are supported, and the user can prepare drafts. A separate approval can authorize posting a particular draft version. Changing the amount after approval must invalidate that approval.

Validate both request and response. A tool error should be structured enough to distinguish invalid input, denied access, transient failure, and an ambiguous external outcome. Do not return raw credentials or a complete database dump to help the model debug.

## What MCP contributes

The Model Context Protocol standardizes interactions between hosts/clients and servers exposing tools, resources, and prompts. It can reduce integration-specific plumbing. It does not make a server trustworthy, authorize every action, or remove the need for input validation.

For a real integration, select and record a dated specification revision, inspect the supported transport and capabilities, and follow that revision's authentication/authorization guidance. This handbook links the [2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28) as a reference, without claiming all installed servers implement it.

## Security at each boundary

| Boundary | Required question |
|---|---|
| User to application | Who is asking, and what may they do? |
| Application to server | Which server is this, and which permissions were granted? |
| Tool name to executor | Is this operation allowlisted for the current task? |
| Arguments to data | Are IDs and ownership checked by trusted code? |
| Server response to model | Is output bounded, sanitized, and treated as data? |
| Approved draft to write | Does approval match the exact action and current state? |

Token audience validation, least privilege, trusted server configuration, and avoiding unsafe credential forwarding matter. A connected tool server should not gain general access to unrelated user data merely because it can describe tools.

## Tool protocols versus agent protocols

A tool protocol exposes capabilities. An agent-to-agent protocol concerns delegating tasks to another agent system. A plain internal HTTP API is often sufficient for a small deployment. Introduce interoperability protocols when they solve a real integration problem; do not add them as decorative boxes.

## Practice and answer

**Question:** a valid tool call requests an invoice ID belonging to another customer. What happens?

**Answer:** reject it based on server-side ownership checks. Valid syntax does not establish authorization. Do not pass the other customer's invoice to the model and ask it not to mention the contents.

Next: [Memory and durable state](16-memory-and-state.md) · [Index](../INDEX.md)
