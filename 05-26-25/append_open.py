f = open("open.txt","a")# "a": acrescentar, abre um arquivo para anexar, cria o arquivo se ele não existir, será anexado ao final do arquivo

f.write("\nAdicionando conteúdo!") #Funciona como se fosse um append

f = open("open.txt","r") #"r": read, ler, ele vai ler o arquivo e armazenar na variavel

print(f.read())#só funcionar se antes ele leu o arquivo
f.close()
