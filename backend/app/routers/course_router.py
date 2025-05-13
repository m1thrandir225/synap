from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from typing import List
from app.database import User
from app.dependencies import get_course_service, get_current_token, get_current_user
from app.models import CreateCourseDTO, UpdateCourseDTO, CourseDTO
from app.services import CourseService

router = APIRouter(
    prefix="/courses", tags=["courses"], dependencies=[Depends(get_current_token)]
)


#idk if this works, untested.
@router.get("/with_files", response_model=List[CourseDTO])
def get_courses_with_uploaded_files(service: CourseService = Depends(get_course_service), current_user: User = Depends(get_current_user)):
    return service.get_courses_with_uploaded_files()

@router.get("/range", response_model=List[CourseDTO])
def get_courses_by_created_at_range(start_date: str, end_date: str, service: CourseService = Depends(get_course_service), current_user: User = Depends(get_current_user)):
    return service.get_courses_by_created_at_range(start_date, end_date)

#FIXME: same reason as note_router.py's /search route
@router.get("/search", response_model=List[CourseDTO])
def get_courses_by_name(name: str, service: CourseService = Depends(get_course_service), current_user: User = Depends(get_current_user)):
    return service.get_courses_by_name(name)


@router.get("/user", response_model=List[CourseDTO])
def get_courses_by_user(service: CourseService = Depends(get_course_service), current_user: User = Depends(get_current_user)):
    return service.get_courses_by_user(current_user.id)


@router.get("/{course_id}", response_model=CourseDTO)
def get_course(course_id: UUID, service: CourseService = Depends(get_course_service), current_user: User = Depends(get_current_user)):
    try:
        return service.get_course(course_id)
    except HTTPException as e:
        raise e

#REDUNDANT, same reason as the note_router's get_all()  
# @router.get("/", response_model=List[CourseDTO])
# def get_all_courses(service: CourseService = Depends(get_course_service), current_user: User = Depends(get_current_user)):
#     return service.get_all_courses()

@router.post("/", response_model=CourseDTO)
def create_course(course_data: CreateCourseDTO, service: CourseService = Depends(get_course_service), current_user: User = Depends(get_current_user)):
    # course_data_dump = course_data.model_dump()
    # if course_data_dump.get("user_id") is None:
    #    course_data_dump["user_id"] = current_user.id
    # course_data.user_id = current_user.id
    return service.create_course(course_data, current_user.id)

@router.put("/{course_id}", response_model=CourseDTO)
def update_course(course_id: UUID, course_data: UpdateCourseDTO, service: CourseService = Depends(get_course_service), current_user: User = Depends(get_current_user)):
    return service.update_course(course_id, course_data)

@router.delete("/{course_id}", response_model=dict)
def delete_course(course_id: UUID, service: CourseService = Depends(get_course_service), current_user: User = Depends(get_current_user)):
    return service.delete_course(course_id)

