from sqlalchemy import UUID, Column, ForeignKey, PrimaryKeyConstraint, null
from sqlalchemy.orm import relationship
from database import Base


class FileTag(Base):
    __tablename__ = "file_tags"

    file_id = Column(UUID, ForeignKey("uploaded_files.id"), nullable=False)
    tag_id = Column(UUID, ForeignKey("tags.id"), nullable=False)

    tag = relationship("Tag", back_populates="files")
    file = relationship("UploadedFile", back_populates="tags")

    __table_args__ = (PrimaryKeyConstraint("file_id", "tag_id", name="file_tag_pk"),)
