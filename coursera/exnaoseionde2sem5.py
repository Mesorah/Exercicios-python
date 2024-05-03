import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Esta equação não possui raízes reais.")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"A raiz desta equação é {raiz}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    
    if raiz1 == raiz2:
        print(f"A raiz dupla desta equação é {raiz1}")
    else:
        print(f"As raízes da equação são {min(raiz1, raiz2)} e {max(raiz1, raiz2)}")
#nao sei como deixar mais enxuto usando funçoes ainda
#so sei uma forma q acho q vai piora quase