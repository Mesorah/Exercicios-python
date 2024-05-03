times = ('Palmeiras', 'Corinthians', 'Fluminense', 'Atlético-mg', 'Atlético-pr', 'Flamengo', 'Internacional',
         'Red bull bragantino', 'Santos', 'São paulo', 'Botafogo', 'Ceará', 'Goiás', 'Chapecoense', 'Avaí', 'Cuiabá',
         'Curitiba', 'Atlético-go', 'Juventude', 'Fortaleza')

print(f'os cinco primeiros times são {times[0:5]}')  
print()    
print(f'os quatro últimos são {times[16:]}')   
print()
print(f'os times em ordem alfabética: {sorted(times)}')
print()
print(f'a Chapecoense está na {times.index("Chapecoense")} posição')