import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from labs.guarded_workflow import ConflictError, connect, post_invoice


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.db = connect()
        self.payload = {"tenant": "acme", "vendor": "vendor-7", "invoice_number": "I-001",
                        "amount": "1250.50", "currency": "USD"}

    def tearDown(self):
        self.db.close()

    def post(self, key="op-1", payload=None, approved=True):
        return post_invoice(self.db, key, payload or self.payload, approved, {"vendor-7"})

    def count(self):
        return self.db.execute("SELECT COUNT(*) FROM entries").fetchone()[0]

    def test_review_gate_has_no_effect(self):
        self.assertEqual(self.post(approved=False)["status"], "review_required")
        self.assertEqual(self.count(), 0)
        self.assertEqual(self.db.execute("SELECT COUNT(*) FROM operations").fetchone()[0], 0)

    def test_retry_reuses_result_and_does_not_repeat_effect(self):
        first = self.post()
        second = self.post()
        self.assertEqual(first["status"], "posted_locally")
        self.assertEqual(second, {"status": "duplicate", "entry_id": first["entry_id"]})
        self.assertEqual(self.count(), 1)
        self.assertEqual(self.db.execute("SELECT amount_cents FROM entries").fetchone()[0], 125050)

    def test_changed_payload_conflicts_and_original_survives(self):
        self.post()
        with self.assertRaises(ConflictError):
            self.post(payload={**self.payload, "amount": "1251.00"})
        self.assertEqual(self.count(), 1)
        self.assertEqual(self.post()["status"], "duplicate")

    def test_duplicate_business_invoice_under_new_key_rolls_back(self):
        self.post()
        with self.assertRaises(ConflictError):
            self.post(key="op-2")
        self.assertEqual(self.count(), 1)
        self.assertEqual(self.db.execute("SELECT COUNT(*) FROM operations").fetchone()[0], 1)

    def test_amount_and_vendor_validation(self):
        for amount in ("NaN", "Infinity", "-1", "0", "1.001", "1000001", 10):
            with self.subTest(amount=amount), self.assertRaises(ValueError):
                self.post(payload={**self.payload, "amount": amount})
        with self.assertRaises(PermissionError):
            self.post(payload={**self.payload, "vendor": "unapproved"})
        self.assertEqual(self.count(), 0)

    def test_tenant_scopes_operation_and_business_identity(self):
        self.post()
        self.post(payload={**self.payload, "tenant": "other"})
        self.assertEqual(self.count(), 2)

    def test_competing_connections_create_only_one_entry(self):
        with tempfile.TemporaryDirectory() as directory:
            path = str(Path(directory) / "ledger.sqlite3")
            connect(path).close()

            def attempt(_):
                db = connect(path)
                try:
                    return post_invoice(db, "shared-op", self.payload, True, {"vendor-7"})["status"]
                finally:
                    db.close()

            with ThreadPoolExecutor(max_workers=4) as pool:
                outcomes = list(pool.map(attempt, range(8)))
            self.assertEqual(outcomes.count("posted_locally"), 1)
            self.assertEqual(outcomes.count("duplicate"), 7)
            db = connect(path)
            try:
                self.assertEqual(db.execute("SELECT COUNT(*) FROM entries").fetchone()[0], 1)
            finally:
                db.close()


if __name__ == "__main__":
    unittest.main()
