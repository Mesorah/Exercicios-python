n1 = int(input('digite um numero'))
n2 = int(input('digite um numero'))
n3 = int(input('digite um numero'))
if n1 < n2 and n1 < n3 and n2 > n1 and n2 < n3 and n3 > n1 and n3 > n2:
    print('crescente')
else:
    print('não está em ordem crescente')