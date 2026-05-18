# Sistema de Gerenciamento de Alunos (API REST com FastAPI)

## Descrição

Esta aplicação consiste em uma API REST desenvolvida em **Python utilizando FastAPI**, responsável pelo gerenciamento de dados de alunos.

A aplicação permite realizar operações de **criação, consulta, atualização e remoção de registros (CRUD)**, utilizando persistência de dados com **PostgreSQL**, integração via **SQLAlchemy** e execução em containers com **Docker**.

---

## Tecnologias Utilizadas

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker / Docker Compose
- Pytest

---

## Estrutura dos Dados

Cada aluno possui os seguintes atributos:

- **ID**
- **Nome**
- **Email**
- **Curso**
- **Matrícula**

---

## Banco de Dados

A aplicação utiliza **PostgreSQL** para persistência dos dados.

O mapeamento objeto-relacional (ORM) é realizado com **SQLAlchemy**, permitindo a comunicação entre a aplicação Python e o banco de dados.

As tabelas são criadas automaticamente na inicialização da aplicação através do comando:

```python
Base.metadata.create_all(bind=engine)
```

---

## Como Executar com Docker

### 1. Construir e subir os containers

```bash
docker compose up --build -d
```

Este comando irá:

- Criar o container da API FastAPI
- Criar o container do PostgreSQL
- Instalar todas as dependências
- Inicializar o banco de dados
- Disponibilizar a API na porta 8000

---

### 2. Verificar containers em execução

```bash
docker ps
```

Containers esperados:

- `alunos_api`
- `alunos_db`

---

### 3. Parar containers

```bash
docker compose down
```

---

## Como Executar Localmente (sem Docker)

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar aplicação

```bash
uvicorn main:app --reload
```

---

## Documentação Swagger

Após iniciar a aplicação, acesse:

```text
http://localhost:8000/docs
```

A interface Swagger permite testar todos os endpoints da API de forma interativa.

---

## Endpoints Disponíveis

### Criar aluno

```http
POST /api/v1/alunos/
```

### Listar alunos

```http
GET /api/v1/alunos/
```

### Buscar aluno por ID

```http
GET /api/v1/alunos/{id}
```

### Atualizar aluno

```http
PATCH /api/v1/alunos/{id}
```

### Remover aluno

```http
DELETE /api/v1/alunos/{id}
```

### Resetar base de alunos

```http
DELETE /api/v1/alunos/
```

---

## Testes Automatizados

Os testes foram desenvolvidos utilizando **pytest**, cobrindo:

- Criação de alunos
- Consulta de registros
- Busca por ID
- Atualização
- Remoção
- Validação de regras de negócio
- Reset de registros

### Executar testes

```bash
pytest -v
```

---

## Evidências dos Testes

### Testes iniciais

![Testes](/API/app/images/image-2.png)

---

### Testes após correções

![Testes corrigidos](/API/app/images/image.png)

---

### Testes com integração ao PostgreSQL

![Testes PostgreSQL](/API/app/images/image-3.png)

---

## Arquitetura do Projeto

```text
app/
├── db/
├── routes/
├── schemas/
├── services/
├── tests/
├── main.py
├── docker-compose.yml
├── dockerfile
└── requirements.txt
```

---

