number = float(input(f"Insira o primeiro número: "))

number_2 = float(input(f"Insira o segundo número: "))

multi = number * number_2

if multi > 100:
    print(f"{multi}, é maior do que 100")
else:
    print(f"{multi}, é menor do que 100")