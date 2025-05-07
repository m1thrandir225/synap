from operator import index
import uuid
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
from app.database import Base


class Summarization(Base):
    __tablename__ = "summarizations"

    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4())
    file_id = Column(UUID, ForeignKey("uploaded_files.id"), nullable=False)

    file = relationship("UploadedFile", back_populates="summarization", single_parent=True)

    summary_text = Column(String, nullable=False)
    ai_model_used = Column(String)
    
    lecture = relationship("Lecture", back_populates="summarization")

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    updated_at = Column(DateTime(timezone=True), server_default=func.now() ,onupdate=func.now(), nullable=False)

    __table_args__ = (UniqueConstraint("file_id"),)
