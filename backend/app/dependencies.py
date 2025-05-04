from fastapi import Depends
from services import CourseService
from sqlalchemy.orm import Session
from database import get_db
from services import (
    user_service,
    tag_service,
    NoteService
    RecommendationService,
    RecommendationInteractionService,
    LearningMaterialService
)
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

def get_learning_material_repository(
    db: Session = Depends(get_db),
) -> LearningMaterialRepository:
    return LearningMaterialRepository(db)
 
# Dependency functions for services 
def get_course_service(course_repo: CourseRepository = Depends(get_course_repository)) -> CourseService:
    return CourseService(course_repo)

def get_user_service(user_repo: UserRepository = Depends(get_user_repository)) -> user_service:
    return user_service(user_repo)

def get_tag_service(tag_repo: TagRepository = Depends(get_tag_repository)) -> tag_service:
    return tag_service(tag_repo)
  
def get_note_service(note_repo: NoteRepository = Depends(get_note_repository)) -> NoteService:
    return NoteService(note_repo)

def get_recommendation_service(recom_repo: RecommendationRepository = Depends(get_recommendation_repository)) -> RecommendationService:
    return RecommendationService(recom_repo)
  
def get_recommendation_interaction_service(
    ri_repo: RecommendationInteractionRepository = Depends(get_recommendation_interaction_repository)
) -> RecommendationInteractionService:
    return RecommendationInteractionService(ri_repo)
  
def get_recommendation_service(db: Session = Depends(get_db)) -> RecommendationService:
    return RecommendationService(db)
  
def get_learning_material_service(lm_repo: LearningMaterialRepository = Depends(get_learning_material_repository)) -> LearningMaterialService:
    return LearningMaterialService(lm_repo)