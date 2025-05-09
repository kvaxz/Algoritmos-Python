maior = float("-inf")
menor = float("inf")
soma = 0 

qntd = int(input("Quantos números serão digitados: "))

for i in range(qntd):
    print(f"Digite o {i+1}º número: ")
    valor = int(input())
    soma = soma + valor

    if valor < menor:
        menor = valor
    elif valor > maior:
        maior = valor

print(f"O maior é {maior}")
print(f"O menor é {menor}")
print(f"A soma é {soma}")
