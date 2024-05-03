tot = 0
n = int(input('digite um numero'))
for c in range (1, n + 1):
    if n % c == 0:
        print(n)
        tot = tot + 1

print(f'o numero {n} foi divisível {tot} vez')