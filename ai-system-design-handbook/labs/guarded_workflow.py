"""Atomic, approved invoice posting INSIDE ONE SQLite database.

No external accounting API is called. The local transaction intentionally
avoids cross-system effects, for which destination idempotency/reconciliation
would also be required. Approval here is a synthetic boolean, not real auth.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from decimal import Decimal, InvalidOperation


class ConflictError(ValueError):
    """An idempotency key or business invoice identity was reused incorrectly."""


def connect(path: str = ":memory:") -> sqlite3.Connection:
    db = sqlite3.connect(path)
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript("""
        CREATE TABLE IF NOT EXISTS entries (
          id INTEGER PRIMARY KEY, tenant TEXT NOT NULL, vendor TEXT NOT NULL,
          invoice_number TEXT NOT NULL, amount_cents INTEGER NOT NULL,
          currency TEXT NOT NULL,
          UNIQUE(tenant, vendor, invoice_number)
        );
        CREATE TABLE IF NOT EXISTS operations (
          tenant TEXT NOT NULL, operation_id TEXT NOT NULL,
          payload_hash TEXT NOT NULL, entry_id INTEGER NOT NULL REFERENCES entries(id),
          PRIMARY KEY(tenant, operation_id)
        );
    """)
    return db


def normalize(payload: dict) -> dict:
    fields = {"tenant", "vendor", "invoice_number", "amount", "currency"}
    if set(payload) != fields:
        raise ValueError("payload requires exactly tenant, vendor, invoice_number, amount, currency")
    for field in ("tenant", "vendor", "invoice_number", "currency"):
        if not isinstance(payload[field], str) or not payload[field].strip():
            raise ValueError(f"{field} must be a nonempty string")
    if payload["currency"] not in {"USD", "INR"}:
        raise ValueError("only synthetic USD and INR examples are supported")
    if not isinstance(payload["amount"], str):
        raise ValueError("amount must be a decimal string")
    try:
        amount = Decimal(payload["amount"])
    except InvalidOperation as exc:
        raise ValueError("invalid amount") from exc
    if not amount.is_finite() or amount <= 0 or amount > Decimal("1000000"):
        raise ValueError("amount must be finite, positive, and no greater than 1000000")
    if amount != amount.quantize(Decimal("0.01")):
        raise ValueError("amount must have at most two nonzero decimal places")
    result = {k: payload[k].strip() for k in ("tenant", "vendor", "invoice_number", "currency")}
    result["amount_cents"] = int(amount * 100)
    return result


def post_invoice(db: sqlite3.Connection, operation_id: str, payload: dict,
                 approved: bool, allowed_vendors: set[str]) -> dict:
    if not isinstance(operation_id, str) or not operation_id.strip():
        raise ValueError("operation_id is required")
    record = normalize(payload)
    if record["vendor"] not in allowed_vendors:
        raise PermissionError("vendor is outside the synthetic allowlist")
    if approved is not True:
        return {"status": "review_required", "entry_id": None}
    digest = hashlib.sha256(json.dumps(record, sort_keys=True).encode()).hexdigest()
    # BEGIN IMMEDIATE serializes competing writers. Both ledger changes are
    # committed together; rollback preserves atomicity when an insert fails.
    try:
        db.execute("BEGIN IMMEDIATE")
        prior = db.execute(
            "SELECT payload_hash, entry_id FROM operations WHERE tenant=? AND operation_id=?",
            (record["tenant"], operation_id),
        ).fetchone()
        if prior:
            if prior[0] != digest:
                raise ConflictError("operation key reused with a different payload")
            db.commit()
            return {"status": "duplicate", "entry_id": prior[1]}
        cursor = db.execute(
            "INSERT INTO entries(tenant,vendor,invoice_number,amount_cents,currency) VALUES (?,?,?,?,?)",
            tuple(record[k] for k in ("tenant", "vendor", "invoice_number", "amount_cents", "currency")),
        )
        db.execute("INSERT INTO operations VALUES (?,?,?,?)",
                   (record["tenant"], operation_id, digest, cursor.lastrowid))
        db.commit()
        return {"status": "posted_locally", "entry_id": cursor.lastrowid}
    except sqlite3.IntegrityError as exc:
        db.rollback()
        raise ConflictError("business invoice already exists under another operation key") from exc
    except BaseException:
        db.rollback()
        raise


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", default=":memory:")
    parser.add_argument("--approve", action="store_true", help="synthetic demo approval only")
    args = parser.parse_args()
    payload = {"tenant": "acme", "vendor": "vendor-7", "invoice_number": "DEMO-001",
               "amount": "1250.50", "currency": "USD"}
    db = connect(args.db)
    try:
        results = [post_invoice(db, "op-demo-1", payload, args.approve, {"vendor-7"}) for _ in range(2)]
        print(json.dumps({"attempts": results, "local_entries": db.execute("SELECT COUNT(*) FROM entries").fetchone()[0]}, indent=2))
    finally:
        db.close()


if __name__ == "__main__":
    main()
