"""
Load environment-specific config from config/<env>/config.yaml.
Set APP_ENV to one of: local, dev, stg, prod (default: local).
"""
from pathlib import Path
from functools import lru_cache

import yaml
from pydantic import BaseModel


class Settings(BaseModel):
    environment: str
    host: str
    port: int
    debug: bool
    reload: bool
    version: str = "1.0.0"


def _config_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "config"


@lru_cache
def get_config() -> Settings:
    env = __import__("os").environ.get("APP_ENV", "local")
    if env not in ("local", "dev", "stg", "prod"):
        env = "local"
    path = _config_dir() / env / "config.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    data = yaml.safe_load(path.read_text())
    return Settings(**data)
