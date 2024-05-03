peso = float(input('qual seu peso?'))
altura = float(input('qual sua altura'))
imc = peso / altura ** 2
print(f'seu imc é {imc:.1f}')
if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('peso ideial')
elif imc >=25 and  imc < 30:
    print('sobrepeso')
elif imc >= 30 and imc < 40:
    print('obesidade')
else:
    print('obesidade mórbida')