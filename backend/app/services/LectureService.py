from uuid import UUID
from sqlalchemy.orm import Session
from ..models.lecture import Lecture
from ..repositories.LectureRepository import LectureRepository

class LectureService:
    def __init__(self, db: Session):
        self.repository = LectureRepository(db)

    def create_lecture(self, summarization_id: UUID, name: str) -> Lecture:
        """Service method to create a new lecture."""
        return self.repository.create_lecture(summarization_id, name)

    def get_lecture_by_id(self, lecture_id: UUID) -> Lecture:
        """Service method to get a lecture by ID."""
        lecture = self.repository.get_lecture_by_id(lecture_id)
        if not lecture:
            raise ValueError(f"Lecture with ID {lecture_id} not found")
        return lecture

    def get_lecture_by_summarization_id(self, summarization_id: UUID) -> Lecture:
        """Service method to get a lecture by summarization ID."""
        lecture = self.repository.get_lecture_by_summarization_id(summarization_id)
        if not lecture:
            raise ValueError(f"Lecture with summarization ID {summarization_id} not found")
        return lecture

    def update_lecture(self, lecture_id: UUID, name: str) -> Lecture:
        """Service method to update a lecture's name."""
        updated_lecture = self.repository.update_lecture(lecture_id, name)
        if not updated_lecture:
            raise ValueError(f"Lecture with ID {lecture_id} not found for update")
        return updated_lecture

    def delete_lecture(self, lecture_id: UUID) -> None:
        """Service method to delete a lecture."""
        deleted = self.repository.delete_lecture(lecture_id)
        if not deleted:
            raise ValueError(f"Lecture with ID {lecture_id} not found for deletion")
