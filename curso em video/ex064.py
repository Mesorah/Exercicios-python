n = s = tot = 0
while n != 999:
    n = int(input('digite um numero [999 para parar]'))
    if n != 999:
        s = s + n
        tot = tot + 1
print(f'você digitou {tot} números e as somas deles resultaram em {s}')