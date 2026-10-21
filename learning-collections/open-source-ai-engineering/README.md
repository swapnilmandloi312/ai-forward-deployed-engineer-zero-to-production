# Open-source AI Engineering: a practical catalog

**54 open-source entries, with 8 separately classified references. Checked 21 October 2026.**

An independent collection by Swapnil AI Labs for FDE and AI system-design learners. Each entry has an original use-case note, a first exercise, canonical repository identity, observed license metadata, and a dated README review. No listed project was installed or benchmarked as part of this catalog.

## Choose a topic

| Topic | Entries |
|---|---:|
| [Agents](categories/agents.md) | 4 |
| [Apps](categories/apps.md) | 5 |
| [Browser](categories/browser.md) | 2 |
| [Data Orchestration](categories/data-orchestration.md) | 5 |
| [Documents](categories/documents.md) | 4 |
| [Evaluation](categories/evaluation.md) | 3 |
| [Learning](categories/learning.md) | 4 |
| [Local Inference](categories/local-inference.md) | 4 |
| [Mcp](categories/mcp.md) | 4 |
| [Models Adaptation](categories/models-adaptation.md) | 4 |
| [Observability](categories/observability.md) | 2 |
| [Retrieval](categories/retrieval.md) | 2 |
| [Search Storage](categories/search-storage.md) | 6 |
| [Voice](categories/voice.md) | 5 |

## Browse locally

Run from this collection folder with Python 3.11+; no packages or API keys are required to browse the snapshot.

```bash
python catalog.py --category evaluation
python catalog.py --classification open-source-core
python catalog.py --classification all --json
python catalog.py --build
```

The last command regenerates this README, category pages, and the appendix from the reviewed JSON plus the original annotations in catalog.py. It does not recheck GitHub or execute upstream software.

## How to learn from the collection

Read [the learning paths](LEARNING-PATHS.md), choose one small experiment, follow its current upstream setup instructions, and record what you actually ran. Keep environment, model/data licenses, errors, timing, and known limits with the result.

## Cost and license scope

Open-source software can require paid hosting, API usage, a GPU, or separately licensed model weights/data. Some examples depend on commercial providers even when the application code is open source. The main list uses identified open-source software-license labels; it is not a complete file-by-file legal audit.

Read [the classified appendix](CLASSIFIED-REFERENCES.md) for open-core, source-available, archived, or unresolved-license projects. Do not silently relabel those as unrestricted open source.

## Source data and maintenance

The [JSON dataset](data/resources.json) records canonical URLs, license evidence, branch, archive status, upstream push timestamp, and verification method. Pushed-at is an observation, not a promise of active support. Recheck upstream before adoption; mark execution-tested only with a separate reproducible report.

Original catalog annotations and tooling are MIT-licensed by Swapnil Mandloi. External projects retain their own terms. Contribute a source, a clear explanation, and an appropriate exercise rather than copying an upstream tutorial.
