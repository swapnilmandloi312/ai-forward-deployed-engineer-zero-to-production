"""Behavioral checks for scope, deduplication, and catalog classification."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


tickets = module("ticket_baseline", "fde-field-drills/analyze_tickets.py")
catalog = module("catalog_browser", "open-source-ai-engineering/catalog.py")


class TicketBaselineTests(unittest.TestCase):
    def analyze(self, lines, tenant="north"):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "tickets.csv"
            source.write_text("tenant,ticket_id,updated_at,category\n" + lines, encoding="utf-8")
            return tickets.summarize(source, tenant)

    def test_fixture_counts_tickets_not_export_rows(self):
        result = tickets.summarize(tickets.DEFAULT_DATA, "north")
        self.assertEqual((result["source_rows"], result["unique_tickets"]), (10, 8))
        self.assertEqual(result["categories"], {"access": 2, "billing": 1, "export": 5})

    def test_latest_category_wins_independent_of_input_order(self):
        rows = ["north,A,2026-10-01T10:00:00+00:00,access\n",
                "north,A,2026-10-01T09:00:00+00:00,export\n"]
        for ordered in (rows, list(reversed(rows))):
            result = self.analyze("".join(ordered))
            self.assertEqual(result["categories"]["access"], 1)
            self.assertEqual(result["categories"]["export"], 0)

    def test_other_tenant_cannot_change_selected_tenant_result(self):
        result = self.analyze("north,A,2026-10-01T09:00:00+00:00,export\n"
                              "south,A,2026-10-02T09:00:00+00:00,access\n")
        self.assertEqual(result["unique_tickets"], 1)
        self.assertEqual(result["categories"]["export"], 1)

    def test_conflicting_same_timestamp_fails_even_if_later_record_exists(self):
        with self.assertRaisesRegex(ValueError, "conflicting"):
            self.analyze("north,A,2026-10-01T10:00:00+00:00,export\n"
                         "north,A,2026-10-01T09:00:00+00:00,access\n"
                         "north,A,2026-10-01T09:00:00+00:00,billing\n")

    def test_naive_timestamp_and_unknown_category_fail(self):
        for row in ("north,A,2026-10-01T09:00:00,export\n",
                    "north,A,2026-10-01T09:00:00+00:00,other\n"):
            with self.assertRaises(ValueError):
                self.analyze(row)

    def test_timezone_offsets_compare_actual_instants(self):
        result = self.analyze("north,A,2026-10-01T10:00:00+02:00,export\n"
                              "north,A,2026-10-01T09:00:00+00:00,access\n")
        self.assertEqual(result["categories"]["access"], 1)

    def test_absent_tenant_returns_explicit_empty_counts(self):
        result = tickets.summarize(tickets.DEFAULT_DATA, "missing")
        self.assertEqual(result["source_rows"], 0)
        self.assertEqual(result["unique_tickets"], 0)
        self.assertEqual(sum(result["categories"].values()), 0)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.rows = catalog.load()

    def load_changed(self, rows):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "catalog.json"
            source.write_text(json.dumps(rows), encoding="utf-8")
            return catalog.load(source)

    def test_default_view_excludes_separate_classifications(self):
        selected = catalog.select(self.rows)
        self.assertGreater(len(selected), 0)
        self.assertTrue(all(r["classification"] == "open-source" and not r["archived"] for r in selected))
        self.assertTrue(any(r["classification"] == "source-available" for r in self.rows))
        self.assertLess(len(selected), len(self.rows))

    def test_category_filter_does_not_bypass_classification(self):
        selected = catalog.select(self.rows, "observability")
        self.assertTrue(selected)
        self.assertTrue(all(r["category"] == "observability" and r["classification"] == "open-source" for r in selected))

    def test_canonical_identity_and_duplicates_are_rejected(self):
        altered = copy.deepcopy(self.rows)
        altered[0]["url"] = "https://github.com/another/project"
        with self.assertRaises(ValueError):
            self.load_changed(altered)
        with self.assertRaises(ValueError):
            self.load_changed(self.rows + [self.rows[0]])

    def test_documentation_review_cannot_be_claimed_as_execution(self):
        altered = copy.deepcopy(self.rows)
        altered[0]["execution_tested"] = True
        with self.assertRaises(ValueError):
            self.load_changed(altered)

    def test_archived_or_custom_license_not_allowed_in_main_list(self):
        index = next(i for i, r in enumerate(self.rows) if r["classification"] == "open-source")
        for key, value in (("archived", True), ("license", "Custom")):
            altered = copy.deepcopy(self.rows)
            altered[index][key] = value
            with self.assertRaises(ValueError):
                self.load_changed(altered)


if __name__ == "__main__":
    unittest.main()
