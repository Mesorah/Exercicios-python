while True:
    t = int(input('quer ver a tabuada de qual valor?'))
    if t >= 0:
        for c in range(1,11):
            print(f'{t} x {c} = {t*c}')
    else:
        break