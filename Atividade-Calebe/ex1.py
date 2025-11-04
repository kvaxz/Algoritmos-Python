class Pessoa:
    def __init__(self,nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        print(f"Seu endereço é, {self.endereco}")

    def alterar_endereco(self):
        novo_end = input("Insira o novo endereço: ")

        self.endereco = novo_end

        print(f"Seu novo endereço é {self.endereco}")
        