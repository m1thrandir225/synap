from sqlalchemy import UUID, Column, ForeignKey, PrimaryKeyConstraint, null
from database import Base


class LearningMaterialTag(Base):
    __tablename__ = "learning_material_tags"

    learning_material_id = Column(
        UUID, ForeignKey("learning_materials.id"), nullable=False
    )
    tag_id = Column(UUID, ForeignKey("tags.id"), nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint(
            "learning_material_id", "tag_id", name="learning_material_tag_pk"
        ),
    )
