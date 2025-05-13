from pydantic import UUID4, BaseModel, ConfigDict, Field
from typing import List, Optional
from datetime import datetime

from .uploaded_file import UploadedFileDTO


class CreateSummarization(BaseModel):
    name: str
    file_id: UUID4
class SummarizationBase(BaseModel):
    id: Optional[UUID4] = None
    file_id: UUID4
    summary_text: str
    ai_model_used: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: datetime
    name: str

    model_config = ConfigDict(str_max_length=255)


class SummarizationDTO(SummarizationBase):
    file: UploadedFileDTO


class OpenAIServiceResponse(BaseModel):
    """
    Pydantic model for the expected OpenAI service response.
    """
    summarization: str = Field(..., description="A summary of the text content.")
    topics: List[str] = Field(..., description="A list of main topics discussed in the text.")
    query: str

    class Config:
        json_schema_extra = {
            "example": {
                "summarization": "The document discusses the features and benefits of the PostgreSQL database system, including its data types, indexing, and scalability.",
                "topics": ["PostgreSQL", "database", "data types", "indexing", "scalability"]
            }
        }
