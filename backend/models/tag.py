from sqlalchemy import UUID, Column, String
from database import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, nullable=False)
