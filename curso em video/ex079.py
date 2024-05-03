lista = []

while True:
    valor = int(input('digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print('valor duplicado')
    
    continuar = input('quer continuar?[s/n]: ').lower()
    
    if continuar[0] == 'n':
        break

print(sorted(lista))