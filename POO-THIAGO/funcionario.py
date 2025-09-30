## HERAN;A E POLIMORFISMO
class funcionario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senho = senha
    
    def logar(self):
        print(f"{self.nome} logou no sistema")

    def set_senha(self, novaSenha):
        self.senha = novaSenha
        return True

class gerente(funcionario):
    def __init__(self, nome, login, senha, setor):
        super().__init__(nome, login, senha)
        self.setor = setor
    
    def logar(self):
        confirm = input("Digite o token")
        if confirm:
            print(f"Gerente {self.nome} logado no sistema com sucesso")


alencar = gerente("Alencar", "alen","5610472938","Produção")
alencar.logar()

f1 = funcionario("Gabriel", "kva", "1029384756")
f2 = funcionario("Cavalieri", "gabs", "5647382910")

f1.logar()
f2.logar()

