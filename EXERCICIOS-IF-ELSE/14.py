number = float(input(f"Insira o número: "))

if number < 0 or number < -10:
    print(f"{number} é negativo, ou menor do que -10!")
else:
    print(f"{number} é positivo!")