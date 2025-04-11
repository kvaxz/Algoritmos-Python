salary = float(input("Informe o salário do colaborador: R$"))

aumento1 = salary*0.2251
aumento2 = salary*0.1539
aumento3 = salary*0.1097
aumento4 = salary*0.0519



if salary <= 280.55:
    print(f"Salário antigo era R${salary}, aumento de %22,51, valor do aumento R${aumento1}, novo salário do colaborador: R${salary*1.2251:.2f}")
elif salary >= 280.56 and salary <= 709.72:
    print(f"Salário antigo era R${salary}, aumento de %15,39, valor do aumento R${aumento2:}, novo salário do colaborador: R${salary*1.1539:.2f}")
elif salary >= 709.73 and salary <= 1501.33:
    print(f"Salário antigo era R${salary}, aumento de %10,97, valor do aumento R${aumento3}, novo salário do colaborador: R${salary*1.1097:.2f}")
elif salary >= 1501.34:
    print(f"Salário antigo era R${salary}, aumento de %5,19, valor do aumento R${aumento4}, novo salário do colaborador: R${salary*1.0519:.2f}")