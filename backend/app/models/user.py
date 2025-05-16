from datetime import datetime
from typing import List, Optional
from pydantic import UUID4, BaseModel, ConfigDict


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str

    model_config = ConfigDict(from_attributes=True, str_max_length=255)


class CreateUserDTO(UserBase):
    id: Optional[UUID4] = None
    password: str


class UpdateUserDTO(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None


class UpdateUserPasswordDTO(BaseModel):
    old_password: str
    new_password: str


class UserDTO(UserBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime
