import time

num1 = int(input("Informe um número inteiro: "))

num2 = int(input("Informe mais um número inteiro(maior do que o primeiro): "))

cont = 0

for i in range(num1+1,num2):
    print(i)

    cont+=i

print(cont)