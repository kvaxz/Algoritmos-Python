number = float(input(f"Insira o primeiro número: "))

number_2 = float(input(f"Insira o segundo número: "))

number_3 = float(input(f"Insira o terceiro número: "))

media = (number + number_2 + number_3)

if media > 100:
    print(f"{media}, é maior do que 100")
else:
    print(f"{media}, é menor do que 100")