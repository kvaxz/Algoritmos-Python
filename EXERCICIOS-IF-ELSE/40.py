number = float(input("Informe o primeiro número: "))

number2 = float(input("Informe o segundo número: "))

if (number-number2) >= 10 or (number2-number) >= 10:
    print("Diferença maior ou igual a 10!")
elif (number-number2) < 10 or (number2-number) < 10:
    print("Diferença menor do que 10!")