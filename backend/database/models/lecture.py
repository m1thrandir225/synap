from sqlalchemy import (
    UUID,
    Column,
    DateTime,
    ForeignKey,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import relationship
from backend.database import Base


class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(UUID, primary_key=True, index=True)

    summarization_id = Column(UUID, ForeignKey("summarizations.id"), nullable=False)
    summarization = relationship(
        "Summarization", back_populates="lecture", single_parent=True
    )

    name = Column(String, nullable=False)

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    __table_args__ = (UniqueConstraint("summarization_id"),)
