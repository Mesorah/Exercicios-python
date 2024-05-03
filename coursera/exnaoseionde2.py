numero = int(input('digite um numero'))
c = 1 
y = False
while numero != 0:
    a = numero % 10
    numero = numero // 10
    b = numero % 10
    c = c +1
    if a == b:
        print('igual')
        y = True
    
    if y != True:
        print('diferente')

