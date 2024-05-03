maior = menor =  0
for c in range(1, 6):
    p = float(input(f'peso da {c} pessoa '))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p

print(f'o maior peso lido foi de {maior}kg e o menor foi de {menor}kg')