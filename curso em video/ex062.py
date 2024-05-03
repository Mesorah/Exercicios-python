tot = 0
mais = 10
cont = 1
p = int(input('primeiro termo:'))
r = int(input('razão:'))
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        p = p + r
        print(p)
        cont = cont + 1 
    mais = int(input('quantos termos quer mostrar a mais?'))
print(f'foram mostrados {tot} valores')
