from pricing.format import format_money


def test_format_money_uses_the_configured_currency():
    assert format_money(1234.5) == "INR 1,234.50"
