def minmax(temperaturas):
    tot = 0
    maior = 0
    menor = 0
    for c in temperaturas:
        if tot == 0:
            maior = c
            menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
        tot += 1
    return maior, menor

temperaturas = [50, 40, 30, 45, 32, 23, 13, 343, 643, 654, 343, 24, 2131]
c = minmax(temperaturas)
print(c)

def maximominimo(temperaturas):
    mini = min(temperaturas)
    maxi = max(temperaturas)
    return mini, maxi

g = [50, 40, 30, 45, 32, 23, 13, 343, 643, 654, 343, 2424, 2131]
d = maximominimo(g)
print(d)