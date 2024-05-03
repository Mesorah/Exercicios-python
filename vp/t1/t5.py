class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None
    
    @property
    def cor(self):
        print('foi')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def cor_tampa(self):
        print('p')
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, cor):
        print('s')
        self._cor_tampa = cor


caneta = Caneta('Azul')

# getter -> obter valor

print(caneta.cor)

print()

caneta.cor = 'Preto'

print(caneta.cor)

caneta.cor_tampa = 'Branco'
