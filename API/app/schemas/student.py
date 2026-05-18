from pydantic import BaseModel, EmailStr
from typing import List


class Student(BaseModel):
    nome: str
    email: EmailStr
    curso: List[str]