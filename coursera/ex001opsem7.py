def n_primos(n):
    c = 1
    tot = 0
    if n >= 2:
        while c <= n:
            if n % c == 0:
                tot = tot + 1
            c += 1
        return tot

n = int(input('digite um numero'))
resultado = n_primos(n)
print(resultado)