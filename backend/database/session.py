from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from config import Settings, settings


def build_db_url_from_settings(_settings: Settings) -> str:
    return (
        f"postgresql://{_settings.POSTGRES_USER}:{_settings.POSTGRES_PASSWORD}"
        f"@{_settings.POSTGRES_HOST}:{_settings.POSTGRES_PORT}/{_settings.POSTGRES_DB}"
    )


def get_engine(database_url: str, echo=False) -> Engine:
    engine = create_engine(database_url, echo=echo)

    return engine


def get_local_session(database_url: str, echo=False, **kwargs) -> sessionmaker:
    engine = get_engine(database_url, echo)

    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return session


DATABASE_URL = build_db_url_from_settings(settings)
