from pydantic import UUID4, BaseModel, ConfigDict


class LearningMaterialTag(BaseModel):
    learning_material_id: UUID4
    tag_id: UUID4

    model_config = ConfigDict(from_attributes=True, str_max_length=255)
