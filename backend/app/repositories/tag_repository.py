from sqlalchemy.orm import Session
from app.database import (
    Tag,
    FileTag,
    LearningMaterialTag,
)  # Adjust based on your file structure
from typing import List, Optional
from uuid import UUID


class TagRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, tag_id: UUID) -> Optional[Tag]:
        """Get a tag by its ID."""
        return self.db.query(Tag).filter(Tag.id == tag_id).first()

    def get_by_name(self, name: str) -> Optional[Tag]:
        """Get a tag by its name."""
        return self.db.query(Tag).filter(Tag.name == name).first()

    def get_all(self) -> List[Tag]:
        """Get all tags."""
        return self.db.query(Tag).all()

    def create(self, tag_data: dict) -> Tag:
        """Create a new tag."""
        db_tag = Tag(**tag_data)
        self.db.add(db_tag)
        self.db.commit()
        self.db.refresh(db_tag)
        return db_tag

    def update(self, tag_id: UUID, tag_data: dict) -> Optional[Tag]:
        """Update an existing tag."""
        tag = self.get_by_id(tag_id)
        if tag:
            for key, value in tag_data.items():
                setattr(tag, key, value)
            self.db.commit()
            self.db.refresh(tag)
            return tag
        return None

    def delete(self, tag_id: UUID) -> bool:
        """Delete a tag."""
        tag = self.get_by_id(tag_id)
        if tag:
            self.db.delete(tag)
            self.db.commit()
            return True
        return False

    def get_files_by_tag(self, tag_id: UUID) -> List[FileTag]:
        """Get all files associated with a specific tag."""
        return self.db.query(FileTag).filter(FileTag.tag_id == tag_id).all()

    def get_learning_materials_by_tag(self, tag_id: UUID) -> List[LearningMaterialTag]:
        """Get all learning materials associated with a specific tag."""
        return (
            self.db.query(LearningMaterialTag)
            .filter(LearningMaterialTag.tag_id == tag_id)
            .all()
        )
