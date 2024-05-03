# Exercício 5: Associação de Classes

# Crie duas classes, Livro e Autor. Uma relação de associação entre essas duas classes, 
# onde um autor pode ter escrito vários livros. 
#Implemente métodos para adicionar um livro à lista de livros de um autor 
# e para obter a lista de livros de um autor.

class Autor:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_livros = []
    
    def adicionar_livro(self, livro):
        return self.lista_de_livros.append(livro)
    
    def obter_livros(self):
        return self.lista_de_livros

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

autor = Autor('gabriel')
livro = Livro('sla', autor)

autor.adicionar_livro(livro)
livros = autor.obter_livros()

for livro in livros:
    print(livro.titulo, autor.nome)
        