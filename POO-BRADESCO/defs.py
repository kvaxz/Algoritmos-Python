import os

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Conta(Pessoa):
    def __init__(self, nome, num_conta, agencia, saldo, extrato, senha):
        super().__init__(nome)
        self.num_conta = num_conta
        self.agencia = agencia
        self. saldo = saldo
        self.extrato = extrato
        self.__senha = senha

    def cadastro(self):
        os.system('cls')
        nome = input("Nome: ")
        while True:
            try:
                num_conta = int(input("Número da conta: "))
                break
            except:
                print("Insira valor valído")
        while True:
            try:  
                agencia = int(input("Agência: "))
                break
            except:
                print("Insira valor valído")
        while True:
            try:  
                saldo = float(input("Saldo: "))
                break
            except:
                print("Insira valor valído")
        senha = input("Senha: ")
        return Conta(nome, num_conta, agencia, saldo, [], senha)

    def get_senha(self):
        return self.__senha

    def depositar(self):
        os.system('cls')
        agen = int(input("Informe agência: "))
        if agen != self.agencia:
            print("ERRADO!")
        else:
            cont = int(input("Informe a conta: "))
            if cont != self.num_conta:
                print("ERRADO!")
            else:
                while True:  
                    try:         
                        valor_deposito = float(input("Valor a ser depositado: R$"))
                        if valor_deposito < 0:
                            print("Não dá chef!")
                        else:
                            self.saldo = self.saldo + valor_deposito
                            print(f"Deposito de R${valor_deposito} realizado.\nNovo saldo: R${self.saldo}")
                            self.extrato.append(f"Deposito: R${valor_deposito:.2f}\n")
                            break
                    except:
                        print("Insira valor valído!")
                    
    def sacar(self):
        os.system('cls')
        agen = int(input("Informe agência: "))
        if agen != self.agencia:
            print("ERRADO!")
        else:
            cont = int(input("Informe a conta: "))
            if cont != self.num_conta:
                print("ERRADO!")
            else:
                senha = input("Informe a senha: ")
                if senha != self.get_senha():
                    print("Senha ERRADA!")
                else:
                    while True:
                        try: 
                            saque = float(input("Valor do saque: R$"))
                            if saque > self.saldo:
                                print("Saque impossivel, ta duro pae")
                            else:
                                self.saldo = self.saldo - saque
                                print(f"Saque de R${saque} realizado!\nNovo saldo: R${self.saldo:.2f}")
                                self.extrato.append(f"Saque: R${saque:.2f}\n")
                                break
                        except:
                            print("Insira um valor valído!")



    def consultar_saldo(self):
        os.system('cls')
        while True:
            conta = int(input("Informe a conta: "))
            if conta != self.num_conta:
                print("Errado!")
            else:
                agencia = int(input("Informe agência: "))
                if agencia != self.agencia:
                    print("Errado!")
                else:
                    senha = input("Informe senha: ")
                    if senha != self.get_senha():
                        print("Errado!")
                    else:
                        print(f"Saldo: R${self.saldo:.2f}")
                        break

    def consultar_extrato(self):
        os.system('cls')
        while True:
            conta = int(input("Informe a conta: "))
            if conta != self.num_conta:
                print("Errado!")
            else:
                agencia = int(input("Informe agência: "))
                if agencia != self.agencia:
                    print("Errado!")
                else:
                    senha = input("Informe senha: ")
                    if senha != self.get_senha():
                        print("Errado!")
                    else:
                        print(f"Extrato:\n{self.extrato}")
                        input("\nPressione ENTER para voltar...")
                        break
