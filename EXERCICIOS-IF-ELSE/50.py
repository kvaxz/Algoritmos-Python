number = float(input("Informe o primeiro número: "))

number2 = float(input("Informe o segundo número: "))

if (number+number2) < 20 and (number2+number) > 10:
    print("Menor do que 20 e maior do que 10!")
elif (number+number2) > 20 or (number2+number) < 10:
    print("Maior do que 20 ou menor do que 10!")