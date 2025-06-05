while True:
    nomes_str = input("Digite os nomes separados por vírgula: ")
    nomes = nomes_str.split(",")  # Sem strip, vai pegar os espaços junto
    if len(nomes) == 0 or nomes == ['']:
        print("Por favor, digite pelo menos um nome.")
    else:
        break

def filtrar_nomes_grandes(lista_de_nomes):
    nomes_grandes = []
    for nome in lista_de_nomes:
        if len(nome) > 5:
            nomes_grandes.append(nome)
    print("Nomes com mais de 5 letras:", nomes_grandes)

filtrar_nomes_grandes(nomes)
