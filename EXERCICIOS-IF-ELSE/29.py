number = float(input(f"Insira a idade: "))

if number > 60:
    print(f"{number}, a pessoa tem mais de 60 anos")
elif number < 18:
    print(f"{number}, a pessoa tem menos de 18 anos")
else:
    print(f"A pessoa não tem mais de 60 anos nem menos de 18")