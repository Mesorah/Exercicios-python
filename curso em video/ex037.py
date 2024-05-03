num = int(input('digite um numero'))
print('''
1- binário
2- octal
3- hexadecimal''')
e = int(input('qual sua escolha?'))
if e == 1:
    print(f'{bin(num)}')
elif e == 2:
    print(f'{oct(num)}')
else:
    print(f'{hex(num)}')