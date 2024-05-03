aluno = {}
aluno['nome'] = str(input('Nome:'))
aluno['media'] = float(input(f'Média de {aluno["nome"]}'))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif aluno['media'] > 5 and aluno['media'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
for k, v in aluno.items():
    print(f' {k} é igual a {v}')