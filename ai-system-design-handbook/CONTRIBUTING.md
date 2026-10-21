# Contributing

Help a reader understand one thing better. Useful contributions include a clearer explanation, a corrected calculation, a small reproducible lab, a carefully labeled evaluation case, or a worked failure/recovery example.

## Before changing content

Read the relevant chapter and its prerequisites. Keep English plain and define new terms before using them. Explain the mechanism, a concrete example, a trade-off, and how to verify the behavior. Avoid unsupported “best tool” claims and invented production outcomes.

For changing APIs, models, pricing, protocol versions, or deployment features, consult the current official primary source and record a verification date. Credit reused material and preserve its license. Do not copy chapters from another learning repository.

## A contribution workflow

1. Fork or branch the repository and make one coherent change.
2. Use only synthetic or explicitly permitted data. Never commit credentials or private records.
3. Add meaningful tests when behavior changes; avoid tests that merely repeat implementation details.
4. Run the local checks below.
5. Open a pull request explaining the problem, resulting behavior, validation, and limitations.

Run these from `ai-system-design-handbook/` inside the parent FDE repository:

```bash
python -m unittest discover -s tests -v
python -m labs.evaluate
python scripts/check_docs.py
```

The docs checker validates this repository's local file links, code fences, fixtures, and promised counts. It does not check external website availability or render every Markdown extension. Inspect diagrams and examples manually when you change them.

## New chapters or labs

Update the main README, index, next/previous navigation where relevant, roadmap, and content counts in the checker. Keep the default quickstart offline unless an added dependency clearly improves the learning outcome. Label simulated providers and missing production controls next to the code and output.

## Review expectations

A reviewer should be able to reproduce your example and understand the change without reading a chat history. Include actual validation results and known gaps. Questions and corrections are welcome even when you do not yet have a code patch.
