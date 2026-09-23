from dataclasses import dataclass


@dataclass(frozen=True)
class LineItem:
    sku: str
    unit_price: float
    quantity: int


def subtotal(items: list[LineItem]) -> float:
    """Sum of unit_price * quantity, rounded to 2 decimals."""
    return round(sum(item.unit_price * item.quantity for item in items), 2)


def apply_discount(amount: float, percent: float) -> float:
    """Applies a percentage discount (0-100)."""
    if percent < 0 or percent > 100:
        raise ValueError(f"invalid discount: {percent}")
    return round(amount * (1 - percent / 100), 2)
