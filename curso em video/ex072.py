t =  ('zero', 'um', 'dois', 'três','quatro', 'cinco',
 'seis', 'sete', 'oito','nove','dez', 'onze', 'doze',
  'treze', 'quatorze','quinze', 'dezesseis', 'dezessete',
   'dezoito', 'dezenove', 'vinte')
n = ' '
while True:
    n = int(input('digite um número de 0 a 20'))
    if n>= 0 and n <=20:
        print(t[n])
        break
    print('digite um numero válido')