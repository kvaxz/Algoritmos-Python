n = int(input("Quantidade de pessoas em sala:"))
cont = 0
pessoas = []

for i in range(n):
    cont += 1
    idade = int(input(f"Idade da {cont}º pessoa: "))
    pessoas.append(idade)

média = sum(pessoas) / n

if média > 0 and média <= 25:
    print(f"Turma jovem, com média de {média} anos.")
elif média > 2 and média <= 60:
    print(f"Turma adulta, com média de {média} anos.")
elif média > 60:
    print(f"Turma idosa, com média de {média} anos.")
    