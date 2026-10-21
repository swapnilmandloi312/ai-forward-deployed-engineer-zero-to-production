# 02 · The Python, API, and SQL bridge

**Prerequisites:** Chapter 1. **Goal:** understand how data moves through an AI application.

## Start with a record

A dictionary stores related fields under keys. A list stores several records. A function turns input into output. An exception tells the caller that an operation could not complete normally.

```python
from decimal import Decimal, InvalidOperation

def invoice_total(record):
    try:
        amount = Decimal(str(record["amount"]))
    except (KeyError, InvalidOperation) as exc:
        raise ValueError("amount is required and must be decimal") from exc
    if not amount.is_finite() or amount < 0:
        raise ValueError("amount must be finite and non-negative")
    return amount

print(invoice_total({"amount": "1250.50"}))
```

Use decimal arithmetic for money. A floating-point number is a useful approximation for many calculations but can introduce small rounding surprises. A real invoice also needs currency, line-item validation, tax treatment, and a defined rounding policy.

**Everyday intuition:** an API is an agreed service counter between two systems. Both sides need to understand the request format, the response format, and the possible errors.

## HTTP and JSON

An HTTP request has a method, a URL, headers, and sometimes a body. A response has a status and a body. JSON is a common text format for structured bodies. A `POST` to create a job might return `202 Accepted` and a job ID while a background worker processes the document.

| Status family | Typical meaning | Application response |
|---|---|---|
| 2xx | Request handled successfully | Validate the response shape too |
| 400/422 | Invalid input | Fix input; blind retry will not help |
| 401/403 | Identity or permission failure | Correct credentials/access; avoid automatic loops |
| 429 | Rate limit reached | Respect retry guidance within a bounded budget |
| 5xx | Server-side problem | Consider bounded retry if the operation is safe to repeat |

A timeout means you did not receive a complete response in time. It does **not** prove the server did nothing. This matters when creating a payment, email, booking, or invoice.

## SQL is still a core AI skill

An LLM should not invent arithmetic over a large table when a database can calculate it exactly. SQL filters, joins, groups, and orders records. Parameters keep input separate from query syntax.

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE invoices (tenant TEXT, amount_cents INTEGER)")
db.executemany("INSERT INTO invoices VALUES (?, ?)",
               [("acme", 125050), ("other", 90000)])
total = db.execute(
    "SELECT SUM(amount_cents) FROM invoices WHERE tenant = ?",
    ("acme",),
).fetchone()[0]
print(total)  # 125050 cents
```

In a deployed service, derive the tenant from authenticated identity rather than trusting an arbitrary request field. Parameterization prevents a class of injection attacks; it does not implement authorization by itself.

## Sync, async, and background work

Synchronous code waits for each operation. Asynchronous code can make progress on other work while an operation waits on I/O. It does not automatically make CPU-heavy processing faster. A background queue lets the API acknowledge work before the full job finishes and lets workers process jobs independently.

Use a queue for a slow PDF extraction. Use a short request path for a chat response. Apply deadlines and concurrency limits to both. Unlimited asynchronous calls can exhaust connections or provider quotas.

## Practice

Write an API contract for “upload document.” Include accepted types, maximum size, authentication, response fields, and error cases. Explain why a successful HTTP status is insufficient if the body is malformed.

**Check:** a useful contract returns a job ID, records ownership, explains polling or callbacks, and never treats an upload acknowledgement as proof that extraction succeeded.

Next: [Requirements and capacity](03-requirements-and-capacity.md) · [Index](../INDEX.md)
