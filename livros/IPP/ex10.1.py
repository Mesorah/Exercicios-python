class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 1
        self.marca = 'LG'

tv = Televisao()
print(tv.canal)
tv.canal = 3
print(tv.canal)