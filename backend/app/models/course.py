from typing import Optional
from pydantic import UUID4, BaseModel, ConfigDict
from datetime import datetime


class CourseBase(BaseModel):
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class CreateCourseDTO(CourseBase):
    user_id: UUID4


class UpdateCourseDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class CourseDTO(CourseBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime
