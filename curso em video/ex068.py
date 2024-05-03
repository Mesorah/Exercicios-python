from random import randint
soma = tot = 0
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    r = randint(1, 10)
    print(r)
    valor = int(input('digite um valor'))
    soma = valor + r
    pi = str(input('par ou impar?')).lower()
    if pi[0] in 'p':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            tot += 1
            print(f'você jogou {valor} e o computador jogou {r} total de {soma} e deu PAR')
        else:
            print('VOCÊ PERDEU!')
            print(f'você jogou {valor} e o computador jogou {r} total de {soma} e deu ÍMPAR')
            break
    elif pi[0] in 'i':
        if soma % 2 == 0:
            print('VOCÊ PERDEU!')
            print(f'você jogou {valor} e o computador jogou {r} total de {soma} e deu PAR')
            break
        else:
            print('VOCÊ VENCEU!')
            tot += 1
            print(f'você jogou {valor} e o computador jogou {r} total de {soma} e deu ÍMPAR')
print(f'GAME OVER! Você venceu {tot} vezes')