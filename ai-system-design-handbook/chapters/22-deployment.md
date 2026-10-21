# 22 · Deployment, CI/CD, and change control

**Prerequisites:** Chapters 18–21. **Goal:** release a reproducible system and recover from a bad change.

## Deploy the configuration, not just the code

AI behavior depends on application code, prompt, model, decoding configuration, tool schemas, retrieval/index version, parser, and policy configuration. Record these together in a release manifest. A source-code commit alone may not reproduce a result if a model alias or document collection changed.

**Everyday intuition:** a recipe needs the ingredients and cooking instructions, not just the filename of the cookbook.

Use dependency lockfiles or explicit versions where appropriate. Containers package runtime dependencies but do not remove the need to patch them, protect secrets, or configure storage correctly. Keep secrets outside source control and build logs.

## A useful delivery pipeline

1. Check syntax, unit tests, contracts, and internal documentation links.
2. Run relevant deterministic and behavioral evaluations.
3. Build an immutable artifact and scan applicable dependencies.
4. Deploy to a test environment using synthetic or approved data.
5. Exercise permissions, migrations, timeouts, and rollback.
6. Release to a limited cohort, monitor the defined indicators, and expand deliberately.

Not every change needs the same expensive checks, but prompt, parser, model, and index changes must not bypass evaluation merely because no Python code changed.

## Stateless APIs and durable workers

Keep API instances replaceable by storing job state in durable services. Return a job ID for long processing. Workers should tolerate restarts and duplicate deliveries. Provide health/readiness checks that reflect useful service behavior without accidentally exhausting a provider quota.

Object storage holds large source files; the database tracks metadata, job state, permissions, and source relationships. Search indexes are derived data that should be rebuildable from controlled sources. Practice rebuild and restore rather than assuming backups are usable.

## Safe migrations

For a new embedding model, build a separate index version, evaluate it, and switch a pointer or routing configuration. Preserve the old index during the rollback window. For database schema changes, use backward-compatible expand/migrate/contract steps when old and new application versions can overlap.

Rollback is more complicated after external effects. You can revert a prompt, but cannot undo a sent email by redeploying old code. Define compensating actions, reconciliation, and human ownership for irreversible or business-sensitive effects.

## Shadow and canary

Shadow traffic sends a copy of an eligible request to a candidate for observation, without exposing candidate output or executing its writes. It still consumes cost and may process sensitive data, so the candidate needs approval for those data flows. A canary serves a limited share of real traffic and needs monitored stop conditions.

Feature flags can disable generation or writes independently. During an incident, a read-only evidence view may remain useful while action execution is paused.

## Practice and answer

**Question:** what should a release record contain for a changed RAG prompt?

**Answer:** code/configuration reference, exact prompt version, model configuration, index/source versions, evaluation dataset/report, thresholds, rollout cohort, responsible owner, and rollback plan. Include known limitations and external data terms where relevant.

Next: [Economics](23-cost-and-economics.md) · [Index](../INDEX.md)
