# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

# atributo = self, metodo = def

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        self.cor = 'amarelo'

        return self.cor
        
    def mostraCor(self):
        print(self.cor)

bola = Bola('azul', '5', 'plastico')
bola.mostraCor()
bola.trocaCor()
bola.mostraCor()