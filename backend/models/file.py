from sqlalchemy import UUID, BigInteger, Column, DateTime, ForeignKey, String, func
from sqlalchemy.orm import relationship
from database import Base


class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(UUID, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_size = Column(BigInteger, nullable=False)
    mime_type = Column(String, nullable=False)
    course_id = Column(UUID, ForeignKey("courses.id"), nullable=True)
    course = relationship("Course", back_populates="uploaded_files")
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="uploaded_files")

    summarization = relationship("Summarization", back_populates="file")

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
