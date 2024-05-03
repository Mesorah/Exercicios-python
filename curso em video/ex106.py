import ex106_m

num = input('digite um valor: ')

try:
    num = int(num)
    print(ex106_m.fatorial(num))
    print(f'o dobro de {num} é {ex106_m.dobro(num)}')
    print(f'o triplo de {num} é {ex106_m.triplo(num)}')
except ValueError:
    print('digite apenas números inteiros')