#saque, deposito, extrato(lista de operaçoes(transaçoes)) resumo

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
    
    def verifica_saque(self, valor):
        if valor <= self.dinheiro:
            return True
        
        return False
    
    def resumo(self):
        print(f'CC N: {self.numero} Saldo: {self.dinheiro:10.2f}')

    def extrato(self):
        for c in self.operacoes:
            print(f'{c[0]:10s} {c[1]:10.2f}')
        print(f'\n     Saldo: {self.dinheiro:10.2f}\n')


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, dinheiro, limite=0):
        Conta.__init__(self, clientes, numero, dinheiro)
        self.limite = limite

    def saque(self, valor):
        if self.dinheiro + self.limite >= valor:
            self.dinheiro -= valor
            self.operacoes.append(['SAQUE', valor])
            
            return True
        
        return False
    
    def extrato(self):
        for c in self.operacoes:
            print(f'{c[0]:10s} {c[1]:10.2f}')
        print(f'\n     Saldo: {self.dinheiro:10.2f}\n')
        saldo_disponivel = self.dinheiro + self.limite
        print(f'{self.limite}')
        print(f'\n {saldo_disponivel}')