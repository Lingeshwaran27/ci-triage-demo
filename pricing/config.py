import os
from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    currency: str


def load_config(env: Mapping[str, str] = os.environ) -> Config:
    """Reads required runtime configuration from the environment."""
    currency = env.get("CURRENCY")
    if not currency:
        raise RuntimeError("Missing required environment variable CURRENCY")
    return Config(currency=currency)
