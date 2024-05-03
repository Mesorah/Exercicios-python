numero = int(input('digite um numero'))
c = numero
tot = 0
while c >= 1 :
    if numero % c == 0:
        tot = tot + 1
    c = c - 1
if tot == 2:
    print('primo')
else:
    print('não primo')