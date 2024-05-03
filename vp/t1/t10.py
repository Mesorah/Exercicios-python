class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
        # Ou por exemplo usar A.metodo() no lugar do super mas é recomendado usa-lo

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('gg')

    def metodo(self):
        super().metodo() # B
        super(B, self).metodo() # A
        # super(A, self).metodo() # object
        print('C')

c = C('Atributo', 'Qualquer')
print(c.outra_coisa)
# c.metodo()

