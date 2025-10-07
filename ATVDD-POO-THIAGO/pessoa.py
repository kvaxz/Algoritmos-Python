class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, nota1bimestre, nota2bimestre, nota3bimestre, nota4bimestre):
        super().__init__(nome, idade)
        self.nota1bimestre = nota1bimestre
        self.nota2bimestre = nota2bimestre
        self.nota3bimestre = nota3bimestre
        self.nota4bimestre = nota4bimestre

    def calcularMedia(self):
        media = (self.nota1bimestre + self.nota2bimestre + self.nota3bimestre + self.nota4bimestre)/4
        self.media = media
        return self.media
    
class Professor(Pessoa):
    def __init__(self, nome, idade,disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario

    def comecar_aula(self):
        return f"Aula da {self.nome} da disciplina {self.disciplina} iniciada!"
    
    def salario_prof(self):
        return f"Salário da professora {self.nome} é R${self.salario}"
    
aluno1 = Aluno("Kva", 10, 8, 7.5, 9, 10)
print(f"Média do {aluno1.nome}: {aluno1.calcularMedia():.2f}")

professor1 = Professor("Claudiana",33,"Matemática",4970.50)
print(professor1.comecar_aula())
print(professor1.salario_prof())
    
