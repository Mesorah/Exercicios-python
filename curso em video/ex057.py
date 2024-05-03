while True:
    d = str(input('informe seu sexo [m/f]')).lower()
    print(d[0])
    if d[0] in 'mfFM':
        print(f'sexo {d} cadastrado com sucesso')
        break
    print('informe um sexo válido')