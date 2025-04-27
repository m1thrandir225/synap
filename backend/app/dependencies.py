from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from services import LearningMaterialTagService
from repositories import (
    UserRepository,
    TagRepository,
    FileTagRepository,
    SummarizationRepository,
    RecommendationRepository,
    LectureRepository,
    NoteRepository,
    UploadedFileRepository,
    CourseRepository,
    RecommendationInteractionRepository,
    LearningMaterialTagRepository,
    LearningMaterialRepository,
)


# Dependency functions for repositories
def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_uploaded_file_repository(
    db: Session = Depends(get_db),
) -> UploadedFileRepository:
    return UploadedFileRepository(db)


def get_course_repository(db: Session = Depends(get_db)) -> CourseRepository:
    return CourseRepository(db)


def get_tag_repository(db: Session = Depends(get_db)) -> TagRepository:
    return TagRepository(db)


def get_file_tag_repository(db: Session = Depends(get_db)) -> FileTagRepository:
    return FileTagRepository(db)


def get_summarization_repository(
    db: Session = Depends(get_db),
) -> SummarizationRepository:
    return SummarizationRepository(db)


def get_recommendation_repository(
    db: Session = Depends(get_db),
) -> RecommendationRepository:
    return RecommendationRepository(db)


def get_recommendation_interaction_repository(
    db: Session = Depends(get_db),
) -> RecommendationInteractionRepository:
    return RecommendationInteractionRepository(db)


def get_lecture_repository(db: Session = Depends(get_db)) -> LectureRepository:
    return LectureRepository(db)


def get_note_repository(db: Session = Depends(get_db)) -> NoteRepository:
    return NoteRepository(db)


def get_learning_material_tag_repository(
    db: Session = Depends(get_db),
) -> LearningMaterialTagRepository:
    return LearningMaterialTagRepository(db)

def get_learning_material_tag_service(
    db: Session = Depends(get_db),
) -> LearningMaterialTagService:
    return LearningMaterialTagService(db)

def get_learning_material_repository(
    db: Session = Depends(get_db),
) -> LearningMaterialRepository:
    return LearningMaterialRepository(db)
