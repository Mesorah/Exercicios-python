s = maior = s1 = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'digite um valor para a posição [{l}, {c}]:'))
        if matriz[l][c] % 2 == 0:
            s = s + matriz[l][c]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'a soma dos valores pares é {s}')
for l in range(0, 3):
    s1 = s1 + matriz[l][2]
print(f'a soma dos valores da terceira coluna é {s1}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'o maior valor da segunda linha é {maior}')
