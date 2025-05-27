while True:
    type = (input("\n\nDigite A para adição\nS para subtração\nM para multiplicação\nD para para divisão\nX para sair\nDigite o desejado: ")).upper()

    if type == "X":
        break
    elif type == "A":
        X = float(input("Informe o primeiro número da adição: "))
        Y = float(input("Informe o segundo número da adição: "))
        Z = X+Y
        print(f"O resultado da soma é {Z}")

    elif type == "S":
        X = float(input("Informe o primeiro número da subtração: "))
        Y = float(input("Informe o segundo número da subtração: "))
        Z = X-Y
        print(f"O resultado da subtração é {Z}")

    elif type == "M":
        X = float(input("Informe o primeiro número da Multiplicação: "))
        Y = float(input("Informe o segundo número da Multiplicação: "))
        Z = X*Y
        print(f"O resultado da multiplicação é {Z}")

    elif type == "D":
        X = float(input("Informe o dividendo da Divisão: "))
        Y = float(input("Informe o divisor da Divisão: "))
        Z = X / Y
        print(f"O consciente da divisão é {Z}")
