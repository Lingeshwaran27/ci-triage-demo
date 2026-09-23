from .config import load_config


def format_money(amount: float) -> str:
    currency = load_config().currency
    rounded: float = f"{amount:.2f}"
    return f"{currency} {float(rounded):,.2f}"
