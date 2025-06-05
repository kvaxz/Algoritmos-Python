while True:
    try:
        num = float(input("Número para verificar se é par: "))
        break
    except:
        print("Apenas números por favor!")

def par(num):
    if num % 2 == 0:
        print(f"{num}, é par")
    else:
        print(f"{num}, não é par")

par(num)