from typing import Annotated
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from app.dependencies import  get_uploaded_files_service
from app.services.summarization_service import SummarizationService, get_summarization_service
from app.services.uploaded_files_service import UploadedFileService
from app.models.summarization import CreateSummarization


router = APIRouter(prefix="/summarization", tags=["summarization_router"])


@router.post("/summarize")
async def summarize_file(
    summarization: CreateSummarization,
    summarization_service: Annotated[SummarizationService, Depends(get_summarization_service)],
    uploaded_files_repo: Annotated[UploadedFileService, Depends(get_uploaded_files_service)], 
):
    uploaded_file = uploaded_files_repo.get_uploaded_file(summarization.file_id)
    
    if not uploaded_file:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")

    return await summarization_service.summarize_file_and_store(
        filename=uploaded_file.file_name, file_id=summarization.file_id, summarization_name=summarization.name
    )

