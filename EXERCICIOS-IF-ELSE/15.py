number = float(input(f"Insira o número: "))

if number % 3 == 0 and number % 2 == 0:
    print(f"{number} é multiplo, de 2, e de 3!")
else:
    print(f"{number} não é multiplo de 2 e 3!")