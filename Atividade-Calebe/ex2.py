class Aluno:
    def __init__(self,nome,matricula,curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostrar_curso(self):
        return f"O aluno cursa {self.curso}"
    
    def alterar_curso(self):
        novo_curso = input("Insira o novo curso: ")
        self.curso = novo_curso
        print(f"O novo curso agora é: `{self.curso}")
        
        