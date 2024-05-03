#classes para estados e cidades
#cada estado tem um nome, sigla e cidades
#cada cidade tem nome e população

class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

class Estado:
    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades

    def soma_populacao(self):
        soma = 0
        for cidade in self.cidades:
            soma += cidade[1]
        return soma