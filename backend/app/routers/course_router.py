from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from typing import List
from app.dependencies import get_course_service, get_current_user
from app.database import  User
from app.models import CreateCourseDTO, UpdateCourseDTO, CourseDTO, CourseBase
from app.services.course_service import CourseService

router = APIRouter()

@router.get("/courses/{course_id}", response_model=CourseBase)
def get_course(course_id: UUID, service: CourseService = Depends(get_course_service)):
    try:
        return service.get_course(course_id)
    except HTTPException as e:
        raise e

@router.get("/courses", response_model=List[CourseBase])
def get_all_courses(service: CourseService = Depends(get_course_service)):
    return service.get_all_courses()

@router.get("/courses/user/{user_id}", response_model=List[CourseBase])
def get_courses_by_user(user_id: UUID, service: CourseService = Depends(get_course_service)):
    return service.get_courses_by_user(user_id)

@router.post("/courses", response_model=CreateCourseDTO)
def create_course(course_data: CourseBase, 
                  service: CourseService = Depends(get_course_service),
                  user: User = Depends(get_current_user) 
                  ):
    create_course_dto = course_data.model_dump() 
    create_course_dto["user_id"] = user.id 
    create_course_dto = CreateCourseDTO.model_validate(create_course_dto)
    
    return service.create_course(create_course_dto)

@router.put("/courses/{course_id}", response_model=CourseBase)
def update_course(course_id: UUID, course_data: UpdateCourseDTO, service: CourseService = Depends(get_course_service)):
    return service.update_course(course_id, course_data)

@router.delete("/courses/{course_id}", response_model=dict)
def delete_course(course_id: UUID, service: CourseService = Depends(get_course_service)):
    return service.delete_course(course_id)

@router.get("/courses/with_notes", response_model=List[CourseBase])
def get_courses_with_notes(service: CourseService = Depends(get_course_service)):
    return service.get_courses_with_notes()

@router.get("/courses/with_files", response_model=List[CourseBase])
def get_courses_with_uploaded_files(service: CourseService = Depends(get_course_service)):
    return service.get_courses_with_uploaded_files()

@router.get("/courses/search", response_model=List[CourseDTO])
def get_courses_by_name(name: str, service: CourseService = Depends(get_course_service)):
    return service.get_courses_by_name(name)

@router.get("/courses/range", response_model=List[CourseDTO])
def get_courses_by_created_at_range(start_date: str, end_date: str, service: CourseService = Depends(get_course_service)):
    return service.get_courses_by_created_at_range(start_date, end_date)