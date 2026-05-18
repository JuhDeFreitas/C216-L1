from fastapi import HTTPException
from sqlalchemy.orm import Session

from API.app.db.models import StudentModel


course_counter = {
    "GES": 0,
    "GEC": 0
}


def generate_id(curso):

    if curso not in course_counter:
        raise HTTPException(
            status_code=400,
            detail="Curso inválido"
        )

    course_counter[curso] += 1

    return f"{curso}{course_counter[curso]}"


# CREATE
def create_student(student, db: Session):

    if len(student.curso) < 2:
        raise HTTPException(
            status_code=400,
            detail="Aluno deve possuir pelo menos 2 cursos"
        )

    aluno_id = generate_id(
        student.curso[0]
    )

    db_student = StudentModel(
        id=aluno_id,
        nome=student.nome,
        email=student.email,
        curso=",".join(student.curso)
    )

    db.add(db_student)

    db.commit()

    db.refresh(db_student)

    return db_student


# LIST
def list_students(db: Session):

    return db.query(
        StudentModel
    ).all()


# GET BY ID
def get_student(aluno_id, db: Session):

    student = db.query(
        StudentModel
    ).filter(
        StudentModel.id == aluno_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return student


# UPDATE
def update_student(aluno_id, data, db: Session):

    student = db.query(
        StudentModel
    ).filter(
        StudentModel.id == aluno_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    if "curso" in data:

        if len(data["curso"]) < 2:
            raise HTTPException(
                status_code=400,
                detail="Aluno deve possuir pelo menos 2 cursos"
            )

        data["curso"] = ",".join(
            data["curso"]
        )

    for key, value in data.items():
        setattr(student, key, value)

    db.commit()

    db.refresh(student)

    return student


# DELETE
def delete_student(aluno_id, db: Session):

    student = db.query(
        StudentModel
    ).filter(
        StudentModel.id == aluno_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    db.delete(student)

    db.commit()

    return {
        "message": "Aluno removido"
    }


# RESET
def reset_students(db: Session):

    db.query(
        StudentModel
    ).delete()

    db.commit()

    return {
        "message": "Lista de alunos resetada"
    }