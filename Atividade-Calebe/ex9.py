class Naosei:
    def __init__(self,p,q):
        self.p = p
        self.q = q

    def trocar_sinal(self):
        self.p = self.p * -1
        return f"{self.p}/{self.q}"
    
    def somar(self, outro):
        novo_p = self.p * outro.q + self.q * outro.p
        novo_q = self.q * outro.q
        print(f"Soma: {novo_p}/{novo_q}")

    def subtrair(self, outro):
        novo_p = self.p * outro.q - self.q * outro.p
        novo_q = self.q * outro.q
        print(f"Subtração: {novo_p}/{novo_q}")

    def subtrair(self, outro):
        novo_p = self.p * outro.q - self.q * outro.p
        novo_q = self.q * outro.q
        print(f"Subtração: {novo_p}/{novo_q}")

    def quociente(self, outro):
            novo_p = self.p * outro.q
            novo_q = self.q * outro.p
            print(f"Quociente: {novo_p}/{novo_q}")

r1 = Naosei(1, 2)
r2 = Naosei(1, 3)

r1.somar(r2)