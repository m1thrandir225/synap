from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime

class Summarization(BaseModel):
    id: str
    file_id: str
    summary_text: str
    ai_model_used: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(str_max_length=255)
