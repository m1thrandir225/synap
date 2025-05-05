from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from app.database import User
from app.dependencies import get_current_token, get_current_user, get_user_service
from app.models import UpdateUserDTO
from app.services import UserService

router = APIRouter(
    prefix="/user", tags=["user"], dependencies=[Depends(get_current_token)]
)


@router.put("/", status_code=status.HTTP_200_OK)
async def update(
    user_data: UpdateUserDTO,
    current_user: User = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service),
):
    user_service.update_user(current_user.id, user_data)
    return {"message": "User updated successfully"}


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    current_user: User = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service),
):
    user_service.delete_user(current_user.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
