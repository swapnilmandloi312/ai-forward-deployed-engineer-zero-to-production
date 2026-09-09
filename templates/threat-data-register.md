# Threat and Data-Control Register

## Data inventory

| Data class | Source | Purpose | Storage/processors | Access | Retention/deletion |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Trust boundaries

Link the system/data-flow diagram and identify user, service, tenant, network, model/provider, tool, storage, logging, and operator boundaries.

## Threat register

| ID | Asset / misuse case | Actor/vector | Impact | Likelihood | Prevention | Detection/recovery | Owner | Residual risk |
|---|---|---|---|---|---|---|---|---|
| T-01 | Prompt injection causes unsafe tool use | Untrusted document |  |  |  |  |  |  |
| T-02 | Cross-tenant data exposure | Identity/filter failure |  |  |  |  |  |  |
| T-03 | Sensitive data enters model/logs | Input or telemetry |  |  |  |  |  |  |
| T-04 | Duplicate high-impact action | Retry/replay |  |  |  |  |  |  |
| T-05 | Runaway token/tool cost | Loop or abuse |  |  |  |  |  |  |

## Tool permission matrix

| Tool/action | Data scope | Service identity | Human approval | Idempotency | Audit | Kill/revoke |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Verification

| Control | Test | Expected safe result | Evidence | Last run | Owner |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Acceptance

- Blocked threats:
- Accepted residual risks, approver, reason, and expiry:
- Required legal/security/privacy reviews:
- Next review trigger:
