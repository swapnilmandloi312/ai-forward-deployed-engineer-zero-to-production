# Security Policy

This repository contains educational material and templates, not a hosted service. Still, examples can accidentally expose secrets or normalize unsafe patterns.

## Report privately

Use the contact channel on [Swapnil AI Labs](https://swapnilailabs.netlify.app/) for a vulnerability, exposed credential, unsafe default, or sensitive-data concern. Do not post secrets, exploit details, or personal data in a public issue.

## Deployment baseline

- keep credentials in a managed secret store, never in source or exported workflows;
- use least-privilege service accounts and separate dev/test/prod access;
- classify data before sending it to any model or external tool;
- document retention, deletion, residency, and subprocessors;
- require human approval for high-impact or irreversible actions;
- log security-relevant events without logging sensitive payloads;
- test prompt injection, tool misuse, cross-tenant access, and provider failure;
- maintain kill switch, rollback, and incident contacts.

Educational examples are not a compliance certification. Perform domain-specific legal and security review before production use.
