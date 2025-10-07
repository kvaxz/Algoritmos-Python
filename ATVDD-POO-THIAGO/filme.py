class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        return f"Filme {self.nome} foi iniciado!"
    
class Acao(Filme):
    def __init__(self,nome, duracao):
        super().__init__(nome,duracao)
    
    def explodir(self):
        return "KABUUUUUUUUUUUM"
    
class Drama(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def medo(self):
        return "Ai que medinho"

class Suspense(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def ansiedade(self):
        return "Ai que ansiedade"
    
