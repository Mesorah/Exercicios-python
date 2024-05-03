soma = tot = totm = menor = menorn = 0
while True:
    nome = str(input('qual o nome do produto?'))
    preco = int(input('qual o preço do produto'))
    soma = soma + preco
    if preco > 1000:
        tot = tot + 1
    if totm == 0:
        menor = preco
        menorn = nome
    else:
        if preco < menor:
            menor = preco
            menorn = nome
    totm = totm + 1
    resp = ' '
    while resp[0] not in 'sn':
        resp = str(input('quer continuar? [s/n]')).lower().strip()[0]
    if resp == 'n':
        break

print(f'o total da compra foi de {soma} reais')
print(f'temos {tot} produtos custando mais de 1000 reais')
print(f'o produto mais barato foi {menorn} que custa {menor} reais')

