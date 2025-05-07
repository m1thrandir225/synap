from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from typing import List
from app.database import User
from app.dependencies import get_current_token, get_current_user, get_lecture_service
from app.models import CreateLectureDTO, UpdateLectureDTO, LectureDTO
from app.services import LectureService

router = APIRouter(
    prefix="/lectures", tags=["lectures"], dependencies=[Depends(get_current_token)]
)


@router.get("/{lecture_id}", response_model=LectureDTO)
def get_lecture(
    lecture_id: UUID, 
    service: LectureService = Depends(get_lecture_service),
    current_user: User = Depends(get_current_user)
):
    try:
        return service.get_lecture_by_id(lecture_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=List[LectureDTO])
def get_lectures(service: LectureService = Depends(get_lecture_service), current_user: User = Depends(get_current_user)):
    return service.get_all_lectures()


@router.get("/by_summarization/{summarization_id}", response_model=LectureDTO)
def get_lecture_by_summarization_id(
    summarization_id: UUID, 
    service: LectureService = Depends(get_lecture_service),
    current_user: User = Depends(get_current_user)
):
    try:
        return service.get_lecture_by_summarization_id(summarization_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=LectureDTO)
def create_lecture(
    lecture_data: CreateLectureDTO,
    service: LectureService = Depends(get_lecture_service),
    current_user: User = Depends(get_current_user)
):
    return service.create_lecture(lecture_data)


@router.put("/{lecture_id}", response_model=LectureDTO)
def update_lecture(
    lecture_id: UUID,
    lecture_data: UpdateLectureDTO,
    service: LectureService = Depends(get_lecture_service),
    current_user: User = Depends(get_current_user)
):
    try:
        return service.update_lecture(lecture_id, lecture_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{lecture_id}", response_model=dict)
def delete_lecture(
    lecture_id: UUID, service: LectureService = Depends(get_lecture_service),
    current_user: User = Depends(get_current_user)
):
    try:
        service.delete_lecture(lecture_id)
        return {"message": "Lecture deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
