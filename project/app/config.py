import logging
from functools import lru_cache

from pydantic import AnyUrl
from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = False
    database_url: AnyUrl = None


@lru_cache
def get_Settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
