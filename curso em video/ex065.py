tot = media = soma =  0
while True:
    n = int(input('digite um numero:'))
    soma = soma + n
    tot = tot + 1
    if tot == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('quer continuar?')).lower()
    if resp[0] in 'Nn':
        break
media = soma / tot 
print(f'você digitou {tot} números e a média deles foi {media}')
print(f'o maior valor foi {maior} e o menor foi {menor}')