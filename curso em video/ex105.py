nota = {}
def notas(*n, sit=False):
    """
    aaaa"""
    tot = s = 0
    for c in n:
        tot += 1
        s += c
        media = s / tot
    nota = {'total': tot, 'maior':max(n), 'menor':min(n), 'média': media}

    if media >= 6 and media < 7 and sit:
        nota['situação'] = 'razoável'
    elif media >= 7 and sit:
        nota['situação'] = 'boa'
    elif media < 6 and sit:
        nota['situação'] = 'ruim'
    
    return nota


print(notas(5,6,7, sit=True))
help(notas)