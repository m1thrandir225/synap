import uuid
from sqlalchemy import UUID, Column, DateTime, String, func
from sqlalchemy.orm import relationship
from app.database import Base


class LearningMaterial(Base):
    __tablename__ = "learning_materials"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, server_default=func.gen_random_uuid(), unique=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    url = Column(String, nullable=False)
    material_type = Column(String, nullable=False)

    recommendations = relationship("Recommendation", back_populates="learning_material", cascade="all, delete")

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
