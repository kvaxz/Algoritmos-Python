class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        self.normalizar()

    def normalizar(self):
        segundos_totais = self.hora * 3600 + self.minuto * 60 + self.segundo
        
        segundos_totais = segundos_totais % 86400

        self.hora = segundos_totais // 3600
        segundos_restantes = segundos_totais % 3600
        self.minuto = segundos_restantes // 60
        self.segundo = segundos_restantes % 60

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

    def to_seconds(self):
        return self.hora * 3600 + self.minuto * 60 + self.segundo
        
    def incrementar(self, segundos_adicionais):
        segundos_totais = self.to_seconds() + segundos_adicionais
        
        nova_hora = segundos_totais // 3600
        segundos_restantes = segundos_totais % 3600
        novo_minuto = segundos_restantes // 60
        novo_segundo = segundos_restantes % 60
        
        return Horario(nova_hora, novo_minuto, novo_segundo)

    def diferenca(self, outro_horario):
        segundos_self = self.to_seconds()
        segundos_outro = outro_horario.to_seconds()
        
        return abs(segundos_self - segundos_outro)



H1 = Horario(10, 30, 45)
H2 = Horario(11, 0, 15)

print(f"Horário 1 (H1): {H1}")
print(f"Horário 2 (H2): {H2}")
print("-" * 35)

segundos_a_adicionar = 3661

H3 = H1.incrementar(segundos_a_adicionar)
print(f"Incrementando H1 por {segundos_a_adicionar}s:")
print(f"Novo Horário (H3): {H3}")
print("-" * 35)

diferenca_segundos = H1.diferenca(H2)
print(f"Diferença entre H1 e H2:")
print(f"Diferença em segundos: {diferenca_segundos} segundos")