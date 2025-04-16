from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import relationship
from database import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, nullable=False)

    files = relationship("UploadedFile", back_populates="tag")
