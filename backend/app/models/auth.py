from pydantic import BaseModel
from datetime import datetime
from .user import UserDTO


class LoginRegisterResponse(BaseModel):
    access_token: str
    access_token_expire_time: datetime
    refresh_token: str
    refresh_token_expire_time: datetime
    user: UserDTO


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshTokenResponse(BaseModel):
    access_token: str
    access_token_expire_time: datetime
