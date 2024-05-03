def soma_elementos(lista):
    s = 0
    for c in lista:
        s = s + c
    return s

lista = [1,2,3,5,7]
c = soma_elementos(lista)
print(c)
        