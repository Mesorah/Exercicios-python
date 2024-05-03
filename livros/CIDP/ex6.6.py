pessoas = {'jen': 'python',
'ian': 'c#',
'felix:': 'c',
'joao': 'html'}
convidados = {'joao': 'css',
'carlos': 'javascript'}
for c in convidados:
    if c in pessoas:
        print(f'obrigado {c}')
    else:
        print(f'participe da nossa pesquisa {c}')
