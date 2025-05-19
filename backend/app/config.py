import os
from app.log import get_logger
from pydantic_settings import BaseSettings, SettingsConfigDict

log = get_logger(__name__)


class Settings(BaseSettings):
    """
    Settings for running the app in production mode
    """

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

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int

    JWT_SECRET: str
    JWT_ALGORITHM: str
    OPENAI_API_KEY: str
    
    PRODUCTION_FRONTEND_URL: str

    S3_BUCKET_NAME: str
    S3_ACCESS_KEY_ID: str
    S3_SECRET_ACCESS_KEY: str
    AWS_REGION_NAME: str

class LocalSettings(Settings):
    """
    Settings for running the app in development mode
    """
    model_config = SettingsConfigDict(
        env_file="./.env.local",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )
    ENV: str = "dev"


def get_settings(env: str = "") -> Settings:
    if env.lower() in ["prod", "production", "p"]:
        return Settings()
    if env.lower() in ["dev", "development", "d"]:
        return LocalSettings()
    raise ValueError("Invalid Environment setup")


_env = os.environ.get("ENV", "prod")

settings = get_settings(_env)
