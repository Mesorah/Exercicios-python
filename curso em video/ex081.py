lista = []
while True:
    valor = int(input('digite um valor'))
    lista.append(valor)
    continuar = input('quer continuar? [s/n]').lower()
    
    if continuar[0] == 'n':
        break

print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('o valor 5 faz parte da lista')
else:
    print('o valor 5 não faz parte da lista')