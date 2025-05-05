
bolsonaro = 0
lula = 0
neymar = 0
ederson = 0
voto_nulo = 0
voto_branco = 0

while True:


    print("Bolsonaro = 1 -- Lula = 2 -- Neymar = 3 -- Ederson = 4 -- Voto Nulo = Qualquer tecla não referente aos candidatos! -- Voto em Branco = 'ENTER'")
    voto = (input("Informe seu voto: "))

    if voto == "1":
        bolsonaro += 1
    elif voto == "2":
        lula += 1
    elif voto == "3":
        neymar += 1
    elif voto == "4":
        ederson += 1
    elif voto == "":
        voto_branco += 1

    if voto == "0":
        if bolsonaro > lula and bolsonaro > neymar and bolsonaro > ederson:
            print(f"O candidato eleito foi Bolsonaro, com {bolsonaro} votos!")
            break
        elif lula > bolsonaro and lula > neymar and lula > ederson:
            print(f"O candidato eleito foi Lula, com {lula} votos!")
            break
        elif neymar > lula and neymar > bolsonaro and neymar > ederson:
            print(f"O candidato eleito foi Neymar, com {neymar} votos!")
            break
        elif ederson > lula and ederson > neymar and ederson > bolsonaro:
            print(f"O candidato eleito foi Ederson, com {ederson} votos!")
            break
        else:
            print(f"Houve algum empate, Bolsonaro com {bolsonaro} votos; Lula com {lula} votos; Neymar com {neymar} votos; Ederson com {ederson} votos!")
            break
    
    else:
        voto_nulo += 1   