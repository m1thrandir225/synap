from datetime import timedelta
from typing import Any
from uuid import uuid4
from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from config import settings
from database import get_db, User
from models import UserDTO, CreateUserDTO
from security import (
    create_access_token,
    decode_token,
    generate_password_hash,
    verify_password,
)

authentication_router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserDTO


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    user_id = decode_token(token)
    if user_id is None:
        raise Exception("")

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise Exception("")
    return user


@authentication_router.post(
    "/signup", response_model=True, status_code=status.HTTP_201_CREATED
)
async def signup(
    user_data: CreateUserDTO, response: Response, db: Session = Depends(get_db)
) -> Any:
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with that email already exists",
        )
    user_dict = {
        "id": uuid4(),
        "first_name": user_data.first_name,
        "last_name": user_data.last_name,
        "email": user_data.email,
        "password": generate_password_hash(user_data.password),
    }

    new_user = User(**user_dict)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(subject=str(new_user.id))
    refresh_token = create_access_token(
        subject=str(new_user.id),
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES + 15),
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES + 15 * 60,
        samesite="lax",
        secure=False if settings.ENV in ["dev", "development"] else True,
    )

    db.refresh(new_user)

    user_dto = UserDTO.model_validate(new_user)

    return {"access_token": access_token, "token_type": "bearer", "user": user_dto}
