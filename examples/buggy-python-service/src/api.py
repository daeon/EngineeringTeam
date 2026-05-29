"""Request boundary.

Parses external checkout payloads into domain calls. This is the adapter
between the human-facing API (percentages) and the domain layer (fractions).
"""

from __future__ import annotations

from .pricing import LineItem, compute_total_cents


def checkout(payload: dict) -> dict:
    """Handle a checkout request.

    payload = {
        "items": [{"name": str, "unit_price_cents": int, "quantity": int}, ...],
        "discount_percent": <number 0-100>,  # human-facing percentage
    }
    """
    items = [
        LineItem(i["name"], i["unit_price_cents"], i["quantity"])
        for i in payload["items"]
    ]
    discount_percent = payload.get("discount_percent", 0)
    total_cents = compute_total_cents(items, discount_percent)
    return {"total_cents": total_cents}
