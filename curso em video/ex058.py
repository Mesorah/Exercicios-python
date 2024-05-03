from random import randint
tot = 0
c = randint(0,10)
print('adivinhe um numero entre 0 a 10')
a = ''
while a != c:
    a = int(input('qual é?'))
    tot = tot + 1
    if a == c:
        print('parabens, acertou')
        break
    else:
        if a > c:
            print('um pouco menos')
        else:
            print('um pouco mais')
print(f'para acertar você usou {tot} chances')