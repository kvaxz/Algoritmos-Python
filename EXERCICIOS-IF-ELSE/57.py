number = float(input("Informe o primeiro número: "))

number2 = float(input("Informe o segundo número: "))

if (number+number2) == 20 or (number2+number) > 50:
    print("Igual a 20 ou maior do que 50!")
elif (number+number2) != 20 or (number2+number) < 50:
    print("Diferente do que 20 ou menor do que 50!")