while True:
    idade = int(input('quantos anos você tem [pressione 999 para parar]'))
    if idade < 3:
        print('ingresso gratuito')
    elif idade >= 3 and idade <= 12:
        print('custa 10 reais')
    elif idade > 12 and idade != 999:
        print('custa 15 reais')
    if idade == 999:
        break