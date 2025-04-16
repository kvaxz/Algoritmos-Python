number = float(input(f"Insira o número: "))

if number > 0 and number % 2 == 0:
    print(f"{number}, é maior do que zero e é par")
else:
    print(f"{number}, , não é maior do que zero, ou não é par")