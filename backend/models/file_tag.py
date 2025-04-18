from pydantic import BaseModel, ConfigDict


class FileTag(BaseModel):
    file_id: str
    tag_id: str

    model_config = ConfigDict(str_max_length=255)
