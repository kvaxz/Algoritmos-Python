num = int(input("Qual número quer saber o fatorial: "))
acu = 1

for i in range(1, num + 1):
    acu *= i

print(acu)