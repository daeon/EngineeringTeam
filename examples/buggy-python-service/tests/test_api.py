import unittest

from src.api import checkout


class CheckoutTest(unittest.TestCase):
    def _payload(self, discount_percent: int) -> dict:
        return {
            "items": [
                {"name": "widget", "unit_price_cents": 1000, "quantity": 2},
                {"name": "gadget", "unit_price_cents": 500, "quantity": 1},
            ],
            "discount_percent": discount_percent,
        }

    def test_checkout_without_discount(self) -> None:
        result = checkout(self._payload(0))
        self.assertEqual(result["total_cents"], 2500)

    # NOTE: there is intentionally no test here for a non-zero discount.
    # That coverage gap is where the boundary bug hides.


if __name__ == "__main__":
    unittest.main()
