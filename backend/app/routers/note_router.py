from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from typing import List
from app.dependencies import get_current_token, get_note_service
from app.models import CreateNoteDTO, UpdateNoteDTO
from app.services import NoteService
from app.models import NoteDTO

router = APIRouter(
    prefix="/notes", tags=["notes"], dependencies=[Depends(get_current_token)]
)


@router.get("/{note_id}", response_model=NoteDTO)
def get_note(note_id: UUID, service: NoteService = Depends(get_note_service)):
    note = service.get_note_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.get("/", response_model=List[NoteDTO])
def get_all_notes(service: NoteService = Depends(get_note_service)):
    return service.get_all_notes()


@router.get("/user/{user_id}", response_model=List[NoteDTO])
def get_notes_by_user(user_id: UUID, service: NoteService = Depends(get_note_service)):
    return service.get_notes_by_user_id(user_id)


@router.get("/course/{course_id}", response_model=List[NoteDTO])
def get_notes_by_course(
    course_id: UUID, service: NoteService = Depends(get_note_service)
):
    return service.get_notes_by_course_id(course_id)


@router.post("/", response_model=NoteDTO)
def create_note(
    note_data: CreateNoteDTO, service: NoteService = Depends(get_note_service)
):
    return service.create_note(note_data)


@router.put("/notes/{note_id}", response_model=NoteDTO)
def update_note(
    note_id: UUID,
    note_data: UpdateNoteDTO,
    service: NoteService = Depends(get_note_service),
):
    updated_note = service.update_note(note_id, note_data)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note


@router.delete("/notes/{note_id}", response_model=dict)
def delete_note(note_id: UUID, service: NoteService = Depends(get_note_service)):
    success = service.delete_note(note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found or already deleted")
    return {"message": "Note deleted successfully"}
