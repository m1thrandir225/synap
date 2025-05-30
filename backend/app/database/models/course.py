import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey, String, func, null
from sqlalchemy.orm import relationship
from app.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, server_default=func.gen_random_uuid(), unique=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)

    user_id = Column(UUID, ForeignKey("users.id"))
    user = relationship("User", back_populates="courses")

    notes = relationship("Note", back_populates="course", cascade="all, delete")

    uploaded_files = relationship("UploadedFile", back_populates="course", cascade="all, delete")

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
