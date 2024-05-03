n = int(input('Digite um número inteiro:'))
soma = 0

while n != 0:
    b = n % 10  
    soma = soma + b
    n = n // 10 
print(soma)
