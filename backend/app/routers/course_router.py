from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from typing import List
from database.models.user import User
from dependencies import get_course_service, get_current_token, get_current_user
from database import Course
from models import CreateCourseDTO, UpdateCourseDTO  # Adjust imports as necessary
from services.course_service import CourseService  

router = APIRouter(
    prefix="/courses", tags=["courses"], dependencies=[Depends(get_current_token)]
)

# Get a single course by ID
@router.get("{course_id}", response_model=Course)
def get_course(course_id: UUID, service: CourseService = Depends(get_course_service)):
    try:
        return service.get_course(course_id)
    except HTTPException as e:
        raise e

@router.get("/", response_model=List[Course])
def get_all_courses(service: CourseService = Depends(get_course_service)):
    return service.get_all_courses()

@router.get("/user/{user_id}", response_model=List[Course])
def get_courses_by_user(user_id: UUID, service: CourseService = Depends(get_course_service)):
    return service.get_courses_by_user(user_id)

@router.post("/", response_model=Course)
def create_course(course_data: CreateCourseDTO, service: CourseService = Depends(get_course_service)):
    return service.create_course(course_data)

@router.put("/{course_id}", response_model=Course)
def update_course(course_id: UUID, course_data: UpdateCourseDTO, service: CourseService = Depends(get_course_service)):
    return service.update_course(course_id, course_data)

@router.delete("/{course_id}", response_model=dict)
def delete_course(course_id: UUID, service: CourseService = Depends(get_course_service)):
    return service.delete_course(course_id)

@router.get("/with_notes", response_model=List[Course])
def get_courses_with_notes(service: CourseService = Depends(get_course_service)):
    return service.get_courses_with_notes()

@router.get("/with_files", response_model=List[Course])
def get_courses_with_uploaded_files(service: CourseService = Depends(get_course_service)):
    return service.get_courses_with_uploaded_files()

@router.get("/search", response_model=List[Course])
def get_courses_by_name(name: str, service: CourseService = Depends(get_course_service), current_user: User = Depends(get_current_user)):
    return service.get_courses_by_name(name, current_user.id)

@router.get("/range", response_model=List[Course])
def get_courses_by_created_at_range(start_date: str, end_date: str, service: CourseService = Depends(get_course_service)):
    return service.get_courses_by_created_at_range(start_date, end_date)