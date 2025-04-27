#no python, o continue interrompe o loop

while True: 
    valor = int(input("Digite o valor 1 ou 0 para encerrar: "))
    if valor <= 1:
        continue
        print("Menor que um")
    if valor > 1:
        print("Maior que um")