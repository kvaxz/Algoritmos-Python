number = float(input(f"Insira o número: "))

if number > 0 and number % 5 != 0:
    print(f"{number}, é maior do que zero e não é multiplo de 5")
else:
    print(f"{number}, , não é maior do que zero nem multiplo de 5")