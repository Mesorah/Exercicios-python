def remove_repetidos(lista):
    nova = []
    for c in lista:
        if c not in nova:
            nova.append(c)
    return sorted(nova)

lista = [2, 4, 2, 2, 3, 3, 1]
c = remove_repetidos(lista)
print(c)