def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

        
    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        while i <= f:
            print(i, end=' ')
            i += p
        print()
        print('-=' * 15)
    elif i > f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        while i >= f:
            print(f'{i}', end=' ')
            i -= p
        print()

contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 15)

print('agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

contador(ini,fim,pas)
