# Crie uma classe chamada Animal com atributos e métodos genéricos. Em seguida, 
#crie uma classe chamada Gato que herda da classe Animal e adicione atributos ou métodos específicos para um gato.

class Animal:
    def __init__(self, nome, raca, cor):
        self.nome = nome
        self.raca = raca
        self.cor = cor
    
    def printar_nome(self):
        print('salve')
        print(self.nome, self.raca, self.cor)

class Gato(Animal):
    def __init__(self, nome, raca, cor, sexo):
        super().__init__(nome, raca, cor)
        self.sexo = sexo
    
    def printar_nome(self):
        super().printar_nome()
        print(self.nome, self.raca, self.cor, self.sexo)

gato = Gato('carlos', 'sla', 'preto', 'masculino')
gato.printar_nome()