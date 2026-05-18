from fastapi import HTTPException


students = {}

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


def create_student(student):

    if len(student.curso) < 2:
        raise HTTPException(
            status_code=400,
            detail="Aluno deve possuir pelo menos 2 cursos"
        )

    curso_base = student.curso[0]

    aluno_id = generate_id(curso_base)

    new_student = {
        "id": aluno_id,
        "nome": student.nome,
        "email": student.email,
        "curso": student.curso,
        "matricula": aluno_id
    }

    students[aluno_id] = new_student

    return new_student


def list_students():
    return list(students.values())


def get_student(aluno_id):

    if aluno_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return students[aluno_id]


def update_student(aluno_id, data):

    if aluno_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    if "curso" in data and len(data["curso"]) < 2:
        raise HTTPException(
            status_code=400,
            detail="Aluno deve possuir pelo menos 2 cursos"
        )

    students[aluno_id].update(data)

    return students[aluno_id]


def delete_student(aluno_id):

    if aluno_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    del students[aluno_id]

    return {"message": "Aluno removido"}


def reset_students():

    students.clear()

    return {"message": "Lista de alunos resetada"}