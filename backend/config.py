import os

from log import get_logger
from pydantic_settings import BaseSettings, SettingsConfigDict

log = get_logger(__name__)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env", env_file_encoding="utf-8", case_sensitive=True
    )
    API_VERSION: str
    ENV: str

    SERVER_HOST: str
    SERVER_PORT: int

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int


class LocalDevSettings(Settings):
    model_config = SettingsConfigDict(
        env_file="./.env.local", env_file_encoding="utf-8", case_sensitive=True
    )
    ENV: str = "local"


class ContainerTestSettings(Settings):
    model_config = SettingsConfigDict(
        env_file="./.env.test", env_file_encoding="utf-8", case_sensitive=True
    )
    ENV: str = "test"


def get_settings(env: str = "dev") -> Settings:
    if env.lower() in ["test"]:
        return ContainerTestSettings()
    elif env.lower() in ["dev"]:
        return LocalDevSettings()

    raise ValueError("Invalid environment")


_env = os.environ.get("ENV", "local")

settings = get_settings()
