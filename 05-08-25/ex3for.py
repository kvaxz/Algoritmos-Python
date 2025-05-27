import time

num1 = int(input("Informe um número inteiro: "))

num2 = int(input("Informe mais um número inteiro(maior do que o primeiro): "))

for i in range(num1+1,num2):
    print(i)
    time.sleep(0.2)
