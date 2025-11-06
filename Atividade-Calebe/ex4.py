class NumeroComplexo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def exibir(self):
        if self.imaginario >= 0:
            return f"{self.real} + {self.imaginario}i"
        else:
            return f"{self.real} - {abs(self.imaginario)}i"

    def soma(self, outro):
        novo_real = self.real + outro.real
        novo_imaginario = self.imaginario + outro.imaginario
        return NumeroComplexo(novo_real, novo_imaginario)

    def subtracao(self, outro):
        novo_real = self.real - outro.real
        novo_imaginario = self.imaginario - outro.imaginario
        return NumeroComplexo(novo_real, novo_imaginario)

    def produto(self, outro):
        novo_real = (self.real * outro.real) - (self.imaginario * outro.imaginario)
        novo_imaginario = (self.real * outro.imaginario) + (self.imaginario * outro.real)
        return NumeroComplexo(novo_real, novo_imaginario)



Z1 = NumeroComplexo(2, 3)
Z2 = NumeroComplexo(5, -1)

print(f"Z1: {Z1.exibir()}")
print(f"Z2: {Z2.exibir()}")
print("-" * 20)

Z_soma = Z1.soma(Z2)
print(f"Soma (Z1 + Z2): {Z_soma.exibir()}") 

Z_sub = Z1.subtracao(Z2)
print(f"Subtração (Z1 - Z2): {Z_sub.exibir()}")

Z_mult = Z1.produto(Z2)
print(f"Produto (Z1 * Z2): {Z_mult.exibir()}")