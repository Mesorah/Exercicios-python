# Exercício 1: Agregação

# Considere um sistema de biblioteca. Crie duas classes: Livro e Biblioteca. 
# A classe Livro deve ter atributos como título, autor e ano de publicação. 
# A classe Biblioteca deve ter uma lista de livros. 
# Implemente a relação de agregação, onde a biblioteca contém vários livros, 
# mas os livros podem existir independentemente da biblioteca.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

class Biblioteca:
    def __init__(self):
        self.lista = []
    
    def adiciona(self, livro):
        return self.lista.append(livro)


livro = Livro('sla', 'eu', 2024)
biblioteca = Biblioteca()

biblioteca.adiciona(livro)

for livro in biblioteca.lista:
    print(f'Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}')
