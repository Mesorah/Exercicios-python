from random import randint

lista = []

def sorteia():
    for c in range(1,6):
        c = randint(1,10)
        lista.append(c)
    print(f'sorteando 5 valores da lista: ', end='')
    for c in lista:
        print(c, end=' ')
    print()


def somapar():
    s = 0
    for c in lista:
        if c % 2 == 0:
            s += c
    print(f'somando os valores {lista}, temos {s}')


sorteia()
somapar()
