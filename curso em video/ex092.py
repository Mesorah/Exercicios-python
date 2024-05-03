from datetime import datetime
c = datetime.today().year
dict = {}
dict['nome'] = str(input('Nome:'))
nasc = int(input('Ano de nascimento:'))
dict['idade'] = c - nasc 
dict['carteira'] = int(input('Carteira de trabalho [0 não tem]'))
if dict['carteira'] == 0:
    for k, v in dict.items():
        print(f'{k} tem o valor {v}')
dict['contratação'] = int(input('Ano de contratação:'))
dict['salário'] = int(input('salário'))
ap = dict['idade'] + ((dict['contratação'] + 35) - c)
dict['aposentadoria'] = ap
for k, v in dict.items():
        print(f'{k} tem o valor {v}')