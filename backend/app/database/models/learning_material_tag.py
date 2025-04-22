from sqlalchemy import UUID, Column, ForeignKey, PrimaryKeyConstraint, null
from sqlalchemy.orm import relationship
from app.database import Base


class LearningMaterialTag(Base):
    __tablename__ = "learning_material_tags"

    learning_material_id = Column(
        UUID, ForeignKey("learning_materials.id"), nullable=False
    )

    learning_materials = relationship("LearningMaterial", back_populates="tags")

    tag_id = Column(UUID, ForeignKey("tags.id"), nullable=False)

    tags = relationship("Tag", back_populates="learning_materials")

    __table_args__ = (
        PrimaryKeyConstraint(
            "learning_material_id", "tag_id", name="learning_material_tag_pk"
        ),
    )
