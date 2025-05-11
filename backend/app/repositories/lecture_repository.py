from sqlalchemy.orm import Session
from uuid import UUID
from app.database import Lecture, Summarization, UploadedFile
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from typing import List

class LectureRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_lecture(self, lec_data: dict) -> Lecture:
        """Create a new lecture"""
        lecture = Lecture(**lec_data)
        try:
            self.db.add(lecture)
            self.db.commit()
            self.db.refresh(lecture)
            return lecture
        except IntegrityError:
            self.db.rollback()
            raise ValueError("Lecture already exists for the given summarization_id")

    def get_all_lectures(self) -> List[Lecture]:
        return self.db.query(Lecture).all()
    
    # def get_lectures_by_user_id(self, user_id: UUID) -> List[Lecture]:
    #     """Get all lectures for a specific user ID"""
    #     return self.db.query(Lecture).filter(Lecture.summarization.file.user_id == user_id).all()

    def get_lectures_by_user_id(self, user_id: UUID) -> List[Lecture]:
        """
        Get all lectures for a specific user ID by traversing
        Lecture -> Summarization -> UploadedFile -> user_id
        """
        return (
            self.db.query(Lecture)
            .join(Lecture.summarization) 
            .join(Summarization.file)
            .filter(UploadedFile.user_id == user_id)
            .all()
        )

    def get_lecture_by_id(self, lecture_id: UUID) -> Lecture:
        """Get a lecture by its ID"""
        return self.db.query(Lecture).filter(Lecture.id == lecture_id).first()

    def get_lecture_by_summarization_id(self, summarization_id: UUID) -> Lecture:
        """Get a lecture by its summarization_id"""
        return (
            self.db.query(Lecture)
            .filter(Lecture.summarization_id == summarization_id)
            .first()
        )

    def update_lecture(self, lecture_id: UUID, lec_data: dict) -> Lecture:
        """Update a lecture's name"""
        lecture = self.get_lecture_by_id(lecture_id)
        for key, value in lec_data.items():
            setattr(lecture, key, value)
        self.db.commit()
        self.db.refresh(lecture)
        return lecture

    def delete_lecture(self, lecture_id: UUID) -> bool:
        """Delete a lecture by its ID"""
        lecture = self.db.query(Lecture).filter(Lecture.id == lecture_id).first()
        if lecture:
            self.db.delete(lecture)
            self.db.commit()
            return True
        return False
