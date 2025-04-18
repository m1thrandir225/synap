from .course import Course
from .lecture import LectureBase, LectureDTO, CreateLectureDTO, UpdateLectureDTO
from .file_tag import FileTag
from .uploaded_file import UploadedFileBase, UpdateUploadedFileDTO, UploadedFileDTO
from .learning_material import (
    LearningMaterialBase,
    LearningMaterialDTO,
    CreateLearningMaterialDTO,
    UpdateLearningMaterialDTO,
)
from .note import NoteBase, NoteResponse, CreateNoteDTO, UpdateNoteDTO
from .recommendation import (
    CreateRecommendationDTO,
    RecommendationBase,
    RecommendationDTO,
    UpdateRecommendationDTO,
)
from .recommendation_interaction import (
    CreateRecommendationInteractionDTO,
    RecommendationInteractionBase,
    UpdateRecommendationInteractionDTO,
    RecommendationInteractionDTO,
)
from .user import User, CreateUserDTO, UpdateUserPassword, EditUserDTO
from .summarization import Summarization
from .learning_material_tag import LearningMaterialTag
from .tag import Tag
