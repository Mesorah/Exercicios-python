s = tot = 0
for c in range(1,7):
    n = int(input('digite um numero'))
    if n % 2 == 0:
        tot = tot + 1
        s = s + n
print(f'voce informou {tot} pares e a soma resultou em {s}')