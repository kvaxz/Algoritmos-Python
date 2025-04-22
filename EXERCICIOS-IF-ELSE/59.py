number = float(input("Informe o primeiro número: "))

number2 = float(input("Informe o segundo número: "))

if (number+number2) > 200 and (number2+number) < 500:
    print("Maior que 200 e menor que 500!")
elif (number+number2) < 200 or (number2+number) > 500:
    print("Menor que 200 ou maior que 500!")