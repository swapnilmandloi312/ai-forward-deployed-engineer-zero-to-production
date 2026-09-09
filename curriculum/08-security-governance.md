# 08 — Security, Privacy, and Governance

## Outcome

Map realistic threats and data obligations to preventive, detective, and recovery controls.

## Learn

- Data classification, minimization, purpose, retention, deletion, and residency
- Authentication, authorization, tenant isolation, and least privilege
- Secret management, encryption, network boundaries, and vendor review
- Prompt injection, insecure output handling, excessive agency, and data exfiltration
- Model and tool supply chain, dependency pinning, and artifact provenance
- Threat modeling, abuse cases, control ownership, and residual risk
- Governance evidence without treating a checklist as compliance

## Build

Threat-model your project using assets, actors, trust boundaries, misuse cases, controls, owner, and verification method. Test at least:

- direct and indirect prompt injection;
- a request for another tenant's data;
- a model-generated unsafe tool argument;
- a secret accidentally present in input;
- an authorization change during an active workflow;
- deletion and retention behavior.

Redact sensitive values from logs and evaluation artifacts. Define who can approve policy exceptions and how access is revoked.

## Evidence

- Data-flow diagram with trust boundaries
- Threat register ranked by impact and likelihood
- Data-control and tool-permission matrices
- Security test results
- Residual-risk acceptance or blocked-release decision

## Proof gate

High-impact actions have least-privilege authorization and human/policy controls. Cross-tenant and injection tests fail safely. The team knows where data is stored, who can access it, how long it remains, and how it is deleted.

## Primary references

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [MITRE ATLAS](https://atlas.mitre.org/)
