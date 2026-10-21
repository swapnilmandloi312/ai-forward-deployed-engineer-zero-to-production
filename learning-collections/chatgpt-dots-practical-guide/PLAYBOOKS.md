# Five dots practice recipes

These recipes are original examples. Replace synthetic input with appropriately permitted sources when you use the product. A prompt in this repository is not an activated task or a saved schedule.

## 1. Turn an ambiguous customer ask into a brief

**Input:** "We need AI to improve support," plus a fictional team handling 200 tickets/day, with no agreed definition of resolution.

```text
Turn this into a discovery brief. Separate known facts, assumptions, and
questions. Propose one small pilot, the baseline to measure, a human owner,
and acceptance criteria. Explain when a rules/search solution could suffice.
Do not invent an automation rate or financial return.
```

**Check:** the result asks what resolution means and who owns escalation. **Improve:** provide one difficult ticket and ask how it changes the scope.

## 2. Review a system design

**Input:** a fictional architecture that retrieves all tenants' documents and asks the model to hide unauthorized ones.

```text
Review this design by tracing one request. Identify where information crosses
a trust boundary, which controls must run in trusted code, and the tests that
would expose a failure. Return a corrected data flow and two alternatives.
Label unverified implementation details as questions.
```

**Check:** authorization belongs before unauthorized content reaches the model or output, including traces. **Improve:** add a stale response cache and repeat the review.

## 3. Prepare a weekly learning report

**Input:** your own study log with attempted exercises and failures.

Ask for concepts you can now explain, experiments that failed, evidence links, and one focused next exercise. If you later schedule it, specify the actual log source, time zone, duration, and output destination. Verify that a schedule was saved.

**Check:** it does not equate checking a box with understanding a topic. **Improve:** ask for three questions you should answer without notes.

## 4. Compare open-source candidates

**Input:** three exact repository URLs from the accompanying catalog.

```text
Compare these projects for the stated workload. Check their current README,
license scope, archived status, setup requirements, and external dependencies.
Separate documentation claims from experiments we have actually run.
Design a small reproducible comparison and list the expected artifacts.
```

**Check:** a hosted service being optional does not mean your chosen example is cost-free. **Improve:** add a constraint requiring local execution and identify what must be verified.

## 5. Package a repository change for review

**Input:** a permitted repository, a precise issue, and the required validation command.

Ask for a scoped change, relevant checks, a reviewable diff, and a short account of resulting behavior and remaining limits. Identify any branch or PR actions you actually want. A request to review code alone does not establish an instruction to merge or deploy it.

**Check:** tests and artifacts actually exist, and unrelated files are preserved. **Improve:** intentionally remove a required source and check whether the dot reports the blocker honestly.

Back: [guide](README.md).
