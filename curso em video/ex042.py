n1 = float(input('qual o primeiro lado?'))
n2 = float(input('qual o segundo lado?'))
n3 = float(input('qual o terceiro lado?'))
if n1 < n1 + n2 and n2 < n2 + n3 and n3 < n1 + n2:
    print('pode formar')
    if n1 == n2 == n3:
        print('equilatero')
    elif n1 != n2 != n3 != n1:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('não pode transformar')