
qntd_caderno = int(input("Quantos cadernos tem em estoque? "))
qntd_caneta = int(input("Quantas caneta tem em estoque? "))
qntd_lapis = int(input("Quantos lápis tem em estoque? "))
qntd_borracha = int(input("Quantas borrachas tem em estoque? "))
qntd_regua = int(input("Quantas réguas tem em estoque? "))

while True:
    
    print("\n\n'E' entrada no estoque; 'S' saida do estoque; 'R' relatório; 'X' para sair")
    operation = input("Operação que deseja executar: ").upper()

    if operation == "E":

        print("\n\n10 - Caderno; 20 - Caneta; 30 - Lápis; 40 - Borracha; 50 - Régua;")
        codigo = int(input("Codigo do produto a ser inserido: "))
        
        if codigo == 10:
            qntd_entrada = int(input("Quantidade do produto será adicionada ao estoque: "))
            qntd_caderno = qntd_caderno + qntd_entrada
            print(f"Agora existe {qntd_caderno} cadernos no estoque!")
        elif codigo == 20:
            qntd_entrada = int(input("Quantidade do produto será adicionada ao estoque: "))
            qntd_caneta = qntd_caneta + qntd_entrada
            print(f"Agora existe {qntd_caneta} canetas no estoque!")
        elif codigo == 30:
            qntd_entrada = int(input("Quantidade do produto será adicionada ao estoque: "))
            qntd_lapis = qntd_lapis + qntd_entrada
            print(f"Agora existe {qntd_lapis} lápis no estoque!")
        elif codigo == 40:
            qntd_entrada = int(input("Quantidade do produto será adicionada ao estoque: "))
            qntd_borracha = qntd_borracha + qntd_entrada
            print(f"Agora existe {qntd_borracha} borrachas no estoque!")
        elif codigo == 50:
            qntd_entrada = int(input("Quantidade do produto será adicionada ao estoque: "))
            qntd_regua = qntd_regua + qntd_entrada
            print(f"Agora existe {qntd_regua} régua no estoque!")

    
    if operation == "S":

        print("\n\n10 - Caderno; 20 - Caneta; 30 - Lápis; 40 - Borracha; 50 - Régua;")
        codigo = int(input("Codigo do produto a ser retirado: "))

        if codigo == 10:
            qntd_saida = int(input("Quantidade de cadernos que será retirada: "))
            if qntd_saida > qntd_caderno:
                print(f"Quantidade solicitada, maior do que a de cadernos ({qntd_caderno})")
            else:
                qntd_caderno = qntd_caderno - qntd_saida
                print(f"Foi retirado {qntd_saida} cadernos, agora possui {qntd_caderno} cadernos!")
        
        if codigo == 20:
            qntd_saida = int(input("Quantidade de canetas que será retirada: "))
            if qntd_saida > qntd_caneta:
                print(f"Quantidade solicitada, maior do que a de canetas ({qntd_caneta})")
            else:
                qntd_caneta = qntd_caneta - qntd_saida
                print(f"Foram retiradas {qntd_saida} canetas, agora possui {qntd_caneta} canetas!")
        
        if codigo == 30:
            qntd_saida = int(input("Quantidade de lápis que será retirada: "))
            if qntd_saida > qntd_lapis:
                print(f"Quantidade solicitada, maior do que a de lápis ({qntd_lapis})")
            else:
                qntd_lapis = qntd_lapis - qntd_saida
                print(f"Foi retirado {qntd_saida} lápis, agora possui {qntd_lapis} lápis!")
        
        if codigo == 40:
            qntd_saida = int(input("Quantidade de borracha que será retirada: "))
            if qntd_saida > qntd_borracha:
                print(f"Quantidade solicitada, maior do que a de borracha ({qntd_borracha})")
            else:
                qntd_borracha = qntd_borracha - qntd_saida
                print(f"Foi retirado {qntd_saida} borrachas, agora possui {qntd_borracha} borrachas!")

        if codigo == 50:

            qntd_saida = int(input("Quantidade de réguas que será retirada: "))
            if qntd_saida > qntd_regua:
                print(f"Quantidade solicitada, maior do que a de réguas ({qntd_regua})")
            else:
                qntd_regua = qntd_regua - qntd_saida
                print(f"Foi retirado {qntd_saida} réguas, agora possui {qntd_regua} réguas!")


    if operation == "R":
        print(f"\n- - - RELÁTORIO - - -")
        print(f"Cadernos: {qntd_caderno}")
        print(f"Canetas: {qntd_caneta}")
        print(f"Lápis: {qntd_lapis}")
        print(f"Borrachas: {qntd_borracha}")
        print(f"Réguas: {qntd_regua}")
    
    if operation == "X":
        print(f"\n\n BYEBYE =)\n\n")
        break
            
