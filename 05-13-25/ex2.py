num = int(input("Qual número quer saber o fatorial: "))
acu = 1

for i in range(1, num + 1):
    acu = acu * i

print(acu)