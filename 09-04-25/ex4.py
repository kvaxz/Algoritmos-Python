salario = float(input("Informe o salario: R$"))

if salario < 500: print("Aumento de 15% : R$", (salario*0.15)+salario)

elif salario >= 500 and salario < 1000: print("Aumento de 10% : R$", (salario*0.1)+salario)

elif salario > 1000: print("Aumento de 5% : R$", (salario*0.05)+salario )