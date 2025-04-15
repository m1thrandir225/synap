from contextlib import contextmanager
from typing import Generator
from database.session import DATABASE_URL, get_local_session
from log import get_logger

log = get_logger(__name__)


def get_db() -> Generator:
    """
    Return a generator that yields a database session
    """
    db = get_local_session(DATABASE_URL, False)()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_ctx_db(database_url: str) -> Generator:
    db = get_local_session(database_url)()
    try:
        yield db
    finally:
        db.close()
