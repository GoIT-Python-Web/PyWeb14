from pydantic import BaseModel

from enum import Enum

class FiveStarsScore(Enum):
    refund: "1"
    bad: "2"
    ok: "3"
    good: "4"
    perfect: "5"

class Course(BaseModel):
    name: str
    score: str
    brief_description: str


class CourseListItem(BaseModel):
    name: str
    score: str
    brief_description: str



class CourseDetailed(Course):
    detailed_description: str 
    authors: list[str]




