from sqlalchemy import UUID, Column, DateTime, Integer, String, func

from sqlalchemy.orm import relationship
from database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)

    courses = relationship("Course", back_populates="user")
    notes = relationship("Note", back_populates="user")
    uploaded_files = relationship("UploadedFile", back_populates="user")
    recommendation_interactions = relationship(
        "RecommendationInteracton", back_populates="user"
    )
