#qm tem mais de 65 voto opcional
def voto(ano=0):
    from datetime import datetime
    ano = datetime.today().year
    nascimento = int(input('que ano você nasceu? '))
    idade = ano - nascimento
    if idade >= 16 and idade < 18 or idade > 65:
        return f'com {idade} anos o voto é facultativo'
    elif idade >= 18 and idade < 65:
        return f'com {idade} anos o voto obrigatório'
    else:
        return f'com {idade} anos não pode votar'

print(voto())

