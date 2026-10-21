"""Check local links, fenced blocks, JSON fixtures, and promised content counts.

External URLs are intentionally not requested: network availability should not
make the offline checks nondeterministic. This is a small checker for this
repository's Markdown conventions, not a complete Markdown parser.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")


def check() -> list[str]:
    errors = []
    markdown = [p for p in ROOT.rglob("*.md") if ".git" not in p.relative_to(ROOT).parts]
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        fenced = False
        visible = []
        for line in text.splitlines():
            if line.lstrip().startswith("```"):
                fenced = not fenced
                continue
            if not fenced:
                visible.append(line)
        if fenced:
            errors.append(f"{path.relative_to(ROOT)}: unclosed code fence")
        for target in LINK.findall("\n".join(visible)):
            target = target.split(' "', 1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(ROOT):
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            elif not destination.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing target: {target}")
    for path in (ROOT / "labs" / "data").glob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
    expected = {"chapters": 26, "cases": 7, "templates": 8, "questions": 60}
    actual = {"chapters": len(list((ROOT / "chapters").glob("[0-9][0-9]-*.md"))),
              "cases": len(list((ROOT / "case-studies").glob("[0-9][0-9]-*.md"))),
              "templates": len([p for p in (ROOT / "templates").glob("*.md") if p.name != "README.md"]),
              "questions": len(re.findall(r"^### \d+\. ", (ROOT / "interview" / "question-bank.md").read_text(encoding="utf-8"), re.M))}
    for key, value in expected.items():
        if actual[key] != value:
            errors.append(f"promised {value} {key}; found {actual[key]}")
    return errors


if __name__ == "__main__":
    problems = check()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        raise SystemExit(1)
    print("Documentation checks passed: local links, code fences, JSON, and content counts.")
