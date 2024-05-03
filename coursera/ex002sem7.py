largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

linha_superior = '#' * largura
linha_lateral = '#' + ' ' * (largura - 2) + '#'

print(linha_superior)

altura_interior = altura - 2
while altura_interior > 0:
    print(linha_lateral)
    altura_interior -= 1

if altura > 1:
    print(linha_superior)
