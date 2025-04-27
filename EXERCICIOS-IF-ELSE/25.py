number = float(input(f"Insira o número: "))

if number < 10:
    print(f"{number}, é menor do que 10")
elif number < 100:
    print(f"{number}, é maior do que 100")
else:
    print(f"{number}, não é nem maior do que 100, nem menor do que 10")