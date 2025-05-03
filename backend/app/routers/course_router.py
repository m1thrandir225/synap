from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from typing import List
from dependencies import get_course_service
from database import Course
from models import CreateCourseDTO, UpdateCourseDTO  # Adjust imports as necessary
from services.course_service import CourseService  

router = APIRouter()

# Get a single course by ID
@router.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: UUID, service: CourseService = Depends(get_course_service)):
    try:
        return service.get_course(course_id)
    except HTTPException as e:
        raise e

@router.get("/courses", response_model=List[Course])
def get_all_courses(service: CourseService = Depends(get_course_service)):
    return service.get_all_courses()

@router.get("/courses/user/{user_id}", response_model=List[Course])
def get_courses_by_user(user_id: UUID, service: CourseService = Depends(get_course_service)):
    return service.get_courses_by_user(user_id)

@router.post("/courses", response_model=Course)
def create_course(course_data: CreateCourseDTO, service: CourseService = Depends(get_course_service)):
    return service.create_course(course_data)

@router.put("/courses/{course_id}", response_model=Course)
def update_course(course_id: UUID, course_data: UpdateCourseDTO, service: CourseService = Depends(get_course_service)):
    return service.update_course(course_id, course_data)

@router.delete("/courses/{course_id}", response_model=dict)
def delete_course(course_id: UUID, service: CourseService = Depends(get_course_service)):
    return service.delete_course(course_id)

@router.get("/courses/with_notes", response_model=List[Course])
def get_courses_with_notes(service: CourseService = Depends(get_course_service)):
    return service.get_courses_with_notes()

@router.get("/courses/with_files", response_model=List[Course])
def get_courses_with_uploaded_files(service: CourseService = Depends(get_course_service)):
    return service.get_courses_with_uploaded_files()

@router.get("/courses/search", response_model=List[Course])
def get_courses_by_name(name: str, service: CourseService = Depends(get_course_service)):
    return service.get_courses_by_name(name)

@router.get("/courses/range", response_model=List[Course])
def get_courses_by_created_at_range(start_date: str, end_date: str, service: CourseService = Depends(get_course_service)):
    return service.get_courses_by_created_at_range(start_date, end_date)