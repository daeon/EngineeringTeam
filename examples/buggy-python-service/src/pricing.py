"""Domain pricing logic.

Pure functions with no IO. This is the core contract layer: callers must
adapt their inputs to these contracts before calling.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LineItem:
    name: str
    unit_price_cents: int
    quantity: int

    def subtotal_cents(self) -> int:
        return self.unit_price_cents * self.quantity


def compute_total_cents(items: list[LineItem], discount_fraction: float) -> int:
    """Return the discounted order total in cents.

    Contract: ``discount_fraction`` is a fraction in the closed interval
    ``[0.0, 1.0]`` where ``0.0`` means no discount and ``1.0`` means free.
    Callers MUST convert human-facing percentages (for example ``20``) into
    fractions (``0.20``) before calling this function.
    """
    if not 0.0 <= discount_fraction <= 1.0:
        raise ValueError(
            f"discount_fraction must be in [0, 1], got {discount_fraction!r}"
        )
    subtotal = sum(item.subtotal_cents() for item in items)
    return round(subtotal * (1.0 - discount_fraction))
