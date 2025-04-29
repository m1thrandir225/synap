from typing import Optional
from pydantic import UUID4, BaseModel, ConfigDict


class TagBase(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class CreateTagDTO(TagBase):
    pass


class UpdateTagDTO(BaseModel):
    name: Optional[str] = None

    model_config = ConfigDict(str_max_length=255)


class TagDTO(TagBase):
    id: UUID4
