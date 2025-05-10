from pydantic import UUID4, BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime

from .uploaded_file import UploadedFileDTO


class SummarizationBase(BaseModel):
    id: Optional[UUID4] = None
    file_id: UUID4
    summary_text: str
    ai_model_used: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: datetime

    model_config = ConfigDict(str_max_length=255)


class SummarizationDTO(SummarizationBase):
    file: UploadedFileDTO
