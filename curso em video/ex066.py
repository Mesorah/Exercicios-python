s = tot = 0
while True:
    n = int(input('digite um valor [999 para parar]'))
    if n == 999:
        break
    else:
        s += n
        tot = tot + 1
print(f'a somas dos {tot} valores resultarem em {s}')