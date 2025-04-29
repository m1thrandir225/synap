from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from app.config import Settings, settings

def build_db_url_from_settings(_settings: Settings) -> str:
    """
    Build a SQLAlchemy URL based on the provided settings.

    Parameters:
        _settings (Settings): An instance of the settings class containing
        PostgreSQL connection details.
    Return:
        str: The generated URL
    """
    return (
        f"postgresql://{_settings.POSTGRES_USER}:{_settings.POSTGRES_PASSWORD}"
        f"@{_settings.POSTGRES_HOST}:{_settings.POSTGRES_PORT}/{_settings.POSTGRES_DB}"
    )


def get_engine(database_url: str, echo=False) -> Engine:
    """
    Creates and returnes a SQLAlchemy Engine object for connecting to the
    database

    Parameters:
        database_url (str): The URL of the database to connect to
        echo (bool): Whether or not to echo SQL statements. (Default =
        False)
    Returns:
        Engine: A SQLAlchemy Engine object represting a database connection
    """
    engine = create_engine(database_url, echo=echo)

    return engine


def get_local_session(database_url: str, echo=False) -> sessionmaker:
    """
    Create and return a session maker object for a local dtabase session.

    Parameters:
        database_url (str): The URL of the database to connect to
        echo (bool): Whether or not to echo SQL Statements.
    Returns:
        sessionmaker: A sessionmaker object configured for the local database
        session.
    """
    engine = get_engine(database_url, echo)

    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return session


DATABASE_URL = build_db_url_from_settings(settings)
