import unittest

from src.pricing import LineItem, compute_total_cents


class ComputeTotalCentsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.items = [
            LineItem("widget", unit_price_cents=1000, quantity=2),
            LineItem("gadget", unit_price_cents=500, quantity=1),
        ]

    def test_no_discount(self) -> None:
        self.assertEqual(compute_total_cents(self.items, 0.0), 2500)

    def test_twenty_percent_as_fraction(self) -> None:
        self.assertEqual(compute_total_cents(self.items, 0.20), 2000)

    def test_full_discount(self) -> None:
        self.assertEqual(compute_total_cents(self.items, 1.0), 0)

    def test_rejects_out_of_range_fraction(self) -> None:
        with self.assertRaises(ValueError):
            compute_total_cents(self.items, 20)


if __name__ == "__main__":
    unittest.main()
