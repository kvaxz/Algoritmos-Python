number = float(input(f"Insira o primeiro número: "))

number_2 = float(input(f"Insira o segundo número: "))

number_3 = float(input(f"Insira o terceiro número: "))

media = (number + number_2 + number_3)

if media < 50:
    print(f"{media}, é menor do que 50")
else:
    print(f"{media}, não é menor do que 50")