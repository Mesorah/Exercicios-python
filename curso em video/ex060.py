c = 1
n = int(input('digite um número para calcular a fatorial'))
while n > 0:
    print(f'{n} x', end= ' ')
    c = c * n
    n = n - 1
print(f'= {c}',end = ' ')