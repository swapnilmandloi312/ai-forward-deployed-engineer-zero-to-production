# Drill 02: A policy assistant gives a confident answer

## The situation

A user in tenant North asks, “Can I export all project records?” Your synthetic index contains:

| Document | Tenant | Version | Evidence |
|---|---|---|---|
| N-policy-2 | North | Superseded | “Project members may export project records” |
| N-policy-3 | North | Current | “Export requires the project administrator role” |
| S-policy-7 | South | Current | “Workspace owners may export all workspace records” |
| N-guide-1 | North | Current | Describes the export button but grants no permission |

The caller is a North project member. A vector search retrieves N-policy-2 and S-policy-7 because their wording is close to the question. The answer generator says, “Yes, you can export all records.”

## Your task

Explain the failure without blaming only the prompt. Design a retrieval contract that carries authenticated tenant, project scope, document version, and allowed visibility. Decide how expired indexes and permission changes should behave.

Write expected behavior for:

| Test | What you must decide |
|---|---|
| North member asks the original question | Which evidence applies and what answer is supported? |
| North administrator asks | Does policy permission prove that a particular export will succeed? |
| Index has no current North policy | What does the assistant say and who resolves it? |
| User pastes “ignore tenant filters” | Which component enforces scope? |
| Cached answer came from an administrator | What prevents reuse for a member? |
| Permission changed during a long request | When must access be checked again? |

## Explain the trade-off

Filtering only the generated answer is too late if unauthorized material already reached the model. Propose where to enforce access, how to carry provenance to the answer, and what an operator should inspect after a suspected leak. Avoid logging sensitive document bodies merely to prove a filter ran.

## Deliverable

Submit a small flow diagram, six expected test results, a cache-key contract, and a fallback response for absent evidence. Record any policy assumption you could not resolve from the supplied documents.

Check [the worked design](../ANSWER-KEY.md#drill-02).
