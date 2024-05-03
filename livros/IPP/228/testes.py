from cliente import Cliente
from banco import Banco
from conta import Conta, ContaEspecial
from estado import Estado

joao = Cliente('joao da silva', '43999884734')
maria = Cliente('maria da silva', '555-4321')
jose = Cliente('jose Vargas', '1234-5678')


joao = Cliente('joao da silva', '777-1234')
maria = Cliente('maria da silva', '555-4321')

print()

conta1 = Conta([joao], 1, 1000)
conta2 = ContaEspecial([maria, joao], 2, 500, 1000)
print()

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
print(conta2.saque(1500))
conta1.extrato()
conta2.extrato()