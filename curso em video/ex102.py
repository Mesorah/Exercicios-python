def fatorial(n, show=False):
    """
    :param n: o numero para calcular a fatorial
    :param show: mostrar ou nao a conta
    :return: returnar o valor
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='') 
        f *= c
    return f   

print(fatorial(5, show=True))
   