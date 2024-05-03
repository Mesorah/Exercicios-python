s = 0
maior = tot = 0
nomevelho = ''

for c in range(1, 5):
    nome = str(input('nome:'))
    idade = int(input('idade:'))
    sexo = str(input('sexo [m/f]:')).lower()
    s = s + idade
    if c == 1 :
        if sexo[0] in 'm':
            nomevelho = nome
            maior = idade
        else:
            if idade > maior:
                maior = idade
    if sexo[0] in 'f':
        if idade < 20:
            tot = tot + 1
    print(sexo[0])
print(f'a media é de {s / 4}')
print(f'o homem mais velho tem {maior} e se chama {nomevelho}')
print(f'ao todo são {tot} mulheres com mais de 20 anos')