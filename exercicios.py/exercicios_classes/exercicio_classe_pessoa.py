# Classe Pessoa: Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
#sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
# atributo = self, metodo = def

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        if self.idade < 21:
            self. altura = self.altura + 0.5

        return self.idade + 1

    def engordar(self, peso):
        novo_peso = self.peso + peso
        self.peso = novo_peso
        return self.peso

    def emagrecer(self, peso):
        novo_peso = self.peso - peso
        self.peso = novo_peso
        return self.peso
    
    def crescer(self, tamanho):
        return self.altura + tamanho
    
pessoa = Pessoa('gabriel', 15, 68, 170)

print(pessoa.envelhecer())
print(pessoa.engordar(10))
print(pessoa.emagrecer(10))
print(pessoa.crescer(2))