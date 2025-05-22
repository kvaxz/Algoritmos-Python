import os #import para usar o "os.system('cls')" para limpar o terminal

clientes = {}

while True:
    print(''' 
----- Bem vindo a Fazuéli Aviações! -----

1 - Cadastrar cliente
2 - Cadastrar passagem
3 - Cadastrar avião
4 - Cadastrar tripulação
5 - Relátorios

------------------------------------------ ''')
    while True:
        try:
            action = int(input("Opção - "))
            break
        except ValueError:
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
        print(f"\nCliente {nome_cliente}.capitalize() {sobrenome_cliente}.capitalize() cadastrado com sucesso") 

        print(clientes["06913517165"])
    

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        break