from pydantic import BaseModel, Field
from typing import List


class OpenAIServiceResponse(BaseModel):
    """
    Pydantic model for the expected OpenAI service response.
    """
    summarization: str = Field(..., description="A summary of the text content.")
    topics: List[str] = Field(..., description="A list of main topics discussed in the text.")
    
    class Config:
        json_schema_extra = {
            "example": {
                "summarization": "The document discusses the features and benefits of the PostgreSQL database system, including its data types, indexing, and scalability.",
                "topics": ["PostgreSQL", "database", "data types", "indexing", "scalability"]
            }
        }
