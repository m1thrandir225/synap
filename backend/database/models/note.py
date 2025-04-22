from sqlalchemy import UUID, Column, DateTime, ForeignKey, String, func
from sqlalchemy.orm import relationship
from backend.database import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(UUID, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="notes")

    course_id = Column(UUID, ForeignKey("courses.id"), nullable=False)
    course = relationship("Course", back_populates="notes")

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)
