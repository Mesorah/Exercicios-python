numeros = [[], []]
for c in range(1,8):
    valores = int(input(f'digite o {c}o. valor: '))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)

numeros.sort()

print(f'Os valores pares digitados foram: {numeros[1]}')
print(f'Os valores ímpares digitados foram: {numeros[0]}')

