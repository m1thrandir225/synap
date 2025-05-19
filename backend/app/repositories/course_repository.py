from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session, selectinload
from uuid import UUID
from app.database import Course, UploadedFile

class CourseRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, course_id: UUID) -> Course | None:
        """
        Get a course by its unique ID.
        """
        return self.db.query(Course).filter(Course.id == course_id).first()

    def get_by_user_id(self, user_id: UUID) -> List[Course]:
        """
        Get all courses created by a specific user.
        """
        return self.db.query(Course).options(
            selectinload(Course.uploaded_files).selectinload(UploadedFile.summarization)
            ).filter(Course.user_id == user_id).all()

    def create(self, course_data: dict) -> Course:
        """
        Create a new course with the provided data.
        """
        db_course = Course(
            **course_data
        )
        self.db.add(db_course)
        self.db.commit()
        self.db.refresh(db_course)
        return db_course

    def update(self, course_id: UUID, course_data: dict) -> Course | None:
        """
        Update an existing course by its ID.
        """
        course = self.get_by_id(course_id)
        if course:
            for key, value in course_data.items():
                setattr(course, key, value)
            self.db.commit()
            self.db.refresh(course)
            return course
        return None

    def delete(self, course_id: UUID):
        """
        Delete a course by its unique ID.
        """
        course = self.get_by_id(course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
            
        self.db.delete(course)
        self.db.commit()
        return True

    def get_courses_with_uploaded_files(self) -> list[Course]:
        """
        Get all courses that have uploaded files.
        """
        return self.db.query(Course).filter(Course.uploaded_files.any()).all()

    def get_courses_by_name(self, name: str) -> list[Course]:
        """
        Get courses by their name (partial match).
        """
        return self.db.query(Course).filter(Course.name.ilike(f"%{name}%")).all()

    def get_courses_by_created_at_range(
        self, start_date: str, end_date: str
    ) -> list[Course]:
        """
        Get courses created within a specific date range.
        """
        return (
            self.db.query(Course)
            .filter(Course.created_at.between(start_date, end_date))
            .all()
        )
