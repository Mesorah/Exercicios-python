f = str(input('digite uma frase:')).strip().upper()
p = f.split()
j = ''.join(p)
i = j[::-1]
print(f'o inverso de {j} é {i}')
if i == j:
    print('palíndromo')
else:
    print('não é')
