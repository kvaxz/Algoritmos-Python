number = float(input("Informe o primeiro número: "))

number2 = float(input("Informe o segundo número: "))

if (number-number2) >= 20 or (number2-number) >= 20:
    print("Diferença maior ou igual a 20!")
elif (number-number2) < 20 or (number2-number) < 20:
    print("Diferença menor do que 20!")