from contextlib import contextmanager
from typing import Generator

from database.session import DATABASE_URL, get_local_session

from backend.exceptions import SQLAlchemyException
from backend.log import get_logger

log = get_logger(__name__)


def get_db() -> Generator:
    """
    Return a generator that yields a database session

    Yields:
        Session: A database session object.
    Raises:
        Exception: If an error occurs while getting the databse session.
    """

    log.debug("Getting database session")
    db = get_local_session(DATABASE_URL, False)()
    try:
        yield db
    finally:
        log.debug("Closing database session")
        db.close()


@contextmanager
def get_ctx_db(database_url: str) -> Generator:
    """
    Context manager that creates a database session and yields
    it for use in a 'with' statement.

    Parameters:
        database_url (str): The URL of the database to connect to.

    Yields:
        Generator: A database session.

    Raises:
        Exception: If an error occurs while getting the database session.
    """

    log.debug("Getting database session")

    db = get_local_session(database_url)()
    try:
        yield db
    except Exception as e:
        log.error(
            "An error occured while getting the database connection. Error: %s", e
        )
        raise SQLAlchemyException from e
    finally:
        log.debug("Closing database session")
        db.close()
