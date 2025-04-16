from sqlalchemy import UUID, Column, DateTime, ForeignKey, String, func, null
from sqlalchemy.orm import relationship
from database.base import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)

    user_id = Column(UUID, ForeignKey("users.id"))
    user = relationship("User", back_populates="courses")

    notes = relationship("Note", back_populates="course")

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)
