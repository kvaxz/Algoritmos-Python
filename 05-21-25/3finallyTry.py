while True:
    try:
        a = int(input("Digite uma palavra: "))
    except ValueError:
        print("Digite apenas números inteiros!")
    except:
        print("Erro desconhecido!")
    finally:
        print("Final do algoritmo")