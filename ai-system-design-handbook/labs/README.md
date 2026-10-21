# Five offline labs

Run from the handbook folder containing `labs/` with Python 3.11+. If you are in the parent FDE repository, first run `cd ai-system-design-handbook`. No installation or API key is required. Every input is synthetic. The labs expose specific mechanisms; they are not deployable services or complete LLM implementations.

## 1. Permission-filtered retrieval

```bash
python -m labs.mini_rag --question "What is the refund window?" --tenant acme
python -m labs.mini_rag --question "When is payroll processed?" --tenant acme
python -m labs.mini_rag --question "When is payroll processed?" --tenant acme --groups finance
```

Expected: the first command cites `returns@2`, including the 30-day unopened-item rule. The second abstains because the synthetic support group lacks payroll access. The third returns `staff-pay@1`.

Read [mini_rag.py](mini_rag.py) in this order: document validation, current-version selection, access filtering, lexical scoring, and evidence formatting. Identity is supplied by CLI flags for the experiment. A real service must obtain identity/groups from trusted authentication and policy systems.

**Limitation:** this is lexical extractive retrieval, with no embeddings, semantic answerability detector, or generative answer. Shared keywords can return irrelevant evidence. Do not call its score confidence.

**Exercise:** ask “refund for a cryptocurrency purchase.” Observe that keyword overlap can find evidence without answering the complete question. Add a labeled case and design a better answerability check; do not simply special-case one phrase.

## 2. Evaluation smoke set

```bash
python -m labs.evaluate
python -m labs.evaluate --output reports/evaluation.json
```

Expected on the bundled ten cases: six answerable source-hit checks, four expected abstentions, and ten passing case checks. The report measures source hit@3 and abstention accuracy. It does not measure generated-answer correctness, faithfulness, or comprehensive access security.

**Exercise:** create a separate development set with paraphrases such as “Can I get my money back?” Lexical retrieval may fail. Compare a stemmer, lexical expansion, and an embedding model as separate experiments while preserving all access tests. Keep a held-out set for final comparison.

## 3. Guarded invoice workflow

```bash
python -m labs.guarded_workflow
python -m labs.guarded_workflow --approve
```

Expected without approval: two `review_required` outcomes and zero local entries. With synthetic approval: `posted_locally`, then `duplicate`, and one entry. Each command uses a new in-memory database by default. Use `--db demo.sqlite3` to inspect persistence across runs; delete that local demo file to start fresh.

Read [guarded_workflow.py](guarded_workflow.py): normalization, vendor allowlist, review gate, canonical payload hash, `BEGIN IMMEDIATE`, uniqueness, and atomic commit. Tests cover a changed-payload conflict and separate business-identity duplicate too.

**Limitation:** both the operation record and ledger entry are in one SQLite transaction. This does not solve external accounting API idempotency. Approval is a boolean in a synthetic demo, not authentication, real reviewer authorization, or an approved document version.

**Exercise:** sketch an adapter for an external accounting API. Add `submitted/confirmed/unknown` states, a stable destination key, and reconciliation. Explain the crash window after external success but before local commit.

## 4. Capacity and cost

```bash
python -m labs.capacity
python -m labs.capacity --requests-per-day 10000 --active-hours 10 --peak-factor 6
```

Default expected values: peak two requests/second, eight mean in-flight requests at that steady peak, 240,000 input tokens/minute, 48,000 output tokens/minute, and $86.40/day at the **fictional** rates. The 10,000-request variant gives $72/day and $2,160 for 30 days.

**Exercise:** double output tokens and calculate both spend and likely generation-time impact. The script does not predict model latency from token length or account for retries/hosting/review.

## 5. Gateway failure simulation

```bash
python -m labs.gateway
```

Expected: the first two primary calls fail, fallbacks succeed, and the third request bypasses the open primary circuit. There are two primary calls, three fallback calls, and an open circuit. Tests cover recovery probes, cancellation, deadline propagation, and bounded concurrency.

**Limitation:** providers are deterministic local coroutines. The breaker and semaphore are process-local; this is not a distributed gateway, quota service, production provider SDK, or content-validation layer. Approved fallback data terms and model compatibility must be checked in a real deployment.

**Exercise:** design per-tenant fairness and a distributed token budget. Explain why adding one semaphore per API process does not create a global limit.

## Verify your changes

```bash
python -m unittest discover -s tests -v
python scripts/check_docs.py
```

The test suite checks behavior such as denied access, stale versions, changed operation payloads, and canceled provider work. It does not prove production security or AI quality. Use [the evaluation chapter](../chapters/18-evaluation.md) to build realistic experiments.

Troubleshooting: [setup and lab issues](../TROUBLESHOOTING.md) · [Index](../INDEX.md)
