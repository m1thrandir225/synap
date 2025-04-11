from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
import os

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy engine for synchronous queries
engine = create_engine(DATABASE_URL, echo=True)

# Database session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the SQLAlchemy models
Base = declarative_base()

# Asynchronous database connection
database = Database(DATABASE_URL)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()