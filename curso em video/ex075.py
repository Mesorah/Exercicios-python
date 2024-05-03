tot = 0
par = ' '
tupla = (int(input('digite um valor')), int(input('digite um valor')),
int(input('digite um valor')), int(input('digite um valor')))
print(f'você digitou os valores {tupla}')
print(f'os valores pares digitados foram', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end = ' ')
    if c == 9:
        tot = tot + 1

d = tupla.index(3)
print(f'\no número 9 apareceu {tot} vezes')
print(f'o valor 3 apareceu na {d + 1} posição')