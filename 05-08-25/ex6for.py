#somar e trazer a média de 5 números

y = 0
z = 0

for i in range(5):
    print(f"Digite {i+1}º valor")
    x = int(input())
    y = y + x
    z = z + 1

print(y)
print(y/z)