number = float(input(f"Insira o número: "))

if number > 100:
    print(f"{number} é positivo e maior do que 100!")

elif number > 0 and number <= 100:
    print(f"{number}, é positivo mas não é maior do que 100")

else:
    print(f"{number}, é negativo")
