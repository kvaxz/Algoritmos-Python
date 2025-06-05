numeros = []

while True:
    print("""
---------------------------------------------------
       Digite números ou insira X para sair
---------------------------------------------------          
          """)
    num_str = input(":").lower()

    if num_str == "x":
        break
    else:
        num_float = float(num_str)
        numeros.append(num_float)

def maior_num(numeros):
    print(f"{max(numeros)} é o maior número informado")

maior_num(numeros)