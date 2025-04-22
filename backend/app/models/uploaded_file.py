from datetime import datetime
from pydantic import UUID4, BaseModel, ConfigDict


class UploadedFileBase(BaseModel):
    file_name: str
    file_path: str
    file_type: str
    file_size: str
    mime_type: str

    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class UpdateUploadedFileDTO(BaseModel):
    course_id: str


class UploadedFileDTO(UploadedFileBase):
    id: UUID4
    course_id: UUID4
    user_id: UUID4
    created_at: datetime
