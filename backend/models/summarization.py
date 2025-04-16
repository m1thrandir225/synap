from operator import index
from sqlalchemy import UUID, Column, DateTime, ForeignKey, String, func
from sqlalchemy.orm import relationship
from database import Base


class Summarization(Base):
    __tablename__ = "summarizations"

    id = Column(UUID, primary_key=True, index=True)
    file_id = Column(UUID, ForeignKey("uploaded_files.id"), nullable=False)

    file = relationship("File", back_populates="summarization", single_parent=True)

    summary_text = Column(String, nullable=False)
    ai_model_used = Column(String)

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)
