import os #import para usar o "os.system('cls')" para limpar o terminal

clientes = {}
passagens = {}
aviao = {}
tripulacao = {}

while True:
    print(''' 
----- Bem vindo a Fazuéli Aviações! -----

1 - Cadastrar cliente
2 - Cadastrar passagem
3 - Cadastrar avião
4 - Cadastrar tripulação
5 - Relátorios
6 - Encerrar programa

------------------------------------------ ''')
    while True:
        try:
            action = int(input("Opção - "))
            if action not in [1,2,3,4,5,6]:
                print("OPÇÃO INVALÍDA")
            else: break
        except:
            print("Digite apenas números de alguma opção")
    os.system('cls') #limpa o terminal

    if action == 1:
        while True: # NOME DO CLIENTE
            nome_cliente = input("Nome: ") 
            if nome_cliente.isdigit():
                print("Nome invalido, digite sem apenas letras!")
            else: break

        while True: # SOBRENOME DO CLIENTE
            sobrenome_cliente = input("Sobrenome: ")
            if sobrenome_cliente.isdigit():
                print("Sobrenome invalido, digite sem apenas letras!")
            else: break

        while True: # RG DO CLIENTE
                rg_cliente = (input("RG: "))
                if not rg_cliente.isdigit():
                    print("APENAS NÚMEROS NO RG!")
                elif len(rg_cliente) != 9:
                    print("TAMANHO DE RG INVALÍDO!")
                else: break
            
        while True: # CPF DO CLIENTE
                cpf_cliente = (input("CPF: "))
                if not cpf_cliente.isdigit():
                    print("APENAS NÚMEROS NO CPF!")
                elif len(cpf_cliente) != 11:
                    print("TAMANHO DE CPF INVALÍDO!")
                else: break

        endereco_cliente = input("Endereço com nº: ") # ENDEREÇO DO CLIENTE

        while True: # TELEFONE DO CLIENTE
                telefone_cliente = (input("Telefone: "))
                if not telefone_cliente.isdigit():
                    print("APENAS DIGITOS NO TELEFONE!")
                elif len(telefone_cliente) != 11:
                     print("INSIRA TELEFONE COM O DDD")
                else: break     

        while True: # IDADE DO CLIENTE
            try:
                idade_cliente = int(input("Idade: "))
                if idade_cliente > 150 or idade_cliente <= 0:
                     print("IDADE INVALÍDA!")
                else: break
            except ValueError:
                print("Insira apenas números")
        
        os.system('cls') #limpa o terminal

        clientes[cpf_cliente] = {
             "nome": nome_cliente,
             "sobrenome": sobrenome_cliente,
             "rg":rg_cliente,
             "cpf":cpf_cliente,
             "endereco":endereco_cliente,
             "telefone":telefone_cliente,
             "idade":idade_cliente
        }
        print(f"\nCliente {nome_cliente.capitalize()} {sobrenome_cliente.capitalize()} cadastrado com sucesso") 

    if action == 2:
        while True:
            destino_passagem = input("Destino: ")
            if destino_passagem.isdigit():
                print("INSIRA UM DESTINO VALÍDO!")
            else: break
        
        while True:
            origem_passagem = input("Origem: ")
            if origem_passagem.isdigit():
                print("INSIRA UMA ORIGEM VALÍDA!")
            else: break

        while True:
            try:
                duracao_passagem = float(input("Duração(em horas): "))
                break
            except ValueError:
                print("DURAÇÃO APENAS EM HORAS!")

        while True:
            try:
                valor_passagem = float(input("Valor: R$"))
                desconto_passagem = valor_passagem * 1.05
                break
            except ValueError:
                print("APENAS NÚMEROS NO VALOR!")

        passagens[destino_passagem] = {
            "destino":destino_passagem,
            "origem":origem_passagem,
            "duracao":duracao_passagem,
            "valor":valor_passagem,
            "desconto":desconto_passagem
        }

    if action == 3:

        modelo_aviao = input("Modelo: ")

        while True:
            try:
                ano_aviao = int(input("Ano: "))
                if ano_aviao > 2026:
                    print("ANO INVALÍDO!")
                else: break
            except ValueError:
                print("APENAS NÚMEROS")

        while True:
            try:
                horas_aviao = float(input("Horas de voo: "))
                break
            except ValueError:
                print("APENAS NÚMEROS!")

        while True:
            cor_aviao = input("Cor: ")
            if cor_aviao.isdigit():
                print("COR INVALÍDA!")
            else: break

        while True:
            try:
                qntd_aviao = int(input("Passageiros: "))
                if qntd_aviao < 0:
                    print("VALOR INVALÍDO")
                else: break
            except ValueError:
                print("APENAS NÚMEROS INTEIROS!")

        aviao[modelo_aviao] = {
            "modelo":modelo_aviao,
            "ano":ano_aviao,
            "horas":horas_aviao,
            "cor":cor_aviao,
            "quantidade":qntd_aviao
        }

    if action == 4:

        while True:
            nome_tripulacao = input("Nome: ")
            if nome_tripulacao.isdigit():
                print("NOME INALÍDO")
            else: break
        
        while True:
            desc_tripulacao = input("Descrição do cargo: ")
            if len(desc_tripulacao) < 4:
                print("DESCRIÇÃO INVALÍDA")
            else: break

        while True:
            try:
                idade_tripulacao = int(input("Idade: "))
                if idade_tripulacao < 0 or idade_tripulacao > 150:
                    print("IDADE INVALÍDA!")
                else: break
            except ValueError:
                print("APENAS NÚMEROS!''")

        while True:
            try:
                admissao_tripulacao = float(input("Data de admissão em 2025(dd.mm):"))
                if admissao_tripulacao > 30.12:
                    print("DATA INVALÍDA!")
                else: break
            except ValueError:
                print("DATA INVALÍDA, INSIRA CONFORME JÁ INFORMADO!")

        while True:
            fone_tripulacao = int(input("Fone: "))
            if len(fone_tripulacao) != 11:
                print("TELEFONE INVALÍDO")
            else: break

        tripulacao[nome_tripulacao] = {
            "nome":nome_tripulacao,
            "desc":desc_tripulacao,
            "idade":idade_tripulacao,
            "admissao":admissao_tripulacao,
            "telefone":fone_tripulacao
        }

    if action == 5:
        os.system('cls') #limpa o terminal
        print("""
====================== RELATÓRIOS ======================
              
1 - Relatório dos clientes
2 - Relatório das passagens
3 - Relatório dos aviões
4 - Relatório da tripulação
5 - Sair da Janela  

=========================================================                          
""")
        
        while True:
            try:
                action_report = int(input("Opção - "))
                if action_report not in [1,2,3,4,5]:
                    print("APENAS ALGUMA DAS OPÇÕES")
                else:
                    os.system('cls') #limpa o terminal
                    break
            except ValueError:
                print("OPÇÃO INVALIDA!")

        if action_report == 1:
            os.system('cls') #limpa o terminal
            while True:
                consulta_cliente = input("""
    [============================================================]
    [-----------Insira o CPF do cliente para relatório-----------]                                  
    [============================================================]
    CPF: """)
                
                cpf_cliente = consulta_cliente

                if cpf_cliente not in clientes:
                    print("CPF NÃO CONSTA NOS CLIENTES")
                else: break

            print(f"""
Nome: {clientes[cpf_cliente]["nome"].capitalize()}
Sobrenome: {clientes[cpf_cliente]["sobrenome"].capitalize()}
RG: {clientes[cpf_cliente]["rg"]}
CPF: {clientes[cpf_cliente]["cpf"]}
Endereço: {clientes[cpf_cliente]["endereco"]}
Telefone: {clientes[cpf_cliente]["telefone"]}
Idade: {clientes[cpf_cliente]["idade"]}
""")
        
        if action_report == 2:
            os.system('cls') #limpa o terminal
            while True:
                consulta_passagem = input("""
    [============================================================]
    [--------------Insira o destino para relatório---------------]                                  
    [============================================================]
    Destino: """)
                
                destino_passagem = consulta_passagem

                if destino_passagem not in passagens:
                    print("DESTINO NÃO CONSTA NO SISTEMA")
                else: break

            print(f"""
Destino: {passagens[destino_passagem]["destino"].capitalize()}
Origem: {passagens[destino_passagem]["origem"].capitalize()}
Duração: {passagens[destino_passagem]["duracao"]}
Valor: {passagens[destino_passagem]["valor"]}
Valor com desconto: {passagens[destino_passagem]["desconto"]}
""")
        
        if action_report == 3:
            os.system('cls') #limpa o terminal
            while True:
                consulta_aviao = input("""
    [============================================================]
    [----------Insira o modelo do avião para relatório-----------]                                  
    [============================================================]
    Modelo: """)
                
                modelo_aviao = consulta_aviao

                if modelo_aviao not in aviao:
                    print("MODELO NÃO CONSTA NO SISTEMA")
                else: break

            print(f"""
Modelo: {aviao[modelo_aviao]["modelo"].capitalize()}
Ano: {aviao[modelo_aviao]["ano"].capitalize()}
Horas: {aviao[modelo_aviao]["horas"]}
Cor: {aviao[modelo_aviao]["cor"]}
Quantidade de passageiros: {aviao[modelo_aviao]["quantidade"]}
""")
            
        if action_report == 4:
            os.system('cls') #limpa o terminal
            while True:
                consulta_tripulacao = input("""
    [============================================================]
    [--------Insira o nome do tripulante para relatório----------]                                  
    [============================================================]
    Modelo: """)
                
                nome_tripulacao = consulta_tripulacao

                if nome_tripulacao not in tripulacao:
                    print("NOME NÃO CONSTA NO SISTEMA")
                else: break

            print(f"""
Nome: {tripulacao[nome_tripulacao]["nome"].capitalize()}
Descrição: {tripulacao[nome_tripulacao]["desc"].capitalize()}
Idade: {tripulacao[nome_tripulacao]["idade"]}
Data de admissão: {tripulacao[nome_tripulacao]["admissao"]}
Telefone: {tripulacao[nome_tripulacao]["telefone"]}
""")
            
        if action_report == 5: break

    if action == 6:break