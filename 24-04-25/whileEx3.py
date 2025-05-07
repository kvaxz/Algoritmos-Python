while True:
    while True:
        nome = input("Informe o nome: ")
        if len(nome) < 3:
            print("Invalido, nome de no minimo 3 letras é exigido!")
        else:
            break

    while True:
        idade = int(input("Informe a idade (0-150): "))
        if idade > 150 or idade < 0:
            print("Idade Invalida!")
        else:
            break
    while True:
        salario = float(input("Informe o salario:R$ "))
        if salario < 0:
            print("Sálario Invalido!")
        else:
            break
    while True:
        sexo = input("Insira o sexo, Feminino ou Masculino: ").upper()
        if sexo != "FEMININO" and sexo != "MASCULINO":
            print("Sexo Invalido!")
        else:
            break
    while True:
        estado_civil = input("Insira o estado civil, S para solteiro, C para casado, V para viuvo, D para divorciado: ").upper()
        if estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D":
            print("Estado Civil Invalido!")
        else:
            break
        

    print(f"\nNome: {nome}\n")
    print(f"Idade: {idade}\n")
    print(f"Salário:R$ {salario}\n")
    print(f"Sexo: {sexo}\n")
    print(f"Estado Civil: {estado_civil}\n")
    break
