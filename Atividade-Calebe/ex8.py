class ContaCorrente:
    def __init__(self,n_conta,nome, saldo = 0):
        self.n_conta = n_conta
        self.nome = nome
        self.saldo = saldo

    def set_name(self):
        novo_nome = input(f"Novo nome: ")
        self.nome = novo_nome

    def deposito(self):
        while True:
            try:
                deposito = float(input(f"Deposito: R$"))
                if deposito > 0:
                    self.saldo = self.saldo + deposito
                    print(f"Novo saldo: R${self.saldo}")
                    break
                else:
                    print("Ai é foda chefe")
            except:
                print("Valor invalido!")

    def saque(self):
        while True:
            try:
                saque = float(input("Saque: R$"))
                if saque <= self.saldo:
                    self.saldo = self.saldo - saque
                    print(f"Novo saldo: R${self.saldo}")
                    break
                else:
                    print("Ta tentando dar golpe chefe")
            except:
                print("Valor invalído")

cli = ContaCorrente("79094600","Gabriel",500)

cli.saque()
