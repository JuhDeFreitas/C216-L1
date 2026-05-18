from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from API.app.schemas.student import Student
from API.app.services import student_service
from API.app.db.database import get_db


router = APIRouter(
    prefix="/api/v1/alunos",
    tags=["Alunos"]
)


# CREATE
@router.post("/")
def create(
    student: Student,
    db: Session = Depends(get_db)
):
    
    return student_service.create_student(
        student,
        db
    )


# LIST
@router.get("/")
def list_all(
    db: Session = Depends(get_db)
):

    return student_service.list_students(
        db
    )


# GET BY ID
@router.get("/{aluno_id}")
def get_by_id(
    aluno_id: str,
    db: Session = Depends(get_db)
):

    return student_service.get_student(
        aluno_id,
        db
    )


# UPDATE
@router.patch("/{aluno_id}")
def update(
    aluno_id: str,
    data: dict,
    db: Session = Depends(get_db)
):

    return student_service.update_student(
        aluno_id,
        data,
        db
    )


# DELETE
@router.delete("/{aluno_id}")
def delete(
    aluno_id: str,
    db: Session = Depends(get_db)
):

    return student_service.delete_student(
        aluno_id,
        db
    )


# RESET
@router.delete("/")
def reset(
    db: Session = Depends(get_db)
):

    return student_service.reset_students(
        db
    )