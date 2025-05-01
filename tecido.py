metro_tecido = int(input("Quantos metros de tecido foram comprados: "))

metro_usado = float(input("Quantos metros de tecido foram usados na bolsa: "))

preco_metro = float(input("Valor do metro de tecido: R$"))

valor_bolsa = preco_metro * metro_usado

print(f"Foram gastos R${metro_tecido*preco_metro} em tecido, e foi usado R${valor_bolsa}, em tecidos na confeecção da bolsa!")