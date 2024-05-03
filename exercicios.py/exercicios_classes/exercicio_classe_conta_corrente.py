# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
#A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
#Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, 
#com valor default zero e os demais atributos são obrigatórios.

# atributo = self, metodo = def

class Conta:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self):
        novo_nome = input('digite seu novo nome: ')
        self.nome_correntista = novo_nome
        print(self.nome_correntista)
        return self.nome_correntista

    def deposito(self):
        deposito = int(input('digite um valor para depositar: '))
        self.saldo += deposito
        print(self.saldo)
        return self.saldo

    def saque(self):
        saque = int(input('digite um valor para sacar: '))
        if saque <= self.saldo:
            self.saldo -= saque
            print(self.saldo)
            return self.saldo
        
        print('valor insuficiente')

conta = Conta(1, 'Gabriel', 150)
conta.alterar_nome()
conta.deposito()
conta.saque()