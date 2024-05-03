soma = 0
lixo = 1
valor = int(input('digite um numero'))
while valor != 0:
    tirar = valor % 10
    valor = valor // 10
    soma = soma + tirar
print(soma)