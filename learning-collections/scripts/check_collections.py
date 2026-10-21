"""Check local links, fenced blocks, package basics, and generated catalog pages."""
from __future__ import annotations

import importlib.util
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = (
    "fde-field-drills", "ai-system-design-patterns", "open-source-ai-engineering",
    "meta-muse-practical-guide", "chatgpt-dots-practical-guide", "grok-bot-practical-guide",
)


def main() -> int:
    errors = []
    markdown_files = sorted(ROOT.rglob("*.md"))
    for path in markdown_files:
        fence = None
        prose = []
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            match = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
            if match:
                marker, tail = match.groups()
                if fence is None:
                    fence = (marker[0], len(marker), number)
                elif marker[0] == fence[0] and len(marker) >= fence[1] and not tail.strip():
                    fence = None
                continue
            if fence is None:
                prose.append(line)
        if fence:
            errors.append(f"{path.relative_to(ROOT)}:{fence[2]}: unclosed code fence")
        for link in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", "\n".join(prose)):
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT):
                errors.append(f"{path.relative_to(ROOT)}: local link leaves collection root: {link}")
            elif not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing local target: {link}")
    for package in PACKAGES:
        for filename in ("README.md", "LICENSE"):
            if not (ROOT / package / filename).is_file():
                errors.append(f"{package}: missing {filename}")
    spec = importlib.util.spec_from_file_location("collection_catalog", ROOT / "open-source-ai-engineering" / "catalog.py")
    catalog = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(catalog)
    try:
        rows = catalog.load()
        source_root = catalog.ROOT
        with tempfile.TemporaryDirectory() as temporary:
            catalog.ROOT = Path(temporary)
            catalog.build(rows)
            generated = list(catalog.ROOT.rglob("*.md"))
            for generated_file in generated:
                relative = generated_file.relative_to(catalog.ROOT)
                original = source_root / relative
                if not original.exists() or original.read_bytes() != generated_file.read_bytes():
                    errors.append(f"catalog generated page is stale: {relative}")
            expected = {p.relative_to(catalog.ROOT) for p in generated if p.parent.name == "categories"}
            actual = {p.relative_to(source_root) for p in (source_root / "categories").glob("*.md")}
            if expected != actual:
                errors.append("catalog category page set is stale")
        catalog.ROOT = source_root
    except (KeyError, TypeError, ValueError) as error:
        errors.append(f"catalog data rejected: {error}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Checked {len(markdown_files)} Markdown files, six package licenses, and reproducible catalog pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
