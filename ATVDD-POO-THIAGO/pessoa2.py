class Pessoa:
    def __init__(self,nome,telefone,email,endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociacao(self):
        return f"Prazer sou {self.nome}, vai ser um prazer negociar com você"
    
class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def pagar_imposto(self):
        return f"Isso ai {self.nome}, pague os impostos certinho pro leão da receita"

class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
    
    def sonegar_imposto(self):
        return f"Isso ai {self.nome}, quem não sonega, não prospera!"
    
juridica1 = PessoaJuridica("Pedrin","6798298980","pedrin@gmail.com","Rua preda 55","208424982928")
print(juridica1.negociacao())
print(juridica1.sonegar_imposto())

fisica1 = PessoaFisica("Joaozin","872794821","jao@gmail.outlook.br","Rua dapre 55","069.782.655-20")
print(fisica1.pagar_imposto())
print(fisica1.negociacao())