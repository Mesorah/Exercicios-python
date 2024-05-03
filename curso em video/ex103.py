def ficha(nome='desconecido', gols=0):
    print(f'o jogador {nome} fez {gols} gols')

nome = str(input('nome do jogador'))
gols = str(input('números de gols'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)