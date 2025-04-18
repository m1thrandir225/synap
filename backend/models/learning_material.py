from typing import Optional
from pydantic import BaseModel, ConfigDict


class LearningMaterialBase(BaseModel):
    title: str
    description: str
    material_type: str

    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class CreateLearningMaterialDTO(LearningMaterialBase):
    pass


class UpdateLearningMaterialDTO(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    material_type: Optional[str] = None


class LearningMaterialDTO(BaseModel):
    url: str
    created_at: str
