from sqlalchemy.orm import Session
from app.database import (
    FileTag,
    UploadedFile,
    Tag,
)  # Adjust based on your file structure
from typing import List, Optional
from uuid import UUID


class FileTagRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_ids(self, file_id: UUID, tag_id: UUID) -> Optional[FileTag]:
        """Get a file tag by the combination of file_id and tag_id."""
        return (
            self.db.query(FileTag)
            .filter(FileTag.file_id == file_id, FileTag.tag_id == tag_id)
            .first()
        )

    def get_by_file_id(self, file_id: UUID) -> List[FileTag]:
        """Get all tags associated with a specific file."""
        return self.db.query(FileTag).filter(FileTag.file_id == file_id).all()

    def get_by_tag_id(self, tag_id: UUID) -> List[FileTag]:
        """Get all files associated with a specific tag."""
        return self.db.query(FileTag).filter(FileTag.tag_id == tag_id).all()

    def create(self, file_id: UUID, tag_id: UUID) -> FileTag:
        """Create a new file-tag association."""
        db_file_tag = FileTag(file_id=file_id, tag_id=tag_id)
        self.db.add(db_file_tag)
        self.db.commit()
        self.db.refresh(db_file_tag)
        return db_file_tag

    def delete(self, file_id: UUID, tag_id: UUID) -> bool:
        """Delete a file-tag association."""
        file_tag = self.get_by_ids(file_id, tag_id)
        if file_tag:
            self.db.delete(file_tag)
            self.db.commit()
            return True
        return False

    def get_tags_by_file(self, file_id: UUID) -> List[Tag]:
        """Get all tags associated with a specific file."""
        return self.db.query(Tag).join(FileTag).filter(FileTag.file_id == file_id).all()

    def get_files_by_tag(self, tag_id: UUID) -> List[UploadedFile]:
        """Get all files associated with a specific tag."""
        return (
            self.db.query(UploadedFile)
            .join(FileTag)
            .filter(FileTag.tag_id == tag_id)
            .all()
        )
