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
