# Crie uma classe chamada ContaBancaria com os atributos saldo e titular.
# Implemente métodos para depositar, sacar e verificar o saldo.
# Utilize encapsulamento para proteger o acesso direto ao saldo.

class ContaBancaria:
    def __init__(self, __saldo, titular):
        self.__saldo = __saldo
        self.titular = titular

    def depositar(self):
        numero_depositado = int(input('quantos reais deseja depositar? '))
        saldo = self.__saldo + numero_depositado
        return saldo
    
    def sacar(self):
        numero_sacar = int(input('quantos reais deseja sacar? '))
        saldo = self.__saldo - numero_sacar
        return saldo
    
    def ver_saldo(self):
        print(self.__saldo)

contabancaria = ContaBancaria(100, 23423)

print(contabancaria.depositar())
print(contabancaria.sacar())
contabancaria.ver_saldo()