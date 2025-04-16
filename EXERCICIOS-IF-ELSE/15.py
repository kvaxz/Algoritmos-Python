number = float(input(f"Insira o número: "))

if number % 3 == 0 and number % 2 == 0:
    print(f"{number} é multiplo, ou por 2, ou por 3!")
else:
    print(f"{number} não é multiplo nem por 2 nem por 3!")