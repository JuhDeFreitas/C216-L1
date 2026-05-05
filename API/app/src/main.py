from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

students = []

@app.get("/")
def root():
    return {"message": "API de alunos funcionando"}

# Create 
@app.post("/students")
def create_student(student: dict):
    required_fields = ["nome", "idade", "curso", "matricula"]
    for field in required_fields:
        if field not in student:
            raise HTTPException(status_code=400, detail=f"Campo '{field}' é obrigatório")

    student["id"] = len(students) + 1
    students.append(student)
    return student

# Listar todos
@app.get("/students")
def list_students():
    return students

# Get por ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Aluno não encontrado")

# Atualizar completamente dos dadsos do aluno
@app.put("/students/{student_id}")
def update_student(student_id: int, new_data: dict):
    for i, student in enumerate(students):
        if student["id"] == student_id:
            students[i].update(new_data)
            return students[i]
    raise HTTPException(status_code=404, detail="Aluno não encontrado")

#  Atualização parcial dos dados do aluno
@app.patch("/students/{student_id}")
def partial_update_student(student_id: int, new_data: dict):
    for student in students:
        if student["id"] == student_id:
            student.update(new_data)
            return student
    raise HTTPException(status_code=404, detail="Aluno não encontrado")

# Deletar aluno por ID
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, student in enumerate(students):
        if student["id"] == student_id:
            students.pop(i)
            return {"message": "Aluno removido"}
    raise HTTPException(status_code=404, detail="Aluno não encontrado")

# Buscar por matrícula
@app.get("/students/matricula/{matricula}")
def get_by_matricula(matricula: str):
    for student in students:
        if student["matricula"] == matricula:
            return student
    raise HTTPException(status_code=404, detail="Aluno não encontrado")

# Filtrar por curso
@app.get("/students/filter/curso")
def filter_by_course(curso: str = Query(...)):
    return [s for s in students if s.get("curso") == curso]

# Filtrar por idade
@app.get("/students/filter/idade")
def filter_by_age(min_idade: int = Query(...)):
    return [s for s in students if s.get("idade", 0) >= min_idade]

# Contagem total de alunos cadastrados
@app.get("/students/count")
def count_students():
    return {"total": len(students)}