from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from typing import List
from dependencies import get_current_token, get_lecture_service
from database import Lecture
from models import CreateLectureDTO, UpdateLectureDTO
from services.lecture_service import LectureService

router = APIRouter(
    prefix="/lectures", tags=["lectures"], dependencies=[Depends(get_current_token)]
)


@router.get("/{lecture_id}", response_model=Lecture)
def get_lecture(
    lecture_id: UUID, service: LectureService = Depends(get_lecture_service)
):
    try:
        return service.get_lecture_by_id(lecture_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/lectures", response_model=List[Lecture])
def get_lectures(service: LectureService = Depends(get_lecture_service)):
    return service.get_all_lectures()


@router.get("/by_summarization/{summarization_id}", response_model=Lecture)
def get_lecture_by_summarization_id(
    summarization_id: UUID, service: LectureService = Depends(get_lecture_service)
):
    try:
        return service.get_lecture_by_summarization_id(summarization_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=Lecture)
def create_lecture(
    lecture_data: CreateLectureDTO,
    service: LectureService = Depends(get_lecture_service),
):
    return service.create_lecture(lecture_data)


@router.put("/{lecture_id}", response_model=Lecture)
def update_lecture(
    lecture_id: UUID,
    lecture_data: UpdateLectureDTO,
    service: LectureService = Depends(get_lecture_service),
):
    try:
        return service.update_lecture(lecture_id, lecture_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{lecture_id}", response_model=dict)
def delete_lecture(
    lecture_id: UUID, service: LectureService = Depends(get_lecture_service)
):
    try:
        service.delete_lecture(lecture_id)
        return {"message": "Lecture deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
