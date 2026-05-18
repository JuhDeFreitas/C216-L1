class Aluno:
    # Variável de classe para contar matrículas por curso
    contadores_curso = {}

    def __init__(self, nome, email, curso):
        self.nome = nome
        self.email = email
        self.curso = curso.upper()
        self.matricula = self._gerar_matricula()

    def _gerar_matricula(self):
        if self.curso not in Aluno.contadores_curso:
            Aluno.contadores_curso[self.curso] = 1
        else:
            Aluno.contadores_curso[self.curso] += 1

        matricula = f"{self.curso}{Aluno.contadores_curso[self.curso]}" 
        return matricula

    def atualizar(self, nome=None, email=None, curso=None):
        if nome:
            self.nome = nome
        if email:
            self.email = email
        if curso:
            self.curso = curso.upper()

    # Representação em string do objeto Aluno
    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Email: {self.email}\n"
            f"Curso: {self.curso}\n"
            f"Matrícula: {self.matricula}"
        )