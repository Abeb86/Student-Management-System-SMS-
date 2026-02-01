from pydantic import BaseModel, EmailStr
from typing import Optional


class Student(BaseModel):
    student_id: int
    name: str
    major: str
    email: EmailStr


class StudentCreate(Student):
    pass


class StudentUpdate(Student):
    name: Optional[str] = None
    major: Optional[str] = None
    email: Optional[EmailStr] = None
    student_id: Optional[int] = None  