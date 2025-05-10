import json
from typing import Annotated
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from app.database.db import get_db
from app.repositories.summarization_repository import SummarizationRepository
from sqlalchemy.orm import Session
from uuid import UUID
from app.dependencies import  get_uploaded_files_service
from app.services.summarization_service import SummarizationService, get_summarization_service
from app.services.uploaded_files_service import UploadedFileService


router = APIRouter(prefix="/summarization", tags=["summarization_router"])


@router.post("/summarize/{file_id}")
async def summarize_file(
    file_id: UUID,
    summarization_service: Annotated[SummarizationService, Depends(get_summarization_service)],
    uploaded_files_repo: Annotated[UploadedFileService, Depends(get_uploaded_files_service)], 
):
    uploaded_file = uploaded_files_repo.get_uploaded_file(file_id)
    if not uploaded_file:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")

    print(uploaded_file.file_name)

    return await summarization_service.summarize_file_and_store(
        filename=uploaded_file.file_name, file_id=file_id
    )

