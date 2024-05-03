princ = []
temp = []
lista = [[], []]
tot = 0
maior = menor = 0

while True:
    nome = input('Nome: ')
    temp.append(nome)
    idade = int(input('Peso: '))
    temp.append(idade)

    if tot == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    tot += 1

    princ.append(temp[:])
    temp.clear()

    continuar = input('quer continuar? [s/n]').lower()
    
    if continuar[0] == 'n':
        break

for c in princ:
    print(c[1])
    if c[1] == maior:
        lista[0].append(c[0])
        
    if c[1] == menor:
        lista[1].append(c[0])
    
print(f'o total de pessoas cadastradas: {tot}')
print(f'o maior peso foi de {maior}Kg. Peso de {lista[0]}')
print(f'o menor peso foi de {menor}KG. Peso de {lista[1]}')
