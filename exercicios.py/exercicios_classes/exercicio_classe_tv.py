# Faça um programa que simule um televisor criando-o como um objeto. 
#O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
#Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

# atributo = self, metodo = def

class Tv:
    def __init__(self, numero_canal, volume):
        self.numero_canal = numero_canal
        self.volume = volume

    def troca_canal(self):
        while True:
            numero_canal_novo = int(input('digite um numero do canal para mudar: '))
            if numero_canal_novo >= 1 and numero_canal_novo <= 100:
                self.numero_canal = numero_canal_novo 
                print(numero_canal_novo)
                return self.numero_canal
            print('canal inexistente')
    
    def aumenta_volume(self):
        while True:
            novo_volume = int(input('quantos de volume quer aumentar? '))
            if self.volume + novo_volume > 100:
                print('você passou do volume máximo')
            else:
                self.volume += novo_volume
                print(self.volume)
                return self.volume

    def diminui_volume(self):
        while True:
            novo_volume = int(input('quantos de volume quer diminir? '))
            if self.volume - novo_volume < 1:
                print('você passou do volume mínimo')
            else:
                self.volume -= novo_volume
                print(self.volume)
                return self.volume
    
tv = Tv(30, 50)

tv.troca_canal()
tv.aumenta_volume()
tv.diminui_volume()