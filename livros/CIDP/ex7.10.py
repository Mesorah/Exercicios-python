lugar_favorito = []
while True:
    lugar = str(input('qual lugar você gostaria de visitar?'))
    if lugar == 'nenhum':
        break
    else:
        lugar_favorito.append(lugar)

for c in lugar_favorito:
    print(c)
    