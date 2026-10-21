import copy
import json
import tempfile
import unittest
from pathlib import Path

from labs.evaluate import CASES, evaluate
from labs.mini_rag import load_documents, retrieve


class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.documents = load_documents()

    def test_current_version_and_tenant_are_enforced(self):
        result = retrieve("refund window", "acme", {"support"}, self.documents)
        self.assertEqual(result["citations"][0]["source"], "returns@2")
        self.assertTrue(all(hit["tenant"] == "acme" for hit in result["citations"]))
        self.assertNotIn("90 day", json.dumps(result))
        self.assertNotIn("Retired", json.dumps(result))

    def test_group_denial_does_not_expose_private_text(self):
        result = retrieve("payroll processed", "acme", {"support"}, self.documents)
        self.assertEqual(result["outcome"], "abstain")
        self.assertNotIn("25th", json.dumps(result))

    def test_allowed_group_can_retrieve(self):
        result = retrieve("payroll processed", "acme", {"finance"}, self.documents)
        self.assertEqual(result["citations"][0]["source"], "staff-pay@1")

    def test_new_version_cannot_fall_back_to_old_permissions(self):
        documents = copy.deepcopy(self.documents)
        old = next(doc for doc in documents if doc["tenant"] == "acme" and doc["id"] == "returns" and doc["version"] == 1)
        old["active"] = True
        current = next(doc for doc in documents if doc["tenant"] == "acme" and doc["id"] == "returns" and doc["version"] == 2)
        current["groups"] = ["finance"]
        result = retrieve("refund window", "acme", {"support"}, documents)
        self.assertEqual(result["outcome"], "abstain")

    def test_unknown_tenant_empty_groups_and_empty_query(self):
        for question, tenant, groups in [("refund", "missing", {"support"}),
                                         ("refund", "acme", set()), ("the is", "acme", {"support"})]:
            with self.subTest(question=question, tenant=tenant, groups=groups):
                self.assertEqual(retrieve(question, tenant, groups, self.documents)["outcome"], "abstain")

    def test_malformed_and_duplicate_documents_rejected(self):
        for value in [{}, [self.documents[0], self.documents[0]], [{"id": "x"}]]:
            with self.subTest(value=value), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "docs.json"
                path.write_text(json.dumps(value), encoding="utf-8")
                with self.assertRaises(ValueError):
                    load_documents(path)

    def test_eval_counts_and_failure_detection(self):
        cases = json.loads(CASES.read_text(encoding="utf-8"))
        report = evaluate(cases, self.documents)
        self.assertEqual(report["answerable_cases"], 6)
        self.assertEqual(report["passed"], len(cases))
        cases[0]["expected_source"] = "nonexistent@99"
        self.assertLess(evaluate(cases, self.documents)["passed"], len(cases))
        with self.assertRaises(ValueError):
            evaluate([], self.documents)


if __name__ == "__main__":
    unittest.main()
