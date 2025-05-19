from typing import Any
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from app.database import User
from app.models import (
    CreateUserDTO,
    UserDTO,
    LoginRegisterResponse,
    RefreshTokenResponse,
    RefreshTokenRequest,
)
from app.services import UserService
from app.dependencies import get_current_token, get_current_user, get_user_service
from app.security import (
    JWT_TYPE,
    create_jwt_token,
    decode_token,
    verify_password,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/signup", status_code=status.HTTP_201_CREATED, response_model=LoginRegisterResponse
)
async def signup(
    user_data: CreateUserDTO,
    userService: UserService = Depends(get_user_service),
):
    new_user = userService.create_user(user_data)

    access_token, access_token_expire_time = create_jwt_token(
        subject=str(new_user.id), type=JWT_TYPE.ACCESS
    )
    refresh_token, refresh_token_expire_time = create_jwt_token(
        subject=str(new_user.id), type=JWT_TYPE.REFRESH
    )

    user_dto = UserDTO.model_validate(new_user)

    return {
        "access_token": access_token,
        "access_token_expire_time": access_token_expire_time,
        "refresh_token": refresh_token,
        "refresh_token_expire_time": refresh_token_expire_time,
        "user": user_dto,
    }


@router.post("/login", response_model=LoginRegisterResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    userService: UserService = Depends(get_user_service),
):
    """
    Authenticate a user and return a new access and refresh token
    """
    user = userService.get_user_email(form_data.username)

    if not user or not verify_password(form_data.password, str(user.password)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_dto = UserDTO.model_validate(user)

    access_token, access_token_expire_time = create_jwt_token(
        subject=str(user.id), type=JWT_TYPE.ACCESS
    )
    refresh_token, refresh_token_expire_time = create_jwt_token(
        subject=str(user.id), type=JWT_TYPE.REFRESH
    )
    return {
        "access_token": access_token,
        "access_token_expire_time": access_token_expire_time,
        "refresh_token": refresh_token,
        "refresh_token_expire_time": refresh_token_expire_time,
        "user": user_dto,
    }


@router.post("/refresh", response_model=RefreshTokenResponse)
async def refresh_token(
    request_data: RefreshTokenRequest,
    userService: UserService = Depends(get_user_service),
):
    refresh_token = request_data.refresh_token
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh Token missing",
        )

    user_id = decode_token(refresh_token, type=JWT_TYPE.REFRESH)

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh Token missing",
        )

    user = userService.get_user_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh Token missing",
        )
    new_access_token, access_token_expire_time = create_jwt_token(
        subject=str(user.id), type=JWT_TYPE.ACCESS
    )
    return {
        "access_token": new_access_token,
        "access_token_expire_time": access_token_expire_time,
    }


@router.post("/logout")
async def logout(response: Response, token: str = Depends(get_current_token)) -> dict:
    return {"detail": "Sucessfully logged out"}


@router.get("/me", response_model=UserDTO)
async def get_current_user_info(
    current_user: User = Depends(get_current_user),
    userService: UserService = Depends(get_user_service),
) -> Any:
    user = userService.get_user_id(current_user.id)

    user_dto = UserDTO.model_validate(user)

    return user_dto
