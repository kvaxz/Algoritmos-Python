A = int(input("Qual número positivo deseja reduzir a 0: "))
numero = 0

while A > 0:

    A = A - 1
    numero = numero + 1
    if A == 0:
        print(f"Este é o número agora: {A}, foi reduzido em 1, {numero} vezes")
if A < 0:
    print("O número deve ser positivo!")