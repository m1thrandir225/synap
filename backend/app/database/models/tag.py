from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import relationship
from app.database import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, nullable=False)

    files = relationship("FileTag", back_populates="tag")

    learning_materials = relationship("LearningMaterialTag", back_populates="tags")
