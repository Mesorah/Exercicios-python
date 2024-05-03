lista = [[], [], []]

while True:
    valor = int(input('Digite um número: '))
    lista[2].append(valor)
    if valor % 2 == 0:
        lista[0].append(valor)
        print(lista)
    else:
        lista[1].append(valor)
        print(lista)
    continuar = input('quer coninuar? [s/n]').lower()

    if continuar[0] == 'n':
        break

print(f'A lista completa é {lista[2]}')
print(f'A lista dos pares é {lista[0]}')
print(f'A lista dos ímpares é {lista[1]}')