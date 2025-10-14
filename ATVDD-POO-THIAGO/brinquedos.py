class Brinquedos:
    def __init__(self,nome,cor,tamanho,preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        return f"Estou brincando com {self.nome}"
    
class Bonecas(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, cor_cabelo):
        super().__init__(nome, cor, tamanho, preco)
        self.cor_cabelo = cor_cabelo
    
    def brincar(self):
        return f"Esta {self.nome} é linda, com um cabelo {self.cor_cabelo}"

class Carrinhos(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, tipo_carro):
        super().__init__(nome, cor, tamanho, preco)
        self.tipo_carro = tipo_carro
    
    def brincar(self):
        return f"Estou brincando com o {self.nome}, que é um {self.tipo_carro}"
    
class Fidgets(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, velocidade):
        super().__init__(nome, cor, tamanho, preco)
        self.velocidade = velocidade

    def brincar(self):
        return f"Esse {self.nome} é top, ele gira a {self.velocidade}km/h!"

class Bicicletas(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, tamanho_aro):
        super().__init__(nome, cor, tamanho, preco)
        self.tamanho_aro = tamanho_aro

    def brincar(self):
        return f"Essa {self.nome} é {self.cor}, com aro {self.tamanho_aro}"
    
class Videogames(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, armazenamento):
        super().__init__(nome, cor, tamanho, preco)
        self.armazenamento = armazenamento

    def brincar(self):
        return f"Esse {self.nome}, foi carro ein (R${self.preco}), mas tem {self.armazenamento}GB de armazenamento!"