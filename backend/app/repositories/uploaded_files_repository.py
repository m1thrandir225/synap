from database import FileTag, Recommendation, UploadedFile
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID


class UploadedFileRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, file_id: UUID) -> Optional[UploadedFile]:
        """Get an uploaded file by its ID."""
        return self.db.query(UploadedFile).filter(UploadedFile.id == file_id).first()

    def get_by_user_id(self, user_id: UUID) -> List[UploadedFile]:
        """Get all uploaded files by a user."""
        return self.db.query(UploadedFile).filter(UploadedFile.user_id == user_id).all()

    def get_by_course_id(self, course_id: UUID) -> List[UploadedFile]:
        """Get all uploaded files associated with a specific course."""
        return (
            self.db.query(UploadedFile)
            .filter(UploadedFile.course_id == course_id)
            .all()
        )

    def create(self, file_data: dict) -> UploadedFile:
        """Create a new uploaded file."""
        db_file = UploadedFile(**file_data)
        self.db.add(db_file)
        self.db.commit()
        self.db.refresh(db_file)
        return db_file

    def update(self, file_id: UUID, file_data: dict) -> Optional[UploadedFile]:
        """Update an existing uploaded file."""
        file = self.get_by_id(file_id)
        if file:
            for key, value in file_data.items():
                setattr(file, key, value)
            self.db.commit()
            self.db.refresh(file)
            return file
        return None

    def delete(self, file_id: UUID) -> bool:
        """Delete an uploaded file by its ID."""
        file = self.get_by_id(file_id)
        if file:
            self.db.delete(file)
            self.db.commit()
            return True
        return False

    def get_files_by_tag(self, tag_name: str) -> List[UploadedFile]:
        """Get files associated with a specific tag."""
        return (
            self.db.query(UploadedFile)
            .join(UploadedFile.tags)
            .filter(FileTag.name == tag_name)
            .all()
        )

    def get_files_by_recommendation(
        self, recommendation_id: UUID
    ) -> List[UploadedFile]:
        """Get files associated with a specific recommendation."""
        return (
            self.db.query(UploadedFile)
            .join(UploadedFile.recommendations)
            .filter(Recommendation.id == recommendation_id)
            .all()
        )

    def get_files_by_course_and_user(
        self, course_id: UUID, user_id: UUID
    ) -> List[UploadedFile]:
        """Get files uploaded by a specific user for a specific course."""
        return (
            self.db.query(UploadedFile)
            .filter(
                UploadedFile.course_id == course_id, UploadedFile.user_id == user_id
            )
            .all()
        )
