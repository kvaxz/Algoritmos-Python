class AlunosTurismo:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def get_nome(self):
        return self.nome
    
    def get_media(self):
        media = (self.nota1 + self.nota2 + self.nota3)/3
        return media
    
    def verif_aprovacao(self, media_aprovacao=6.0):
        media = self.get_media()
        if media >= media_aprovacao:
            return "Aprovado!"
        else:
            return "Reprovado!"
            
    def __str__(self):
        return (f"Matrícula: {self.matricula} | Nome: {self.nome:<15} | "
                f"Média: {self.get_media():.2f} | Situação: {self.verif_aprovacao()}")


def obter_dados_aluno(i):
    print(f"\n--- Cadastro do Aluno {i} ---")
    
    matricula = input("Digite a matrícula: ")
    nome = input("Digite o nome: ")

    while True:
        try:
            nota1 = float(input("Digite a nota da 1ª prova (0-10): "))
            nota2 = float(input("Digite a nota da 2ª prova (0-10): "))
            nota3 = float(input("Digite a nota da 3ª prova (0-10): "))
            
            if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
                break
            else:
                print("ERRO: As notas devem estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("ERRO: Entrada inválida. Digite um número para a nota.")

    return AlunosTurismo(matricula, nome, nota1, nota2, nota3)


def maior_menor(lista_alunos):
    
    if not lista_alunos:
        return None, None 

    aluno_maior = lista_alunos[0]
    media_maior = aluno_maior.get_media()

    aluno_menor = lista_alunos[0]
    media_menor = aluno_menor.get_media()

    for aluno in lista_alunos:
        media_atual = aluno.get_media()

        if media_atual > media_maior:
            aluno_maior = aluno

        if media_atual < media_menor:
            aluno_menor = aluno

    return aluno_maior, aluno_menor


def main():
    
    num_alunos = 5
    lista_alunos = []

    print("**** INÍCIO DO CADASTRO DE ALUNOS ****")
    
    for i in range(1, num_alunos + 1):
        aluno = obter_dados_aluno(i) 
        lista_alunos.append(aluno)
        
    print("\n" + "="*50)
    print("           RELATÓRIO DE DESEMPENHO")
    print("="*50)
    print("\n**Situação de Todos os Alunos (Média de Corte 6.0)**")
    for aluno in lista_alunos:
        print(aluno)
    print("-" * 50)
    
    aluno_melhor, aluno_pior = maior_menor(lista_alunos)
    
    if aluno_melhor:
        print("\n**Análise de Extremos**")
        print(f"MAIOR MÉDIA ({aluno_melhor.get_media():.2f}): {aluno_melhor.get_nome()}")
        print(f"MENOR MÉDIA ({aluno_pior.get_media():.2f}): {aluno_pior.get_nome()}")

if __name__ == "__main__":
    main()