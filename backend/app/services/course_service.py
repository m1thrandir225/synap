from uuid import UUID
from typing import List
import uuid
from fastapi import HTTPException
from app.repositories import CourseRepository
from app.database import Course
from app.models import CreateCourseDTO, UpdateCourseDTO, CourseDTO, CourseNoteDTO, UploadedFileDTO, SummarizationBase
from datetime import datetime



class CourseService:
    def __init__(self, course_repo: CourseRepository):
        self.course_repo = course_repo

    def _to_dto(self, course: Course):
        if course is None:
            return None
        notes: List[CourseNoteDTO] = []
        uploaded_files: List[UploadedFileDTO] = []
        summaries: List[SummarizationBase] = []

        for note in course.notes:
            notes.append(CourseNoteDTO(id=note.id, title=note.title, content=note.content, user_id=note.user_id, course_id=note.course_id,
                                       created_at=note.created_at, updated_at=note.updated_at))
        
        for file in course.uploaded_files:
            for summary in file.summarization:
                summaries.append(SummarizationBase(
                    id=summary.id,
                    file_id=summary.file_id,
                    summary_text=summary.summary_text,
                    ai_model_used=summary.ai_model_used,
                    updated_at=summary.updated_at,
                    name=summary.name,
                    created_at=summary.created_at,
                ))

            uploaded_files.append(UploadedFileDTO(file_name=file.file_name, 
                                                  file_path=file.file_path, 
                                                  file_type=file.file_type, 
                                                  file_size=file.file_size,
                                                  mime_type=file.mime_type,
                                                  id=file.id, 
                                                  course_id= file.course_id, 
                                                  user_id=file.user_id, 
                                                  created_at= file.created_at,
                                                  ))


        return CourseDTO(
            name=course.name,
            description=course.description, 
            id=course.id,
            user_id=course.user_id,
            created_at=course.created_at,
            updated_at=course.updated_at,
            notes=notes,
            uploaded_files=uploaded_files,
            summaries=summaries
        )
    
    def get_course(self, course_id: UUID) -> CourseDTO:
        course: Course = self.course_repo.get_by_id(course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return self._to_dto(course=course)

    # def get_all_courses(self) -> List[CourseDTO]:
    #     courses: List[Course] = self.course_repo.get_all()
    #     course_dto = []
    #     for c in courses:
    #         course_dto.append(self._to_dto(course=c))
    #     return course_dto

    def get_courses_by_user(self, user_id: UUID) -> List[CourseDTO]:
        courses: List[Course] = self.course_repo.get_by_user_id(user_id)
        course_dto = []
        for c in courses:
            course_dto.append(self._to_dto(course=c))
        return course_dto

    def create_course(self, course_data: CreateCourseDTO, user_id: UUID) -> CourseDTO:
        existing_course: List[Course] = self.course_repo.get_courses_by_name(course_data.name)
        if existing_course:
            raise HTTPException(
                status_code=400, detail="Course with this name already exists."
            )
        
        course_data_dump = course_data.model_dump()
        course_data_dump["id"] = uuid.uuid4()
        course_data_dump["user_id"] = user_id
        course_data_dump["created_at"] = datetime.now()
        course_data_dump["updated_at"] = datetime.now()
        course: Course = self.course_repo.create(
            course_data_dump
        )
        return self._to_dto(course=course)

    def update_course(self, course_id: UUID, course_data: UpdateCourseDTO) -> CourseDTO:
        course_data_dump = course_data.model_dump(exclude_unset=True)
        course_data_dump["updated_at"] = datetime.now()
        course: Course = self.course_repo.update(course_id, course_data_dump)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return self._to_dto(course=course)

    def delete_course(self, course_id: UUID) -> dict:
        if not self.course_repo.delete(course_id):
            raise HTTPException(status_code=404, detail="Course not found")
        return {"message": f"Course has been successfully deleted."}

    # def get_courses_with_notes(self) -> List[CourseDTO]:
    #     courses: List[Course] = self.course_repo.get_courses_with_notes()
    #     course_dto = []
    #     for c in courses:
    #         course_dto.append(self._to_dto(course=c))
    #     return course_dto

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
        courses: List[Course] = self.course_repo.get_courses_by_created_at_range(start_date, end_date)
        course_dto = []
        for c in courses:
            course_dto.append(self._to_dto(course=c))
        return course_dto