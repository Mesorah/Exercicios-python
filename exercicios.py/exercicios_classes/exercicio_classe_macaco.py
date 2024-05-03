# Desenvolva uma classe Macaco,que possua os atributos(self)
# nome e bucho (estomago) e pelo menos os 
#métodos comer(), verBucho() e digerir(). 
# Faça um programa ou teste interativamente, criando pelo menos dois macacos, 
# alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
# Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

# atributo = self, metodo = def

class Macaco:
    def __init__(self, nome, bucho=None):
        self.nome = nome
        self.bucho = bucho

    def comer(self):
        comer = input('o que você vai comer? ')
        self.bucho = comer
        return self.bucho
    
    def digerir(self):
        print(f'o {self.nome} está digerindo {self.bucho}')
        self.bucho = None
        return self.bucho
    
    def ver_bucho(self):
        if self.bucho is None:
            print(f'{self.nome} não tem nada no bucho')
        else:
            print(self.bucho)


macaco = Macaco('wilson')
macaco2 = Macaco('jorge')
macaco.ver_bucho()
macaco.comer()
macaco.ver_bucho()
macaco.digerir()

print()

macaco2.ver_bucho()
macaco2.comer()
macaco2.ver_bucho()
macaco2.digerir()