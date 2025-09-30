class mecanico:
    def __init__(self, nome, matricula, nivel): ### CONSTRUTOR
        self.nome = nome
        self.matricula = matricula
        self.nivel = nivel
        self.salario = 0

    def passarOrcamento(self):
        print("Seu carro ficou R$xx,xx")

    def realizarDiagnostico(self):
        print(f"{self.nome} diagnosticando o veículo")

    def get_salario(self):
        return self.salario
    
    def set_salario(self, valor):
        self.salario = valor 

    def caucularComissao(self, servicos):
        comissao = servicos * 0.15
        self.salario += comissao

mec1 = mecanico("Kvalieri", "129480-65", "N-1")

mec1.passarOrcamento()
mec1.realizarDiagnostico()
sal = mec1.get_salario()
print(sal)

mec1.set_salario(5000)
sal2 = mec1.get_salario()
print(sal2)

mec2 = mecanico("Joaozin", "198422-54", "N-3")

mec2.set_salario(9000)
x = mec2.get_salario()
print(f"Salário do {mec2.nome} é R${mec2.salario}")

mec1.caucularComissao(9000)

y = mec1.get_salario()
print(y)
 


