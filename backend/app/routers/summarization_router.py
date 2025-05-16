from uuid import UUID
from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from app.dependencies import  get_uploaded_files_service, get_summarization_service
from app.services import SummarizationService
from app.services import UploadedFileService
from app.models import CreateSummarization


router = APIRouter(prefix="/summarization", tags=["summarization_router"])


@router.post("/summarize")
async def summarize_file(
    summarization: CreateSummarization,
    summarization_service: SummarizationService = Depends(get_summarization_service),
    uploaded_files_service: UploadedFileService = Depends(get_uploaded_files_service), 
):
    uploaded_file = uploaded_files_service.get_uploaded_file(summarization.file_id)
    
    if not uploaded_file:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")

    return await summarization_service.summarize_file_and_store(
        filename=uploaded_file.file_name, 
        file_id=summarization.file_id, 
        summarization_name=summarization.name, 
        original_filename=uploaded_file.file_name
    )


@router.get("/{summarization_id}")
def get_summarization_by_id(summarization_id: UUID, service: SummarizationService = Depends(get_summarization_service)):
    try:
        return service.get_summary_by_id(summarization_id)
    except HTTPException as e:
        raise e
