number = float(input(f"Insira o número: "))

if number < 0 and number % 2 == 1:
    print(f"{number}, é menor do que zero e é impar")
else:
    print(f"{number}, , não é menor do que zero, ou não é impar")