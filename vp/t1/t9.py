class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Não sai da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'outra coisa'

c1 = Cliente('Gabriel', 'Rodrigues')
c1.falar_nome_classe()

c2 = Aluno('Aguiar', 'Junior')
c2.falar_nome_classe() 
print(c2.cpf)

