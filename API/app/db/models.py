from sqlalchemy import Column, String
from .database import Base


class StudentModel(Base):

    __tablename__ = "students"

    id = Column(String, primary_key=True)

    nome = Column(String)

    email = Column(String, unique=True)

    curso = Column(String)