
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
            print()
