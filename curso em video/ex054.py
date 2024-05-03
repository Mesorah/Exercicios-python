tot = totm = 0
from datetime import datetime
for c in range(1, 8):
    p = int(input(f'em que ano a pessoa {c} nasceu?'))
    a = datetime.today().year - p
    print(a)
    if a >= 18:
        tot = tot + 1
    else:
        totm = totm + 1
print(f'ao todo tivemos {tot} pessoas maiores de idade e {totm} pessoas menores de idade')