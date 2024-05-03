n = int(input('Digite um valor a ser testado: '))

y = False

while n != 0 :
    a = n % 10
    n = n // 10
    b = n % 10
    if a == b:
        print('sim')
        y = True



if y != True :
    print("não")