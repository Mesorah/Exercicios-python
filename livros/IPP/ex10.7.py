#saque, deposito, extrato(lista de operaçoes(transaçoes)) resumo
#from cliente import Cliente


class Conta:
    def __init__(self, clientes, numero, dinheiro=0):
        self.dinheiro = dinheiro
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []

    def deposito(self, valor):
        self.operacoes.append(['DEPÓSITO', valor])
        self.dinheiro += valor
    
    def saque(self, valor):
        if valor <= self.dinheiro:
            self.operacoes.append(['SAQUE', valor])
            self.dinheiro -= valor
        else:
            print('Saldo insuficiente')
    
    def resumo(self):
        print(f'CC N{self.numero} Saldo: {self.dinheiro:10.2f}')
        for cliente in self.clientes:
            print(f'Nome: {cliente.nome}  Telefone: {cliente.telefone}')

    def extrato(self):
        for c in self.operacoes:
            print(f'{c[0]:10s} {c[1]:10.2f}')
        print(f'\n     Saldo: {self.dinheiro:10.2f}\n')