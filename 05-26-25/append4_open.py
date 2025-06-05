try:
    f = open("open.txt", "x")# "x" cria o arquivo especificado e retorna um erro se o arquivo existir

except FileExistsError: # <-- erro que ocorre
    print("Já existe essa pasta")

#use X quando quiser ter certeza de que não vai sobrescrever acidentalmente um arquivo existente