bolsonaro = 0
lula = 0
neymar = 0
ederson = 0
voto_nulo = 0
voto_branco = 0

while True:


    print("Bolsonaro = 1 -- Lula = 2 -- Neymar = 3 -- Ederson = 4 -- Voto Nulo = 5 -- Voto em Branco = 6")
    voto = int(input("Informe seu voto: "))

    if voto == 1:
        bolsonaro += 1
    elif voto == 2:
        lula += 1
    elif voto == 3:
        neymar += 1
    elif voto == 4:
        ederson += 1
    elif voto == 5:
        voto_nulo += 1
    elif voto == 6:
        voto_branco += 1
    elif voto == 0:
        print(f"Votos para Bolsonaro: {bolsonaro}; Votos para Lula: {lula}; Votos para Neymar: {neymar}; Votos para Ederson: {ederson}; Votos nulos: {voto_nulo}; Votos em branco: {voto_branco}")
        break
    else:
        print("Número invalido")

