s = cont = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        cont = cont + 1
        s = s + c
print(f'são {cont} valores que somados dão {s}')