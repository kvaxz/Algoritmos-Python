while True:
    try:
        num = int(input("Número inteiro que deseja saber o fatorial: "))
        break
    except:
        print("APENAS NÚMEROS INTEIROS")

def fatorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    
    print(result)

fatorial(num)