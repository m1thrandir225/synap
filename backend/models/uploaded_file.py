from pydantic import BaseModel, ConfigDict


class UploadedFileBase(BaseModel):
    file_name: str
    file_path: str
    file_type: str
    file_size: str
    mime_type: str


# No create DTO since the upload will be handled from the UploadFile class from fastapi


class UpdateUploadedFileDTO(BaseModel):
    course_id: str


class UploadedFileDTO(UploadedFileBase):
    id: str
    course_id: str
    user_id: str
    created_at: str
