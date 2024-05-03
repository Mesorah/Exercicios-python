lista = []
for c in range(0,5):
    numeros = int(input(f'digite um valor para a posição {c}: '))
    lista.append(numeros)

print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)}')
print(f'O menor valor digitado foi {min(lista)}')

for k,v in enumerate(lista):
    if v == max(lista):
        print(k)
    
    if v == min(lista):
        print(k)
