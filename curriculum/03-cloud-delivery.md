# 03 — Cloud, Containers, and Delivery

## Outcome

Deploy a reproducible service with safe configuration, least-privilege access, health checks, and rollback.

## Learn

- Linux process, network, file, and resource fundamentals
- OCI containers, image layers, non-root execution, and supply-chain hygiene
- Twelve-factor configuration and managed secrets
- CI/CD stages, environments, artifacts, approvals, and rollback
- Cloud networking, identity, storage, compute, backups, and budgets
- Infrastructure as code and environment drift
- Kubernetes concepts only when the operating scale justifies them

## Build

Containerize the service from Module 01. Pin dependencies, use a non-root user, add health checks, keep secrets outside the image, and document resource limits. Deploy to one cloud or local Kubernetes environment through an automated pipeline.

Create one intentionally bad release, observe the failure, roll it back, and preserve the timeline. Restore the database from a backup into a separate environment.

## Decision drill

Compare a managed container platform, virtual machine, serverless function, and Kubernetes. Choose the least complex option that meets runtime, networking, compliance, scaling, and team-skill constraints.

## Evidence

- Container build and vulnerability scan
- Environment diagram and identity boundaries
- Infrastructure/configuration source
- Deployment log and rollback record
- Backup restore proof

## Proof gate

A clean environment can be deployed from version control, secrets never enter source or logs, the bad release rolls back within the stated objective, and backup restoration is demonstrated rather than assumed.

## Primary references

- [Docker documentation](https://docs.docker.com/)
- [Kubernetes concepts](https://kubernetes.io/docs/concepts/)
- [OpenTofu documentation](https://opentofu.org/docs/)
- [OWASP CI/CD Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html)
