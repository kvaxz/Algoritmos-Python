class Funcionario:
    def __init__(self,nome,matricula,salario=float):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def bater_ponto(self):
        while True:
            entrada = input(f"{self.nome}, bata o ponto (True ou False): ").capitalize()
            
            if entrada == "True":
                ponto = True
                break
            elif entrada == "False":
                ponto = False
                break
            else:
                print("Digite apenas True ou False!")
                continue

        self.pontos.append(ponto)
        if ponto == True:
            status = "Presente"
        else:
            status = "Ausente"
        return f"{self.nome} ({self.matricula}) -> {status}"

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, setor, salario=float,meta=float):
        super().__init__(nome, matricula, salario)
        self.meta = meta
        self.setor = setor

    def bater_meta(self):
        while True:
            try:
                total = float(input("Informe valor vendido até o momento: R$"))
                if total < self.meta:
                    return f"{self.nome}, você ainda não bateu sua meta de R${self.meta}, vendeu apenas R${total}!"
                else:
                    return f"Brabo {self.nome}, bateu tua meta de R${self.meta}"
            except:
                print("Coloque algo valido pfv!")

class Gerente(Funcionario):
    def __init__(self, nome, matricula, setor, salario=float, num_vendedores=int):
        super().__init__(nome, matricula, salario)
        self.setor = setor
        self.num_vendedores = num_vendedores

    def receber_aumento(self):
        entrada = input("Seus funcionarios bateram as metas?(s/n): ").lower()

        if entrada == "s":
            return "Brabo, receba aumento!"
        elif entrada != "s":
            return "Então fodase, tmj"







func1 = Funcionario("Kvalieri","KJ235UI10",9999.99)
print(func1.bater_ponto())

vend1 = Vendedor("Gabs","OIQ2981LO","9",7999.99,50000)
print(vend1.bater_meta())

gerente1 = Gerente("Alencar","TRE99OI9",7,45997,28)
print(gerente1.receber_aumento())