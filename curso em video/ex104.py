def leiaint(n=0):
    while True:
        n = str(input('Digite um número: ')).strip()
        if n.isnumeric():
            return n
        else:
            print('erro')

print(leiaint())