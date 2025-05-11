import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey, String, func
from sqlalchemy.orm import relationship
from app.database import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, server_default=func.gen_random_uuid(), nullable=False, unique=True)

    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="notes", cascade="all, delete")

    course_id = Column(UUID, ForeignKey("courses.id"), nullable=False)
    course = relationship("Course", back_populates="notes", cascade="all, delete")

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(DateTime(timezone=True), server_default=func.now() ,onupdate=func.now(), nullable=False)