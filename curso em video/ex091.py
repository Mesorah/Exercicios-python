from random import randint
from operator import itemgetter
jogo = {'jogador 1': randint(1,6),
'jogador 2': randint(1,6),
'jogador 3': randint(1,6),
'jogador 4': randint(1,6)}
ranking = []

for k, v in jogo.items():
    print(f'o {k} tirou {v} no dado')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'em {k+1} ficou o {v[0]} que tirou {v[1]} no dado')