from datetime import datetime
ida = int(input('Digite o ano de nascimento'))
c = datetime.today().year - ida
print(f'quem nasceu em {ida} tem {c} anos em {datetime.today().year}')
if c == 18:
    print('voce tem que se alista agora')
elif c > 18:
    print(f'voce deveria ter se alistado ha {c - 18} anos')
else:
    print(f'falta {18 - c} anos para voce se alistar')
