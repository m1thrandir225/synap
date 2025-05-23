from datetime import datetime
from typing import Optional
from fastapi import UploadFile
from pydantic import UUID4, BaseModel, ConfigDict


class UploadedFileBase(BaseModel):
    file_name: str
    file_path: str
    file_type: str
    file_size: int
    mime_type: str
    openai_id: Optional[str]
    
    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class CreateUploadedFile(UploadedFileBase):
    user_id: UUID4
    course_id: UUID4


class UpdateUploadedFileDTO(BaseModel):
    course_id: str


class UploadedFileDTO(UploadedFileBase):
    id: UUID4
    course_id: UUID4
    user_id: UUID4
    created_at: datetime
    has_summarization: bool 


class UploadFileRequest(BaseModel):
    file: UploadFile
    course_id: UUID4

class PresignedUrlDTO(BaseModel):
    url: str
    filename: str