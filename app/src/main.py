from aluno import Aluno

# Lista Global de alunos
alunos = []

def cadastrar_aluno():
    nome = input("Nome: ")
    email = input("Email: ")
    curso = input("Curso: ")

    aluno = Aluno(nome, email, curso)
    alunos.append(aluno)
    print(f"\nAluno cadastrado! Matrícula: {aluno.matricula}")


def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print("\n-----------------")
        print(aluno)


def buscar_aluno(matricula):
    for aluno in alunos:
        if aluno.matricula == matricula.upper():
            return aluno
    return None


def atualizar_aluno():
    mat = input("Matrícula: ")
    aluno = buscar_aluno(mat)
    if not aluno:
        print("Aluno não encontrado.")
        return

    nome = input("Novo nome (enter para manter): ")
    email = input("Novo email (enter para manter): ")
    curso = input("Novo curso (enter para manter): ")

    aluno.atualizar(nome or None, email or None, curso or None)
    print("Aluno atualizado!")


def deletar_aluno():
    mat = input("Matrícula: ")
    aluno = buscar_aluno(mat)

    if not aluno:
        print("Aluno não encontrado.")
        return
    alunos.remove(aluno)
    print("Aluno removido!")


def menu():
    while True:
        print("\n--- Sistema de Gerenciamento de Alunos ---")
        print("\n1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Sair")

        op = input("Opção: ")

        if op == "1":
            cadastrar_aluno()
        elif op == "2":
            listar_alunos()
        elif op == "3":
            atualizar_aluno()
        elif op == "4":
            deletar_aluno()
        elif op == "0":
            break
        else:
            print("Opção inválida")


menu()