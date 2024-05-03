jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador:'))
tot = int(input(f'quantas partidas {jogador["nome"]} jogou'))
for c in range(0, tot):
    partidas.append(int(input(f'quantos gols ele fez na {c} partida')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-=' * 30)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for k, v in enumerate (jogador['gols']):
    print(f'na partida {k} ele fez {v} gols')