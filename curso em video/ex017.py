import math
n1 = float(input('comprimento do cateto oposto'))
n2 = float(input('comprimento do cateto adjacente'))
n3 = math.hypot(n1, n2)
print(f'a hipotenusa é {n3:.2f}')