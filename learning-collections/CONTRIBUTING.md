# Contributing

Make the next learner's first useful step easier. Contributions should use clear English, original explanations, synthetic or permitted data, and concrete expected behavior.

## Product guide updates

Use the current official documentation. Add its URL and review date to the collection's SOURCES file. Distinguish documented behavior from a proposed exercise and from an actual executed result. Do not add guessed SDKs, subscriptions, menu labels, or availability claims. Never contribute credentials or private account material.

## Catalog updates

Update `open-source-ai-engineering/data/resources.json`, then add an original purpose note and an appropriate exercise in `catalog.py`. Verify canonical repository identity, README, archive status, and license scope. An open core, custom license, unresolved license, or archived repository belongs in its corresponding separate classification.

The dataset records a documentation review. Keep `execution_tested` false; attach reproducible run reports separately with environment, version, commands, inputs, observed result, and limitations. Do not turn a metadata review into an execution claim.

Regenerate catalog pages with:

```bash
python open-source-ai-engineering/catalog.py --build
```

## Drills and patterns

Explain the problem before naming a tool. Include an invariant or success condition, a failure case, and a way to inspect the result. Keep planning assumptions separate from measured outcomes. Credit external sources without copying their tutorials.

## Before submitting

From the `learning-collections` directory:

```bash
python scripts/check_collections.py
python -m unittest discover -s tests -v
```

Describe what changed, why it helps a learner, and what you actually checked. Original contributions are offered under this collection's MIT License; upstream projects keep their own terms.
