class Televisao:
    def __init__(self,canal, mini=2, maxi=14):
        self.ligada = False
        self.canal = canal
        self.minimo = mini
        self.maximo = maxi

    def mudar_canal_cima(self):
        if self.canal < self.maximo:
            self.canal += 1
        else:
            self.canal = self.minimo
    
    def mudar_canal_baixo(self):
        if self.canal > self.minimo:
            self.canal -= 1
        else:
            self.canal = self.maximo

tv = Televisao(99)
print(tv.canal)
tv.mudar_canal_cima()
print(tv.canal)
tv.mudar_canal_cima()
print(tv.canal)
