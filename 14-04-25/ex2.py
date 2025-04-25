#-------------Variaveis-------------#
hour_price = float(input("Informe o valor da hora de trabalho: R$"))
hours = float(input("Informe as horas trabalhadas no mês: "))

brute = hour_price + hours
fgts = brute*0.11
inss = brute*0.1

#-------------Salário menor do que R$900-------------#
if brute <= 900:
    print(f"\n\nSalário bruto: (R${hour_price:.2f} * {hours:.2f} horas trabalhadas): R${brute:.2f}")
    print(f"(-) IR (ISENTO)                                                     : R$00.00")
    print(f"(-) INSS (10%)                                                      : R${inss:.2f}")
    print(f"FGTS (11%)                                                          : R${fgts:.2f}")
    print(f"Total de descontos                                                  : R${inss:.2f}")
    print(f"Salário líquido                                                     : R${brute-inss}")
   
#-------------Salário mmaior do que R$900 e menor igual a R$1500-------------#
elif brute > 900 and brute <= 1500:
    ir5 = brute * 0.05 
    discounts = ir5 + inss
    print(f"Salário bruto: (R${hour_price:.2f} * {hours:.2f} horas trabalhadas) : R${brute:.2f}")
    print(f"(-) IR (5%)                                                         : R${ir5:.2f}")
    print(f"(-) INSS (10%)                                                      : R${inss:.2f}")
    print(f"FGTS (11%)                                                          : R${fgts:.2f}")
    print(f"Total de descontos                                                  : R${discounts:.2f}")
    print(f"Salário líquido                                                     : R${brute-discounts}")

#-------------Salário menor do que R$2500 e maior do que R$1500-------------#
elif brute > 1500 and brute <= 2500:
    ir10 = brute * 0.1 
    discounts = ir10 + inss
    print(f"Salário bruto: (R${hour_price:.2f} * {hours:.2f} horas trabalhadas) : R${brute:.2f}")
    print(f"(-) IR (10%)                                                        : R${ir10:.2f}")
    print(f"(-) INSS (10%)                                                      : R${inss:.2f}")
    print(f"FGTS (11%)                                                          : R${fgts:.2f}")
    print(f"Total de descontos                                                  : R${discounts:.2f}")
    print(f"Salário líquido                                                     : R${brute-discounts}")


#-------------Salário mmaior do que R$2500-------------#
elif brute > 2500:
    ir20 = brute * 0.2
    discounts = ir20 + inss
    print(f"Salário bruto: (R${hour_price:.2f} * {hours:.2f} horas trabalhadas) : R${brute:.2f}")
    print(f"(-) IR (10%)                                                        : R${ir20:.2f}")
    print(f"(-) INSS (10%)                                                      : R${inss:.2f}")
    print(f"FGTS (11%)                                                          : R${fgts:.2f}")
    print(f"Total de descontos                                                  : R${discounts:.2f}")
    print(f"Salário líquido                                                     : R${brute-discounts}")
