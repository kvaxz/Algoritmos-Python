x = int(input("Quantas temperaturas serão informadas: "))

lista = []

for i in range(x):
    temp = int(input(f"Temperatura:"))
    data = input(f"Informe o mês e ano que ocorreu: ")
    lista.append((temp, data))

maior = lista[0]
menor = lista[0]
soma = 0

for temp, data in lista:
    if temp < menor[0]:
        menor = (temp, data)
    if temp > maior[0]:
        maior = (temp, data)
    soma += temp

media = soma / x

print(f"Menor temperatura: {menor[0]}°C em {menor[1]}")
print(f"Maior temperatura: {maior[0]}°C em {maior[1]}")
print(f"Média das temperaturas: {media:.2f}°C")