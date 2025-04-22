number = float(input("Informe o primeiro número: "))

number2 = float(input("Informe o segundo número: "))

if (number+number2) < 10 or (number2+number) > 100:
    print("Menor que 10 ou maior que 100!")
elif (number+number2) > 10 or (number2+number) < 100:
    print("Maior que 10 ou menor que 100")