class Aluno:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
    
    def exibir_nome(self):
        return f"{self.nome}"
    
pessoa = Aluno("gabriel","98298989")