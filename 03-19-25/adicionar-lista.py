lista = ["a","d","f"]

lista[1:1] = ["b","c"]
print(lista)

lista[4:4] = ["e"]
print(lista)

#lista[1:1] = ["b","c"], na posição um, ele ira adicionar os dois elementos
#lista[4:4] = ["e"], na posição 4 que passou a exister depois do acrescimo do b e c, ele inseri o elemento e na posição 4