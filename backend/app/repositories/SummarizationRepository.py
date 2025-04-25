from sqlalchemy.orm import Session
from database.models import Summarization, UploadedFile, Lecture  # Adjust based on your file structure
from typing import List, Optional
from uuid import UUID

class SummarizationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, summarization_id: UUID) -> Optional[Summarization]:
        """Get a summarization by its ID."""
        return self.db.query(Summarization).filter(Summarization.id == summarization_id).first()

    def get_by_file_id(self, file_id: UUID) -> Optional[Summarization]:
        """Get a summarization associated with a specific file."""
        return self.db.query(Summarization).filter(Summarization.file_id == file_id).first()

    def get_all(self) -> List[Summarization]:
        """Get all summarizations."""
        return self.db.query(Summarization).all()

    def create(self, summarization_data: dict) -> Summarization:
        """Create a new summarization."""
        db_summarization = Summarization(**summarization_data)
        self.db.add(db_summarization)
        self.db.commit()
        self.db.refresh(db_summarization)
        return db_summarization

    def update(self, summarization_id: UUID, summarization_data: dict) -> Optional[Summarization]:
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

    def get_file_by_summarization(self, summarization_id: UUID) -> Optional[UploadedFile]:
        """Get the file associated with a specific summarization."""
        summarization = self.get_by_id(summarization_id)
        return summarization.file if summarization else None

    def get_lecture_by_summarization(self, summarization_id: UUID) -> Optional[Lecture]:
        """Get the lecture associated with a specific summarization."""
        summarization = self.get_by_id(summarization_id)
        return summarization.lecture if summarization else None
