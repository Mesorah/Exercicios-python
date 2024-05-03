from ex108 import moeda

num = input('digite um valor: ')

try:
    num = float(num)
    print(f'a metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
    print(f'o dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
    print(f'aumentando 10% temos {moeda.aumentar(num, 10)}')
    print(f'reduzindo 13% temos {moeda.diminuir(num, 13)}')
except ValueError:
    print('digite apenas números inteiros')