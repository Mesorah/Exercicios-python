class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abre_contas(self, conta):
        self.contas.append(conta)
    
    def listar_contas(self):
        for c in self.contas:
            c.resumo()