from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Course(BaseModel):
    user_id: str
    name: str
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(str_max_length=255)  # or customize as needed
