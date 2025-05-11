import uuid
from sqlalchemy import UUID, Column, DateTime, Float, ForeignKey, func
from sqlalchemy.orm import relationship
from app.database import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, server_default=func.gen_random_uuid(), nullable=False, unique=True)

    file_id = Column(UUID, ForeignKey("uploaded_files.id"), nullable=False)
    file = relationship("UploadedFile", back_populates="recommendations", cascade="all, delete")

    learning_material_id = Column(
        UUID, ForeignKey("learning_materials.id"), nullable=False
    )

    learning_material = relationship(
        "LearningMaterial", back_populates="recommendations"
    )

    relevance_score = Column(Float, nullable=False)

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
