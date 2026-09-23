import pytest

from pricing.core import LineItem, apply_discount, subtotal


def test_subtotal_multiplies_price_by_quantity():
    assert subtotal([LineItem("a", 2.5, 4), LineItem("b", 1, 3)]) == 13


def test_apply_discount_takes_a_percentage_off():
    assert apply_discount(200, 15) == 170


def test_apply_discount_rejects_out_of_range_percentages():
    with pytest.raises(ValueError):
        apply_discount(10, 120)
