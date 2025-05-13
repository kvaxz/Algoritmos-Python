fallen = 0
neymar = 0
bolsonaro = 0

cont = 0

n = int(input(f"Informe o número de eleitores: "))

for i in range(n):
    cont += 1
    voto = int(input(f"Eleitor {cont}: 1 para votar no Bolsonaro, 2 para votar no Neymar, e 3 para votar no Fallen: "))
    
    if voto == 1:
        bolsonaro += 1
    if voto == 2:
        neymar += 1
    if voto == 3:
        fallen += 1
    if voto != 1 and voto != 2 and voto != 3: 
        print(f"\nVoçê estragou a eleição com sua falta de interpretação, parabéns, comece denovo, apenas utilize os números informados\n")
        exit()

print(f"\nBolsonaro: {bolsonaro} votos\nNeymar: {neymar} votos\nFallen: {fallen} votos\n")

if bolsonaro > neymar and bolsonaro > fallen:
    print(f"\nBolsonaro ganhou com {bolsonaro} votos!\n")
elif neymar > bolsonaro and neymar > fallen:
    print(f"\nNeymar ganhou com {neymar} votos!\n")
elif fallen > bolsonaro and fallen > neymar:
    print(f"\nFallen ganhou com {fallen} votos!\n")
else:
    print(f"Pode ter ocorrido um empate nesta eleição, aguarde o segundo turno!")
    exit()