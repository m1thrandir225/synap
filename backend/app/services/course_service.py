from uuid import UUID
from typing import List
import uuid
from fastapi import HTTPException
from app.repositories import CourseRepository
from app.database import Course
from app.models import (
    CreateCourseDTO,
    UpdateCourseDTO,
    CourseDTO,
    CourseNoteDTO,
    UploadedFileDTO,
    SummarizationBase,
    NoteDTO,
)
from datetime import datetime


class CourseService:
    def __init__(self, course_repo: CourseRepository):
        self.course_repo = course_repo

    def _to_dto(self, course: Course):
        if course is None:
            return None
        notes_dto: List[CourseNoteDTO] = []
        if hasattr(course, "notes"):
            for note_model in course.notes:
                notes_dto.append(CourseNoteDTO.model_validate(note_model))

        uploaded_files_dto: List[UploadedFileDTO] = []
        summaries_collected: List[SummarizationBase] = []
        if hasattr(course, "uploaded_files"):
            for file_model in course.uploaded_files:
                if hasattr(file_model, "summarization"):
                    if(file_model.has_summarization):
                        summaries_collected.append(
                            SummarizationBase.model_validate(file_model.summarization)
                        )
                        
                uploaded_files_dto.append(UploadedFileDTO.model_validate(file_model))

        course_data_dto = {
            "id": course.id,
            "name": course.name,
            "description": course.description,
            "created_at": course.created_at,
            "updated_at": course.updated_at,
            "user_id": course.user_id,
            "notes": notes_dto,
            "uploaded_files": uploaded_files_dto,
            "summaries": summaries_collected,
        }

        dto = CourseDTO.model_validate(course_data_dto)
        return dto

    def get_course(self, course_id: UUID) -> CourseDTO:
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")

        return self._to_dto(course=course)

    def get_courses_by_user(self, user_id: UUID) -> List[CourseDTO]:
        courses: List[Course] = self.course_repo.get_by_user_id(user_id)
        course_dto = [self._to_dto(course) for course in courses]
        return course_dto

    def create_course(self, course_data: CreateCourseDTO, user_id: UUID) -> CourseDTO:
        existing_course: List[Course] = self.course_repo.get_courses_by_name(
            course_data.name
        )
        if existing_course:
            raise HTTPException(
                status_code=400, detail="Course with this name already exists."
            )

        course_data_dump = course_data.model_dump()
        course_data_dump["id"] = uuid.uuid4()
        course_data_dump["user_id"] = user_id
        course_data_dump["created_at"] = datetime.now()
        course_data_dump["updated_at"] = datetime.now()
        course: Course = self.course_repo.create(course_data_dump)
        return self._to_dto(course=course)

    def update_course(self, course_id: UUID, course_data: UpdateCourseDTO) -> CourseDTO:
        course_data_dump = course_data.model_dump(exclude_unset=True)
        course_data_dump["updated_at"] = datetime.now()
        course = self.course_repo.update(course_id, course_data_dump)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")

        return self._to_dto(course=course)

    def delete_course(self, course_id: UUID) -> dict:
        if not self.course_repo.delete(course_id):
            raise HTTPException(status_code=404, detail="Course not found")
        return {"message": f"Course has been successfully deleted."}

    def get_courses_with_uploaded_files(self) -> List[CourseDTO]:
        courses: List[Course] = self.course_repo.get_courses_with_uploaded_files()
        course_dto = []
        for c in courses:
            course_dto.append(self._to_dto(course=c))
        return course_dto

    def get_courses_by_name(self, name: str) -> List[CourseDTO]:
        courses: List[Course] = self.course_repo.get_courses_by_name(name)
        course_dto = []
        for c in courses:
            course_dto.append(self._to_dto(course=c))
        return course_dto

    def get_courses_by_created_at_range(
        self, start_date: str, end_date: str
    ) -> List[CourseDTO]:
        courses: List[Course] = self.course_repo.get_courses_by_created_at_range(
            start_date, end_date
        )
        course_dto = []
        for c in courses:
            course_dto.append(self._to_dto(course=c))
        return course_dto

