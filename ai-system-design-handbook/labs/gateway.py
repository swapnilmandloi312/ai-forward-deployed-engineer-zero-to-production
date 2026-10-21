"""Offline gateway simulation: deadlines, bounded concurrency, and a breaker.

Providers are deterministic local coroutines. This does not call a model,
enforce real token quotas, validate content, or implement distributed limits.
"""
from __future__ import annotations

import asyncio
import json
import time
from collections import deque
from collections.abc import Callable


class ProviderError(RuntimeError):
    pass


class CircuitBreaker:
    def __init__(self, threshold: int = 2, cooldown: float = 1,
                 clock: Callable[[], float] = time.monotonic):
        if threshold < 1 or cooldown < 0:
            raise ValueError("invalid circuit-breaker configuration")
        self.threshold = threshold
        self.cooldown = cooldown
        self.clock = clock
        self.failures = 0
        self.opened_at: float | None = None
        self.probe_in_flight = False

    def allow(self) -> bool:
        if self.opened_at is None:
            return True
        if self.clock() - self.opened_at < self.cooldown or self.probe_in_flight:
            return False
        self.probe_in_flight = True
        return True

    def success(self) -> None:
        self.failures = 0
        self.opened_at = None
        self.probe_in_flight = False

    def failure(self) -> None:
        self.failures += 1
        if self.failures >= self.threshold or self.probe_in_flight:
            self.opened_at = self.clock()
        self.probe_in_flight = False

    def canceled(self) -> None:
        # Release a half-open probe without interpreting caller cancellation
        # as proof that the dependency is unhealthy.
        self.probe_in_flight = False


class SimulatedProvider:
    def __init__(self, name: str, outcomes: list[str] | None = None, delay: float = 0.001):
        self.name = name
        self.outcomes = deque(outcomes or [])
        self.delay = delay
        self.calls = self.active = self.max_active = 0

    async def complete(self, prompt: str) -> str:
        self.calls += 1
        self.active += 1
        self.max_active = max(self.max_active, self.active)
        outcome = self.outcomes.popleft() if self.outcomes else "ok"
        try:
            if outcome == "timeout":
                await asyncio.sleep(3600)  # caller deadline cancels this await
            await asyncio.sleep(self.delay)
            if outcome == "error":
                raise ProviderError(f"{self.name} simulated failure")
            return f"{self.name}: simulated response to {prompt}"
        finally:
            self.active -= 1


class Gateway:
    def __init__(self, primary: SimulatedProvider, fallback: SimulatedProvider,
                 concurrency: int = 2, attempt_timeout: float = 0.05,
                 breaker: CircuitBreaker | None = None):
        if concurrency < 1 or attempt_timeout <= 0:
            raise ValueError("invalid gateway configuration")
        self.primary, self.fallback = primary, fallback
        self.semaphore = asyncio.Semaphore(concurrency)
        self.attempt_timeout = attempt_timeout
        self.breaker = breaker or CircuitBreaker()

    async def complete(self, prompt: str, total_timeout: float = 0.2) -> dict:
        if total_timeout <= 0:
            raise ValueError("total_timeout must be positive")
        loop = asyncio.get_running_loop()
        deadline = loop.time() + total_timeout

        async def invoke(provider: SimulatedProvider) -> str:
            remaining = deadline - loop.time()
            if remaining <= 0:
                raise TimeoutError("overall deadline exhausted")
            return await asyncio.wait_for(provider.complete(prompt), min(self.attempt_timeout, remaining))

        async def run() -> dict:
            # Queue waiting is inside the overall deadline.
            async with self.semaphore:
                if self.breaker.allow():
                    try:
                        result = await invoke(self.primary)
                    except (TimeoutError, ProviderError):
                        self.breaker.failure()
                    except asyncio.CancelledError:
                        self.breaker.canceled()
                        raise
                    else:
                        self.breaker.success()
                        return {"provider": self.primary.name, "fallback": False, "text": result}
                result = await invoke(self.fallback)
                return {"provider": self.fallback.name, "fallback": True, "text": result}

        return await asyncio.wait_for(run(), total_timeout)


async def demo() -> None:
    primary = SimulatedProvider("primary", ["error", "timeout"])
    fallback = SimulatedProvider("fallback")
    gateway = Gateway(primary, fallback)
    results = [await gateway.complete("summarize synthetic policy") for _ in range(3)]
    print(json.dumps({"results": results, "primary_calls": primary.calls,
                      "fallback_calls": fallback.calls,
                      "circuit_open": gateway.breaker.opened_at is not None}, indent=2))


if __name__ == "__main__":
    asyncio.run(demo())
