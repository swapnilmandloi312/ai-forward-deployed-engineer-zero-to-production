import unittest

from labs.capacity import calculate


class CapacityTests(unittest.TestCase):
    def test_worked_peak_example(self):
        result = calculate()
        self.assertEqual(result["estimated_peak_requests_per_second"], 2)
        self.assertEqual(result["estimated_mean_in_flight_at_peak"], 8)
        self.assertEqual(result["peak_input_tokens_per_minute"], 240000)
        self.assertEqual(result["fictional_base_daily_cost_usd"], 86.4)

    def test_worked_cost_example_and_scaling(self):
        result = calculate(requests_per_day=10000)
        self.assertEqual(result["fictional_base_period_cost_usd"], 2160)
        doubled = calculate(requests_per_day=20000)
        self.assertEqual(doubled["fictional_base_daily_cost_usd"], result["fictional_base_daily_cost_usd"] * 2)
        self.assertEqual(calculate(requests_per_day=0)["estimated_mean_in_flight_at_peak"], 0)

    def test_invalid_inputs(self):
        for kwargs in ({"active_hours": 0}, {"active_hours": 25}, {"requests_per_day": -1},
                       {"input_tokens": 1.5}, {"peak_factor": 0.5}, {"days": 0},
                       {"mean_latency_seconds": float("nan")}, {"input_price_per_million": -1},
                       {"requests_per_day": True}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                calculate(**kwargs)


if __name__ == "__main__":
    unittest.main()
