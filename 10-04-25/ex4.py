product1 = float(input("Informe o valor do primeiro produto: "))
product2 = float(input("Informe o valor do segundo produto: "))
product3 = float(input("Informe o valor do terceiro produto: "))

if product1 < product2 and product1 < product3:
    print("Compre o produto 1")
elif product2 < product1 and product2 < product3:
    print("Compre o produto 2")
elif product3 < product2 and product3 < product1:
    print("Compre o produto 3")