# 16-Week Zero-to-Production Roadmap

This plan assumes 8–10 focused hours per week. Compress it only by passing the evidence gates—not by skipping them.

| Week | Focus | Artifact | Gate |
|---:|---|---|---|
| 0 | Role target and baseline | Skills scorecard + learning contract | Target role and proof gaps are explicit |
| 1 | Discovery | Problem brief + workflow map | User, pain, frequency, owner, baseline identified |
| 2 | Software delivery | API/service with tests and CI | Clean setup; failure paths tested |
| 3 | Data integration | Sync pipeline + audit events | Retry and duplicate inputs are safe |
| 4 | Cloud delivery | Containerized environment | Fresh-machine deploy and rollback succeed |
| 5 | LLM system design | Model ADR + structured-output flow | Fallbacks handle malformed output and outage |
| 6 | Retrieval | Corpus, retrieval set, cited response | Retrieval measured separately from generation |
| 7 | Agent/workflow | Bounded tool-using workflow | Side effects require policy/approval |
| 8 | Evaluation | Versioned regression suite | Quality, safety, latency, and cost thresholds pass |
| 9 | Security | Threat model + control matrix | High-risk paths have prevention and detection |
| 10 | Observability | Traces, metrics, alerts | A seeded incident is detected and diagnosed |
| 11 | Product adoption | Pilot and feedback plan | Owner, cohort, success and stop conditions agreed |
| 12 | Commercial case | ROI model + executive memo | Assumptions, ranges, and measured data separated |
| 13 | Capstone hardening | Release candidate | Full Definition of Done passes |
| 14 | Customer simulation | Discovery, demo, objection handling | Another person can operate the handoff |
| 15 | Interview system | Architecture and incident drills | Decisions defended under follow-up questions |
| 16 | Publish | Case study, demo, resume bullets | No secrets; links work; evidence is reproducible |

## Weekly review

At the end of each week, answer:

1. What evidence did I produce?
2. Which customer or operator assumption did I invalidate?
3. What failed, and is it now a test or control?
4. What did the system cost per successful outcome?
5. What is the highest-risk unknown for next week?

## Fast-track rules

You may skip a week when you can link to current evidence that meets its gate. “I used this at work” is context, not evidence. A sanitized demo, test result, runbook, design decision, or postmortem counts.

## Graduation test

Run a 45-minute simulated customer review:

- 10 minutes: problem, users, baseline, and business case;
- 10 minutes: live workflow, including one failure path;
- 10 minutes: architecture, tradeoffs, security, and data flow;
- 10 minutes: evaluations, production metrics, and incident response;
- 5 minutes: adoption plan, next decision, and clear ask.

If the review exposes a gap, add it to the scorecard and return to the relevant module.
