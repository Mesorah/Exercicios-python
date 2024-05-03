toti = tots = totm = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'mh':
        sexo = str(input('Sexo: [h/m]')).lower()
    if idade >= 18:
        toti = toti + 1
    if sexo[0] in 'h':
        tots = tots + 1
    if sexo[0] in 'm' and idade < 20:
        totm = totm + 1
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar?')).lower()
    if resp[0] in 'n':
        break
print(f'total de pessoas com mais de 18 anos: {toti}')
print(f'ao todo temos {tots} homens cadastrados')
print(f'e temos {totm} mulheres com menos de 20 anos')