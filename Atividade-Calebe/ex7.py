class Carros:
    def __init__(self,marca,ano,preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostrar_preco(self):
        return f"Preço: R${self.preco}"
    
    def mostrar_dados(self):
        return f"\nMarca: {self.marca} | Ano: {self.ano} | Preço: R${self.preco}"
    
def cadastrar_carro(i):
    print(f"--- Cadastro do carro {i} ---")
    marca = input("Marca: ")
    ano = input("Ano: ")
    preco = float(input("Preço: R$"))
    return Carros(marca,ano,preco)

def main():
    num_carros = 5
    lista_carros = []

    for i in range(1, num_carros+1):
        car = cadastrar_carro(i)
        lista_carros.append(car)

    p = float(input(f"Filtro de valor: R$"))

    for carro in lista_carros:
        cont = 0
        if carro.preco < p:
            print(carro.mostrar_dados())
        cont+=1
    if cont >= num_carros:
        print("Tem não")
        


if __name__ == "__main__":
    main()
