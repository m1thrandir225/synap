from datetime import datetime
from uuid import UUID
import uuid
from sqlalchemy.orm import Session
from app.database import Lecture
from app.repositories import LectureRepository
from app.models import CreateLectureDTO, UpdateLectureDTO, LectureDTO, SummarizationDTO
from typing import List


class LectureService:
    def __init__(self, lec_repo: LectureRepository):
        self.repository = lec_repo

    def _to_dto(self, lecture: Lecture | None):
        if lecture is None:
            return None
        return LectureDTO(
            name=lecture.name, 
            summarization_id=lecture.summarization_id, 
            id=lecture.id, 
            summarization=SummarizationDTO(
            id=lecture.summarization.id,
            file_id=lecture.summarization.file_id,
            summary_text=lecture.summarization.summary_text,
            ai_model_used=lecture.summarization.ai_model_used,
            )
        )

    def create_lecture(self, lec_data: CreateLectureDTO) -> LectureDTO:
        lecture_data_dump = lec_data.model_dump()
        lecture_data_dump["id"] = uuid.uuid4()
        lecture: Lecture = self.repository.create_lecture(lecture_data_dump)
        return self._to_dto(lecture=lecture)

    def get_all_lectures(self) -> List[LectureDTO]:
        lectures: List[Lecture] = self.repository.get_all_lectures()
        lecture_dto = []
        for lec in lectures:
            lecture_dto.append(self._to_dto(lecture=lec))
        return lecture_dto

    def get_lecture_by_id(self, lecture_id: UUID) -> LectureDTO:
        lecture = self.repository.get_lecture_by_id(lecture_id)
        if lecture is None:
            return None
        return self._to_dto(lecture=lecture)

    def get_lecture_by_summarization_id(self, summarization_id: UUID) -> LectureDTO:
        lecture = self.repository.get_lecture_by_summarization_id(summarization_id)
        if lecture is None:
            return None
        return self._to_dto(lecture=lecture)

    def update_lecture(self, lecture_id: UUID, lec_data: UpdateLectureDTO) -> LectureDTO:

        lec_data_dump = lec_data.model_dump(exclude_unset=True)
        lec_data_dump["updated_at"] = datetime.now()
        updated_lecture = self.repository.update_lecture(
            lecture_id, lec_data_dump
        )
        
        if updated_lecture is None:
            return None
        return self._to_dto(lecture=updated_lecture)

    def delete_lecture(self, lecture_id: UUID) -> None:
        deleted = self.repository.delete_lecture(lecture_id)
        if deleted is None:
            None
