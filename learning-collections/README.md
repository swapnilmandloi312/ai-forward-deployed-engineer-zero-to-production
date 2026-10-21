# FDE and AI System Design Learning Collections

**Practical, plain-English learning by Swapnil Mandloi · Swapnil AI Labs.**

Build engineering judgment through clear explanations, synthetic exercises, source-backed product guides, and a searchable open-source catalog. These six self-contained collections are published here inside the FDE repository. Each has its own README and license so it can also be maintained as a separate repository.

## Choose a collection

| Collection | What you get | Start with |
|---|---|---|
| [FDE Field Drills](fde-field-drills/README.md) | Three worked cases, answer keys, a submission template, synthetic data, and an offline baseline tool | Count the support tickets correctly before proposing an agent |
| [AI System Design Patterns](ai-system-design-patterns/README.md) | Eight architecture cards with diagrams, failure modes, exercises, and a review template | Design retrieval that preserves permissions and freshness |
| [Open-source AI Engineering](open-source-ai-engineering/README.md) | 54 open-source entries across 14 categories, eight separately classified references, learning paths, JSON data, and a Python browser | Choose one experiment rather than install every tool |
| [Meta Muse Practical Guide](meta-muse-practical-guide/README.md) | Agent/model distinction, first-task walkthrough, four playbooks, review steps, and official sources | Prepare a bounded research brief with visible evidence gaps |
| [ChatGPT dots Practical Guide](chatgpt-dots-practical-guide/README.md) | Setup, task scope, source access, ongoing responsibilities, five recipes, and troubleshooting | Turn a vague project request into a reviewable artifact |
| [Grok Bot Practical Guide](grok-bot-practical-guide/README.md) | Bot creation, role handoffs, memory/state boundaries, four playbooks, and official sources | Give a research Bot one clear job and inspect its output |

The product guides cover proprietary services. They are not entries in the open-source software list. Documentation was reviewed on **21 October 2026**; access and interface details can change. Product recipes have not been executed in signed-in accounts, and no comparative benchmark is claimed.

## A practical route through the material

1. Complete the first FDE drill using the included CSV and baseline tool.
2. Read the authorized-retrieval and reviewed-action design cards.
3. Choose one open-source learning path and follow current upstream setup instructions.
4. Try a product recipe only if your account supports it; inspect the actual resulting artifact.
5. Write a short evidence report with commands, failures, sources, assumptions, and next decisions.

For broader preparation, use the [AI System Design Handbook](https://github.com/swapnilmandloi312/ai-forward-deployed-engineer-zero-to-production/tree/main/ai-system-design-handbook), the [FDE roadmap](https://github.com/swapnilmandloi312/ai-forward-deployed-engineer-zero-to-production/blob/main/ROADMAP.md), and the [FDE resource repository](https://github.com/swapnilmandloi312/swapnil-fde-resources).

## Run the offline tools

From this `learning-collections` directory with Python 3.11+:

```bash
python fde-field-drills/analyze_tickets.py --tenant north
python open-source-ai-engineering/catalog.py --category evaluation
python open-source-ai-engineering/catalog.py --classification all --json
python scripts/check_collections.py
python -m unittest discover -s tests -v
```

These commands need no API keys or third-party Python packages. They analyze the included synthetic data, browse the reviewed catalog, and check this educational collection. Running a listed upstream project is a separate task and may require dependencies, compute, model access, or payment.

## Compare products fairly

Use [the same-task review worksheet](SAME-TASK-REVIEW.md) if you try more than one product. Keep inputs, source access, requested outcome, and review criteria comparable. Separate product unavailability from task failure. Record the date and account capabilities; do not publish invented scores or infer private product architectures.

## Contribute useful evidence

Read [CONTRIBUTING.md](CONTRIBUTING.md). Improvements should make a concept clearer, reproduce a failure, add a useful original exercise, or update an official source. A long link dump without explanation is harder to learn from than a small collection with a clear first step.

Original text, diagrams, and local tooling use the [MIT License](LICENSE). External software, documentation, model weights, datasets, and connected services retain their own terms. An open-source library does not make every hosted feature or model free.
