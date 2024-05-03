palavras = ('Viajar', 'Elegante', 'Animal', 'Carro', 'Brasileiro', 'Abacate')
for c in palavras:
    print(f'\nna palavra {c} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
