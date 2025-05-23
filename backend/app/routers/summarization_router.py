from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from app.dependencies import get_uploaded_files_service, get_summarization_service, get_current_user
from app.log import get_logger
from app.services import SummarizationService
from app.services import UploadedFileService
from app.models import CreateSummarization, SummarizationBase, SummarizationDTO
from app.database import User


log = get_logger(__name__)
router = APIRouter(prefix="/summarization", tags=["summarization_router"])


@router.post("/summarize")
async def summarize_file(
    summarization: CreateSummarization,
    summarization_service: SummarizationService = Depends(get_summarization_service),
    uploaded_files_service: UploadedFileService = Depends(get_uploaded_files_service),
):
    uploaded_file = uploaded_files_service.get_uploaded_file(summarization.file_id)

    return await summarization_service.summarize_file_and_store(
        filename=uploaded_file.file_name,
        file_id=summarization.file_id,
        openai_id=uploaded_file.openai_id,
        summarization_name=summarization.name,
        original_filename=uploaded_file.file_name,
    )


@router.get("/{summarization_id}", response_model=SummarizationDTO)
def get_summarization_by_id(
    summarization_id: UUID,
    service: SummarizationService = Depends(get_summarization_service),
):
    try:
        summarization = service.get_summary_by_id(summarization_id)
        return summarization
    except HTTPException as e:
        raise e

@router.get("/", response_model=List[SummarizationBase])
def get_summarizations_for_user(
    service: SummarizationService = Depends(get_summarization_service),
    current_user: User = Depends(get_current_user)
):
    try:
        summarizations = service.get_all_summaries(current_user.id)
        return summarizations
    except HTTPException as e:
        raise e