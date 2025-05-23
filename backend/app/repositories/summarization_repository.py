from sqlalchemy.orm import Session, joinedload
from app.database import (
    Summarization,
    UploadedFile,
    Recommendation,
)
from typing import List, Optional
from uuid import UUID


class SummarizationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, summarization_id: UUID) -> Optional[Summarization]:
        """Get a summarization by its ID."""
        return (
            self.db.query(Summarization)
            .filter(Summarization.id == summarization_id)
            .first()
        )

    def get_by_file_id(self, file_id: UUID) -> Optional[Summarization]:
        """Get a summarization associated with a specific file."""
        return (
            self.db.query(Summarization)
            .filter(Summarization.file_id == file_id)
            .first()
        )

    def get_all(self, user_id: UUID) -> List[Summarization]:
        """Get all summarizations."""
        query = (
            self.db.query(Summarization)
            .join(Summarization.file)
            .filter(UploadedFile.user_id == user_id)
            .options(joinedload(Summarization.file))
        )
        return query.all()

    def create(self, summarization_data: dict) -> Summarization:
        """Create a new summarization."""

        summarization_dict = summarization_data.model_dump()
        db_summarization = Summarization(**summarization_dict)
        self.db.add(db_summarization)
        self.db.commit()
        self.db.refresh(db_summarization)
        return db_summarization

    def update(
        self, summarization_id: UUID, summarization_data: dict
    ) -> Optional[Summarization]:
        """Update an existing summarization."""
        summarization = self.get_by_id(summarization_id)
        if summarization:
            for key, value in summarization_data.items():
                setattr(summarization, key, value)
            self.db.commit()
            self.db.refresh(summarization)
            return summarization
        return None

    def delete(self, summarization_id: UUID) -> bool:
        """Delete a summarization."""
        summarization = self.get_by_id(summarization_id)
        if summarization:
            self.db.delete(summarization)
            self.db.commit()
            return True
        return False

    def get_file_by_summarization(
        self, summarization_id: UUID
    ) -> Optional[UploadedFile]:
        """Get the file associated with a specific summarization."""
        summarization = self.get_by_id(summarization_id)
        return summarization.file if summarization else None

