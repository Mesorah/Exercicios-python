from datetime import datetime
ano = int(input('em que ano voce nasceu?'))
c = datetime.today().year - ano
if c <= 9:
    print('mirim')
elif c > 9 and c <=14:
    print('infantil')
elif c > 14 and c <= 19:
    print('junior')
elif c > 19 and c <= 25:
    print('senior')
else:
    print('master')