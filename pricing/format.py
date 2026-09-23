from .config import load_config


def format_money(amount: float) -> str:
    currency = load_config().currency
    return f"{currency} {amount:,.2f}"
