from .course import CourseDTO, CreateCourseDTO, UpdateCourseDTO
from .file_tag import FileTag
from .learning_material import (
    LearningMaterialDTO,
    CreateLearningMaterialDTO,
    UpdateLearningMaterialDTO,
)
from .learning_material_tag import LearningMaterialTag
from .lecture import CreateLectureDTO, UpdateLectureDTO, LectureDTO
from .note import CreateNoteDTO, UpdateNoteDTO, NoteDTO
from .recommendation import (
    RecommendationDTO,
    CreateRecommendationDTO,
    UpdateRecommendationDTO,
)

from .recommendation_interaction import (
    RecommendationInteractionDTO,
    UpdateRecommendationInteractionDTO,
    CreateRecommendationInteractionDTO,
)
from .summarization import SummarizationDTO, SummarizationBase
from .tag import TagDTO, CreateTagDTO, UpdateTagDTO
from .uploaded_file import UploadedFileDTO, UpdateUploadedFileDTO
from .user import UserDTO, CreateUserDTO, UpdateUserDTO, UpdateUserPasswordDTO
