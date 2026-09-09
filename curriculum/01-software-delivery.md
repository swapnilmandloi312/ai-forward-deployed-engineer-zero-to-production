# 01 — Python, APIs, and Delivery Quality

## Outcome

Build a small service that is understandable, testable, observable, and safe to change.

## Learn

- Python types, data validation, modules, exceptions, and dependency boundaries
- HTTP semantics, REST contracts, authentication, pagination, timeouts, and rate limits
- Relational modeling, transactions, migrations, and indexes
- Unit, integration, contract, and end-to-end tests
- Structured configuration, secrets, logging, and error responses
- CI gates, code review discipline, and small reversible changes

## Build

Create an intake service for work items such as documents, support tickets, or leads. It must expose:

- `POST /items` with schema validation and an idempotency key;
- `GET /items/{id}` with stable status and error contracts;
- `GET /health` separating liveness from dependency readiness;
- a persistence layer with a migration;
- structured logs containing a request or trace identifier.

Write tests for duplicate submission, invalid input, missing record, dependency timeout, and retry after partial failure. Add a CI workflow that runs formatting, linting, tests, and a secret scan.

## Decision drill

Write an ADR comparing direct synchronous processing, a background job, and a queue. Choose using latency, failure isolation, throughput, operational complexity, and user expectations—not fashion.

## Evidence

- OpenAPI contract and example requests
- Automated test results and coverage note
- Database schema and migration
- ADR with rejected alternatives
- Setup and local troubleshooting instructions

## Proof gate

A fresh user can start the service from the README. Duplicate requests do not create duplicate side effects. Failure responses are stable, useful, and do not leak sensitive information.

## Primary references

- [Python tutorial](https://docs.python.org/3/tutorial/)
- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [PostgreSQL documentation](https://www.postgresql.org/docs/)
- [GitHub Actions documentation](https://docs.github.com/actions)
