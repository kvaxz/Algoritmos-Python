class Compras:
    def __init__(self,numero,produto,valor, valor_total=0):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = valor_total

    def calcular_valor_total(self):
        valor_total = self.valor + (self.valor * 0.17) + (self.valor * 0.05)
        self.valor_total = valor_total

class CompraAvista(Compras):
    def __init__(self, numero, produto, valor, desconto, valor_total=0):
        super().__init__(numero, produto, valor, valor_total)
        self.__desconto = desconto

    def calcular_valor_total(self):
        super().calcular_valor_total()
        desconto_valor = self.valor_total * (self.__desconto / 100)
        self.valor_total = self.valor_total - desconto_valor

    def get_desconto(self):
        return self.__desconto

    def set_desconto(self, novo_desconto):
        if 0 <= novo_desconto <= 100:
            self.__desconto = novo_desconto
        else:
            print("Desconto inválido.")


class CompraParcelada(Compras):
    def __init__(self, numero, produto, valor, parcelas, valor_total=0):
        super().__init__(numero, produto, valor, valor_total)
        self.__parcelas = parcelas

    def simular_numero_de_parcelas(self):
        super().calcular_valor_total()
        self.valor_total = self.valor_total / self.__parcelas

    def get_parcelas(self):
        return self.__parcelas

    def set_parcelas(self, nova_qtd):
        if nova_qtd > 0:
            self.__parcelas = nova_qtd
        else:
            print("Quantidade de parcelas inválida.")

c1 = Compras(1, "Notebook", 5000)
c1.calcular_valor_total()
print(c1.valor_total)

c2 = CompraAvista(2, "Geladeira", 3000, 10)
c2.calcular_valor_total()
print(c2.valor_total)

c3 = CompraParcelada(3, "Celular", 2400, 6)
c3.simular_numero_de_parcelas()
print(c3.valor_total)