alunos = []
alunos_o = []
while True:
    nome = input('Nome: ')
    alunos.append(nome)
    nota1 = float(input('Nota 1: '))
    alunos.append(nota1)
    nota2 = float(input('Nota 2: '))
    alunos.append(nota2)

    media = (nota1 + nota2) / 2
    alunos.append(media)

    alunos_o.append(alunos[:])
    alunos.clear()

    continuar = input('Quer continuar? [s/n]').lower()
    
    if continuar[0] == 'n':
        break

tot = 0
print(f'{'NO': <4}{'NOME':<10}{'Média':>8}')
for c in alunos_o:
    print(f'{tot:<4}  {c[0]:<10}  {c[2]:>8.1f}')
    tot += 1

while True:
    mostrar = int(input('mostrar a nota de qual aluno? (999 interrompe): '))

    if mostrar == 999:
        break
    else:
        print(f'as notas de {alunos_o[mostrar][0]} são {alunos_o[mostrar][1]}, ', end='')
        print(f'{alunos_o[mostrar][2]}')