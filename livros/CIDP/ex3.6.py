convidados = ['João', 'Eduardo', 'Kayo']
convites = ['Gustavo', 'Andrey', 'André']

print(f'encontrei uma mesa maior {convidados[0]}, {convidados[1]}, {convites[0]}, {convites[1]}, {convites[2]}')
convidados.insert(0, convites[0])
convidados.insert(2, convites[1])
convidados.append(convidados[2])
print(convidados) 