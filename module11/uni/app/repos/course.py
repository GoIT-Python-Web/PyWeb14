from app.database.connection import db
from app.schemas.course import Course


class CourseRepo:
    async def get_all(self): 
        return await db.courses.find()
    
    async def create_one(self, course_data: Course):
        await db.course.insert_one(course_data.dict())
        return 200