class Imoveis:
    def __init__(self,inscricao_municipal,valor_aluguel,valor_iptu):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.valor_iptu = valor_iptu

    def obter_boleto_iptu(self):
        return f"Parcela IPTU R${self.valor_iptu}"
    
    def set_valor_aluguel(self):
        novo_valor = input("Insira novo valor do aluguel: R$")
        self.valor_aluguel = novo_valor
        return f"Novo valor do aluguel é: R${self.valor_aluguel}"

class Casa(Imoveis):
    def __init__(self, inscricao_municipal, valor_aluguel, valor_iptu,qntdd_quartos):
        super().__init__(inscricao_municipal, valor_aluguel, valor_iptu)
        self.qntdd_quartos = qntdd_quartos

    def get_qntdd_quartos(self):
        return f"Essa casa possui {self.qntdd_quartos} quartos!"
    
class Apartamento(Imoveis):
    def __init__(self, inscricao_municipal, valor_aluguel, valor_iptu,andar):
        super().__init__(inscricao_municipal, valor_aluguel, valor_iptu)
        self.andar = andar

    def get_num_andar(self):
        return f"Este apartamento está no {self.andar}° andar"

class Terreno(Imoveis):
    def __init__(self, inscricao_municipal, valor_aluguel, valor_iptu,bairro):
        super().__init__(inscricao_municipal, valor_aluguel, valor_iptu)
        self.bairro = bairro

    def get_bairro(self):
        return f"Este terreno é no bairro {self.bairro}"

class Chacara(Imoveis):
    def __init__(self, inscricao_municipal, valor_aluguel, valor_iptu, hectares):
        super().__init__(inscricao_municipal, valor_aluguel, valor_iptu)
        self.hectares = hectares

    def num_hectares(self):
        return f"Chácara possui {self.hectares} hectares!"
