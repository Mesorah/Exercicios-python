p = int(input('primeiro termo:'))
r = int(input('razão:'))
d = p + (10 - 1) * r
for c in range(p, d + r,r):
    print(c)