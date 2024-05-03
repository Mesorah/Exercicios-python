#len, iter, getitem, indicicevalido, adiciona, remove, pesquisa(index), verificatipo(isintance), ordena

class Listaunica:
    def __init__(self, elem_class):
        self.elem_class = elem_class
        self.lista = []

    def __len__(self):
        return len(self.lista)
    
    def __iter__(self):
        return iter(self.lista)
    
    def getitem(self, p):
        return self.lista[p]
    
    def indicicevalido(self, i):
        return i >= 0 and i <= len(self.lista)
    
    def adiciona(self, a):
        if a not in self.lista:
            self.lista.append(a)
    
    def remove(self, a):
        if a in self.lista:
            self.lista.remove(a)
    
    def pesquisa(self, elemento):
        self.verifica_tipo(elemento)
        try:
            return self.lista.index(elemento)
        
        except ValueError:
            return -1
    
    def verifica_tipo(self, elemento):
        if not isinstance(elemento, self.elem_class):
            raise TypeError('tipo inválido')
        
    def ordena(self, chave=None):
        return self.lista.sort(key=chave)
        

lista = Listaunica(int)

lista.adiciona(5)
lista.adiciona(2)
print(lista.pesquisa(5))
lista.verifica_tipo(5)
lista.ordena()
print(lista.lista)
print(len(lista))
            