# Exercício 2: Composição

# Ainda no contexto de uma biblioteca, crie duas classes: Biblioteca e Estante. 
# A classe Biblioteca deve ter uma lista de estantes. Cada Estante deve conter uma lista de livros. 
# Implemente a relação de composição, onde a existência das estantes e dos livros 
# está completamente ligada à existência da biblioteca. Se a biblioteca for destruída, 
# as estantes e os livros associados também devem ser destruídos.

# Lembre-se de adicionar métodos apropriados para adicionar, remover e listar livros nas estantes e bibliotecas.

class Biblioteca:
    def __init__(self):
        self.lista_estantes = []


class Estante:
    #listas de livros
    pass