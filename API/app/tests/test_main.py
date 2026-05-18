import sys
import os

from fastapi.testclient import TestClient

# Ajuste de path (caso rode dentro de /tests)
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from API.app.main import app

client = TestClient(app)

def create_student(nome):
    return client.post("/api/v1/alunos/", json={
        "nome": nome,
        "email": f"{nome.lower()}@email.com",
        "curso": ["GES", "GEC"]
    })


def test_create_students():
    r1 = create_student("A1")
    r2 = create_student("A2")
    r3 = create_student("A3")

    assert r1.status_code == 200
    assert "id" in r1.json()


def test_list_students():
    response = client.get("/api/v1/alunos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_by_id():
    r = create_student("Teste")
    aluno_id = r.json()["id"]

    response = client.get(f"/api/v1/alunos/{aluno_id}")
    assert response.status_code == 200


def test_update_student():
    r = create_student("Update")
    aluno_id = r.json()["id"]

    response = client.patch(f"/api/v1/alunos/{aluno_id}", json={
        "nome": "Atualizado"
    })

    assert response.status_code == 200
    assert response.json()["nome"] == "Atualizado"


def test_delete_student():
    r = create_student("Delete")
    aluno_id = r.json()["id"]

    response = client.delete(f"/api/v1/alunos/{aluno_id}")
    assert response.status_code == 200


def test_min_two_courses():
    response = client.post("/api/v1/alunos/", json={
        "nome": "Erro",
        "email": "erro@email.com",
        "curso": ["GES"]
    })

    assert response.status_code == 400


def test_reset_students():
    create_student("A")
    response = client.delete("/api/v1/alunos/")
    assert response.status_code == 200