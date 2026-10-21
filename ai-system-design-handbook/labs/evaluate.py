"""Evaluate synthetic source hits and abstention; not answer faithfulness."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from labs.mini_rag import load_documents, retrieve

CASES = Path(__file__).parent / "data" / "eval_cases.json"


def evaluate(cases: list[dict], documents: list[dict]) -> dict:
    if not cases:
        raise ValueError("at least one evaluation case is required")
    rows = []
    relevant_count = source_hits = correct_abstention = 0
    for case in cases:
        result = retrieve(case["question"], case["tenant"], set(case["groups"]), documents)
        source_ids = [hit["source"] for hit in result["citations"]]
        hit = case["expected_source"] in source_ids if case["expected_source"] else None
        if hit is not None:
            relevant_count += 1
            source_hits += int(hit)
        abstention_ok = (result["outcome"] == "abstain") == case["should_abstain"]
        correct_abstention += int(abstention_ok)
        rows.append({"id": case["id"], "source_hit": hit,
                     "abstention_correct": abstention_ok,
                     "pass": abstention_ok and hit is not False})
    return {"cases": len(cases), "answerable_cases": relevant_count,
            "source_hit_at_3": source_hits / relevant_count if relevant_count else None,
            "abstention_accuracy": correct_abstention / len(cases),
            "passed": sum(row["pass"] for row in rows), "results": rows,
            "limitation": "Tiny synthetic smoke set; source hits do not establish answer correctness or security."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=CASES)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evaluate(json.loads(args.cases.read_text(encoding="utf-8")), load_documents())
    rendered = json.dumps(report, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    if report["passed"] != report["cases"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
