conversor = int(input('Por favor, entre com o número de d que deseja converter:'))

a = conversor // (24 * 3600)
resto = conversor % (24 * 3600)
b = resto // 3600
resto = resto % 3600
c = resto // 60
d = resto % 60

print(a,'dias', b,'horas', c,'minutos e', d,'segundos')
