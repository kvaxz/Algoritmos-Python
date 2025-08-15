i = 0 #Contador para percorrer as linhas
j = 0 #Contador para percorrer as colunas

line = int(input("Digite a quantidade de linhas: "))
col = int(input("Digite a quantidade de colunas: "))

matriz = []

while i < line :
    linha = []

    while j < col:
        num = 1
        linha.append(num)
        j+=1
    matriz.append(linha)
    i+=1
    j=0

print(matriz)