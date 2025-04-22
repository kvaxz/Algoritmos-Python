number = float(input("Informe o número: "))

if number > 0 and number % 3 == 0 and number % 5 != 0:
    print("Positivo, divisivel por 3 e não divisivel por 5!")
else:
    print("Negativo, ou não é divislve por 3 ou é divisivel por 5!")