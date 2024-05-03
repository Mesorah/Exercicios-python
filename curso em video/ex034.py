s = int(input('qual seu salário?'))
if s <= 1250:
    s = s * 15 / 100 + s
    print(s)
else:
    s = s * 10 / 100 + s
    print(s)