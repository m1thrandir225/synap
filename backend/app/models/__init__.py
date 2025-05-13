from .course import CourseDTO, CreateCourseDTO, UpdateCourseDTO, CourseBase
from .file_tag import FileTag
from .learning_material import (
    LearningMaterialDTO,
    CreateLearningMaterialDTO,
    UpdateLearningMaterialDTO,
)
from .note import CreateNoteDTO, UpdateNoteDTO, NoteDTO, CourseNoteDTO
from .recommendation import (
    RecommendationDTO,
    CreateRecommendationDTO,
    UpdateRecommendationDTO,
)
from .summarization import SummarizationDTO, SummarizationBase, CreateSummarization
from .uploaded_file import UploadedFileDTO, UpdateUploadedFileDTO, UploadedFileBase, UploadFileRequest, CreateUploadedFile
from .user import UserDTO, CreateUserDTO, UpdateUserDTO, UpdateUserPasswordDTO
from .auth import LoginRegisterResponse, RefreshTokenResponse, RefreshTokenRequest
