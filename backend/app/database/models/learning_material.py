import uuid
from sqlalchemy import UUID, Column, DateTime, String, func
from sqlalchemy.orm import relationship
from app.database import Base


class LearningMaterial(Base):
    __tablename__ = "learning_materials"

    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4())
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    url = Column(String, nullable=False)
    material_type = Column(String, nullable=False)

    tags = relationship("LearningMaterialTag", back_populates="learning_materials")

    recommendations = relationship("Recommendation", back_populates="learning_material")

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
