from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

# ===== Banco em memória =====
students = {}

# contador por curso (NÃO reinicia)
course_counter = {
    "GES": 0,
    "GEC": 0
}

# ===== Model =====
class Student(BaseModel):
    nome: str
    email: EmailStr
    curso: List[str]


# ===== Função para gerar ID =====
def generate_id(curso):
    if curso not in course_counter:
        raise HTTPException(status_code=400, detail="Curso inválido")

    course_counter[curso] += 1
    return f"{curso}{course_counter[curso]}"


# ===== ROOT =====
@app.get("/")
def root():
    return {"message": "API de alunos funcionando"}


# ===== CREATE =====
@app.post("/api/v1/alunos/")
def create_student(student: Student):
    
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


# ===== LIST =====
@app.get("/api/v1/alunos/")
def list_students():
    return list(students.values())


# ===== GET BY ID =====
@app.get("/api/v1/alunos/{aluno_id}")
def get_student(aluno_id: str):
    if aluno_id not in students:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    return students[aluno_id]


# ===== UPDATE (PATCH) =====
@app.patch("/api/v1/alunos/{aluno_id}")
def update_student(aluno_id: str, data: dict):

    if aluno_id not in students:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    if "curso" in data and len(data["curso"]) < 2:
        raise HTTPException(
            status_code=400,
            detail="Aluno deve possuir pelo menos 2 cursos"
        )

    students[aluno_id].update(data)
    return students[aluno_id]


# ===== DELETE POR ID =====
@app.delete("/api/v1/alunos/{aluno_id}")
def delete_student(aluno_id: str):
    if aluno_id not in students:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    del students[aluno_id]
    return {"message": "Aluno removido"}


# ===== RESET LIST =====
@app.delete("/api/v1/alunos/")
def reset_students():
    students.clear()
    return {"message": "Lista de alunos resetada"}