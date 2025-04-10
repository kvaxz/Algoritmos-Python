salario = float(input("Informe o salario: R$"))

if salario < 500: print("Aumento de 15% : R$",{salario*1.15 :.2f})

elif salario >= 500 and salario < 1000: print("Aumento de 10% : R$",salario*1.1)

elif salario > 1000: print("Aumento de 5% : R$",salario*1.05)