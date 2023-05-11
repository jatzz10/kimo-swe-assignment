from pydantic import BaseModel
from typing import List


class Chapter(BaseModel):
    name: str
    text: str
    rating: int = 0

class Course(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]
    rating: int = 0