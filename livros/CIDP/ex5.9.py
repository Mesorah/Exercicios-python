nomes = ['gabriel', 'admin', 'kayo', 'eduardo', 'toneto']
if len(nomes) > 0:
    for c in nomes:
        if c == 'admin':
            print(f'ola {c}, gostaria de ver o relatório?')
        else:
            print(f'ola {c} que bom te ver aqui')
else:
    print('prescisa de pelo menos um usuário')