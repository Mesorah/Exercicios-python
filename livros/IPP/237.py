#verificador para ver se é um espaço em branco ou nulo, usar o tuder str, tunder repr, tunder eq, tuder lt
from functools import total_ordering

@total_ordering
class Nome:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return(f'<Class ...')

    def __eq__(self, outro):
        print('eq chamado')
        return self.nome == outro.nome
    
    def __lt__(self, outro):
        print('lt chamado')
        return self.nome < outro.nome

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if valor == None or not valor.strip(): 
            raise ValueError('Não deixe o nome nulo ou em branco')
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)

    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()

A = Nome('Nilo')
print(A)

A.nome = 'Nilo Menezes'
print(A)

print(A.nome)
