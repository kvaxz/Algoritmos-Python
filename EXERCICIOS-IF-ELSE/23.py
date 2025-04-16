number = float(input(f"Insira o primeiro número: "))

number_2 = float(input(f"Insira o segundo número: "))

soma = number + number_2

if soma > 50:
    print(f"{soma}, é maior do que 50")
else:
    print(f"{soma}, é menor do que 50")