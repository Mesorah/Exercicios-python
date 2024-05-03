largura = int(input('digite a largura: '))
altura = int(input('digite a altura'))

linha = 0
while altura > linha:
    coluna = 0
    while largura > coluna:
        print('#', end= '')
        coluna += 1
    print()
    linha += 1