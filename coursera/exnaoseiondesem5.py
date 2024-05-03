def fatorial(n):
    f = 1
    for c in range(n,0,-1):
        f *= c
    return f
def numero_binomial(n,k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

print(numero_binomial(5,3))