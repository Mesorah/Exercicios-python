tot = maior = menor = 0
n1 = int(input('primeiro valor'))
n2 = int(input('segundo valor'))
n3 = int(input('terceiro valor'))
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:   
    menor = n2
else:
    menor = n3
print(maior, menor)