from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str

    model_config = ConfigDict(str_max_length=255)


class CreateUserDTO(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    model_config = ConfigDict(str_max_length=255)


class EditUserDTO(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str

    model_config = ConfigDict(str_max_length=255)


class UpdateUserPassword(BaseModel):
    id: str
    new_password: str

    model_config = ConfigDict(str_max_length=255)
