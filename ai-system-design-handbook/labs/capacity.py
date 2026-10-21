"""Illustrative steady-state capacity and base token cost calculator."""
from __future__ import annotations

import argparse
import json
import math


def calculate(requests_per_day: int = 12000, active_hours: float = 10,
              peak_factor: float = 6, mean_latency_seconds: float = 4,
              input_tokens: int = 2000, output_tokens: int = 400,
              input_price_per_million: float = 2, output_price_per_million: float = 8,
              days: int = 30) -> dict:
    values = locals().copy()
    if any(type(v) not in (int, float) or not math.isfinite(v) for v in values.values()):
        raise ValueError("all inputs must be finite numbers")
    for key in ("requests_per_day", "input_tokens", "output_tokens", "days"):
        if type(values[key]) is not int or values[key] < 0:
            raise ValueError(f"{key} must be a non-negative integer")
    if not 0 < active_hours <= 24 or peak_factor < 1 or mean_latency_seconds <= 0 or days < 1:
        raise ValueError("invalid hours, peak factor, latency, or days")
    if input_price_per_million < 0 or output_price_per_million < 0:
        raise ValueError("prices must be non-negative")
    average_rps = requests_per_day / (active_hours * 3600)
    peak_rps = average_rps * peak_factor
    cost_per_request = (input_tokens * input_price_per_million + output_tokens * output_price_per_million) / 1_000_000
    return {"average_requests_per_second": round(average_rps, 6),
            "estimated_peak_requests_per_second": round(peak_rps, 6),
            "estimated_mean_in_flight_at_peak": round(peak_rps * mean_latency_seconds, 4),
            "peak_input_tokens_per_minute": round(peak_rps * input_tokens * 60, 2),
            "peak_output_tokens_per_minute": round(peak_rps * output_tokens * 60, 2),
            "fictional_base_cost_per_request_usd": round(cost_per_request, 8),
            "fictional_base_daily_cost_usd": round(cost_per_request * requests_per_day, 4),
            "fictional_base_period_cost_usd": round(cost_per_request * requests_per_day * days, 4),
            "assumptions": "Mean steady-state duration; fictional rates; excludes retries, cache pricing, tools, hosting, storage, and review. Not a measured capacity limit."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--requests-per-day", type=int, default=12000)
    parser.add_argument("--active-hours", type=float, default=10)
    parser.add_argument("--peak-factor", type=float, default=6)
    parser.add_argument("--mean-latency-seconds", type=float, default=4)
    parser.add_argument("--input-tokens", type=int, default=2000)
    parser.add_argument("--output-tokens", type=int, default=400)
    parser.add_argument("--input-price-per-million", type=float, default=2)
    parser.add_argument("--output-price-per-million", type=float, default=8)
    parser.add_argument("--days", type=int, default=30)
    args = parser.parse_args()
    try:
        result = calculate(**vars(args))
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
