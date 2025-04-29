from datetime import datetime, timezone
from typing import Any
from uuid import uuid4
from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.config import settings
from app.database import User, get_db
from app.models import CreateUserDTO, UserDTO
from app.security import (
    JWT_TYPE,
    create_jwt_token,
    decode_token,
    generate_password_hash,
    verify_password,
)

router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserDTO


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    user_id = decode_token(token, type=JWT_TYPE.ACCESS)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
        )

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )

    return user


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=Token)
async def signup(
    user_data: CreateUserDTO, response: Response, db: Session = Depends(get_db)
) -> Any:
    # FIXME: move to repository
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
        "updated_at": datetime.now(timezone.utc),
    }

    new_user = User(**user_dict)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_jwt_token(subject=str(new_user.id), type=JWT_TYPE.ACCESS)
    refresh_token = create_jwt_token(subject=str(new_user.id), type=JWT_TYPE.REFRESH)

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES + 15 * 60,
        samesite="none",
        secure=False if settings.ENV in ["dev", "development"] else True,
    )

    db.refresh(new_user)

    user_dto = UserDTO.model_validate(new_user)

    return {"access_token": access_token, "token_type": "bearer", "user": user_dto}


@router.post("/login", response_model=Token)
async def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> Any:
    """
    Authenticate a user and return a new access and refresh token
    """
    # FIXME: move to repository
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or not verify_password(form_data.password, str(user.password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_dto = UserDTO.model_validate(user)

    access_token = create_jwt_token(subject=str(user.id), type=JWT_TYPE.ACCESS)
    refresh_token = create_jwt_token(subject=str(user.id), type=JWT_TYPE.REFRESH)

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        max_age=settings.REFRESH_TOKEN_EXPIRE_MINUTES * 60,
        samesite="none",
        secure=False if settings.ENV in ["dev", "development"] else True,
    )

    return {"access_token": access_token, "token_type": "bearer", "user": user_dto}


@router.post("/refresh", response_model=Token)
async def refresh_token(
    request: Request, response: Response, db: Session = Depends(get_db)
):
    refresh_token = request.cookies.get("refresh_token")

    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh Token missing",
            headers={"WWW-Authentication", "Bearer"},  # type: ignore
        )

    user_id = decode_token(refresh_token, type=JWT_TYPE.REFRESH)

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh Token missing",
            headers={"WWW-Authentication", "Bearer"},  # type: ignore
        )

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh Token missing",
            headers={"WWW-Authentication", "Bearer"},  # type: ignore
        )
    new_access_token = create_jwt_token(subject=str(user.id), type=JWT_TYPE.ACCESS)

    db.refresh(user)

    user_dto = UserDTO.model_validate(user)

    return {"access_token": new_access_token, "token_type": "bearer", "user": user_dto}


@router.post("/logout")
async def logout(
    response: Response, current_user: User = Depends(get_current_user)
) -> dict:
    response.delete_cookie(
        key="refresh_token",
        httponly=True,
        samesite="lax",
        secure=False if settings.ENV in ["dev", "development"] else True,
    )
    return {"detail": "Sucessfully logged out"}


@router.get("/me", response_model=UserDTO)
async def get_current_user_info(
    current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
) -> Any:
    db.refresh(current_user)

    user_dto = UserDTO.model_validate(current_user)

    return user_dto
