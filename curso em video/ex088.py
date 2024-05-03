from random import randint

jogos = []
temp = []

quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

while quantidade_jogos > 0:
    qtd = 0
    while qtd < 6:
        c = randint(1,60)
        if c not in temp:
            temp.append(c)
            qtd += 1
    jogos.append(temp[:])
    temp.clear()
    quantidade_jogos -= 1

tot = 1
for c in jogos:
    print(f'jogo {tot}: {c}')
    tot += 1
