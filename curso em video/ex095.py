time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador:'))
    tot = int(input(f'quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('quer continuar? [s/n]')).upper()[0]
        if resp in 'SN':
            break
        print('erro')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i}', end='')
print()
print('-'* 40)
#incompleto
