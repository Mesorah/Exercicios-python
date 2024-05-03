v = int(input('qual a velocidade do carro?'))
c = v - 80
if v > 80:
    print(f'voce terá que pagar uma multa de {c * 7} reais')
else:
    print('tudo certo')