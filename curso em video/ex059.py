resp = 0
n1 = int(input('qual o primeiro valor?'))
n2 = int(input('qual o segundo valor?'))
while resp != 5:
    print('''
[1] soma
[2] multiplicar 
[3] maior
[4] novos números
[5] saior do programa''')
    resp = int(input('qual sua opção?'))
    if resp == 1:
        print(f'a soma entre {n1} e {n2} é {n1 + n2}')
    elif resp == 2:
        print(f'a multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif resp == 3:
        if n1 > n2:
            print(f'o maior valor entre {n1} e {n2} é {n1}')
        else:
            print(f'o maior valor entre {n1} e {n2} é {n2}')
    if resp == 4:
        n1 = int(input('qual o primeiro valor?'))
        n2 = int(input('qual o segundo valor?'))
    print('opção inválida')