class Passagem:
    def __init__(self,preco,assento):
        self.preco = preco
        self.assento = assento
    
    def alterar_preco(self,novo_preco):
        while True:
            try:
                novo_preco = float(input("Novo preço: R$"))
                self.preco = novo_preco
                break
            except:
                print("Preço invalído!")

    def escolher_assento(self,assento_escolhido):
        while True:
            try:
                assento_escolhido = int(input("Escolha o número do assento: "))
                self.ssento = assento_escolhido
                break
            except:
                print("Escolha um válido")
            
class PassagemBus(Passagem):
    def __init__(self, preco, assento,placa,leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito
    
    def abastecer(self, litragem = 0):
        self.litragem = litragem
        return f"Foram abastecidos {self.litragem} litros!"

class PassagemAviao(Passagem):
    def __init__(self, preco, assento,portao_embarque,checkin):
        super().__init__(preco, assento)
        self.portao_embarque = portao_embarque
        self.checkin = checkin

    def decolar(self,horario):
        self.horario = horario
        return f"Decolagem permitida, HORÁRIO: {self.horario}"
    
bus = PassagemBus(799,30,"QRE3910",2)
aviao = PassagemAviao(2959,"a-5",12,"12pm")

print(bus.abastecer(50))
print(aviao.decolar("12:30"))


    