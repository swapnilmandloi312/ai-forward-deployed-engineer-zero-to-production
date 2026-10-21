import asyncio
import unittest

from labs.gateway import CircuitBreaker, Gateway, ProviderError, SimulatedProvider


class BreakerTests(unittest.TestCase):
    def test_open_half_open_single_probe_and_recovery(self):
        now = [0.0]
        breaker = CircuitBreaker(threshold=1, cooldown=5, clock=lambda: now[0])
        breaker.failure()
        self.assertFalse(breaker.allow())
        now[0] = 5.0
        self.assertTrue(breaker.allow())
        self.assertFalse(breaker.allow())
        breaker.failure()
        self.assertFalse(breaker.allow())
        now[0] = 10.0
        self.assertTrue(breaker.allow())
        breaker.success()
        self.assertTrue(breaker.allow())


class GatewayTests(unittest.IsolatedAsyncioTestCase):
    async def test_fallback_and_open_circuit(self):
        primary = SimulatedProvider("primary", ["error", "error"])
        fallback = SimulatedProvider("fallback")
        gateway = Gateway(primary, fallback, breaker=CircuitBreaker(cooldown=60))
        results = [await gateway.complete("x") for _ in range(3)]
        self.assertTrue(all(result["fallback"] for result in results))
        self.assertEqual(primary.calls, 2)
        self.assertEqual(fallback.calls, 3)

    async def test_attempt_timeout_cancels_primary_before_fallback(self):
        primary = SimulatedProvider("primary", ["timeout"])
        fallback = SimulatedProvider("fallback")
        gateway = Gateway(primary, fallback, attempt_timeout=0.01)
        self.assertTrue((await gateway.complete("x"))["fallback"])
        self.assertEqual(primary.active, 0)

    async def test_overall_deadline_cancels_provider_and_recovers_capacity(self):
        primary = SimulatedProvider("primary", ["timeout"])
        fallback = SimulatedProvider("fallback")
        gateway = Gateway(primary, fallback, concurrency=1, attempt_timeout=1)
        with self.assertRaises(TimeoutError):
            await gateway.complete("x", total_timeout=0.01)
        self.assertEqual(primary.active, 0)
        self.assertEqual(fallback.calls, 0)
        self.assertFalse((await gateway.complete("y"))["fallback"])

    async def test_concurrency_limit(self):
        primary = SimulatedProvider("primary", delay=0.01)
        gateway = Gateway(primary, SimulatedProvider("fallback"), concurrency=2, attempt_timeout=0.1)
        results = await asyncio.gather(*(gateway.complete(str(i), total_timeout=1) for i in range(8)))
        self.assertEqual(len(results), 8)
        self.assertLessEqual(primary.max_active, 2)

    async def test_fallback_failure_is_visible(self):
        gateway = Gateway(SimulatedProvider("primary", ["error"]), SimulatedProvider("fallback", ["error"]))
        with self.assertRaises(ProviderError):
            await gateway.complete("x")


if __name__ == "__main__":
    unittest.main()
