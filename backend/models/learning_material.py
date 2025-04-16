from sqlalchemy import UUID, Column, DateTime, String, func
from database import Base


class LearningMaterial(Base):
    __tablename__ = "learning_materials"

    id = Column(UUID, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    url = Column(String, nullable=False)
    material_type = Column(String, nullable=False)

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
