tot = 3
t1 = 0
t2 = 1
n = int(input('quantos termos quer mostrar?'))
print(t1)
print(t2)
while tot <= n:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    tot = tot + 1