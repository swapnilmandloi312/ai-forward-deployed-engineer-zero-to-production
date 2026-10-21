"""Compute an exact, tenant-scoped baseline from a synthetic ticket export."""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

DEFAULT_DATA = Path(__file__).resolve().parent / "data" / "tickets.csv"
CATEGORIES = {"export", "access", "billing"}


def summarize(path: Path, tenant: str) -> dict:
    if not tenant.strip():
        raise ValueError("tenant is required")
    latest = {}
    observations = {}
    row_count = 0
    with path.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        if not {"tenant", "ticket_id", "updated_at", "category"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV is missing required columns")
        for row in reader:
            # Scope first: another tenant's data must not affect this result.
            if row["tenant"] != tenant:
                continue
            row_count += 1
            ticket = row["ticket_id"]
            if not ticket or row["category"] not in CATEGORIES:
                raise ValueError("ticket ID and a recognized category are required")
            timestamp = datetime.fromisoformat(row["updated_at"])
            if timestamp.tzinfo is None or timestamp.utcoffset() is None:
                raise ValueError("updated_at must include a UTC offset")
            key = (ticket, timestamp)
            if key in observations and observations[key] != row["category"]:
                raise ValueError("conflicting categories at the same ticket timestamp")
            observations[key] = row["category"]
            if ticket not in latest or timestamp > latest[ticket][0]:
                latest[ticket] = (timestamp, row["category"])
    counts = Counter(value[1] for value in latest.values())
    return {
        "tenant": tenant,
        "source_rows": row_count,
        "unique_tickets": len(latest),
        "duplicate_rows_removed": row_count - len(latest),
        "categories": {category: counts[category] for category in sorted(CATEGORIES)},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--tenant", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = summarize(args.input, args.tenant)
    except (OSError, ValueError) as error:
        parser.exit(2, f"Input rejected: {error}\n")
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Tenant: {result['tenant']}")
        print(f"{result['source_rows']} rows; {result['unique_tickets']} unique tickets; "
              f"{result['duplicate_rows_removed']} duplicate rows removed")
        for category, count in result["categories"].items():
            print(f"{category}: {count}")


if __name__ == "__main__":
    main()
