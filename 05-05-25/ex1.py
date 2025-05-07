#-# BANCO FAZUELI #-#

while True:
    cadastro = []

    print("Bem-Vindo ao Banco Fazueli, aqui seu dinheiro é nossa diversão")

    print("- - - - CADASTRO BANCO FAZUELI - - - -")

    while True:
        nome = input(f"Nome: ")
        if nome.isdigit():
            print(f"!!ERRO!! Insira um nome valído, por favor!")
        
        cadastro.append(nome)
        break
    while True:
        cpf = (input(f"CPF: "))
        if not cpf.isdigit() or len(cpf) != 11:
            print(f"!!ERRO!! Apenas cpf valído, por favor!")
        
        cadastro.append(cpf)
        break
    while True:
        rg = (input(f"RG: "))
        if not rg.isdigit() or len(rg) != 7:
            print(f"!!ERRO!! Apenas rg valído, por favor!")
        
        cadastro.append(rg)
        break
    while True:
        telefone = (input(f"Telefone: "))
        if not telefone.isdigit() or len(telefone) != 11:
            print(f"!!ERRO!! Digite apenas números, e com o DDD, por favor!")
        
        cadastro.append(telefone)
        break
    while True:
        n_agencia = (input(f"Número da agência: "))
        if not n_agencia.isdigit() or len(n_agencia) != 4:
            print(f"!!ERRO!! Digite uma agência valida, apenas números, por favor!")
    
        cadastro.append(n_agencia)
        break
    while True:
        n_conta = (input(f"Número da conta: "))
        if not n_conta.isdigit() or len(n_conta) != 6:
            print(f"!!ERRO!! Apenas números, e com digito, por favor!")
        
        cadastro.append(n_conta)
        break
    while True:
        saldo_inicial = float(input(f"Saldo Inicial: R$"))
        if saldo_inicial < 0:
            print(f"!!ERRO!! Insira um valor valído, por favor!")
        
        cadastro.append(saldo_inicial)
        break

    print(f"Cadastro realizado!\nNome:{cadastro[0]}\nCPF:{cadastro[1]}\nRG:{cadastro[2]}\nTelefone:{cadastro[3]}\nNúmero da agência:{cadastro[4]}\nNúmero da conta:{cadastro[5]}\nSaldo Inicial:{cadastro[6]}")

    while True:
        action = input(f"=== MENU BANCÁRIO ===\n1 - Ver Saldo\n2 - Depositar\n3 - Sacar\n4 - Sair\nAção desejada: ")

        if action == "1":
            print(f"Saldo: R${cadastro[6]}")
        if action == "2":
            deposito = float(input(f"Valor do deposito: R$"))
            cadastro[6] = cadastro[6] + deposito
        if action == "3":
            sacar = float(input("Valor do saque: R$"))
            if sacar > cadastro[6]:
                print(f"Valor acima doque existe em conta!")
            else:
                cadastro[6] = cadastro[6] - sacar
        if action == "4":
            break