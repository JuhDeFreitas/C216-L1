# Sistema de Gerenciamento de Alunos (API REST com FastAPI)

## Descrição

Esta aplicação consiste em uma API REST desenvolvida em **Python utilizando FastAPI**, responsável por gerenciar dados de alunos.

A API permite realizar operações de criação, consulta, atualização e remoção de registros, além de filtros e buscas específicas.

---

## Estrutura dos Dados

Cada aluno possui os seguintes atributos:

* **Nome**
* **Idade**
* **Curso**
* **Matrícula**

---

## Como Executar a API

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o servidor:

```bash
uvicorn src.main:app --reload
```

---

## Documentação (Swagger)

Após iniciar a aplicação, acesse:

```text
http://localhost:8000/docs
```

Interface interativa para testar todos os endpoints da API.

---

## Testes Automatizados

Os testes foram desenvolvidos utilizando **pytest**, cobrindo as principais rotas da API.

Para executar os testes:

```bash
pytest -v
```

---

## Testes

Abaixo está um exemplo da execução dos testes com sucesso:

Os testes cobrem:

- Criação de alunos
- Consulta (lista e por ID/matrícula)
- Atualização (total e parcial)
- Remoção
- Tratamento de erros (ex: aluno não encontrado)

![alt text](/API/app/images/image-2.png)

--- 

Testes após correções da Aula 4:

![alt text](/API/app/images/image.png)

---
