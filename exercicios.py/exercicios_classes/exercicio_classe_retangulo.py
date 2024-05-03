# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, 
#deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

# atributo = self, metodo = def

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def mudar_valor_lados(self):
        base = False
        altura = False

        from random import randint

        while True:
            base_aleatorio = randint(1, self.base + 1)
            if base_aleatorio != self.base:
                base = True
                self.base = base_aleatorio
            altura_aleatorio = randint (1, self.altura + 1)

            if altura_aleatorio != self.altura:
                altura = True
                self.altura = altura_aleatorio

            if base and altura:
                return self.base, self.altura

    def retorna_valor(self):
        return self.base, self.altura
    
    def calcula_area(self):
        return self.base * self.altura
    
    def calcula_perimetro(self):
        return (self.base * 2) + (self.altura * 2)


try:
    lado = int(input('Digite um valor para a base: '))
    altura = int(input('Digite um valor para a altura: '))
except ValueError:
    raise ValueError('Digite apenas valores inteiros')
except Exception:
    raise ValueError('Erro desconhecido')


retangulo = Retangulo(lado, altura)

print(retangulo.mudar_valor_lados())
print(retangulo.retorna_valor())
print(retangulo.calcula_area())
print(retangulo.calcula_perimetro())
    
