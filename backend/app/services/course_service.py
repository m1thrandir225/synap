from uuid import UUID
from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories import CourseRepository
from app.database import Course
from app.models import CreateCourseDTO, UpdateCourseDTO 


class CourseService:
    def __init__(self, course_repo: CourseRepository):
        self.course_repo = course_repo

    def get_course(self, course_id: UUID) -> Course:
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return course

    def get_all_courses(self) -> List[Course]:
        return self.course_repo.get_all()

    def get_courses_by_user(self, user_id: UUID) -> List[Course]:
        return self.course_repo.get_by_user_id(user_id)

    def create_course(self, course_data: CreateCourseDTO) -> Course:
        # Ensure the course name doesn't already exist or any other business logic
        existing_course = self.course_repo.get_courses_by_name(course_data.name)
        if existing_course:
            raise HTTPException(
                status_code=400, detail="Course with this name already exists."
            )

        course = self.course_repo.create(
            course_data.model_dump(),
        ) 
        return course

    def update_course(self, course_id: UUID, course_data: UpdateCourseDTO) -> Course:
        course = self.course_repo.update(
            course_id, course_data.dict(exclude_unset=True)
        )
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return course

    def delete_course(self, course_id: UUID) -> dict:
        if not self.course_repo.delete(course_id):
            raise HTTPException(status_code=404, detail="Course not found")
        return {"message": f"Course has been successfully deleted."}

    def get_courses_with_notes(self) -> List[Course]:
        return self.course_repo.get_courses_with_notes()

    def get_courses_with_uploaded_files(self) -> List[Course]:
        return self.course_repo.get_courses_with_uploaded_files()

    def get_courses_by_name(self, name: str) -> List[Course]:
        return self.course_repo.get_courses_by_name(name)

    def get_courses_by_created_at_range(
        self, start_date: str, end_date: str
    ) -> List[Course]:
        return self.course_repo.get_courses_by_created_at_range(start_date, end_date)
