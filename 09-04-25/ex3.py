nota_1 = float(input("Informe a primeira nota: "))
nota_2 = float(input("Informe a segunda nota: "))

media = (nota_1 + nota_2) / 2

if media >= 7: print("Aprovado! Nota:",media)

elif media < 7: print("Reprovado! Nota:",media)