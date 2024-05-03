#30% do salário
c = int(input('qual o valor da casa?'))
s = int(input('qual o salário do comprador?'))
a = int(input('quantos anos de financiamento?'))

meses = a * 12
salario = s * 30 / 100 
d = c / meses
dsalario = s * 30 / 100 
print(f'para pagar uma casa de {c} em {a} a prestação será de {d}')
print(dsalario)
if d > dsalario:
    print('negado')
else:
    print('aprovado')
