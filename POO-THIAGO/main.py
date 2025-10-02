from produto import produto

lista_prod = []

i = 0 
while i < 5:
    nome = input("Digite o nome do produto: ")
    marca = input("Digite a marca do produto: ")
    modelo = input("Digite o modelo do produto: ")
    preco = input("Digite o preço do produto: ")
    prod = produto(nome,marca,modelo,preco)
    lista_prod.append(prod)
    i += 1

for item in lista_prod:
    print(item.mostrar_dados())
    
