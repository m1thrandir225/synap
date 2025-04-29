from pydantic import UUID4, BaseModel, ConfigDict


# FIXME: reduntant? will we actually use this as a response in any api?
class FileTag(BaseModel):
    file_id: UUID4
    tag_id: UUID4

    model_config = ConfigDict(from_attributes=True, str_max_length=255)
