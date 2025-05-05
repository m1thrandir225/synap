from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from app.dependencies import get_current_token, get_user_service
from models import UpdateUserDTO
from app.services import UserService

router = APIRouter(
    prefix="/user", tags=["user"], dependencies=[Depends(get_current_token)]
)


@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
async def update(
    user_id: str,
    user_data: UpdateUserDTO,
    user_service: UserService = Depends(get_user_service),
):
    user_service.update_user(user_id, user_data)
    return {"message": "User updated successfully"}


@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: str, user_service: UserService = Depends(get_user_service)):
    user_service.delete_user(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
