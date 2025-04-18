from pydantic import BaseModel, ConfigDict


class LearningMaterialTag(BaseModel):
    learning_material_id: str
    tag_id: str

    model_config = ConfigDict(str_max_length=255)
