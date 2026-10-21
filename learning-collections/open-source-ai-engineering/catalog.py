"""Browse and render a documentation-reviewed AI engineering resource catalog.

This script performs no network calls, installations, or product execution.
The metadata is a dated snapshot, not an upstream availability monitor.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "resources.json"
OSI_LABELS = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "PostgreSQL", "Apache-2.0 AND MIT"}
PURPOSES = {
    "ollama/ollama": "Run supported models through a local model service.",
    "ggml-org/llama.cpp": "Explore efficient local inference and model-format trade-offs.",
    "vllm-project/vllm": "Study model serving, batching, and GPU memory behavior.",
    "sgl-project/sglang": "Investigate high-throughput language-model serving.",
    "huggingface/transformers": "Work with tokenizers and supported pretrained model architectures.",
    "huggingface/peft": "Explore parameter-efficient model adaptation.",
    "huggingface/trl": "Study post-training workflows and preference-learning experiments.",
    "huggingface/diffusers": "Inspect diffusion-model pipelines and generation components.",
    "langchain-ai/langchain": "Build language applications with reusable integrations.",
    "langchain-ai/langgraph": "Represent stateful agent workflows with explicit control flow.",
    "run-llama/llama_index": "Connect application data to retrieval and language workflows.",
    "deepset-ai/haystack": "Compose retrieval and document-processing pipelines.",
    "pydantic/pydantic-ai": "Build typed agent applications with inspectable interfaces.",
    "microsoft/autogen": "Study agent patterns after resolving component-level license scope.",
    "crewAIInc/crewAI": "Explore role-oriented agent coordination and handoffs.",
    "modelcontextprotocol/python-sdk": "Implement MCP capabilities in Python.",
    "modelcontextprotocol/typescript-sdk": "Implement MCP capabilities in TypeScript.",
    "PrefectHQ/fastmcp": "Build and inspect MCP tool servers with a higher-level interface.",
    "modelcontextprotocol/inspector": "Inspect and debug MCP server interactions.",
    "pgvector/pgvector": "Add vector similarity operations alongside relational data.",
    "qdrant/qdrant": "Explore vector search with structured metadata constraints.",
    "chroma-core/chroma": "Prototype an application vector index and retrieval path.",
    "weaviate/weaviate": "Study search features in the documented open-source core.",
    "milvus-io/milvus": "Investigate vector-data infrastructure at larger scale.",
    "facebookresearch/faiss": "Compare local similarity-search indexes and recall trade-offs.",
    "opensearch-project/OpenSearch": "Explore searchable documents, filters, and ranking.",
    "vibrantlabsai/ragas": "Design retrieval and language-application evaluation experiments.",
    "confident-ai/deepeval": "Express and run language-application evaluation checks.",
    "promptfoo/promptfoo": "Compare prompt/model behavior with repeatable test cases.",
    "Arize-ai/phoenix": "Study AI tracing under the repository's source-available terms.",
    "langfuse/langfuse": "Inspect model traces and evaluation workflows in the MIT core.",
    "open-telemetry/opentelemetry-python": "Instrument request paths with standard telemetry concepts.",
    "mlflow/mlflow": "Track experiments and model/application evaluation artifacts.",
    "docling-project/docling": "Extract document structure for review and retrieval.",
    "Unstructured-IO/unstructured": "Partition document content into useful processing elements.",
    "pymupdf/PyMuPDF": "Inspect and transform PDFs under the applicable AGPL terms.",
    "PaddlePaddle/PaddleOCR": "Explore OCR and document-image extraction.",
    "openai/whisper": "Experiment with speech recognition on permitted audio.",
    "SYSTRAN/faster-whisper": "Compare an optimized Whisper implementation on your hardware.",
    "OHF-Voice/piper1-gpl": "Explore local speech synthesis and separate voice-model licensing.",
    "livekit/agents": "Build real-time voice-agent application flows.",
    "pipecat-ai/pipecat": "Compose streaming voice and multimodal application stages.",
    "streamlit/streamlit": "Build a small Python interface around a data experiment.",
    "gradio-app/gradio": "Create an inspectable interface for an AI demonstration.",
    "fastapi/fastapi": "Expose validated application behavior over HTTP.",
    "pydantic/pydantic": "Validate input/output shape and domain data structures.",
    "apache/airflow": "Schedule and observe dependency-based data jobs.",
    "dagster-io/dagster": "Model data assets and their operational dependencies.",
    "PrefectHQ/prefect": "Orchestrate Python tasks and inspect failed runs.",
    "duckdb/duckdb": "Run exact analytical queries over local datasets.",
    "dbt-labs/dbt": "Study versioned SQL transformation workflows.",
    "microsoft/ai-agents-for-beginners": "Learn agent patterns through lessons and code examples.",
    "microsoft/generative-ai-for-beginners": "Build foundational generative-AI understanding with exercises.",
    "anthropics/claude-cookbooks": "Study documented application and evaluation examples.",
    "humanlayer/12-factor-agents": "Review engineering principles for agent applications.",
    "BerriAI/litellm": "Study provider routing in the MIT core and its integration boundaries.",
    "FlowiseAI/Flowise": "Inspect an archived visual-workflow project as a historical reference.",
    "langflow-ai/langflow": "Explore visual composition of AI application workflows.",
    "browser-use/browser-use": "Study model-directed browser interaction with scoped tasks.",
    "microsoft/playwright": "Automate and verify browser behavior through deterministic code.",
    "n8n-io/n8n": "Study workflow orchestration under Sustainable Use and enterprise terms.",
    "open-webui/open-webui": "Inspect a model interface under its custom license conditions.",
}
EXERCISES = {
    "local-inference": "Measure one small prompt's latency and peak memory; record hardware and model license.",
    "models-adaptation": "Inspect a minimal example; separate training data, validation data, and held-out evaluation.",
    "agents": "Build a bounded synthetic task and deliberately trigger one failed tool call.",
    "retrieval": "Retrieve a policy exception and test a question with no supporting evidence.",
    "mcp": "Expose a read-only synthetic lookup and test malformed arguments and denied scope.",
    "search-storage": "Compare exact-ID and paraphrase queries while preserving a tenant filter.",
    "evaluation": "Create normal, missing-evidence, and denied-action cases; inspect a false pass.",
    "observability": "Trace a synthetic request without logging its full payload; locate a deliberately slow stage.",
    "documents": "Parse a synthetic table and check reading order, headers, and source coordinates.",
    "voice": "Use permitted synthetic audio; inspect entity errors, interruption behavior, and latency.",
    "apps": "Create a small review interface with explicit unknown and error states.",
    "data-orchestration": "Run an incremental synthetic data job twice and inspect duplicate/retry behavior.",
    "learning": "Complete one exercise and explain one failure without reading the solution.",
    "gateway": "Simulate a timeout and verify the fallback stays inside the original time/data policy.",
    "browser": "Complete a synthetic local-page task and verify the actual final page state.",
    "source-available": "Read the current license and identify which proposed uses need further review.",
}


def load(path: Path = DATA) -> list[dict]:
    rows = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(rows, list) or not rows:
        raise ValueError("catalog must be a nonempty array")
    seen = set()
    for r in rows:
        required = ("repository", "url", "category", "classification", "license", "checked_on", "readme_url")
        if any(not isinstance(r.get(k), str) or not r[k] for k in required):
            raise ValueError("missing catalog evidence")
        if r["repository"] in seen or r["url"] != "https://github.com/" + r["repository"]:
            raise ValueError("duplicate or mismatched repository identity")
        if r["verification"] != "metadata_and_readme_reviewed" or r["execution_tested"] is not False:
            raise ValueError("review and execution status must remain explicit")
        if r["classification"] == "open-source" and (r["license"] not in OSI_LABELS or r["archived"]):
            raise ValueError("unresolved/archived project in active open-source list")
        if r["repository"] not in PURPOSES:
            raise ValueError("add an original use-case annotation before publishing")
        seen.add(r["repository"])
    return rows


def select(rows: list[dict], category: str | None = None, classification: str = "open-source") -> list[dict]:
    return [r for r in rows if (category is None or r["category"] == category)
            and (classification == "all" or r["classification"] == classification)]


def table(rows: list[dict]) -> str:
    lines = ["| Project | What to use it for | First exercise | License/scope |", "|---|---|---|---|"]
    for r in sorted(rows, key=lambda x: x["repository"].lower()):
        scope = r.get("license_note", r["license"])
        lines.append(f"| [{r['repository']}]({r['url']}) | {PURPOSES[r['repository']]} | {EXERCISES[r['category']]} | {scope} |")
    return "\n".join(lines)


def build(rows: list[dict]) -> None:
    categories = sorted({r["category"] for r in rows if r["classification"] == "open-source"})
    directory = ROOT / "categories"
    directory.mkdir(exist_ok=True)
    for category in categories:
        subset = select(rows, category)
        text = f"# {category.replace('-', ' ').title()}\n\nDocumentation-reviewed candidates; no installation or end-to-end execution is claimed. Start from each project's current README.\n\n{table(subset)}\n\nSoftware licensing does not include every model weight, dataset, hosted feature, or third-party service. Local hardware and hosted APIs may introduce costs.\n\nBack: [catalog](../README.md).\n"
        (directory / f"{category}.md").write_text(text, encoding="utf-8")
    main = select(rows)
    appendix = [r for r in rows if r["classification"] != "open-source"]
    lines = ["# Open-source AI Engineering: a practical catalog", "",
             f"**{len(main)} open-source entries, with {len(appendix)} separately classified references. Checked 21 October 2026.**", "",
             "An independent collection by Swapnil AI Labs for FDE and AI system-design learners. Each entry has an original use-case note, a first exercise, canonical repository identity, observed license metadata, and a dated README review. No listed project was installed or benchmarked as part of this catalog.", "",
             "## Choose a topic", "", "| Topic | Entries |", "|---|---:|"]
    lines += [f"| [{c.replace('-', ' ').title()}](categories/{c}.md) | {len(select(rows,c))} |" for c in categories]
    lines += ["", "## Browse locally", "", "Run from this collection folder with Python 3.11+; no packages or API keys are required to browse the snapshot.", "", "```bash", "python catalog.py --category evaluation", "python catalog.py --classification open-source-core", "python catalog.py --classification all --json", "python catalog.py --build", "```", "",
              "The last command regenerates this README, category pages, and the appendix from the reviewed JSON plus the original annotations in catalog.py. It does not recheck GitHub or execute upstream software.", "",
              "## How to learn from the collection", "", "Read [the learning paths](LEARNING-PATHS.md), choose one small experiment, follow its current upstream setup instructions, and record what you actually ran. Keep environment, model/data licenses, errors, timing, and known limits with the result.", "",
              "## Cost and license scope", "", "Open-source software can require paid hosting, API usage, a GPU, or separately licensed model weights/data. Some examples depend on commercial providers even when the application code is open source. The main list uses identified open-source software-license labels; it is not a complete file-by-file legal audit.", "",
              "Read [the classified appendix](CLASSIFIED-REFERENCES.md) for open-core, source-available, archived, or unresolved-license projects. Do not silently relabel those as unrestricted open source.", "",
              "## Source data and maintenance", "", "The [JSON dataset](data/resources.json) records canonical URLs, license evidence, branch, archive status, upstream push timestamp, and verification method. Pushed-at is an observation, not a promise of active support. Recheck upstream before adoption; mark execution-tested only with a separate reproducible report.", "",
              "Original catalog annotations and tooling are MIT-licensed by Swapnil Mandloi. External projects retain their own terms. Contribute a source, a clear explanation, and an appropriate exercise rather than copying an upstream tutorial."]
    (ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    appendix_text = ["# Separately classified references", "", "These entries are excluded from the main active open-source list. Their exact component, license, or maintenance status matters.", ""]
    for classification in sorted({r["classification"] for r in appendix}):
        appendix_text += ["## " + classification.replace("-", " ").title(), "", table([r for r in appendix if r["classification"] == classification]), ""]
    appendix_text += ["Back: [catalog](README.md).", ""]
    (ROOT / "CLASSIFIED-REFERENCES.md").write_text("\n".join(appendix_text), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--category")
    parser.add_argument("--classification", choices=["open-source", "open-source-core", "source-available", "license-review-needed", "archived-reference", "all"], default="open-source")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--build", action="store_true")
    args = parser.parse_args()
    rows = load()
    if args.build:
        build(rows)
    result = select(rows, args.category, args.classification)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for r in result:
            print(f"{r['repository']} | {r['license']} | {r['classification']}")
        print(f"{len(result)} matching entries; documentation review only.")


if __name__ == "__main__":
    main()
