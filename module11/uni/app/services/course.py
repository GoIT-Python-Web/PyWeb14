
from app.repos.course import CourseRepo
from app.schemas.course import CourseDetailed, CourseListItem


class CourseService:
    def __init__(self) -> None:
        self.repo = CourseRepo()

    async def get_all(self)-> list[CourseListItem]:
        courses_from_db = await self.repo.get_all()
        return [CourseListItem(**course) for course in courses_from_db]

    async def get_detailed_view(self, course_id) -> CourseDetailed:
        course_from_db =  await self.repo.get_one(course_id)
        return CourseDetailed(**course_from_db)

    async def create_course(self, course_data: CourseListItem):
        await self.repo.create_one(course_data)
        return 200