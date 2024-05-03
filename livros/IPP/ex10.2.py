class Televisao:
    def __init__(self,canal, mini, maxi):
        self.ligada = False
        self.canal = canal
        self.minimo = mini
        self.maximo = maxi

    def mudar_canal_cima(self):
        if self.canal < self.maximo:
            self.canal += 1
    
    def mudar_canal_baixo(self):
        if self.canal > self.minimo:
            self.canal -= 1



tv = Televisao(1)
print(tv.canal)
tv.mudar_canal_baixo()
print(tv.canal)
