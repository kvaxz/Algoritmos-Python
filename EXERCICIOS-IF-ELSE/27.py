number = float(input(f"Insira a idade: "))

if number < 18:
    print(f"{number}, é menor do que 18 anos")
elif number > 65:
    print(f"{number}, é maior do que 65 anos")
else:
    print(f"Não é maior do que 65 anos, e nem menor do que 18 anos")