class Vetor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def soma(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y, self.z + outro.z)

    def subtracao(self, outro):
        return Vetor(self.x - outro.x, self.y - outro.y, self.z - outro.z)

    def produto_escalar(self, outro):
        return self.x * outro.x + self.y * outro.y + self.z * outro.z

    def produto_vetorial(self, outro):
        x = self.y * outro.z - self.z * outro.y
        y = self.z * outro.x - self.x * outro.z
        z = self.x * outro.y - self.y * outro.x
        return Vetor(x, y, z)

    def modulo(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5


v1 = Vetor(2, 3, 4)
v2 = Vetor(1, 5, 2)

print(v1)
print(v2)
print(v1.soma(v2))
print(v1.subtracao(v2))
print(v1.produto_escalar(v2))
print(v1.produto_vetorial(v2))
print(v1.modulo())