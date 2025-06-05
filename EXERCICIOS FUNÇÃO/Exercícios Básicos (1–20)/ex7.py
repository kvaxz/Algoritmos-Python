while True:
    try:
        num = int(input("Número para verificar se é primo: "))
        break
    except:
        print("APENAS NÚMEROS INTEIROS")

def primo(num):
    if num <= 1:
        print("0, 1 E NEGATIVOS NÃO SÃO PRIMOS!")
    else:
        for i in range(2, num):
            
            if num % i == 0:
                print(f"{num}, NÃO É PRIMO, É DIVISIVEL POR {i}")
                break
        else:
            print(f"{num}, é primo")

primo(num)
