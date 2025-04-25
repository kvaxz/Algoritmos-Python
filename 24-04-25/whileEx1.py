while True:
    nota = float(input("Informe a nota: "))

    if nota >= 0 and nota <= 10:
        print(f"A nota é {nota}")
        break
    else:
        print("Valor invalido!")