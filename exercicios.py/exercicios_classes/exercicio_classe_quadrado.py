# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

# atributo = self, metodo = def

class Quadrado:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        
    def mudar_lado(self):
        from random import randint
        while True:
            lado_aleatorio = randint(1,10)
            if lado_aleatorio != self.tamanho:
                self.tamanho = lado_aleatorio

                return self.tamanho
    
    def retorna_valor(self):
        return self.tamanho
    
    def calcula_area(self):
        return self.tamanho ** 2
    
quadrado = Quadrado(5)

print(quadrado.mudar_lado())
print(quadrado.retorna_valor())
print(quadrado.calcula_area())