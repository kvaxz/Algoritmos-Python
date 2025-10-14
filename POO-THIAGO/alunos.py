class Aluno:
    def __init__(self, nome, ra):
        self.nome = nome
        self.ra = ra

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        print(f"Alunos da {self.nome}:")
        for a in self.alunos:
            print(f"Nome: {a.nome} | RA: {a.ra}")

a1 = Aluno("João", "12345")
a2 = Aluno("Maria", "67890")

f = Universidade("Faculdade XYZ")
f.adicionar_aluno(a1)
f.adicionar_aluno(a2)

f.listar_alunos()