class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self,novo_preco):
        self.preco = novo_preco
        print(f"Novo preço é R${novo_preco}")

    def mostrar_setor(self):
        return f"Setor: {self.setor}"

class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote=False,open_bar=False,open_food=True,estacionamento=False):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.open_bar == False:
            return "Não é open bar chefe!"
        elif self.open_bar == True:
            return "Vodka Martini. Shaken, not stirred."
    
    def acessar_camarote(self):
        if self.camarote == False:
            return "PA acesso negado!"
        elif self.camarote == True:
            return "Bem-vindo, rei do camarote!"

ingressovip = IngressoVIP(300,7,False,True,False,True)
print(ingressovip.mostrar_setor())
print(ingressovip.pegar_bebida())
print(ingressovip.acessar_camarote())