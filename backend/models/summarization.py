from pydantic import UUID4, BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime

from models.uploaded_file import UploadedFileDTO


class SummarizationBase(BaseModel):
    id: UUID4
    file_id: UUID4
    summary_text: str
    ai_model_used: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(str_max_length=255)


class SummarizationDTO(SummarizationBase):
    file: UploadedFileDTO
