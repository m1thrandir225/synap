from pydantic import BaseModel, ConfigDict


class Tag(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(str_max_length=255)
