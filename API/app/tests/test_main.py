import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def create_default_student():
    return client.post("/students", json={
        "nome": "Julia",
        "idade": 20,
        "curso": "Engenharia",
        "matricula": "12345"
    })

def test_create_student():
    response = create_default_student()
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Julia"

def test_create_student_missing_field():
    response = client.post("/students", json={
    "nome": "Erro"
    })
    assert response.status_code == 400

def test_list_students():
    response = client.get("/students")
    assert response.status_code == 200

def test_get_student():
    create_default_student()
    response = client.get("/students/1")
    assert response.status_code == 200

def test_get_by_matricula():
    create_default_student()
    response = client.get("/students/matricula/12345")
    assert response.status_code == 200

def test_filter_by_course():
    create_default_student()
    response = client.get("/students/filter/curso?curso=Engenharia")
    assert response.status_code == 200

def test_filter_by_age():
    create_default_student()
    response = client.get("/students/filter/idade?min_idade=18")
    assert response.status_code == 200

def test_update_student():
    create_default_student()
    response = client.put("/students/1", json={
        "nome": "Atualizado",
        "idade": 25,
        "curso": "Computação",
        "matricula": "999"
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Atualizado"

def test_delete_student():
    create_default_student()
    response = client.delete("/students/1")
    assert response.status_code == 200

def test_not_found():
    response = client.get("/students/999")
    assert response.status_code == 404