from fastapi import APIRouter

from API.app.schemas.student import Student
from API.app.services import student_service


router = APIRouter(
    prefix="/api/v1/alunos",
    tags=["Alunos"]
)


@router.post("/")
def create(student: Student):
    return student_service.create_student(student)


@router.get("/")
def list_all():
    return student_service.list_students()


@router.get("/{aluno_id}")
def get_by_id(aluno_id: str):
    return student_service.get_student(aluno_id)


@router.patch("/{aluno_id}")
def update(aluno_id: str, data: dict):
    return student_service.update_student(
        aluno_id,
        data
    )


@router.delete("/{aluno_id}")
def delete(aluno_id: str):
    return student_service.delete_student(aluno_id)


@router.delete("/")
def reset():
    return student_service.reset_students()