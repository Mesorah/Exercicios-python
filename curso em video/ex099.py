def maior(*n):
    for c in n:
        print(c, end=' ')
    if len(n) >= 1:
        print(f'foram informados {len(n)} valores')
        print(f'o maior valor informado foi {max(n)}')
    else:
        print(f'foram informados {len(n)}')
        print('o maior valor informado foi 0')
    print('-=' * 15)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()