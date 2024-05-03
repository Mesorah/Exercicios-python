galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear
    pessoa["nome"] = (str(input('Nome:')))
    while True:
        pessoa['sexo'] = str(input('Sexo [m/f]')).lower()[0]
        if pessoa['sexo'] in 'mf':
            break
        print('digite apenas m ou f')
    pessoa['idade'] = int(input('Idade:'))
    soma = soma + pessoa ['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('quer continuar?[s/n]')).lower()[0]
        if resp in 'sn':
            break
        print('erro, responde somente com s ou n')
    if resp == 'n':
        break
print('-=' * 30)
print(f'ao todo temos {len(galera)} cadastradas')
media = soma /len(galera)
print(f'a média de idade é de {media:5.2f} anos')
print('as mulheres cadastradas foram:' , end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()