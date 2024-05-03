from random import randint
print('''
[0] pedra
[1] papel
[2] tesoura''')
r = randint(0, 2)
e = int(input('qual sua escolha'))
if r == 0 and e == 1:
    print('jogador jogou papel e a maquina jogou pedra')
elif r == 1 and e == 2:
    print('jogador jogou tesoura e a maquina jogou papel')
elif r == 2 and e == 0:
    print('jogador jogou pedra e a maquina jogou tesoura')

#muito grande cansei