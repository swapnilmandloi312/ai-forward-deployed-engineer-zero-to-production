# FDE Field Drills

**Original, synthetic practice by Swapnil AI Labs. No customer results are claimed.**

Learn to turn an unclear request into a small system with a measurable result. These drills combine customer discovery, data checks, architecture, evaluation, and handoff. You can complete them with a text editor and Python 3.11+; no paid model account is required.

## Start with one complete drill

| Drill | What you practice | Evidence to produce |
|---|---|---|
| [01: A support team asks for an agent](drills/01-support-triage.md) | Decomposition, exact counts, an honest baseline | Problem brief, reproducible data summary, scoped pilot |
| [02: A policy assistant gives a confident answer](drills/02-policy-retrieval.md) | Permissions, freshness, refusal, evaluation | Retrieval contract, test cases, escalation rules |
| [03: The pilot looks successful on average](drills/03-pilot-release.md) | Release decisions, failure analysis, adoption | Segmented report, go/no-go decision, handoff |

Attempt each problem before reading [the worked answers](ANSWER-KEY.md). A defensible alternative is welcome when you state its assumptions and tests. The answers illustrate reasoning; they are not a script to memorize.

## Run a useful baseline

From this collection folder:

```bash
python analyze_tickets.py --tenant north
python analyze_tickets.py --tenant south --json
```

The first command reads the included [synthetic export](data/tickets.csv), scopes records to one tenant, selects the newest row per ticket, and calculates exact category totals. It makes no model or network calls. The default tenant has **10 export rows, eight unique tickets, and five export-related tickets**. Counting rows would overstate the work volume.

The tool accepts a CSV through `--input`. Required columns are `tenant`, `ticket_id`, `updated_at`, and `category`. Timestamps must include a UTC offset. Categories are `export`, `access`, or `billing`; unknown values fail visibly. A conflicting category at the same ticket timestamp also fails. This is an intentionally small analytical baseline, not a customer-support integration.

## What a complete submission contains

1. A problem statement identifying the user, workflow, and current pain.
2. A source inventory with missing and contradictory information visible.
3. A baseline you can reproduce, including the unit being counted.
4. One bounded design and one rejected alternative.
5. Normal, denied, missing-data, and failure tests with expected results.
6. A release decision and a named owner for the next action.

Use the [submission template](SUBMISSION.md). Add actual commands, outputs, and limitations as you work. A diagram or polished demo alone does not establish a successful pilot.

## How to review your work

Score each dimension from 0 to 2: absent, plausible, or evidenced. Dimensions are problem clarity, data correctness, permission boundaries, evaluation, operational recovery, and handoff. A score helps identify the next practice area; it is not a hiring prediction. An unexplained permission violation blocks release regardless of the total.

After a drill, explain it aloud in five minutes: what changed, what evidence supports it, what failed, and what you would do next. Publish the synthetic exercise and your reasoning if useful. Keep real customer material out of public submissions.

Original material and the baseline tool use the [MIT License](LICENSE).
