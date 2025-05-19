from fastapi import Depends, HTTPException, status
from starlette.status import HTTP_401_UNAUTHORIZED
from app.database import User, get_db
from sqlalchemy.orm import Session
from app.services import (
    UserService,
    UploadedFileService,
    NoteService,
    RecommendationService,
    LearningMaterialService,
    CourseService,
    OpenAIService,
    SummarizationService,
    FileService
)
from app.repositories import (
    UserRepository,
    SummarizationRepository,
    RecommendationRepository,
    NoteRepository,
    UploadedFileRepository,
    CourseRepository,
    LearningMaterialRepository,
)
from fastapi.security import OAuth2PasswordBearer
from app.security import JWT_TYPE, decode_token
from .storage_provider import LocalStorageProvider
from .s3_storage_provider import S3StorageProvider
from .config import Settings, settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_uploaded_file_repository(
    db: Session = Depends(get_db),
) -> UploadedFileRepository:
    return UploadedFileRepository(db)


def get_course_repository(db: Session = Depends(get_db)) -> CourseRepository:
    return CourseRepository(db)

def get_summarization_repository(
    db: Session = Depends(get_db),
) -> SummarizationRepository:
    return SummarizationRepository(db)


def get_recommendation_repository(
    db: Session = Depends(get_db),
) -> RecommendationRepository:
    return RecommendationRepository(db)

def get_note_repository(db: Session = Depends(get_db)) -> NoteRepository:
    return NoteRepository(db)

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


def get_note_service(
    note_repo: NoteRepository = Depends(get_note_repository),
) -> NoteService:
    return NoteService(note_repo)

def get_recommendation_service(
    recom_repo: RecommendationRepository = Depends(get_recommendation_repository),
) -> RecommendationService:
    return RecommendationService(recom_repo)

def get_learning_material_service(
    lm_repo: LearningMaterialRepository = Depends(get_learning_material_repository),
) -> LearningMaterialService:
    return LearningMaterialService(lm_repo)


def get_uploaded_files_service(
    uploaded_file_repo: UploadedFileRepository = Depends(get_uploaded_file_repository),
) -> UploadedFileService:
    return UploadedFileService(uploaded_file_repo)

def get_openai_service(
) -> OpenAIService:
    return OpenAIService()

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
    print(f"Decoded user_id: {user_id}")
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

def get_local_storage_provider(
    user: User = Depends(get_current_user)
) -> LocalStorageProvider:
    return LocalStorageProvider(user=user)

def get_s3_storage_provider(
        user: User = Depends(get_current_user),
        settings: Settings = settings
) -> S3StorageProvider:
    return S3StorageProvider(
        user=user,
        bucket_name=settings.S3_BUCKET_NAME,
        aws_access_key_id=settings.S3_ACCESS_KEY_ID,
        aws_secret_access_key=settings.S3_SECRET_ACCESS_KEY,
        endpoint_url=None,
        region_name=settings.AWS_REGION_NAME
    )

def get_file_service(
        repo: UploadedFileRepository = Depends(get_uploaded_file_repository),
        service: UploadedFileService = Depends(get_uploaded_files_service),
        s3: S3StorageProvider = Depends(get_s3_storage_provider)
) -> FileService:
    return FileService(repo=repo, s3_provider=s3, uploaded_file_service=service)

def get_summarization_service(
        repo: SummarizationRepository = Depends(get_summarization_repository), openai_service: OpenAIService  = Depends(get_openai_service), learning_material_service: LearningMaterialService = Depends(get_learning_material_service), 
        recommendation_service: RecommendationService = Depends(get_recommendation_service), 
) -> SummarizationService:
    return SummarizationService(
        summarization_repository=repo, 
        openai_service=openai_service, learning_material_service=learning_material_service, recommendation_service=recommendation_service
    )


