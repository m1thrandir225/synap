from fastapi import Depends, HTTPException, status
from starlette.status import HTTP_401_UNAUTHORIZED
from app.database import User, get_db
from sqlalchemy.orm import Session
from app.services import (
    UserService,
    TagService,
    FileTagService,
    UploadedFileService,
    NoteService,
    RecommendationService,
    RecommendationInteractionService,
    LearningMaterialService,
    LearningMaterialTagService,
    LectureService,
    CourseService,
)
from app.repositories import (
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
from fastapi.security import OAuth2PasswordBearer
from app.security import JWT_TYPE, decode_token
# Security

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


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
def get_course_service(
    course_repo: CourseRepository = Depends(get_course_repository),
) -> CourseService:
    return CourseService(course_repo)


def get_user_service(
    user_repo: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(user_repo)


def get_tag_service(
    tag_repo: TagRepository = Depends(get_tag_repository),
) -> TagService:
    return TagService(tag_repo)


def get_note_service(
    note_repo: NoteRepository = Depends(get_note_repository),
) -> NoteService:
    return NoteService(note_repo)


def get_recommendation_service(
    recom_repo: RecommendationRepository = Depends(get_recommendation_repository),
) -> RecommendationService:
    return RecommendationService(recom_repo)


def get_recommendation_interaction_service(
    ri_repo: RecommendationInteractionRepository = Depends(
        get_recommendation_interaction_repository
    ),
) -> RecommendationInteractionService:
    return RecommendationInteractionService(ri_repo)


def get_learning_material_service(
    lm_repo: LearningMaterialRepository = Depends(get_learning_material_repository),
) -> LearningMaterialService:
    return LearningMaterialService(lm_repo)


def get_file_tag_service(
    file_tag_repo: FileTagRepository = Depends(get_file_tag_repository),
) -> FileTagService:
    return FileTagService(file_tag_repo)


def get_uploaded_files_service(
    uploaded_file_repo: UploadedFileRepository = Depends(get_uploaded_file_repository),
) -> UploadedFileService:
    return UploadedFileService(uploaded_file_repo)


def get_learning_material_tag_service(
    repo: LearningMaterialTagRepository = Depends(get_learning_material_tag_repository),
) -> LearningMaterialTagService:
    return LearningMaterialTagService(repo)


def get_lecture_service(
    lec_repo: LectureRepository = Depends(get_lecture_repository),
) -> LectureService:
    return LectureService(lec_repo)


def get_current_token(token: str = Depends(oauth2_scheme)):
    if not decode_token(token):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED, detail="Access token is invalid"
        )
    return token


async def get_current_user(
    token: str = Depends(get_current_token),
    userService: UserService = Depends(get_user_service),
) -> User:
    user_id = decode_token(token, type=JWT_TYPE.ACCESS)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
        )

    user = userService.get_user_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )
    return user
