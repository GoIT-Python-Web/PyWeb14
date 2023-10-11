from fastapi import APIRouter

from app.schemas.course import CourseDetailed, CourseListItem, Course
from app.services.course import CourseService


router = APIRouter(prefix="/courses")




@router.get("/")
async def list_courses()-> list[CourseListItem]:
    service = CourseService()
    return await service.get_all()



@router.get("/{course_id}")
async def get_course_details(course_id: int)-> CourseDetailed:
    service = CourseService()
    return service.get_detailed_view(course_id)



@router.post("/")
async def get_course_details(body: Course)-> CourseDetailed:
    service = CourseService()
    await service.create_course(body)
    return {"status": "OK"}
