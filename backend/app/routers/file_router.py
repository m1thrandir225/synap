import os
import uuid
from typing import Annotated, List

from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from openai import OpenAI
from pydantic import BaseModel

from app.config import settings
from app.database.models import User
from app.dependencies import (get_current_token, get_current_user,
                              get_file_service, get_s3_storage_provider,
                              get_uploaded_files_service)
from app.log import get_logger
from app.models import CreateUploadedFile, PresignedUrlDTO, UploadedFileDTO
from app.s3_storage_provider import S3StorageProvider
from app.services import FileService, UploadedFileService
from app.storage_provider import LocalStorageProvider

log = get_logger(__name__)

router = APIRouter(
    prefix="/files", tags=["Files"], dependencies=[Depends(get_current_token)]
)


@router.get("/", response_model=List[UploadedFileDTO])
async def list_user_files(
    uploaded_files_service: UploadedFileService = Depends(get_uploaded_files_service),
    user: User = Depends(get_current_user),
):
    """
    Lists all files stored for the current authenticated user.
    Requires authentication because LocalStorageProvider depends on the user.
    """

    response = uploaded_files_service.get_uploaded_files_by_user(user_id=user.id)
    return response


@router.post("/", status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile,
    course_id: Annotated[str, Form()],
    user: User = Depends(get_current_user),
    service: FileService = Depends(get_file_service)
):
    """
    Uploads a new file for the current authenticated user.
    Requires authentication.
    """
    courseId = uuid.UUID(course_id)
    return await service.upload_file_and_create_record(file, user.id, courseId, None)


@router.get("/{file_id}", response_model=PresignedUrlDTO)
async def get_file(
    file_id: uuid.UUID,
    service: FileService = Depends(get_file_service),
    user: User = Depends(get_current_user)
):
    """
    Retrieves a specific file for the current authenticated user.
    Requires authentication.
    """
    return await service.get_file_download_url(file_id=file_id, user_id=user.id)


@router.delete("/{file_id}")
async def delete_file(
    file_id: uuid.UUID,
    service: FileService = Depends(get_file_service),
    user: User = Depends(get_current_user),
):
    """
    Deletes a specific file for the current authenticated user.
    Requires authentication.
    """
    return await service.delete_file_record_and_s3_object(file_id=file_id, user_id=user.id)