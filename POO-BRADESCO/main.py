from defs import Conta
import os

conta = None  # nenhuma conta cadastrada ainda

while True:
    os.system('cls')
    print("=====  BANCO DO KVA  =====")
    print("1 - Cadastrar conta")
    print("2 - Consultar saldo")
    print("3 - Consultar extrato")
    print("4 - Sacar dinheiro")
    print("5 - Depositar dinheiro")
    print("6 - Sair")
    print("==============================")

    opc = input("Escolha uma opção: ")

    if opc == '1':
        os.system('cls')
        conta_temp = Conta("", 0, 0, 0, [], "")
        conta = conta_temp.cadastro()
        print("\nConta cadastrada com sucesso!")
        input("Pressione ENTER pra continuar...")

    elif opc == '2':
        if conta:
            conta.consultar_saldo()
            input("Pressione ENTER pra voltar...")
        else:
            print("Nenhuma conta cadastrada ainda!")
            input("Pressione ENTER pra voltar...")

    elif opc == '3':
        if conta:
            conta.consultar_extrato()
            input("Pressione ENTER pra voltar...")
        else:
            print("Nenhuma conta cadastrada ainda!")
            input("Pressione ENTER pra voltar...")

    elif opc == '4':
        if conta:
            conta.sacar()
        else:
            print("Cadastre uma conta primeiro!")
            input("Pressione ENTER pra voltar...")

    elif opc == '5':
        if conta:
            conta.depositar()
        else:
            print("Cadastre uma conta primeiro!")
            input("Pressione ENTER pra voltar...")

    elif opc == '6':
        os.system('cls')
        print("Valeu por usar o Banco do Kva, campeão!")
        break

    else:
        print("Opção inválida!")
        input("Pressione ENTER pra tentar de novo...")