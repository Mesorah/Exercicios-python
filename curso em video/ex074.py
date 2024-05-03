tot = maior = menor = 0
from random import randint
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10))
for c in tupla:
    if tot == 0:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    tot = tot + 1
print(tupla)
print(maior)
print(menor)

#ou podemos usar
#from random import randint
#tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10))
#for c in tupla:
# print(c)
#print(max(tupla))
#print(min(tupla))