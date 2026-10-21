"""A lexical, extractive retrieval lab: filtering happens before scoring.

This is not semantic RAG, authentication, or a complete policy-answer engine.
The caller supplies synthetic identity for experiments; real services must
derive identity and groups from a trusted authentication/authorization layer.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

DATA = Path(__file__).parent / "data" / "documents.json"
STOPWORDS = frozenset("a an the is are be can what when how does do long it i to of for on in at my me and with please".split())


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower())) - STOPWORDS


def load_documents(path: Path = DATA) -> list[dict]:
    documents = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(documents, list):
        raise ValueError("documents must be an array")
    seen = set()
    for doc in documents:
        if not isinstance(doc, dict):
            raise ValueError("each document must be an object")
        for field in ("id", "tenant", "title", "section", "text"):
            if not isinstance(doc.get(field), str) or not doc[field]:
                raise ValueError(f"invalid document field: {field}")
        if type(doc.get("version")) is not int or doc["version"] < 1:
            raise ValueError("version must be a positive integer")
        if type(doc.get("active")) is not bool:
            raise ValueError("active must be boolean")
        if not isinstance(doc.get("groups"), list) or not all(isinstance(g, str) and g for g in doc["groups"]):
            raise ValueError("groups must be a list of nonempty strings")
        key = (doc["tenant"], doc["id"], doc["version"])
        if key in seen:
            raise ValueError("duplicate document version")
        seen.add(key)
    return documents


def retrieve(question: str, tenant: str, groups: set[str], documents: list[dict], limit: int = 3) -> dict:
    if limit < 1:
        raise ValueError("limit must be positive")
    query = tokens(question)
    # Choose the latest active version BEFORE access evaluation, so a group
    # cannot fall back to an old version after permissions change.
    current: dict[str, dict] = {}
    for doc in documents:
        if doc["tenant"] == tenant and doc["active"]:
            if doc["id"] not in current or doc["version"] > current[doc["id"]]["version"]:
                current[doc["id"]] = doc
    permitted = [doc for doc in current.values() if groups.intersection(doc["groups"])]
    hits = []
    for doc in permitted:
        overlap = query.intersection(tokens(doc["title"] + " " + doc["text"]))
        if not overlap:
            continue
        # A teaching score, not a confidence probability or BM25.
        score = len(overlap) / max(len(query), 1)
        sentences = re.split(r"(?<=[.!?])\s+", doc["text"])
        excerpts = [s for s in sentences if tokens(s).intersection(query)]
        hits.append({"source": f"{doc['id']}@{doc['version']}",
                     "tenant": doc["tenant"], "title": doc["title"],
                     "section": doc["section"], "score": round(score, 4),
                     "evidence": " ".join(excerpts) or doc["text"]})
    hits.sort(key=lambda item: (-item["score"], item["source"]))
    selected = hits[:limit]
    return {"question": question, "outcome": "evidence_found" if selected else "abstain",
            "note": "Extractive lexical evidence only; no generated answer or semantic verification.",
            "citations": selected}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--question", required=True)
    parser.add_argument("--tenant", default="acme")
    parser.add_argument("--groups", nargs="*", default=["support"])
    parser.add_argument("--limit", type=int, default=3)
    args = parser.parse_args()
    print(json.dumps(retrieve(args.question, args.tenant, set(args.groups), load_documents(), args.limit), indent=2))


if __name__ == "__main__":
    main()
